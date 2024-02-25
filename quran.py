from tkinter import *
import pygame
from PIL import ImageTk, Image
from tkinter import ttk

pygame.mixer.init()

def all_sounds():
    al_fatiha = "السور/al fatiha (الفاتحة).mp3"
    al_fatiha = al_fatiha.replace("السور/", "")
    al_fatiha = al_fatiha.replace(".mp3", "")
    sound_list.insert(END, al_fatiha)

    al_baqarah = "السور/al baqarah (البقرة).mp3"
    al_baqarah = al_baqarah.replace("السور/", "")
    al_baqarah = al_baqarah.replace(".mp3", "")
    sound_list.insert(END, al_baqarah)


def play_sound():
    global surah
    surah = sound_list.get(ACTIVE)
    surah = f"السور/{surah}.mp3"
    pygame.mixer.music.load(surah)
    pygame.mixer.music.play(loops=0)


count = 0
def pause():
    global count
    if count == 0:
        pygame.mixer.music.pause()
        count = 1
    elif count == 1:
        pygame.mixer.music.unpause()
        count = 0


def vol(x):
    pygame.mixer.music.set_volume(volumeS.get())

def Length(x):
    sliderL.config(text=int(slider.get()))


def stop_sound():
    pygame.mixer.music.stop()

def next():
    nextS = sound_list.curselection()
    nextS = nextS[0] + 1
    surah = sound_list.get(nextS)
    surah = f"السور/{surah}.mp3"
    pygame.mixer.music.load(surah)
    pygame.mixer.music.play(loops=0)

    sound_list.selection_clear(0, END)
    sound_list.activate(nextS)
    sound_list.selection_set(nextS, last=None)


def pre():
    preS = sound_list.curselection()
    preS = preS[0] - 1
    surah = sound_list.get(preS)
    surah = f"السور/{surah}.mp3"
    pygame.mixer.music.load(surah)
    pygame.mixer.music.play(loops=0)

    sound_list.selection_clear(0, END)
    sound_list.activate(preS)
    sound_list.selection_set(preS, last=None)


def Main_root():
    global mainroot
    mainroot = Tk()
    mainroot.title("tilawat ali jaber")
    mainroot.geometry("600x400")
    mainroot.resizable(width=False, height=False)
    mainroot.configure(bg="#d1a054")

    lbl = Label(mainroot, text="الشيخ علي جابر", font=('arial', 18), bg="#d1a054")
    lbl. place(x=230, y=15)

    img = Image.open("256x256bb.jpg")
    img_tk = ImageTk.PhotoImage(img)
    img_lbl = Label(image=img_tk)
    img_lbl.place(x=175, y=50)

    button = Button(mainroot, text="السور", command=Root)
    button.place(x=275, y=350)

    mainroot.mainloop()


def Root():
    global slider
    global sliderL
    global volumeS
    global sound_list
    global root
    root = Tk()
    root.geometry("600x400")
    root.title("tilawat ali jaber")
    root.resizable(width=False, height=False)
    root.configure(bg="#d1a054")
    #
    sound_list = Listbox(root, bg="gray", fg="white", width=70, height=16)
    sound_list.place(x=150, y=50)
    #
    all_sounds()
    #
    playB = Button(root, text="تشغيل", command=play_sound)
    playB.place(x=350, y=375)
    pauseB = Button(root, text="ايقاف", command=pause)
    pauseB.place(x=400, y=375)
    stopB = Button(root, text="انهاء", command=stop_sound)
    stopB.place(x=300, y=375)
    nextB = Button(root, text="التالي",width=10, height=5, command=next)
    nextB.place(x=73, y=100)
    preB = Button(root, text="السابق",width=10, height=5, command=pre)
    preB.place(x=73, y=200)

    backB = Button(root, text="العودة الى الصفحة الرئيسية", command=main)
    backB.place(x=0, y=380)

    #
    volumeS = ttk.Scale(root, from_=0, to=1, orient=VERTICAL, value=1, command=vol)
    volumeS.place(x=0, y=100)


    slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, length=424, command=Length)
    slider.place(x=150, y=315)
    sliderL = Label(root, text="0")
    sliderL.place(x=300, y=350)

    mainroot.destroy()
    root.mainloop()


def main():
    global mainroot
    root.destroy()
    mainroot = Tk()
    mainroot.geometry("600x400")
    mainroot.resizable(width=False, height=False)
    mainroot.configure(bg="#d1a054")

    lbl = Label(mainroot, text="الشيخ علي جابر", font=('arial', 18), bg="#d1a054")
    lbl. place(x=230, y=15)

    img = Image.open("256x256bb.jpg")
    img_con = ImageTk.PhotoImage(img)
    img_lbl = Label(image=img_con)
    img_lbl.place(x=175, y=50)

    button = Button(mainroot, text="السور", command=Root)
    button.place(x=275, y=350)


    mainroot.mainloop()


Main_root()