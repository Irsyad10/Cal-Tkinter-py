from tkinter import *

def MyCalc(source, side):
    sObj = Frame(source, borderwidth=4, bd=4, bg='powder blue')
    sObj.pack(side=side, expand=YES, fill=BOTH)
    return sObj

def tombol(source, side, text, command=None, bg='powder blue'):
    sObj = Button(source, text=text, command=command, bg=bg)
    sObj.pack(side=side, expand=YES, fill=BOTH)
    return sObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Kalkulator')

        display = StringVar()
        Entry(self, relief=FLAT, textvariable=display, bd=30, bg='white').pack(side=TOP, expand=YES, fill=BOTH)

        for TombAngka in ('789', '456', '123', '0.+', '/*-'):
            fNum = MyCalc(self, TOP)
            for isdm in TombAngka:
                tombol(fNum, LEFT, isdm, lambda sObj=display, q=isdm: sObj.set(sObj.get() + q))

        for TombolC in (['C']):
            ers = MyCalc(self, RIGHT)
            for ichar in TombolC:
                tombol(ers, RIGHT, ichar, lambda sObj=display, q=ichar: sObj.set(''), bg='red')
        
        SamaDengan = MyCalc(self, LEFT)
        for sd in '=':
            if sd == '=':
                TombolSama = tombol(SamaDengan, LEFT, sd)
                TombolSama.bind('<ButtonRelease-1>', lambda e,s=self, sObj=display: s.hitung(sObj), '+')
            else:
                TombolSama = tombol(SamaDengan, LEFT, sd, lambda sObj=display, s=' %s ' % sd: sObj.set(sObj.get()+s))
        
    def hitung(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set('ERROR')

if __name__=='__main__':
    Tk.mainloop(app())