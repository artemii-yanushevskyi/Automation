# a.grid(row = k, column = n, sticky = (N, S, E, W), padx = 5(px), pady = 5(px))

from tkinter import *
from Polynomial import Polynomial

# s = StringVar()
# IntVar()
# FloatVar()
# BooleanVar()
# s.get()
# Entry(top, textvariable = s)
# s.set() # changes s value in corresponding field
# p1 = a0x^n + a1x^n-1 + ... + an
# p = p1*p2 + p1
# result p
# t24.10

top = Tk()

class WidgetEditor:
    def __init__(self, master, coef1, coef2, n, stringExpression, has_buttons = True):
        self.master = master
        self.coef1 = coef1
        self.coef2 = coef2
        self.pow = n
        self.exprE = stringExpression
        self.has_buttons = has_buttons
        self._make_widgets()
        # self.master.minsize(width=666, height=666)
        print('in')
        
    def _make_widgets(self):
        self.fedet = Frame(self.master, relief = 'sunken')
        self._make_label_entries()
        self._layout_labels_entries()
        if self.has_buttons:
            fbut = Frame(self.master)
            fbut.grid(row = 4, column = 0, sticky = ('n'))
            # exit button
            bexit = Button(fbut, text = 'Exit', command = self.exit_handler)
            bexit.grid(row = 3, column = 1, sticky = ('w'), padx = 5, pady = 5)
            # ok button
            bok = Button(fbut, text = 'Ok', command = self.ok_handler)
            bok.grid(row = 3, column = 0, sticky = ('w'), padx = 5, pady = 5)
            # configure
            fbut.rowconfigure(0, weight = 1)
            
    def exit_handler(self):
        exit()
    
    def ok_handler(self):
        c = []
        d = []
        for i in range(self.pow + 1):
            print(self.entries1[i].get())
            c.append(self.entries1[i].get())
        print('next')
        for i in range(self.pow + 1):
            print(self.entries2[i].get())
            d.append(self.entries2[i].get())
        c = Polynomial(list(map(float, c)))
        d = Polynomial(list(map(float, d)))
        # get operation
        if '+' in self.enterOperation.get():
            r = c + d
            self.answer.config(text = str(r))
        if '*' in self.enterOperation.get():
            r = c * d
            self.answer.config(text = str(r))
        if '-' in self.enterOperation.get():
            r = c - d
            self.answer.config(text = str(r))

        
    def _make_label_entries(self):
        self.var1 = []
        self.labels1 = []
        self.entries1 = []
        # first line
        self.poly1 = Label(self.fedet, text = 'P1')
        for k in range(self.pow + 1):
            self.labels1.append(Label(self.fedet, text = 'a[' + str(k) + '] = '))
            self.var1.append(StringVar())
            self.var1[len(self.var1) - 1].set(self.coef1[k])
            self.entries1.append(Entry(self.fedet, textvariable = self.var1[len(self.var1) - 1]))
        self.var2 = []
        self.labels2 = []
        self.entries2 = []
        
        # second line
        self.poly2 = Label(self.fedet, text = 'P2')
        for k in range(self.pow + 1):
            self.labels2.append(Label(self.fedet, text = 'b[' + str(k) + '] = '))
            self.var2.append(StringVar())
            self.var2[len(self.var2) - 1].set(self.coef2[k])
            self.entries2.append(Entry(self.fedet, textvariable = self.var2[len(self.var2) - 1]))

        fbut1 = Frame(self.master)
        fbut1.grid(row = 3, column = 0, sticky = ('n'))
        
        self.info1 = Label(self.fedet, text = 'Enter operation')
        self.enterOperation = Entry(self.fedet, textvariable = StringVar())
        self.answer = Label(fbut1, text = 'Here goes the answer')
        
    def _layout_labels_entries(self):
        self.poly1.grid(row = 0, column = 0, sticky = ('w'), padx = 2, pady = 2)
        for i in range(1, self.pow + 2):
            self.labels1[i-1].grid(row = 0, column = 2*i, sticky = ('w'), padx = 2, pady = 2)
            self.entries1[i-1].grid(row = 0, column = 2*i+1, sticky = ('w'), padx = 2, pady = 2)
        self.fedet.grid(row = 0, column = 0, sticky = ('W', 'E', 'N', 'S'))
        self.master.columnconfigure(0, weight = 1)
        for i in range(1, 2*self.pow + 1):
            self.fedet.columnconfigure(i, weight = 1)

        self.poly2.grid(row = 1, column = 0, sticky = ('w'), padx = 2, pady = 2)
        for i in range(1, self.pow + 2):
            self.labels2[i-1].grid(row = 1, column = 2*i, sticky = ('w'), padx = 2, pady = 2)
            self.entries2[i-1].grid(row = 1, column = 2*i+1, sticky = ('w'), padx = 2, pady = 2)
        self.fedet.grid(row = 1, column = 0, sticky = ('W', 'E', 'N', 'S'))
        self.master.columnconfigure(0, weight = 1)
        for i in range(1, 2*self.pow + 1):
            self.fedet.columnconfigure(i, weight = 1)

            
        self.info1.grid(row = 3, column = 0, sticky = ('w'),padx = 5, pady = 5)
        self.enterOperation.grid(row = 3, column = 1, sticky = ('w'))
        self.answer.grid(row = 4, column = 2, sticky = ('n'))


a = WidgetEditor(top, [0, 2, 4, 6], [3, 5, 7, 4], 3, 'fff')
top.mainloop()
