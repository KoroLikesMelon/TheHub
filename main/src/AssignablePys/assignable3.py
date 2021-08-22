import PySimpleGUI as sg
def assignable3():
    with open("userinfo//Assignables//name1.txt", "r") as file:
        name = file.read()
    sg.theme("DarkPurple1")
    with open("userinfo//Assignables//path3.txt", "r") as file:
       path = file.read()
       
    layout = [
        [sg.Text("Welcome to the settings!")],
        [sg.Text("Is it going to start an app, or a website?")],
        [sg.Button("Website", key="WEBSITE"), sg.Button("App", key="APP")],
        [sg.Button("Wipe Settings", key="WIPE")],
        [sg.Text("Type the path to the file or if it is a website, type the url here!")],
        [sg.Input(path, key="IN")],
        [sg.Button("Apply", key="APPLY")],
        [sg.Text("Enter a name for the button:")],
        [sg.Input(name, key="NAME")]

    ]
    window = sg.Window("Test", layout, size=(400,350))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "APPLY":
            with open("userinfo//Assignables//path3.txt", "w") as file:
                file.write(values["IN"])
            with open("userinfo//Assignables//name3.txt", "w") as file:
                file.write(values['NAME'])    
                
        if event == "WEBSITE":
            with open("userinfo//Assignables//assign3.txt", "w") as file:
                file.write("Website\n")
                file.close()
    
        if event == "APP":
            with open("userinfo//Assignables//assign3.txt", "w") as file:
                file.write("App\n")
                file.close()        
        if event == "WIPE":
                   open("userinfo//Assignables//assign3.txt", "w").close()                   