import tkinter as tk
from hand_tracker.hand_tracker import HandTracker

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hand Tracker App")
        self.attributes('-fullscreen', True)
        self.panel = tk.Label(self)
        self.panel.pack(side="bottom", fill="both", expand="yes")
        self.bind("<Escape>", lambda e: self.quit())

        self.hand_tracker = HandTracker(self.panel)
        self.hand_tracker.start()

    def start_app(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start_app()
