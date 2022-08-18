import tkinter as tk
from tkinter import ttk
from pathlib import Path
from pytube import YouTube
from .SearchVideo import SearchVideo
from .AlertClass import Alert


class MainWindow:
    def __init__(self):
        self.window = self.get_window()

    def get_window(self):
        win = tk.Tk()
        win.geometry("700x130+300+300")
        win.title('YouTube Downloader')
        win.resizable(False, False)
        photo = tk.PhotoImage(file=Path('GUI', 'icons', 'youtube.png'))
        win.iconphoto(False, photo)

        tk.Label(win, text='Сюда вставьте ссылку для поиска видео', font='arial 9', ) \
            .grid(row=0, column=0, sticky='ws', padx=10)
        win.rowconfigure(0, minsize=30)

        self.entry = tk.Entry(win, font='arial 14', width=50)
        self.entry.grid(row=1, column=0, sticky='w', padx=10)
        win.rowconfigure(1, minsize=40)

        tk.Button(win, text='Найти', command=self.search_video,
                       font='arial 10 bold',
                       width=10,
                  background='red')\
                       .grid(row=1, column=1, sticky='e')
        win.columnconfigure(1, minsize=110)

        tk.Button(win, text='В разработке', command=self.view_downloaded_video, # Будет сделано в ДЗ10
                  font='arial 10 bold',
                  width=30,
                  background='light blue') \
            .grid(row=2, column=0, padx=20)
        win.rowconfigure(2, minsize=50)
        win.mainloop()

        return win

    def search_video(self):
        link = self.entry.get()
        if 'https://' in link:
            yt = YouTube(link)
            SearchVideo(yt=yt)
        else:
            Alert(title='Ошибка url!!!',
                  text ='Введенная ссылка не верна!!!\n'\
                        'Ссылка должна иметь вид:\n https://youtu.be/link_text!!!',
                  color='red')

    def view_downloaded_video(self):
        pass


