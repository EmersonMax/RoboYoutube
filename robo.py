from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
import chromedriver_binary
import time
import smtplib
from datetime import date, timedelta

class RoboYoutube():
    def __init__(self):
        self.webdriver = webdriver.Chrome()
        self.host = 'SERVIDOR SMPTP'
        self.port = 587
        self.user = 'LOGIN EMAIL'
        self.password = 'SENHA'
        self.server = smtplib.SMTP(self.host, self.port)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.user, self.password)
        self.data = date.today()
        self.hoje = self.data.strftime('%d/%m/%Y')
        
    def busca(self):
        url = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"
        self.webdriver.get(url)
        titulos = self.webdriver.find_elements_by_xpath("//a[@id='video-title']")
        message=f"Os videos em alta do youtube no dia {self.hoje} são: \n \n"
        
        for titulo in titulos:
            message = message + "-------------------------- \n"
            message=message + ("TÍTULO: \n" + titulo.text +'\n')
            message=message + ("LINK: \n" +  titulo.get_attribute('href') + "\n")
            
        
        time.sleep(5)
        self.webdriver.close()
        email_msg = MIMEMultipart()
        email_msg['From'] = self.user
        email_msg['To'] = 'EMAIL DESTINO'
        email_msg['Subject'] = f"Videos em Alta do YouTube {self.hoje}"
        email_msg.attach(MIMEText(message, 'plain'))
        self.server.send_message(email_msg)
        self.server.quit()
        
           
    
bot = RoboYoutube()
bot.busca()        
