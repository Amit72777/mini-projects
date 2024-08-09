import tkinter as tk
from tkinter import ttk
import random
from PIL import Image

# Global variable for animation control
global anim
count = 0

# ______________ Functions _____________


def calculateFrame(img):
    """ Get all frames from a GIF image """
    image = Image.open(img)
    image_count = image.n_frames
    frames = [tk.PhotoImage(file=img, format=f"gif -index {i}") for i in range(image_count)]
    return frames, image_count


def animation(frames, cnt, count):
    """ Display GIF frames in sequence """
    global anim
    gif_labe.config(image=frames[count], bg='pink', foreground='pink')
    count += 1
    if count == cnt:
        count = 0
    anim = win.after(100, lambda: animation(frames, cnt, count))


def yesPhase():
    """ Actions when 'Yes' is pressed """
    global anim
    win.after_cancel(anim)
    frames, cnt = calculateFrame("t5.gif")
    animation(frames, cnt, 0)
    sub_tittle.config(text="I knew it!")
    question_label.config(text="I Love you too 🥰🥰")
    yes_btn.destroy()
    no_btn.destroy()


def firstPhase():
    """ First phase of 'No' response """
    global anim
    win.after_cancel(anim)
    frames, cnt = calculateFrame("reqest.gif")
    animation(frames, cnt, 0)
    sub_tittle.config(text="itti jaldi nhi mat bol 😎")
    question_label.config(text="Soch lo Acche se! 🙄")
    no_btn.config(command=SecondPhase)


def SecondPhase():
    """ Second phase of 'No' response """
    global anim
    win.after_cancel(anim)
    frames, cnt = calculateFrame("t3.gif")
    animation(frames, cnt, 0)
    gif_labe.config(bg='pink')
    sub_tittle.config(text="Kyu Aise ka rhi h 😥")
    question_label.config(text="Ek baar aur Soch le 😕😕")
    no_btn.config(command=thridPhase)


def thridPhase(event=None):
    """ Third phase of 'No' response """
    global anim
    win.after_cancel(anim)
    frames, cnt = calculateFrame("t4.gif")
    animation(frames, cnt, 0)
    sub_tittle.config(text="bahut galat baat h 😕")
    question_label.config(text="Man ja na! kitta bhav khayegi 😭")
    no_btn.bind("<Enter>", move_action)


def move_action(event=None):
    """ Move the 'No' button to a random position """
    new_x = random.randint(0, win.winfo_width() - no_btn.winfo_width())
    new_y = random.randint(0, win.winfo_height() - no_btn.winfo_height())
    no_btn.place(x=new_x, y=new_y)


# Main window setup
FONT = ('Times New Roman', 30, 'bold')
win = tk.Tk()
win.title("Love Proposal")
win.config(bg='pink')
win.minsize(width=800, height=700)

# GIF label setup
gif_labe = tk.Label(win, bg='pink')
gif_labe.pack()

# Start the initial GIF animation
frames, cnt = calculateFrame("t1.gif")
animation(frames, cnt, 0)

# Question label
question_label = tk.Label(win, text="Do you love me 🙄🙄 ?", font=FONT, bg='pink')
question_label.pack()

# Subtitle label
sub_tittle = tk.Label(win, text="Request for you", font=('Times New Roman', 15, 'normal'), bg="pink")
sub_tittle.pack()

# Buttons setup
yes_btn = ttk.Button(win, text="Yes", command=yesPhase)
yes_btn.pack()

no_btn = ttk.Button(win, text="No", command=firstPhase)
no_btn.pack()

# Run the application
win.mainloop()
