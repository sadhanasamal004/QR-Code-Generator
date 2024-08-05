                            # PROJECT 6: QR CODE GENERATOR


from tkinter import *
import pyqrcode
from PIL import ImageTk,Image

root=Tk()

def generate():
    link_name=entry_name.get()
    link=entry_link.get()
    file_name=link_name + ".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,400,window=image_label)

canvas=Canvas(root,width=400,height=600)
canvas.pack()

label=Label(root,text='QR Code Generator',fg='blue',font=('Algerian',25))
canvas.create_window(200,50,window=label)

name_label=Label(root,text='Link name:',font=('Cascadia Code',15))
link_label=Label(root,text='Link:',font=('Cascadia Code',15))
canvas.create_window(100,100,window=name_label)
canvas.create_window(70,150,window=link_label)

entry_name=Entry(root)
entry_link=Entry(root)
canvas.create_window(230,100,window=entry_name)
canvas.create_window(180,150,window=entry_link)

button=Button(root,text='Generate QR Code',font=('Elephant',12),command=generate)
canvas.create_window(200,200,window=button)

root.mainloop()