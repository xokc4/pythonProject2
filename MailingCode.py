from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import  basename
from email.mime.text import MIMEText
import smtplib
class Mail:
    def __init__(self,login='null',password='null'):
        self.login=login,
        self.password=password
    def ToString(self):
        print(self.login, "и", self.password)
    def CreatMailingCode(self,PathEmailAdress="null",messageBox="null",messageFile='null'):
        #пароль для рассылки "kgHFTcTzDbApGaw7ENDd"
        print(messageFile)
        email_sender=self.login
        email_password=self.password

        smpt_server=smtplib.SMTP("smtp.mail.ru",587)
        smpt_server.starttls()
        test = MIMEMultipart()
        test.attach(MIMEText(messageBox))

        if messageFile!='null':
            m=open(messageFile,'r')
            with open(m.name,"rb") as f:
                file = MIMEApplication(f.read(),Name=basename(m.name))
                test.attach(file)
            if '<html>' in file:
                test.attach(MIMEText(file,'html'))
            m.close()


        if PathEmailAdress=="null":
            print("нет файла для рассылок")
        if PathEmailAdress!="null":
            with open(PathEmailAdress) as f:
               txtAdress = f.read()
            listAdress = txtAdress.split('\n')
            smpt_server.login(email_sender, email_password)
            smpt_server.sendmail(email_sender, listAdress, test.as_string())

        print("идет рассылка")