# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos
# seleccionables, también debe de tener un label con el texto que queráis.

import tkinter

# Imprime por consola el valor seleccionado de la listbox
def selected_item():
    for i in listbox.curselection():
        print(listbox.get(i))


def close_window():
    window.quit()


window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=3)

lista = ['Windows', 'MacOs', 'Linux', 'BeOs', 'OS/2', 'MS-DOS']
lista_items = tkinter.StringVar(value=lista)

label_titulo = tkinter.Label(window, text="Selecciona un sistema operativo")
listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
cerrar_ventana = tkinter.Button(window, text="Cerrar", command=close_window)
ver_seleccion = tkinter.Button(window, text="Ver selección", command=selected_item)

label_titulo.grid(column=0, row=0, sticky=tkinter.W, ipady=10, ipadx=10)
listbox.grid(column=0, row=1, sticky=tkinter.N, ipadx=5, ipady=5)
cerrar_ventana.grid(column=0, row=2, sticky=tkinter.W)
ver_seleccion.grid(column=0, row=4, sticky=tkinter.W)

window.mainloop()
