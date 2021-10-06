from math import pi
from tkinter import *
from PIL import  ImageTk, Image
from tkinter.filedialog import askopenfilename
import os
from pygame import mixer
import random
import time
from mutagen.mp3 import EasyMP3 as MP3

mixer.init()





class Music_player(Tk):
    def __init__(self):
        super().__init__()
        self.height = 530
        self.title("Omnific Music Player")
        self.width = 900
        self.geometry(f"{self.width}x{self.height}")
        self.minsize(width=self.width, height=self.height)
        self.maxsize(width=self.width, height=self.height)
        self.photos = []
        self.song_list = []
        self.paused = mixer.music.get_busy()
        self.volume_value = 0
        self.filename = NONE
        self.myslider2  = NONE
        self.song =NONE
        
    
    def icon_image(self):
        self.p1 = PhotoImage(file = 'images/favicon.png')
        self.iconphoto(False, self.p1)
        
        
    def Music_Display(self):
        frame = Frame(self, padx=10, pady=10, bg="#212021", borderwidth=3)
        frame.pack(side = LEFT, fill=BOTH)

        scrollbar = Scrollbar(frame, orient="vertical")
        self.song_list = Listbox(frame, width=30)
        self.song_list.pack(side=LEFT, fill=Y)
        scrollbar.pack(side=RIGHT, fill=BOTH)

            
            
    def Title(self):
        frame = Frame(self, padx=20, pady=10, bg="#212021", borderwidth=3)
        frame.pack(side = TOP, fill=BOTH)
        text = Label(frame, text="Welcome To Omnific Music Player", bg="#212021", fg="white", font="Lucida 20 bold")
        text.pack(fill=BOTH)        
    
    
    
        
        
    
    def music_playing(self):
        for i in range(1,5):
            image = Image.open(f"images/music{i}.jpg")
            image = image.resize((225, 225), Image.ANTIALIAS)
            self.photos.append(ImageTk.PhotoImage(image))
        
        frame = Frame(self, padx=10, pady=10, bg="#212021", borderwidth=5)
        frame.pack(fill=BOTH) 
        
        song_name = Text(frame)
        Label(song_name, image=random.choice(self.photos),anchor="e").pack(padx=7, pady=10)
        
        self.song = Label(frame,bg="white",width=40, anchor="nw" ,borderwidth=0, pady=20, font="lucida 12 bold")
        song_name.pack(fill=BOTH, side=LEFT)
        self.song.pack(fill=BOTH, side=LEFT)


    def song_info(self):
        
        # Time
        time_ = mixer.music.get_pos()/ 1000
        current_time = time.strftime('%H:%M:%S', time.gmtime(int(time_))) 
        
        # Song Length
        current_song = self.song_list.curselection()
        song = self.song_list.get(current_song)
        a = self.music_file.split(os.path.basename(self.music_file))[0]
        song = os.path.join(str(a), os.path.basename(self.song_list.get(ACTIVE)) )
        
        # mutagen
        song_mut = MP3(song)
        length = song_mut.info.length
        
       
       
        # changing time format
        song_length = time.strftime('%M:%S', time.gmtime(length))
        

        self.song.config(text = f"\tCurrent Song : {self.song_list.get(ACTIVE)}\n\nTime : {current_time}\n\nLength : {song_length}")
        self.song.after(1000, self.song_info)
        

        # title
        try:
            title = song_mut['title'][0]
            self.song.config(text = f"\tCurrent Song : {self.song_list.get(ACTIVE)}\n\nTime : {current_time}\n\nLength : {song_length}\n\n  Title = {title}")
        except Exception as e:
            e
      
        # Artist  
        try:
           artist = song_mut['artist'][0]
           self.song.config(text = f"\tCurrent Song : {self.song_list.get(ACTIVE)}\n\nTime : {current_time}\n\nLength : {song_length}\n\n  Title = {title}")
        except Exception as e:
            e
            
        # Album
        try:
            album = song_mut['album'][0]
            self.song.config(text = f"\tCurrent Song : {self.song_list.get(ACTIVE)}\n\nTime : {current_time}\n\nLength : {song_length}\n\n  Title = {title}\n\nArtist : {artist}\n\n\t Album : {album}")
        except Exception as e:
            e
        
              
        
    # Functions
    
    def add_music(self):
        self.music_file = askopenfilename(defaultextension=".mp3", filetypes=[("Music Files", "*.mp3")])
        if self.music_file != "":
            self.song_list.insert(END, os.path.basename(self.music_file))
    
    
    def delete_music(self):
        current_selection = self.song_list.curselection()
        if current_selection:
            self.song_list.delete(current_selection)
        else:
            self.song_list.delete(1)
    
    
    def play_music(self):
        for i in self.song_list.curselection():
            if self.music_file != None:  
                a = self.music_file.split(os.path.basename(self.music_file))[0]
                mixer.music.load(os.path.join(str(a), os.path.basename(self.song_list.get(ACTIVE))))
                mixer.music.play()
                try:
                    mixer.music.queue(os.path.join(str(a), os.path.basename(self.song_list.get(i+1))))
                    
                except Exception as e:
                    e
        self.song_info()
        
    def pause_music(self):
        if self.paused:
            mixer.music.unpause()
        
        if not self.paused:
            mixer.music.pause()
        
        self.paused = not self.paused

    
    def stop_music(self):
        mixer.music.stop()
        
    
    def volume(self, vol):
        vol = self.myslider2.get()
        volume = int(vol)/100
        mixer.music.set_volume(volume)
    
    def music_volume(self):
        frame = Frame(self, padx=10, pady=10, bg="#212021", borderwidth=5)
        frame.pack(side = TOP, fill=BOTH)
        self.myslider2 = Scale(frame,from_=0, to=100, orient=HORIZONTAL,troughcolor="white",command=self.volume, bg="#c88aff", fg="black",length=500 ,label="Volume",font="lucida 12 bold")
        self.myslider2.set(60)
        self.myslider2.pack(side=TOP)
        
    

    
    def button(self):
        frame = Frame(self, padx=10, pady=10, bg="#212021", borderwidth=5)
        frame.pack(side = TOP, fill=BOTH)
        
        Button(frame, text="Add",bg="#38ebe2",padx=10, pady=10, font="lucida 15 bold", command=self.add_music).pack(side=LEFT, padx=30)
        Button(frame, text="⏸️",bg="#fcef32", font="lucida 20 bold", command=self.pause_music).pack(side=LEFT, padx=20)
        Button(frame, text="▶",bg="#3bff29", font="lucida 20 bold", command=self.play_music).pack(side=LEFT, padx=20)
        Button(frame, text="⏹",bg="red", font="lucida 20 bold", command=self.stop_music).pack(side=LEFT, padx=20)
        Button(frame, text="Delete",bg="#38ebe2", font="lucida 15 bold",pady=10,command=self.delete_music).pack(side=LEFT, padx=30)
    
    
    def length_of_song():
        pass
    

    



if __name__ == '__main__':
    window = Music_player()
    window.Title()
    window.icon_image()
    window.Music_Display()
    window.music_playing()
    window.music_volume()
    window.button()
    window.mainloop()