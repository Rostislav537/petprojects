import conectLIB
from tkinter import *
def led_reverse():
    if btn['text']=="Включить":
        f.led(1)
        btn['text'] = "Выключить"
    else:
        f.led(0)
        btn['text'] = "Включить"
def Buzzer_reverse():
    if btn2['text']=="Включить зуммер":
        f.zummer(1)
        btn2['text'] = "Выключить зуммер"
    else:
        f.zummer(0)
        btn2['text'] = "Включить зуммер"
f=conectLIB.connect_to_server("192.168.0.43", 8000)
f.connect_to_s()
root=Tk()
root.geometry("320x200")
root.title("SmartHouse")
root['bg']='orange'
btn=Button(text="Включить", bg="grey", command=led_reverse)
btn.pack( )
btn2=Button(text="Включить зуммер", bg="grey", command=Buzzer_reverse)
btn2.pack( )
mainloop()