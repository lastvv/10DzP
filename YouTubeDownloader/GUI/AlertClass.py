import tkinter as tk

class Alert:
    def __init__(self, text: str, title: str, color:str):
        self.text = text
        self.color = color
        self.title = title
        self.get_alert_window()

    def get_alert_window(self):
        alert = tk.Tk()
        alert.title(self.title)
        alert.geometry("230x60+500+500")
        alert.resizable(False, False)

        tk.Label(alert,
                 text=self.text,
                 font='arial 10 bold',
                 background=self.color,
                 justify='center').grid(row=0, column=0)
        alert.rowconfigure(0, minsize=30)
        alert.mainloop()