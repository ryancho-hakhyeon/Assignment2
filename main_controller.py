import eyed3
import requests
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os
#import vlc
from pygame import mixer
from main_window import AudioLibraryWindow
from playsong_window import PlaySongWindow


class MainAppController(tk.Frame):

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)
        self._root_win = tk.Toplevel()
        self._chooser = AudioLibraryWindow(self._root_win, self)

    def quit_callback(self):
        self.master.quit()

    def clear_callback(self):
        response = requests.delete("http://localhost:5000/song/all")
        if response.status_code == 200:
            msg_str = f'All songs removed from the database'
            messagebox.showinfo(title='Delete All', message=msg_str)
        else:
            messagebox.showerror(title='Delete All', message="Something went wrong")

    def remove_callback(self, event):
        title = self._chooser.get_title()
        self._chooser.delete_list()
        response = requests.get("http://localhost:5000/song/titles")

        title_list_1 = [f'{s["file_name"]}' for s in response.json()]
        title_list_2 = [f'{s["title"]}' for s in response.json()]

        for i in range(len(title_list_1)):
            if title == title_list_2[i]:
                file_name = title_list_1[i]
                response = requests.delete("http://localhost:5000/song/" + str(file_name))
                if response.status_code == 200:
                    msg_str = f'{title}/{file_name} deleted to the database'
                    messagebox.showinfo(title='Delete Song', message=msg_str)

    def show_callback(self, event):
        title = self._chooser.get_title()
        response = requests.get("http://localhost:5000/song/titles")

        title_list_1 = [f'{s["file_name"]}' for s in response.json()]
        title_list_2 = [f'{s["title"]}' for s in response.json()]

        for i in range(len(title_list_1)):
            if title == title_list_2[i]:
                file_name = title_list_1[i]
                response = requests.get("http://localhost:5000/song/" + str(file_name))
                if response.status_code == 200:
                    song_info = response.json()
                    self._chooser.display_song(song_info)
                elif response.status_code == 404:
                    messagebox.showinfo(title='Song Information', message="No Song in DB")

    def list_song(self):
        response = requests.get("http://localhost:5000/song/titles")
        title_list = [f'{s["title"]}' for s in response.json()]

        return title_list

    def add_song(self):
        selected_file = askopenfilename(initialdir="*.mp3",
                                        filetypes=(("MPR File", "*.mp3"), ("All Files", "*.*")),
                                        title="Choose a file.")
        if selected_file:
            mp3_file = eyed3.load(selected_file)
            file_name = os.path.basename(selected_file)
            value = eyed3.load(selected_file).info.time_secs
            min = int(value / 60)
            sec = int(value % 60)
            times = str(min) + ':' + str(sec)
            tags = ['title', 'artist', 'album', 'genre']

            title = getattr(mp3_file.tag, tags[0])
            artist = getattr(mp3_file.tag, tags[1])
            album = getattr(mp3_file.tag, tags[2])
            genre = getattr(mp3_file.tag, tags[3])

            data = {'file_name': file_name, 'title': title, 'artist': artist, 'runtime': times, 'album': album,
                    'genre': str(genre), 'location': selected_file}
            response = requests.post("http://localhost:5000/song", json=data)

            if response.status_code == 200:
                msg = f'{file_name} song added to DB.'
                messagebox.showinfo(title='Load Songs', message=msg)

    def play_window_popup(self):
        self._class_win = tk.Toplevel()
        self._class = PlaySongWindow(self._class_win,
                                     self._play_play, self._stop_play, self._pause_play, self._set_volume)
        title = self._chooser.get_title()
        response = requests.get("http://localhost:5000/song/titles")

        title_list_1 = [f'{s["file_name"]}' for s in response.json()]
        title_list_2 = [f'{s["title"]}' for s in response.json()]
        for i in range(len(title_list_2)):
            if title == title_list_2[i]:
                file_name = title_list_1[i]
                response = requests.get("http://localhost:5000/song/" + str(file_name))
                song_info = response.json()
                self._class.display_song(song_info)

    def _play_play(self):
        try:
            paused
        except NameError:
            file_path = self._class.get_file()
            mixer.init()
            mixer.music.load(file_path)
            mixer.music.play()
            #player = vlc.MediaPlayer(file_path)
            #player.play()
        else:
            mixer.music.unpause()

    def _stop_play(self):
        mixer.music.stop()
        #player.stop()

    def _pause_play(self):
        global paused
        paused = True
        mixer.music.pause()
        #player.pause()

    def _set_volume(self, val):
        volume = int(val)/100
        mixer.music.set_volume(volume)



if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack()
    tk.mainloop()