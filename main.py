from tkinter import *
from tkinter.messagebox import showinfo


def donothing():
    x = 0


root = Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("Control de Ventas Dinastia 777")
label = Label(root, text="Control de Ventas Dinastia 777")
label.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Agregar Producto", command=donothing)
filemenu.add_command(label="Venta", command=donothing)
filemenu.add_command(label="Ingresos Extra", command=donothing)
filemenu.add_command(label="Gastos", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Corte Semanal", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Ventas", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Indice de Ayuda", command=donothing)
helpmenu.add_command(label="Acerca...", command=donothing)
menubar.add_cascade(label="Ayuda", menu=helpmenu)


productos = ('Jitomate', 'Serrano', 'Jalapeño', 'Húngaro', 'Habanero',
         'Caloro', 'Morrón', 'Pepino Persa', 'Limón')

var = Variable(value=productos)

listbox = Listbox(
    root,
    listvariable=var,
    height=6,
    selectmode=EXTENDED)

listbox.pack(expand=True, fill=BOTH, side=LEFT)

scrollbar = Scrollbar(
    root,
    orient=VERTICAL,
    command=listbox.yview
)

listbox['yscrollcommand'] = scrollbar.set

scrollbar.pack(side=LEFT, expand=True, fill=Y)


def items_selected(event):
    selected_indices = listbox.curselection()
    selected_langs = ",".join([listbox.get(i) for i in selected_indices])
    msg = f'You selected: {selected_langs}'

    showinfo(title='Information', message=msg)


listbox.bind('<<ListboxSelect>>', items_selected)

root.config(menu=menubar)
root.mainloop()