from tkinter import *
import pafy

app=Tk()
app.geometry("650x400")
app.title("Youtube Downloader")
app.config(bg="purple")


class App(object):
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False

    def keyPressed(self,event):
        print("HERE")
        if event.keysym =='Escape':
            root.destroy()
        elif event.keysym == 'Right':
            self.right = True
        elif event.keysym == 'Left':
            self.left = True
        elif event.keysym == 'Up':
            self.up = True

    def keyReleased(self,event):
        if event.keysym == 'Right':
            self.right = False
        elif event.keysym == 'Left':
            self.left = False
        elif event.keysym == 'Up':
            self.up = False
application = App()


def dwnload():

    url=e1.get()
    print(url)
    #url = "https://www.youtube.com/watch?v=N_iW0VC3IdI"
    video = pafy.new(url)

    streams = video.videostreams
    for i in streams:
        print(i)

    # get best resolution regardless of format
    best = video.getbest()

    print(best.resolution, best.extension)
    print(best.get_filesize())

    # Download the video
    best.download()



#pw = PanedWindow(orient ='vertical' )

title=Label(app,text="Youtube Downloader ", font=("algerian",40,"bold"), bg="purple", fg="white")
title.pack(side=TOP)

l1=Label(app,text="Enter video URL :", font=("algerian",20,"bold"), bg="purple", fg="white")
l1.pack(side = TOP)

string=StringVar()

e1=Entry(app, textvariable = string, font =('arial', 30, 'bold') ,width='50')
e1.pack(side = TOP ,fill=BOTH)

b1=Button(app, text = "Click here !!" ,font =('arial',25, 'bold' ) ,bg='green', command="dwnload")
b1.pack(side = TOP)

copyright=Label(app, text = "All rights reserved by SUBUSTAR's software product.Ltd.,",  font =('arial', 10, 'bold'))
copyright.pack(side=BOTTOM)



app.bind_all('<Key>', application.keyPressed)
app.bind_all('<KeyRelease>', application.keyReleased)
app.bind('<Return>',lambda e:dwnload())
#windows executions



app.mainloop()