import os
from tkinter.font import Font
from typing import ValuesView
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import CUSTOM_MENUBAR_METADATA_MARKER, Multiline
from datetime import date
import webbrowser
from randomFact import fact
import time
file =open("name.txt", "r")  
name = file.read() 
searchengine = "None"
def settings():
    sg.theme('DarkPurple1')
    centered = [
        [sg.Text("What is your preffered search engine?")]
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
          [sg.Button("DuckDuckGo", key="DUCKDUCKGO"), sg.Button("Google", key="GOOGLE")]
              
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
         with open("name.txt", "w") as file:
             file.write(values['name'])
     if event == "WIPE":        
         open("name.txt", "w").close() #deletes contents
     if event == "DUCKDUCKGO":
         with open("searchengine.txt", "w") as file:
             file.write("duckduckgo")
             file.close()
     if event == "GOOGLE":
         with open("searchengine.txt", "w") as file:
             file.write("google")
             file.close()      
     if event == "FIREFOX":
         with open("searchengine.txt", "w") as file:
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
        file1 = open("searchengine.txt", "r")
        readfile = file1.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "SEARCHBUTTON":
            if "google" in readfile:
                  search = values["SEARCH"]
                  webbrowser.open("https://www.google.com/search?client=google-b-d&q={}".format(search)) 
            if "duckduckgo" in readfile:
                  search = values["SEARCH"]
                  webbrowser.open("https://duckduckgo.com/?q={}&t=hy&va=g&ia=web".format(search))            
        if event == "WEBSEARCH":
            search = values["SEARCH"]    
            webbrowser.open("https://www.{}.com".format(search))

def toDoList():
    file = open("todolist.txt", "r")
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
            open("todolist.txt", "w").close()       
                
            
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
        [sg.Text(fact)],
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





def main():
    welcomeMessage = "Welcome to the Hub! {} ".format(name)
    menu_def = [['File',  ['Settings', 'About Me', 'Random Facts', 'Text File Viewer', 'ToDos', 'Search The Web!']]]
    SAVE_FILE = "text.txt"
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
        [sg.Text("Tinker, and explore the application, add new elements to your liking, and most important of all, have fun!")],
        [sg.HorizontalSeparator()],
        [sg.Button("Youtube", key="YOUTUBE"),
        sg.Button("Twitter", key="TWITTER"),
        sg.Button("Spotify", key="SPOTIFY"),
        sg.Button("VSCODE", key="VSCODE"),
        sg.Button("Twitch", key="TWITCH"),
        sg.Button("Steam",key="STEAM")],
        [sg.HorizontalSeparator()],
        [sg.Text(date.today(),justification='center')],
        [sg.Cancel()]  
        ]
    sg.theme('DarkPurple6')
    window = sg.Window("Main", layout, size=(650,300))
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
     if event == "YOUTUBE":
         webbrowser.open("https://youtube.com")
     if event == "TWITTER":
         webbrowser.open("https://twitter.com")
     if event == "SPOTIFY":
         filepath = "C:\\Users\\gotst\\AppData\\Roaming\\Spotify\\Spotify.exe" # set your path to the exe here, also this should be the default install location for spotify
         os.startfile(filepath)
     if event == "TWITCH":
         webbrowser.open("https://twitch.com")
     if event == "STEAM":
         filepath = "C:\Program Files (x86)\Steam\Steam.exe" # default install location for steam
         os.startfile(filepath)
             
                         
    
          

if __name__ == '__main__':
    main()       
    
 