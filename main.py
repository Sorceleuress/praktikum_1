import tkinter as tk
root = tk.Tk()
root.title('Cookie clicker')
root.geometry('600x600')
c = tk.Canvas(width=600, height=600)
c.pack()

img1 = tk.PhotoImage(file='cookiee.png')
i1 = c.create_image(300, 300, image=img1)
count = 0
txt = c.create_text(125, 50, text=f'Количество очков: {count}', font='Verdana 14')


def left_click(event):
    global count
    global txt
    x, y = event.x, event.y
    if 250 <= x <= 350 and 250 <= y <= 350:
        count += 1

    c.delete(txt)
    txt = c.create_text(125, 50, text=f'Количество очков: {count}', font='Verdana 14')


root.bind('<Button-1>', left_click)
root.mainloop()

print(123123)