from tkinter import *
slovarb={"USD":16.35,
         "RusRub":0.25,
         "Euro":25}
spisokvalut=["USD", "RusRub", "Euro"]
def convert():
    eitog.delete(0,END)
    eitog.insert(0, int(evvod.get())*slovarb[valuta.get()])
    evvod.delete(0,END)
root=Tk()
root.geometry("320x200")
root.title("Конвертер")
root['bg']='orange'
lblvvod=Label(text="Введите сумму в валюте:", bg='orange', font=10)
lblvvod.grid(column=1, row=1)
evvod=Entry(width=10,)
evvod.grid(column=2, row=1)
lblvaluta=Label(text="Выберете валюту:", bg='orange', font=10)
lblvaluta.grid(column=1, row=2)
valuta=StringVar(value=spisokvalut[0])
valuti=OptionMenu(root,valuta,spisokvalut[0], spisokvalut[1],spisokvalut[2])
valuti.grid(column=2, row=2)
btn=Button(text="Конвертировать", bg="grey", command=convert)
btn.grid(column=1, row=3)
lblitog=Label(text="Итоговая сумма в рублях ПМР:", bg='orange', font=10)
lblitog.grid(column=1, row=4)
eitog=Entry(width=10)
eitog.grid(column=2,row=4)
mainloop()