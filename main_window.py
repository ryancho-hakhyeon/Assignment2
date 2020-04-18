import tkinter as tk


class AudioLibraryWindow(tk.Frame):
    """ Main Application Window """

    def __init__(self, parent, my_controller):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)

        parent.title('Audio Library')
        parent.geometry("550x260")

        main_menu = tk.Menu(master=parent)
        parent.config(menu=main_menu)
        file_menu = tk.Menu(main_menu)
        main_menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Add Song', command=my_controller.add_song)
        file_menu.add_command(label='Clear')
        file_menu.add_command(label='Quit', command=my_controller.quit_callback)

        top_left_frame = tk.Frame(master=parent)
        top_left_frame.grid(row=0, column=0, padx=5, pady=5)
        top_right_frame = tk.Frame(master=parent)
        top_right_frame.grid(row=0, column=1, padx=5, pady=5)

        mid_frame = tk.Frame(master=parent)
        mid_frame.grid(row=1, columnspan=2, padx=5, pady=5)
        bot_frame = tk.Frame(master=parent)
        bot_frame.grid(row=2, columnspan=2, padx=5, pady=5)

        tk.Label(top_left_frame, text='Title:', width=20).grid(row=0, column=0, sticky=tk.E)
        self._title = tk.Label(top_left_frame, text='')
        self._title.grid(row=0, column=1, sticky=tk.W)
        tk.Label(top_left_frame, text='Artist:', width=20).grid(row=1, column=0, sticky=tk.E)
        self._artist = tk.Label(top_left_frame, text='')
        self._artist.grid(row=1, column=1, sticky=tk.W)
        tk.Label(top_left_frame, text='Runtime:', width=20).grid(row=2, column=0, sticky=tk.E)
        self._runtime = tk.Label(top_left_frame, text='')
        self._runtime.grid(row=2, column=1, sticky=tk.W)
        tk.Label(top_left_frame, text='Album:', width=20).grid(row=3, column=0, sticky=tk.E)
        self._album = tk.Label(top_left_frame, text='')
        self._album.grid(row=3, column=1, sticky=tk.W)
        tk.Label(top_left_frame, text='Genre:', width=20).grid(row=4, column=0, sticky=tk.E)
        self._genre = tk.Label(top_left_frame, text='')
        self._genre.grid(row=4, column=1, sticky=tk.W)
        tk.Label(top_left_frame, text='File Location:', width=20).grid(row=5, column=0, sticky=tk.E)
        self._location = tk.Label(top_left_frame, text='', width=20)
        self._location.grid(row=5, column=1, sticky=tk.W)

        self.listbox = tk.Listbox(top_right_frame, width=30)
        self.listbox.grid(row=0, column=0, sticky=tk.E)
        self._titles = my_controller.list_song()
        self.set_titles()

        tk.Label(mid_frame, text='Rating to add:').grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self._new_entry = tk.Entry(mid_frame, width=20)
        self._new_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self._new_entry.bind("<Return>")

        tk.Button(bot_frame, text='Add', width=10) \
            .grid(row=0, column=0, sticky=tk.E, padx=15, pady=5)

        delete_button = tk.Button(bot_frame, text='Delete', width=10)
        delete_button.grid(row=0, column=1, sticky=tk.E, padx=15, pady=5)
        delete_button.bind("<Button-1>", my_controller.remove_callback)

        show_button = tk.Button(bot_frame, text='Show', width=10)
        show_button.grid(row=0, column=2, sticky=tk.E, padx=15, pady=5)
        show_button.bind("<Button-1>", my_controller.show_callback)

        tk.Button(bot_frame, text='Play Song', width=10, command=my_controller.play_window_popup)\
            .grid(row=0, column=3, sticky=tk.E, padx=15, pady=5)

    def set_titles(self):
        self.listbox.delete(0, tk.END)
        for title in self._titles:
            self.listbox.insert(tk.END, title)

    def delete_list(self):
        self.listbox.delete(tk.ANCHOR)

    def get_title(self):
        selected = self.listbox.curselection()
        return self.listbox.get(selected)

    def display_song(self, song_info):
        self._title['text'] = song_info['title']
        self._artist['text'] = song_info['artist']
        self._runtime['text'] = song_info['runtime']
        self._album['text'] = song_info['album']
        self._genre['text'] = song_info['genre']
        self._location['text'] = song_info['location']