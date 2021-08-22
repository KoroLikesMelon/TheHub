import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import HorizontalSeparator
from psutil import cpu_percent
from datetime import datetime


def cpulevel():
    file = open("userinfo//cpulevel.txt", "r")
    column = [
        [sg.Text("CPU LEVEL RECORDS")],
        [sg.Multiline(file.read(), key="MULTI")]
    ]
    file.close()
    column1 = [
        [sg.Button("Record Level", key="LEVELRECORD"), sg.Button("Display Level", key="LEVELDISPLAY")],
        [sg.Cancel()]
    ]
    layout = [
        [sg.Column(column1), sg.VerticalSeparator(), sg.Column(column)]
    ]
    window = sg.Window("CPU LEVEL", layout, size=(700, 250))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Cancel":
            window.close()
            break
        if event == "LEVELRECORD":
            with open("userinfo//cpulevel.txt", "w") as file:
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                file.write("This was recorded at: ")
                file.write(time)
                file.write("\n")
                file.write(str(cpu_percent()))
                file.close()
                file = open("userinfo//cpulevel.txt", "r")
                window["MULTI"].update(file.read())
                file.close()
        if event == "LEVELDISPLAY":
            [sg.PopupOK(str(cpu_percent()))]
            
