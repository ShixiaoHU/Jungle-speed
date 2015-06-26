import model, test

from tkinter import *


class Controller():

    def __init__(self):
        pass
        
    def run(self):
        self.root = Tk()
        self.app = test.Application(master=self.root)
        self.callcard()
        self.root.resizable(width=FALSE, height=FALSE)
        nextButton = self.app.setNextButton()

        endButton = self.app.setEndButton()
        nextButton.bind('<Button-1>', self.nextCtrl)
        endButton.bind('<Button-1>', self.endCtrl)

        self.root.bind('<Key>', self.keypress)

        self.app.mainloop()


    def keypress(self, event):
        if  self.check():
            if event.keysym == 'Control_L' or event.keysym == 'Control_R':
                #self.end()
                if event.keysym == 'Control_L':
                    print('Left WIN')
                elif event.keysym == 'Control_R':
                    print('Right WIN')
        else:
            if event.keysym == 'Control_L' or event.keysym == 'Control_R':
                if event.keysym == 'Control_L':
                    print('Left LOSE')
                elif event.keysym == 'Control_R':
                    print('Right LOSE')
                
    
    def check (self):
        if self.c1.color == self.c2.color:
            if self.c1.number == self.c2.number:
                return True
        else:
            return False
            
    def callcard(self):
        self.c1 = model.Card()
        self.c2 = model.Card()
        self.app.setPhoto(self.c1)
        self.app.setPhoto(self.c2)
        
    def setButton(self):
        self.next = Button(self, text="next", command=next)
        self.next.pack(side=LEFT)
        
        self.end = Button(self, text="end", command=self.quit)
        self.end.pack(side=RIGHT)
    
    def nextCtrl(self, event):
        #print ('next ctrl')
        self.end()
        self.run()

    def endCtrl(self, event):
        self.end()

    #def judge(self, callback):
        #if callback == 2:
            #self.next()
        #else:
            #self.end()
    
    def end(self):
        self.root.destroy()

ctrl = Controller()
ctrl.run()