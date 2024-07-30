from tkinter import*
import random
import calendar
from tkinter import messagebox
from PIL import Image, ImageTk

win = Tk()
win.geometry('1000x680+300+20')
win.config(bg='White')

def show():
    m = int(month.get())
    y = int(year.get())
    output = calendar.month(y,m)
    print(cal.insert('end', output))

def clear():
    cal.delete(1.0, 'end')


img = Image.open('cal_pic/22.jpeg')
img = img.resize((999,679), Image.BILINEAR)
pic_img = ImageTk.PhotoImage(img)
lbl_img = Label(win, image=pic_img, bd=4, relief=RIDGE)
lbl_img.place(x=0, y=0)

frame_cal = LabelFrame(win, text='Calendar', bg='Deepskyblue', fg='darkgreen', font=('Didot', 16))
frame_cal.place(x=300, y=80, width=420, height=440)

m_lbl = Label(frame_cal, text='Month', font=('Didot', 18), fg='darkorange', bg='Deepskyblue')
m_lbl.place(x=15, y=10)
month = Spinbox(frame_cal, from_= 1, to=12, width=6, font=('Didot', 20), fg='darkorange')
month.place(x=100, y=10)

y_lbl = Label(frame_cal, text='Year', font=('Didot', 18), fg='darkorange', bg='Deepskyblue')
y_lbl.place(x=220, y=10)
year = Spinbox(frame_cal, from_= 1900, to=2050, width=6, font=('Didot', 20), fg='darkorange')
year.place(x=290, y=10)

cal = Text(frame_cal, font=('Didot', 20), bg='LemonChiffon', fg='darkgreen', width=22, height=8, relief=RIDGE, borderwidth=1)
cal.place(x=45, y=70)

# -------- Buttons -------
show = Button(frame_cal, text='Show', font=('Didot', 18), fg='darkgreen', command=show, width=6)
show.place(x=20, y=350)

exit_btn = Button(frame_cal, text='Exit', font=('Didot', 18), fg='darkorange', command=exit, width=6)
exit_btn.place(x=160, y=350)

clear = Button(frame_cal, text='Clear', font=('Didot', 18), fg='darkgreen',command=clear, width=6)
clear.place(x=300, y=350)

win.mainloop()
