import rumps
import os

class ProduktivitaetsApp(rumps.App):
    def __init__(self):
        # Wir entfernen den Text-Titel (den Apfel) und setzen dafür das Icon
        super(ProduktivitaetsApp, self).__init__(name="", icon="uhr_icon.png")
        
        # Variablen für den Status
        self.pomodoro_aktiv = False
        self.zeit_uebrig = 25 * 60
        self.wasser_zaehler = 0
        
        # Die Datei, in der deine Notizen dauerhaft gespeichert werden
        self.notizen_datei = "meine_notizen.txt"
        
        # Menüstruktur aufbauen
        self.menu = [
            "Start Pomodoro",
            "Reset Timer",
            None,  
            "💧 Wasser trinken (0)",
            "💧 Wasser zurücksetzen",
            None,  
            "📝 Neue Notiz...",
            "📋 Alle Notizen ansehen",
            "🗑️ Alle Notizen löschen"  # <-- Der neue Eintrag zum Zurücksetzen
        ]

    @rumps.clicked("Start Pomodoro")
    def toggle_pomodoro(self, sender):
        self.pomodoro_aktiv = not self.pomodoro_aktiv
        sender.title = "Pause Pomodoro" if self.pomodoro_aktiv else "Start Pomodoro"

    @rumps.clicked("Reset Timer")
    def reset_timer(self, _):
        self.pomodoro_aktiv = False
        self.zeit_uebrig = 25 * 60
        # Das Icon bleibt, der Text daneben wird gelöscht
        self.title = ""
        self.menu["Start Pomodoro"].title = "Start Pomodoro"

    @rumps.clicked("💧 Wasser trinken (0)")
    def wasser_trinken(self, sender):
        self.wasser_zaehler += 1
        sender.title = f"💧 Wasser trinken ({self.wasser_zaehler})"

    @rumps.clicked("💧 Wasser zurücksetzen")
    def reset_wasser(self, _):
        self.wasser_zaehler = 0
        self.menu["💧 Wasser trinken (0)"].title = "💧 Wasser trinken (0)"

    # --- NOTIZEN FUNKTIONEN ---
    
    @rumps.clicked("📝 Neue Notiz...")
    def neue_notiz(self, _):
        fenster = rumps.Window(
            message="Was möchtest du dir für später merken?",
            title="Notiz erfassen",
            default_text="",
            cancel=True,
            dimensions=(300, 100)
        )
        antwort = fenster.run()
        
        if antwort.clicked and antwort.text.strip():
            with open(self.notizen_datei, "a", encoding="utf-8") as datei:
                datei.write(f"- {antwort.text}\n")
            
            rumps.notification(
                title="Gespeichert", 
                subtitle="", 
                message="Deine Notiz wurde erfolgreich gesichert."
            )

    @rumps.clicked("📋 Alle Notizen ansehen")
    def zeige_notizen(self, _):
        if os.path.exists(self.notizen_datei):
            with open(self.notizen_datei, "r", encoding="utf-8") as datei:
                notizen = datei.read()
            
            if not notizen.strip():
                notizen = "Du hast aktuell keine Notizen."
        else:
            notizen = "Du hast aktuell keine Notizen."
            
        rumps.alert(title="Deine Notizen", message=notizen)

    # --- NEU: Notizen löschen/zurücksetzen ---
    @rumps.clicked("🗑️ Alle Notizen löschen")
    def notizen_loeschen(self, _):
        # Fragt zur Sicherheit nochmal nach
        bestaetigung = rumps.alert(
            title="Notizen löschen?", 
            message="Bist du sicher, dass du alle Notizen unwiderruflich löschen möchtest?", 
            cancel=True
        )
        
        # Wenn der User auf "Ok" (Wert 1) klickt
        if bestaetigung == 1:
            if os.path.exists(self.notizen_datei):
                os.remove(self.notizen_datei)
                rumps.notification(
                    title="Gelöscht", 
                    subtitle="", 
                    message="Alle Notizen wurden erfolgreich zurückgesetzt."
                )
            else:
                rumps.notification(
                    title="Hinweis", 
                    subtitle="", 
                    message="Es gab keine Notizen zum Löschen."
                )

    # --- TIMER FUNKTION ---

    @rumps.timer(1)
    def tick(self, _):
        if self.pomodoro_aktiv:
            if self.zeit_uebrig > 0:
                self.zeit_uebrig -= 1
                minuten, sekunden = divmod(self.zeit_uebrig, 60)
                # Wir setzen jetzt nur noch die Zeit als Titel neben das Icon
                self.title = f" {minuten:02d}:{sekunden:02d}"
            else:
                self.pomodoro_aktiv = False
                self.title = ""
                self.menu["Start Pomodoro"].title = "Start Pomodoro"
                self.zeit_uebrig = 25 * 60
                
                rumps.notification(
                    title="Pomodoro Tracker",
                    subtitle="Zeit abgelaufen!",
                    message="Mach eine kurze Pause."
                )

if __name__ == "__main__":
    ProduktivitaetsApp().run()