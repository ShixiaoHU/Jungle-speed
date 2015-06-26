from tkinter import *



class Application(Frame):


    def setPhoto(self, card):
        self.background = Canvas(self)
        self.background.pack()
        self.background.create_rectangle(1000,\
            1000, 0, 100, fill=card.color)
        self.numb = self.background.create_text(10, 10, font=(10))
        self.background.itemconfig(self.numb, text=card.number)

    
    def setNextButton(self):
        self.next = Button(self, text="next")
        self.next.pack(side=LEFT)
        
        return self.next

    def setEndButton(self):
        self.end = Button(self, text="end")
        self.end.pack(side=RIGHT)
        
        return self.end
    
    def result(self, resu):
        self

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        master.minsize(width=1000, height=700)