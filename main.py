from tkinter import *
import math

window = Tk()


def add():
    count = int(entry.get()) * 60  # Convert input to seconds
    countdown(count)


def countdown(count):
    count_min = math.floor(count / 60)
    count_second = count % 60

    if count_min == 0 and count_second == 0:
        canvas.itemconfig(img_display, image=ringing_img)
    else:
        if count_second < 10:
            count_second = f"0{count_second}"
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")

        if count > 0:
            window.after(1000, countdown, count - 1)


window.title("Alarm")
window.config(padx=630, pady=50, bg="black")

text_label = Label(text="Reminder", fg="pink", bg="black", font=("Noto Serif", 40, "bold"))
text_label.grid(column=1, row=0)
text_label2 = Label(text=" ", fg="pink", bg="black", font=("Noto Serif", 20, "bold"))
text_label2.grid(column=1, row=2)

alarm_img = PhotoImage(file="alarm.png")
ringing_img = PhotoImage(file="ringingAlarm.png")

canvas = Canvas(width=300, height=350, bg="blue", highlightthickness=0)
img_display = canvas.create_image(150, 150, image=alarm_img)
timer_text = canvas.create_text(150, 320, text="00:00", fill="white", font=("Noto Serif", 50, "bold"))
canvas.grid(column=1, row=1)

add_button = Button(text="Add Timer", highlightthickness=0, font=("Noto Serif", 10), command=add)
add_button.grid(column=2, row=3)

entry = Entry(width=20, font=("Noto Serif", 15, "bold"))
entry.grid(column=1, row=3)

window.mainloop()
