import os
import sys
import pyautogui
import time
import threading
import tkinter as tk

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Avail.py")

        # Set a fixed window size (wider and taller for readability)
        self.root.geometry("300x200")
        self.root.resizable(False, False)  # Prevent resizing

        self.running = False
        self.interval = 15  # Interval in seconds

        # GUI Elements
        self.start_button = tk.Button(root, text="Start", command=self.start, width=15)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop, width=15)
        self.stop_button.pack(pady=5)

        self.status_label = tk.Label(root, text="Status: Stopped", fg="red")
        self.status_label.pack(pady=5)

        self.action_frame = tk.Frame(root)
        self.action_frame.pack(pady=5)

        self.action_label = tk.Label(self.action_frame, text="Next Action:", font=("Helvetica", 10))
        self.action_label.pack(side="left")

        self.next_action_label = tk.Label(self.action_frame, text="", font=("Helvetica", 10))
        self.next_action_label.pack(side="left")

        self.countdown_label = tk.Label(root, text="", font=("Helvetica", 10))
        self.countdown_label.pack(pady=5)

    def start(self):
        if not self.running:
            self.running = True
            self.status_label.config(text="Status: Running", fg="green")
            self.thread = threading.Thread(target=self.run)
            self.thread.start()

    def stop(self):
        if self.running:
            self.running = False
            self.status_label.config(text="Status: Stopped", fg="red")

    def run(self):
        next_action = "Mouse Move"
        while self.running:
            for i in range(self.interval, 0, -1):
                self.next_action_label.config(text=next_action)
                self.countdown_label.config(text=f"in {i} seconds")
                time.sleep(1)
                if not self.running:
                    return

            if next_action == "Mouse Move":
                self.move_mouse()
                next_action = "Alt+Tab"
            else:
                self.alt_tab()
                next_action = "Mouse Move"

    def move_mouse(self, distance=10):
        pyautogui.moveRel(distance, 0)  # Move mouse right
        time.sleep(0.5)
        pyautogui.moveRel(-distance, 0)  # Move mouse left

    def alt_tab(self):
        pyautogui.hotkey('alt', 'tab')  # Perform Alt+Tab

if __name__ == "__main__":
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.mainloop()
