# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que
# contenga un botón de reinicio para que deje todo como al principio.
#
# Al principio no tiene que haber una opción seleccionada.

# import tkinter
from tkinter import *


def reset():
    seleccionado.set(None)

def cerrarVentana():
    window.quit()

window = Tk()
window.columnconfigure(3, weight=5, minsize=80)
window.rowconfigure(4, weight=5, minsize=20)

seleccionado = StringVar()
reset()

r1 = Radiobutton(window, text='Sí', value='1', variable=seleccionado)
r2 = Radiobutton(window, text='No', value='2', variable=seleccionado)
r3 = Radiobutton(window, text='Puede ser', value='3', variable=seleccionado)
clear = Button(window, text='Reset', command=reset)
cerrar = Button(window, text='Cerrar', command=cerrarVentana)

r1.grid(column=1, row=1, padx=2, pady=2, sticky=W)
r2.grid(column=1, row=2, padx=2, pady=2, sticky=W)
r3.grid(column=1, row=3, padx=2, pady=2, sticky=W)
clear.grid(column=2, row=4, padx=2, pady=2, sticky=E)
cerrar.grid(column=3, row=4, padx=2, pady=2, sticky=E)

window.mainloop()