from tkinter import *


class Tablero(Tk):
    def __init__(self, *args, **hwargs):
        super().__init__(*args, **hwargs)
        self.geometry("640x640")
        self.tablero = Canvas(self)
        self.tablero.pack(fill="both", expand=1)
        self.cuadrado()


    def cuadrado(self):
        cont = 0

        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0:
                    self.tablero.create_rectangle(j*80, i*80, (j+1)*80, (i+1)*80, fill="black")
                    if(cont<12):
                        self.tablero.create_oval(j*80, i*80, (j+1)*80, (i+1)*80, fill="red")
                    if(cont>19):
                        self.tablero.create_oval(j*80, i*80, (j+1) * 80, (i+1) * 80, fill="blue")
                    cont = cont+1
                else:
                    self.tablero.create_rectangle(j*80, i*80, (j+1)*80, (i+1)*80, fill="white")

if __name__ == "__main__":
    app = Tablero()
    app.mainloop()