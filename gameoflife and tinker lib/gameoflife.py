from random import randint
from tkinter import *
from time import sleep


SIZE=21
OFFSET= 21.9

def event(p):
    return(randint(0,100) < p)

def paint(self):
   python_green = "#476042"
   x1, y1 = ( self._x - 1 ), ( self._y - 1 )
   x2, y2 = ( self._x + 1 ), ( self._y + 1 )
   self._canvas.create_oval( x1, y1, x2, y2, fill = python_green )

class Example(Frame):
    _grid = [[0 for x in range(SIZE)] for y in range(SIZE)]
    def  __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    class Node:
        def __init__(self, canvas, x, y):
            self._canvas = canvas
            self._state = randint(0,3)
            self.updateState(self._state)
            self._rect = canvas.create_rectangle(x, y , x+OFFSET, y+OFFSET, outline="#000", fill=self._color)

        def getState(self):
            return  self._state

        def updateState(self, state):
            self._state = state
            # 0 defective “red”
            if self._state == 0:
                self._color = "#FF0000"
            # 1 new “dark green”
            if self._state == 1:
                self._color = "#006400"
            # 2 normal “green”
            if self._state == 2:
                self._color = "#32CD32"
            # 3 aged “light green”
            if self._state == 3:
                self._color = "#ADFF2F"

        def update(self, repair, Neighborstate):
            if(self._state == 0):
                # repair: % of defective cells (total # of defective cells divided by total # of cells)
                if event(repair):
                    self.updateState(1)
            if(self._state == 1):
                # install: 40%
                if event(40):
                    self.updateState(2)
                # lemon: 5%
                if event(5):
                    self.updateState(1)
            if(self._state == 2):
                # wear & tear: 5%
                if event(5):
                    self.updateState(3)
                # prevention: 15%
                if event(15):
                    self.updateState(1)
                # neighbor: 20% if one of the possible 8 (max) neighboring cells is defective
                if Neighborstate == 0:
                    if event(20):
                        self.updateState(0)
            # decay: 10%
            if(self._state == 3):
                if event(10):
                    self.updateState(0)
            self._canvas.itemconfig(self._rect, fill=self._color)

    def initUI(self):

        def paint( event ):
           python_green = "#476042"
           x1, y1 = ( event.x - 1 ), ( event.y - 1 )
           x2, y2 = ( event.x + 1 ), ( event.y + 1 )
           canvas.create_oval( x1, y1, x2, y2, fill = python_green )

        self.parent.title("Colours")
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        x = 0
        y= 0
        for i in range(SIZE):
            x = 0;
            for j in range(SIZE):
                self._grid[i][j] = self.Node(canvas, x, y)
                x = x + OFFSET
            y = y + OFFSET
        canvas.pack(fill=BOTH, expand=1)
        canvas.pack(expand = YES, fill = BOTH)
        canvas.bind( "<B1-Motion>", paint )

        #button 100
        button = Button(canvas, text ="Next 100 day", command= self.next100Day)
        button.pack(side=BOTTOM, expand = NO)
        #button 10
        button = Button(canvas, text ="Next 10 day", command= self.next10Day)
        button.pack(side=BOTTOM, expand = NO)
        #button
        button = Button(canvas, text ="Next day", command= self.nextDay)
        button.pack(side=BOTTOM, expand = NO)


    def checkNeighbor(self, i , j):
        Neighborstate = 1
        try:
            if self._grid[i+1][j].getState() == 0:
                Neighborstate = 0;
        except IndexError:
            pass
        try:
            if self._grid[i+1][j+1].getState() == 0:
                Neighborstate = 0;
        except IndexError:
            pass
        try:
            if self._grid[i+1][j-1].getState() == 0:
                Neighborstate = 0;
        except IndexError:
            pass
        try:
            if self._grid[i-1][j].getState() == 0:
                Neighborstate = 0;
        except IndexError:
            pass
        try:
            if self._grid[i-1][j+1].getState() == 0:
                Neighborstate = 0;
        except IndexError:
            pass
        try:
            if self._grid[i-1][-j].getState() == 0:
                Neighborstate = 0;
        except IndexError:
            pass
        try:
            if self._grid[i][j-1].getState() == 0:
                Neighborstate = 0;
        except IndexError:
            pass
        try:
            if self._grid[i][j+1].getState() == 0:
                Neighborstate = 0;
        except IndexError:
            pass
        return Neighborstate

    def nextDay(self):
        defective_cell =0;
        for i in range(SIZE):
            for j in range(SIZE):
                if self._grid[i][j].getState()== 0:
                    defective_cell = defective_cell + 1;
        repair = defective_cell / (SIZE*SIZE) * 100
        for i in range(SIZE):
            for j in range(SIZE):
                self._grid[i][j].update(repair, self.checkNeighbor(i, j));
        print("Defective Cell%: ")
        print(repair)

    def next10Day(self):
        for x in range(0, 10):
            defective_cell =0;
            for i in range(SIZE):
                for j in range(SIZE):
                    if self._grid[i][j].getState()== 0:
                        defective_cell = defective_cell + 1;
            repair = defective_cell / (SIZE*SIZE) * 100
            for i in range(SIZE):
                for j in range(SIZE):
                    self._grid[i][j].update(repair, self.checkNeighbor(i, j));
        print("Defective Cell%: ")
        print(repair)

    def next100Day(self):
        for x in range(0, 100):
            defective_cell =0;
            for i in range(SIZE):
                for j in range(SIZE):
                    if self._grid[i][j].getState()== 0:
                        defective_cell = defective_cell + 1;
            repair = defective_cell / (SIZE*SIZE) * 100
            for i in range(SIZE):
                for j in range(SIZE):
                    self._grid[i][j].update(repair, self.checkNeighbor(i, j));
        print("Defective Cell%: ")
        print(repair)


def main():
    root = Tk()
    ex = Example(root)
    root.geometry("920x550+0+0")
    root.mainloop()

if __name__ == '__main__':
    main()
