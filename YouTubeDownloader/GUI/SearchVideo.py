import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from .AlertClass import Alert


class SearchVideo:
    def __init__(self, yt: YouTube):
        self.yt = yt
        self.s_window = self.get_s_window()


    def get_s_window(self):

        win = tk.Tk()
        win.geometry("700x100+400+400")
        win.title('YouTube Downloader')
        win.resizable(False, False)

        tk.Label(win, text=f'Название видео: {self.yt.title}', font='arial 9 bold', ) \
            .grid(row=0, column=0, columnspan=2)
        win.rowconfigure(0, minsize=30)

        win.columnconfigure(1, minsize=100)
        win.columnconfigure(2, minsize=100)
        win.columnconfigure(3, minsize=100)

        tk.Label(win, text='Выберите качество', font='arial 9', ) \
            .grid(row=1, column=0, sticky='e')
        win.rowconfigure(1, minsize=30)

        self.cmb = ttk.Combobox(win, values=('360p', '720p'))
        self.cmb.grid(row=1, column=1, sticky='w')
        self.cmb.current(1)

        tk.Button(win, text='Скачать аудио', font='arial 10 bold', background='green', command=self.a_downloading) \
            .grid(row=1, column=2)

        tk.Button(win, text='Скачать видео', font='arial 10 bold', background='red', command=self.v_downloading) \
            .grid(row=1, column=3)

        win.mainloop()

    def a_downloading(self):
        stream = self.yt.streams.get_by_itag(251)
        stream.download('download_files/')
        Alert(title='Аудио',
              text=f'Аудио скачено в /download_files/',
              color='green')

    def v_downloading(self):
        iTag = 22 if self.cmb.get() == '720p' else 18

        stream = self.yt.streams.get_by_itag(iTag)
        stream.download('download_files/')
        Alert(title='Видео',
             text=f'Видео скачено в /download_files/',
             color='green')

