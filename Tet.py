import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import json
import os


class AvailabilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Team-Planer: Wer hat wann Zeit?")
        self.root.geometry("400x500")

        self.data_file = "availability.json"
        self.load_data()

        # --- UI Elemente ---
        tk.Label(root, text="Dein Name:", font=("Arial", 10, "bold")).pack(pady=5)
        self.name_entry = tk.Entry(root, font=("Arial", 12))
        self.name_entry.pack(pady=5)

        tk.Label(root, text="Wähle ein Datum:", font=("Arial", 10, "bold")).pack(pady=5)
        self.cal = Calendar(root, selectmode='day', locale='de_DE')
        self.cal.pack(pady=10, fill="both", expand=True)

        self.btn_save = tk.Button(root, text="Ich habe Zeit!", command=self.add_availability, bg="#4CAF50", fg="white")
        self.btn_save.pack(pady=5)

        self.btn_show = tk.Button(root, text="Wer hat noch Zeit?", command=self.show_availability)
        self.btn_show.pack(pady=5)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=4)

    def add_availability(self):
        name = self.name_entry.get().strip()
        date = self.cal.get_date()

        if not name:
            messagebox.showwarning("Fehler", "Bitte gib deinen Namen ein!")
            return

        if date not in self.data:
            self.data[date] = []

        if name not in self.data[date]:
            self.data[date].append(name)
            self.save_data()
            messagebox.showinfo("Erfolg", f"{name} wurde für den {date} eingetragen!")
        else:
            messagebox.showinfo("Info", "Du bist für diesen Tag bereits eingetragen.")

    def show_availability(self):
        date = self.cal.get_date()
        people = self.data.get(date, [])

        if people:
            names = "\n".join(people)
            messagebox.showinfo(f"Verfügbarkeit am {date}", f"Folgende Personen haben Zeit:\n\n{names}")
        else:
            messagebox.showinfo(f"Verfügbarkeit am {date}", "Bisher hat niemand Zeit eingetragen.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AvailabilityApp(root)
    root.mainloop()