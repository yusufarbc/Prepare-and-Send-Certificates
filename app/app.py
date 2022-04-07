import csv
from time import sleep
from PIL import Image, ImageDraw, ImageFont
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class App():
    def __init__(self):
        #arguments
        self.template = "template.png"
        self.mailList = "list.csv"

        #login configs
        self.username = "***********"
        self.password = "**********"

        #mail configs
        self.subject = "Sertifikanız Hazır"
        self.message = "Etkinliğimize katıldığınız için teşekkür ederiz. Sertifikanız ektedir."

        #font configs
        self.font = ImageFont.truetype("PaytoneOne.ttf",60)
        self.color = 28, 48, 85

        print("configurations are successful")

    def readCSV(self):
        self.rows = []
        with open(self.mailList, encoding="utf8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            for row in csvreader:
                self.rows.append(row)

    def createCertificate(self, text):
        img = Image.open(self.template)
        img_width = img.width
        img_height = img.height

        draw = ImageDraw.Draw(img)
        t_width, t_height = draw.textsize(text, self.font)
        position = ((img_width - t_width)/2, (img_height - t_height)/2-60)
        draw.text(position, text, self.color, font=self.font)
        return img

    def prepareCertificates(self):
        try:
            os.mkdir("certificates")
        except:
            print("directorry can't generated")
        for i in self.rows:
            text = i[1]
            certificate = self.createCertificate(text)
            path = "certificates/{}.png".format(text)
            certificate.save(path)
            print("{}.png is created".format(text))

    def prepareMail(self, row):
        mail = MIMEMultipart()
        mail['Subject'] = self.subject
        mail['From'] = self.username
        mail['To'] = row[2]

        msgText = MIMEText('<b>%s</b>' % (self.message), 'html')
        mail.attach(msgText)

        with open("certificates/"+row[1]+".png", 'rb') as fp:
            img = MIMEImage(fp.read())
            img.add_header('Content-Disposition', 'attachment', filename= row[1]+".png")
            mail.attach(img)
        mail = mail.as_string()

        return mail

    def sendMails(self):
        try:
            with smtplib.SMTP('smtp.office365.com', 587) as smtpObj:
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.login(self.username, self.password)
                for i in self.rows:
                    mail = self.prepareMail(i)
                    try:
                        smtpObj.sendmail(self.username, i[2], mail)
                        print("mail sended to {}".format(i[2]))
                    except Exception as e:
                        print(e)
                    sleep(3)
        except Exception as e:
            print(e)

if __name__=="__main__":
    app = App()
    app.readCSV()
    print("csv file OK.")
    app.prepareCertificates()
    print("certificates are created")
    while True:
        confirm = input("Send mails? (yes/no): ")
        if confirm == "yes":
            app.sendMails()
            break
        elif confirm == "no":
            exit()
        else:
            print("wrong word. try again")
    print("transaction terminated\npress any key to continue...")
    input()
