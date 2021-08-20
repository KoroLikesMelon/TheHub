import os
from tkinter.font import Font
from typing import ValuesView
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import CUSTOM_MENUBAR_METADATA_MARKER, Multiline
from datetime import date
import webbrowser
from randomFact import facta
import time
import getpass
import os.path
from os import path
from AssignablePys.assignable1 import assignable1
from AssignablePys.assignable2 import assignable2
from AssignablePys.assignable3 import assignable3
from AssignablePys.assignable4 import assignable4
from AssignablePys.assignable5 import assignable5
username = getpass.getuser()
file =open("userinfo//name.txt", "r")  
name = file.read() 
searchengine = "None"
def settings():
    with open("userinfo//spotifypath.txt", "r") as file:
      spotifypath = file.read()
    with open("userinfo//steampath.txt", "r") as file:
        steampath = file.read()
    with open("userinfo//VSCODEPATH.txt", "r") as file:
        VSCODEpath = file.read()       
    sg.theme('DarkPurple1')
    centered = [
        [sg.Text("What is your preffered search engine?")]
    ]
    centered2 = [
        [sg.Text("Enter the path to your exe's (leave empty to use default install directory)")]
    
    
    ]
    layout = [  
          
          [sg.Text('Username', size =(15, 1))],
          [sg.Input(name, key="name")],
          [sg.HorizontalSeparator()],
          [sg.Cancel()],
          [sg.Button("Apply", key="-APPLY-"), sg.Button("Wipe", key="WIPE")], 
          [sg.Text('', pad=(0,0),key='-EXPAND2-')],              # the thing that expands from left
          [sg.Column(centered, vertical_alignment='center', justification='center',  k='-C-')],
          [sg.HorizontalSeparator()],
          [sg.Button("DuckDuckGo", key="DUCKDUCKGO"), sg.Button("Google", key="GOOGLE")],
          [sg.Text('', pad=(0,0),key='-EXPAND3-')],              # the thing that expands from left
          [sg.Column(centered2, vertical_alignment='center', justification='center',  k='-C2-')],
          [sg.HorizontalSeparator()],
          [sg.Text("Enter the path to steam.exe")],
          [sg.Input(steampath, key="STEAMPATH")],
          [sg.Text("Enter the path to spotify.exe")],
          [sg.Input(spotifypath, key="SPOTIFYPATH")],
          [sg.Text("Enter the path to VSCODE.exe")],
          [sg.Input(VSCODEpath, key="VSCODEPATH")]
              
    ]
    window = sg.Window("Settings", layout, modal=True)
    while True: 
     event, values = window.read()
     if event == sg.WIN_CLOSED:
         break
     if event == "Cancel":
         window.close()
         break
     if event == "-APPLY-":
         with open("userinfo//name.txt", "w") as file:
             file.write(values['name'])
         with open("userinfo//spotifypath.txt", "w") as file:
             file.write(values["SPOTIFYPATH"])
         with open("userinfo//steampath.txt", "w") as file:
             file.write(values["STEAMPATH"])
         with open("userinfo//VSCODEPATH.txt", "w") as file:
             file.write(values["VSCODEPATH"])            
     if event == "WIPE":        
         open("userinfo//name.txt", "w").close() #deletes contents
         open("userinfo//searchengine.txt", "w").close()
         open("userinfo//spotifypath.txt", "w").close()
         open("userinfo//steampath.txt", "w").close()
         open("userinfo//VSCODEPATH.txt", "w").close()
     if event == "DUCKDUCKGO":
         with open("userinfo//searchengine.txt", "w") as file:
             file.write("duckduckgo")
             file.close()
     if event == "GOOGLE":
         with open("userinfo//searchengine.txt", "w") as file:
             file.write("google")
             file.close()      
     if event == "FIREFOX":
         with open("userinfo//searchengine.txt", "w") as file:
             file.write("firefox")
             file.close()
           
             


def search():
    sg.theme('DarkPurple1')
    column = [
        [sg.Text("Search something! :D")]
    ]
    layout = [
        [sg.Text('', pad=(0,0),key='-EXPAND2-')],              # the thing that expands from left
        [sg.Column(column, vertical_alignment='center', justification='center',  k='-C-')],
        [sg.HorizontalSeparator()],
        [sg.Input(key="SEARCH")],
        [sg.Button("Search Up!", key="SEARCHBUTTON"), sg.Button("Search for a Website", key="WEBSEARCH"), sg.Cancel()]
    ]
    window = sg.Window("Search", layout, size=(500,300))
    while True:
        event, values = window.read()
        file1 = open("userinfo//searchengine.txt", "r")
        readfile = file1.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Cancel":
            window.close()
            break
        if event == "SEARCHBUTTON":
            if "google" in readfile:
                  search = values["SEARCH"]
                  webbrowser.open("https://www.google.com/search?client=google-b-d&q={}".format(search)) 
            if "duckduckgo" in readfile:
                  search = values["SEARCH"]
                  webbrowser.open("https://duckduckgo.com/?q={}&t=hy&va=g&ia=web".format(search))     
            else:
                search = values["SEARCH"]
                webbrowser.open("https://www.google.com/search?client=google-b-d&q={}".format(search))
                            
        if event == "WEBSEARCH":
            search = values["SEARCH"]    
            webbrowser.open("https://www.{}.com".format(search))

def toDoList():
    file = open("userinfo//todolist.txt", "r")
    sg.theme('DarkPurple1')
    todos = file.read()
    column = [
        [sg.Text("WIP!! You need to relaunch it to get a todo", font=("50"))],
        [sg.Text("Enter a To Do", font=("50"))]
    ]
    layout = [
        [sg.Text('', pad=(0,0),key='-EXPAND2-')],              # the thing that expands from left
        [sg.Column(column, vertical_alignment='center', justification='center',  k='-C-')],
        [sg.HorizontalSeparator()],
        [sg.Input(key="ToDos")],
        [sg.Text(todos)],
        [sg.Button("Enter", key="ENTER"), sg.Button("Wipe", key="WIPE")],
        [sg.Cancel()]
    ]
    window = sg.Window("To Do List", layout, size=(500,300))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Cancel":
            window.close()
            break
        if event == "ENTER":
            file.close()
            with open("todolist.txt", "w") as file:
                file.write(values["ToDos"])
                file.close()
        if event == "WIPE":
            open("userinfo//todolist.txt", "w").close()       
                
            
def txtViewer():
    #sg.multiline read into by txt or smth like that
    sg.theme('DarkPurple1')
    layout = [
        [sg.Text("Select a TXT file")],
        [sg.FileBrowse(size=(10, 1), file_types=(("TXT files", "*.txt"),), key="-FILE-"),],
        [sg.Button("View", key='-VIEW-')],
        [sg.Cancel()]
    ]
    
    
    window = sg.Window("Text Viewer", layout, size=(500,300))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Cancel":
            window.close()
            break
        if event == '-VIEW-':
          with open(values['-FILE-'], 'r') as file:
              sg.Popup(file.read()) # add new window with multiline
              
                    
def randomFact():
    sg.theme('DarkPurple1')

    layout2 = [
        [sg.Text("Your random fact:")],
        [sg.Text(facta)],
        [sg.Cancel()]
    ]
    layout = [
        [sg.Text("Click the Button to get a random fact")],
        [sg.Button("Generate Fact", key='-FACTBUTTON-')],
        [sg.Cancel()]
    ]
    window = sg.Window("Random Fact", layout, size=(300,200))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Cancel":
            window.close()
            break
        if event == "-FACTBUTTON-":
            window.close()
            window = sg.Window("Random Fact", layout2, size=(600,200)) # add "new" window here too
def aboutMe():
    sg.theme('DarkPurple1')
    layout = [
        [sg.Text("https://github.com/KoroLikesMelon", enable_events=True, key="TEXTLINK")],
        [sg.Cancel()]
    ]
    window = sg.Window("ABOUT ME", layout, size=(200,300))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Cancel":
            window.close()
            break
    
        if event == "TEXTLINK":
            webbrowser.open("https://github.com/KoroLikesMelon")
            #Implement github page later here
column = [[sg.Text("Welcome to the button settings!, head on over to the menu to configure your buttons!", font=("50"))]]
def buttonSettings():
    sg.theme('DarkPurple1')
    menu_def = [['Buttons',  ['Assignable1', 'Assignable2', 'Assignable3', 'Assignable4', 'Assignable5']]]
    layout = [
          [sg.Menu(menu_def, key='-MENU-')],
          [sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],  # the thing that expands from top
          [sg.Text('', pad=(0,0),key='-EXPAND2-'),              # the thing that expands from left
             sg.Column(column, vertical_alignment='center', justification='center',  k='-C-')],
          [sg.Button("WIPE ALL", key="WIPE")]
    ]
    window = sg.Window("Button Settings", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "WIPE":
            open("userinfo//Assignables//assign1.txt", "w").close()
            open("userinfo//Assignables//assign2.txt", "w").close()
            open("userinfo//Assignables//assign3.txt", "w").close()
            open("userinfo//Assignables//assign4.txt", "w").close()
            open("userinfo//Assignables//assign5.txt", "w").close()
            open("userinfo//Assignables//path1.txt", "w").close()
            open("userinfo//Assignables//path2.txt", "w").close()
            open("userinfo//Assignables//path3.txt", "w").close()
            open("userinfo//Assignables//path4.txt", "w").close()
            open("userinfo//Assignables//path5.txt", "w").close()
            open("userinfo//Assignables//name1.txt", "w").close()
            open("userinfo//Assignables//name2.txt", "w").close()
            open("userinfo//Assignables//name3.txt", "w").close()
            open("userinfo//Assignables//name4.txt", "w").close()
            open("userinfo//Assignables//name5.txt", "w").close()
            
            
            
        if event == 'Assignable1':
            assignable1()
        if event == "Assignable2":
            assignable2()    
        if event == "Assignable3":
            assignable3()    
        if event == "Assignable4":
            assignable4()    
        if event == "Assignable5":
            assignable5()    
            

    




def main():
    with open("userinfo//Assignables//name5.txt", "r") as file:
        name5 = file.read()
        file.close()
    with open("userinfo//Assignables//name4.txt", "r") as file:
        name4 = file.read()
        file.close()
    with open("userinfo//Assignables//name3.txt", "r") as file:
        name3 = file.read()
        file.close()

    with open("userinfo//Assignables//name2.txt", "r") as file:
        name2 = file.read()
        file.close()
    with open("userinfo//Assignables//name1.txt", "r") as file:
        name1 = file.read()
        file.close()
    welcomeMessage = "Welcome to the Hub! {} ".format(name)
    menu_def = [['File',  ['Settings', 'Assignables', 'About Me', 'Random Facts', 'Text File Viewer', 'ToDos', 'Search The Web!']]]
    sg.theme('DarkPurple6')
    column = [  
          [sg.Text(welcomeMessage, font=("70"))]
           
    ]
    
    centerd2 = [[sg.Text(date.today(),justification='center')]]
    sg.theme('DarkPurple6')
    layout = [
        [sg.Menu(menu_def, key='-MENU-')],
        [sg.Text(key='-EXPAND-', font='ANY 1', pad=(0, 0))],  # the thing that expands from top
        [sg.Text('', pad=(0,0),key='-EXPAND2-'),              # the thing that expands from left
        sg.Column(column, vertical_alignment='center', justification='center',  k='-C-')],
        [sg.HorizontalSeparator()],
        [sg.Text("Welcome to the main screen, navigate into the settings to set your username!")],
        [sg.Text("Check the about me for additional information about the project")],
        [sg.Text("The Assignable buttons can be customized for your preference, set them up in the AssignableSettings window")],
        [sg.Text("Tinker, and explore the application, add new elements to your liking, and most important of all, have fun!")],
        [sg.HorizontalSeparator()],
        [sg.Button("Youtube", key="YOUTUBE"),
        sg.Button("Twitter", key="TWITTER"),
        sg.Button("Spotify", key="SPOTIFY"),
        sg.Button("VSCODE", key="VSCODE"),
        sg.Button("Twitch", key="TWITCH"),
        sg.Button("Steam",key="STEAM"),
        sg.Button(name1, key="ASSIGN1"),
        sg.Button(name2, key="ASSIGN2"),
        sg.Button(name3, key="ASSIGN3"),
        sg.Button(name4, key="ASSIGN4"),
        sg.Button(name5, key="ASSIGN5"),],
        [sg.HorizontalSeparator()],
        [sg.Text(date.today(),justification='center')],
        [sg.Cancel()]  
        ]
    sg.theme('DarkPurple6')
    window = sg.Window("Main", layout, size=(815,300))
    while True: 
     event, values = window.read()
     if event == sg.WIN_CLOSED:
         break
     if event == "Cancel":
         break
     if event == "Settings":
         settings()
     if event == "About Me":
         aboutMe()    
     if event == "Random Facts":
         randomFact()    
     if event == "Text File Viewer":
         txtViewer()   
     if event == "ToDos":
         toDoList()   
     if event == "Search The Web!":
         search()    
     if event == "Assignables":
         buttonSettings()    
     if event == "ASSIGN1":
          with open("userinfo//Assignables//assign1.txt", "r") as file:
                readfile = file.read()
                if "Website" in readfile:
                    filer = open("userinfo//Assignables//path1.txt", "r")
                    webbrowser.open(filer.read())
                elif "App" in readfile:
                    os.startfile(filer.read())   
     if event == "ASSIGN2":
          with open("userinfo//Assignables//assign2.txt", "r") as file:
                readfile = file.read()
                if "Website" in readfile:
                    filer = open("userinfo//Assignables//path2.txt", "r")
                    webbrowser.open(filer.read())
                elif "App" in readfile: # put file close
                    os.startfile(filer.read())       
     if event == "ASSIGN3":
          filer = open("userinfo//Assignables//path3.txt", "r")
          with open("userinfo//Assignables//assign3.txt", "r") as file:
                readfile = file.read()
                if "Website" in readfile:
                    webbrowser.open(filer.read())
                    filer.close()
                elif "App" in readfile:
                    os.startfile(filer.read())
                    filer.close()                       
     if event == "ASSIGN4":
          filer = open("userinfo//Assignables//path4.txt", "r")
          with open("userinfo//Assignables//assign4.txt", "r") as file:
                readfile = file.read()
                if "Website" in readfile:
                    webbrowser.open(filer.read())
                elif "App" in readfile:
                    os.startfile(filer.read())  
     if event == "ASSIGN5":
          filer = open("userinfo//Assignables//path5.txt", "r")
          with open("userinfo//Assignables//assign5.txt", "r") as file:
                readfile = file.read()
                if "Website" in readfile:
                    webbrowser.open(filer.read())
                elif "App" in readfile:
                    os.startfile(filer.read())                                                     
                           
             
     if event == "VSCODE":
         file = open("userinfo//VSCODEPATH.txt", "r")
         readfile = file.read()
         if not "" == readfile:
            filepath = readfile
            if not path.exists(filepath):
                sg.PopupError("PATH {} DOES NOT EXIST".format(filepath))
                break
            os.startfile(filepath)
         else:
             os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")
     if event == "YOUTUBE":
         webbrowser.open("https://youtube.com")
     if event == "TWITTER":
         webbrowser.open("https://twitter.com")
     if event == "SPOTIFY":
       
         file = open("userinfo//spotifypath.txt", "r") 
         readfile = file.read()
         if not "" == readfile:
             filepath = readfile
             if not path.exists(filepath):
                 sg.PopupError("PATH {} DOES NOT EXIST".format(filepath))
                 break
             os.startfile(filepath)
         else:
             if not path.exists(defaultstart):
                 sg.PopupError("DEFAULT INSTALLATION DIRECTORY DOES NOT EXIST, PLEASE SET IT IN SETTINGS")
                 break
             os.startfile("C:\\Users\\{}\\AppData\\Roaming\\Spotify\\Spotify.exe".format(username))
       
       
     if event == "TWITCH":
         webbrowser.open("https://twitch.com")
         
     if event == "STEAM":
         file = open("userinfo//steampath.txt", "r") 
         readfile = file.read()
         if not "" == readfile:
             filepath = readfile
             if not path.exists(filepath):
                 sg.PopupError("PATH {} DOES NOT EXIST".format(filepath))
                 break
             os.startfile(filepath)
         else:
             defaultstart = "C:\\Program Files (x86)\\Steam\\Steam.exe"
             if not path.exists(defaultstart):
                 sg.PopupError("DEFAULT INSTALLATION DIRECTORY DOES NOT EXIST, PLEASE SET IT IN SETTINGS")
                 break
             os.startfile(defaultstart)       
    
             
                         
    
          

if __name__ == '__main__':
    main()       
    
 