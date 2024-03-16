import easygui
class File:
    def __init__(self,Path='null',):
        self.Path=Path

    def OpenFile(self):
        input_file = easygui.fileopenbox(filetypes=["*.docx"])
        self.Path=input_file.title()
        print(f"открываем файл для адрессов")

class MessFile:
    def __init__(self,PathMessage='null'):
        self.PathMessage=PathMessage

    def OpenFileMessage(self):
        input_file = easygui.fileopenbox(filetypes=["*.docx"])
        self.PathMessage= input_file.title()
        print(f"открываем файл для отправки")