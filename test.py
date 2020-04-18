import tkinter as tk
import eyed3
from tkinter.filedialog import askopenfilename


class AudioLibraryWindow(tk.Frame):
    """ Main Application Window """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        parent.title('Audio Library')
        parent.geometry("400x260")

        main_menu = tk.Menu(master=parent)
        parent.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Add Song', command=self.add_song)
        file_menu.add_command(label='Clear')
        file_menu.add_command(label='Quit')

        top_frame = tk.Frame(master=self)
        top_frame.grid(row=0, padx=30, pady=10)
        mid_frame = tk.Frame(master=self)
        mid_frame.grid(row=1, padx=30, pady=10)
        bot_frame = tk.Frame(master=self)
        bot_frame.grid(row=2, padx=30, pady=10)

        tk.Label(top_frame, text='Title:', width=20).grid(row=0, column=0, sticky=tk.E)
        self.title = tk.Label(top_frame, text='')
        self.title.grid(row=0, column=1, sticky=tk.E)
        tk.Label(top_frame, text='Artist:', width=20).grid(row=1, column=0, sticky=tk.E)
        tk.Label(top_frame, text='Album:', width=20).grid(row=2, column=0, sticky=tk.E)
        tk.Label(top_frame, text='Runtime:', width=20).grid(row=3, column=0, sticky=tk.E)
        tk.Label(top_frame, text='Genre:', width=20).grid(row=4, column=0, sticky=tk.E)
        tk.Label(top_frame, text='File Location:', width=20).grid(row=5, column=0, sticky=tk.E)

        tk.Label(mid_frame, text='Name to add:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

        self._new_entry = tk.Entry(mid_frame, width=20)
        self._new_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self._new_entry.bind("<Return>")

        tk.Button(bot_frame, text='Add', width=10) \
            .grid(row=0, column=0, sticky=tk.E, padx=20, pady=5)
        add_button = tk.Button(bot_frame, text='Remove', width=10)
        add_button.grid(row=0, column=1, sticky=tk.E, padx=20, pady=5)
        add_button.bind("<Button-1>")

        tk.Button(bot_frame, text='Song List', width=10)\
            .grid(row=0, column=2, sticky=tk.E, padx=20, pady=5)

    def add_song(self):
        selected_file = askopenfilename(initialdir='.')
        if selected_file:
            mp3_file = eyed3.load(selected_file)
            value = eyed3.load(selected_file).info.time_secs
            min = int(value / 60)
            sec = int(value % 60)
            self.times = str(min) + ':' + str(sec)

            tags = ['title', 'artist', 'album', 'genre']
            title = getattr(mp3_file.tag, tags[3])

            self.title['text'] = title
            self.artist = getattr(mp3_file.tag, tags[1])
            self.album = getattr(mp3_file.tag, tags[2])
            self.genre = getattr(mp3_file.tag, tags[3])

if __name__ == "__main__":
    root = tk.Tk()
    AudioLibraryWindow(root).pack()
    tk.mainloop()



