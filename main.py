import tkinter as tk
from hand_tracker.hand_tracker import HandTracker

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hand Tracker App")
        self.attributes('-fullscreen', True)

        self.configure(bg="#333333")
        self.option_add('background', '#333333')
        self.option_add('foreground', '#333333')

        self.bind("<Escape>", lambda e: self.quit())

        self.create_frames()

    # FUNCTION TO CREATE THE WIDGETS
    def create_frames(self):

        camera_frame = tk.Frame(self, bg="#333333")

        camera_frame.pack(side=tk.TOP,fill=tk.BOTH, expand=True)

        self.app_name = tk.Label(camera_frame, text="IntelliHome", fg="white", bg="#333333", font=("Arial", 70))
        self.app_name.pack(expand=True)

        self.panel = tk.Label(camera_frame, bg="#333333")
        self.panel.pack_propagate(0)
        self.panel.pack(side=tk.TOP)

        self.hand_tracker = HandTracker(self.panel)
        self.hand_tracker.start()

    def start_app(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.start_app()
