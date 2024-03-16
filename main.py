from tkinter import *
import EditFile
import MailingCode
import MailText
file = EditFile.File()
txt = MailText.TextMAil()
mail = MailingCode.Mail()
window = Tk()
MessFile=EditFile.MessFile()
window.title("Добро пожаловать в приложение Рассылки")
window.geometry('650x450')
labelOne=Label(window, text='Введите логин',font=("Arial Bold", 15))
TextLogin=Text(window, font=("Arial Bold", 15),width=25,height=1,border=2)

LabelTwo=Label(window, text='Ведите пароль',font=("Arial Bold", 15))
TextPassword=Text(window,font=("Arial Bold", 15),width=25,height=1,border=2)

LabelThri=Label(window,text='Ведите текст для рассылки',font=("Arial Bold", 15))
TextMail=Text(window,font=("Arial Bold", 15),width=25,height=3,border=2)
def CreateEditFile():
    EditFile.File.OpenFile(file)
    print('Открываем файл')
def MailingText():
    mail.login=TextLogin.get("1.0","end")
    mail.password=TextPassword.get("1.0","end")
    print("Почта с котороой будет отправлятся письма")
    mail.CreatMailingCode(file.Path,txt.text,MessFile.PathMessage)

def MailText():
    textPer = TextMail.get("1.0","end")
    txt.text=textPer
    print(f'Записываем текст, контект= {txt.text}')
def FileMessage():
    EditFile.MessFile.OpenFileMessage(MessFile)
    print("сохраняем файл для сообщения")

buttonTextMailing=Button(window,text='Сохранить Текст',command=MailText )

buttonFile=Button(window,text='посмотреть файл с почтами', command=CreateEditFile)
buttonCreateRas=Button(window, text='Рассылать',command=MailingText)
buttonFileMessage=Button(window,text="Файл для рассылки", command=FileMessage)


labelOne.grid(column=0,row=0)
LabelTwo.grid(column=0,row=1)
LabelTwo.place(x=0,y=40)
LabelThri.grid(column=0,row=2)
LabelThri.place(x=0,y=80)

TextLogin.grid(column=1,row=0)
TextLogin.place(x=270,y=0)
TextPassword.grid(column=1,row=1)
TextPassword.place(x=270,y=40)
TextMail.grid(column=1,row=2)
TextMail.place(x=270,y=80)

buttonTextMailing.grid(column=3,row=0)
buttonTextMailing.place(x=0,y=180)

buttonFile.grid(column=3,row=1)
buttonFile.place(x=120,y=180)

buttonCreateRas.grid(column=3,row=2)
buttonCreateRas.place(x=300,y=180)

buttonFileMessage.place(x=380, y=180)


window.mainloop()


