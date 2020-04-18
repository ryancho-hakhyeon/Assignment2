import tkinter as tk

class PlaySongWindow(tk.Frame):

    def __init__(self, parent, play_callback, stop_callback, pause_callback, volume_callback):
        tk.Frame.__init__(self, parent)
        self._play_song = play_callback
        self._stop_song = stop_callback
        self._pause_song = pause_callback
        self._set_volume = volume_callback

        parent.title('Play Song')

        self.top_frame = tk.Frame(self.master)
        self.bot_frame = tk.Frame(self.master)
        self.top_frame.grid(row=0, padx=10, pady=10)
        self.bot_frame.grid(row=1, padx=10, pady=10)

        self.listbox = tk.Listbox(self.top_frame, width=40, selectmode=tk.BROWSE)
        self.scrollbar = tk.Scrollbar(self.top_frame, orient='horizon')
        self.scrollbar.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scrollbar.set)

        play_button = tk.Button(self.bot_frame, text='Play', width=10, command=self._play_song)\
            .grid(row=0, column=0, sticky=tk.E, padx=15, pady=5)

        stop_button = tk.Button(self.bot_frame, text='Stop', width=10, command=self._stop_song)\
            .grid(row=0, column=1, sticky=tk.E, padx=15, pady=5)

        pause_button = tk.Button(self.bot_frame, text='Pause', width=10, command=self._pause_song)\
            .grid(row=0, column=2, sticky=tk.E, padx=15, pady=5)

        self.scale = tk.Scale(self.bot_frame, from_=100, to=0, command=self._set_volume)\
            .grid(row=0, column=3)


        self.listbox.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    def get_file(self):
        return self.file_path

    def display_song(self, song_info):
        self.listbox.delete(0, tk.END)
        for song in song_info:
            self.listbox.insert(tk.END, song_info[song])
            self.file_path = song_info['location']