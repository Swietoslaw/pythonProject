# -*- coding: utf-8 -*-
import PySimpleGUI as sg



layout = [
    [sg.Text("Tekst który zmieniamy: ")],
    [sg.InputText(key='text')],
    [sg.Text("Co chcesz usunąć z tekstu: ")],
    [sg.InputText(key='text2')],
    [sg.Submit(), sg.Cancel()],
]

window = sg.Window(title="Zmiana", layout=layout)

event,values = window.read()

window.close()

tekst = values['text']
tekst2 = values['text2']
a = tekst.replace(tekst2, "")
sg.popup(a)