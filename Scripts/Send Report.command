#!/usr/bin/env python

# Program to make a simple  
# login screen   
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.ttk import *
import smtplib
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pretty_html_table import build_table
import cronitor
cronitor.api_key = '#'

myflag = 0

cronitor.Monitor.put(
    key='fypCOz',
    type='job'
)


monitor = cronitor.Monitor('fypCOz')
monitor.ping(state='run')

def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our HTML email"""

    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = SUBJECT
    MESSAGE['To'] = TO
    MESSAGE['From'] = FROM
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please visit us online!"""

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)

    # Credentials (if needed) for sending the mail
    password = '#'

    server.starttls()
    server.login(FROM,password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:45:55 2021

@author: vishnurajan
"""

from datetime import date, timedelta
today = date.today()
datenow = today.strftime("%d-%m-%Y")
print(datenow)

   
root=tk.Tk() 
root.title('@#$%^&*$%^&*   Linways Daily Report Hacker for HODs   @#$%^&#$%^&*')
# setting the windows size 
root.geometry("450x300") 


   
# declaring string variable 
# for storing name and password 
name_var=tk.StringVar() 
passw_var=tk.StringVar() 
date_var=tk.StringVar() 

staff = ['Dr.Vishnu Rajan','Binet Rose Devassy', 'Chinchu Jose', 'Deepak Joseph Babu', 'Dr. Arun Thomas', 'Dr. G.R.Gnana King', 'Dr. K.R.Joy', 'Jisha Jacob', 'Priyanka Menon A S', 'Santhosh Kumar M S', 'Silpa P A', 'Vidyamol K', 'Ambily Francis'] 




def submit(): 
    global myflag
    if myflag == 0:
        myflag =1
        import time
        from selenium import webdriver 
        from selenium.webdriver.support.ui import WebDriverWait 
        from selenium.webdriver.support import expected_conditions as EC 
        from selenium.webdriver.common.keys import Keys 
        from selenium.webdriver.common.by import By 
        user = name_entry.get() 
        pasw = passw_var.get()
        days = date_entry.get()
        #chrome driver path
        driver = webdriver.Chrome('/Users/vishnurajan/Documents/Developer/Python/Linways/chromedriver') 
        #opening website
        driver.get("https://sahrdaya.linways.com/staff/staff.php?menu=staffDailyWorkLog&action=worklogNotSubmittedReport&report=worklogreport")
        # delay
        wait = WebDriverWait(driver, 600)
        #Defining messages:
        #Reading number of days to fill
        
        username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))) 
        password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))) 
        username.send_keys(user)
        password.send_keys(pasw + Keys.ENTER)
        
        prev = date.today()-timedelta(days=int(days))
        prevday = prev.strftime("%d-%m-%Y")
        print(prevday)
        
        date1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="datepicker"]')))
        driver.execute_script("arguments[0].removeAttribute('readonly')",date1)
        date1.clear()
        date1.send_keys(prevday)
        
        yday = date.today()-timedelta(days=1)
        ydayday = yday.strftime("%d-%m-%Y")
        print(ydayday)
        
        date2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="datepicker1"]')))
        driver.execute_script("arguments[0].removeAttribute('readonly')",date2)
        date2.clear()
        date2.send_keys(ydayday)
        
        sel = wait.until(EC.presence_of_element_located((By.ID, 'deptId')))
        select = Select(sel)
        select.select_by_visible_text('EC')
        clicker = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div/div[2]/div/div[2]/div[1]/div[3]/div/button')))
        clicker.click()
        time.sleep(1)
        
    
        soup = BeautifulSoup(driver.page_source, 'lxml')
        tables = soup.find_all('table')
        dfs = pd.read_html(str(tables))
        stafftable = dfs[0].drop(['Department','Details'], 1)
        stafftable = stafftable[stafftable['Staff Name'].isin(staff)]
        
        body = """
        <html>
        <head>
        </head>
        
        <body>
        
        <h3>Respected madam,</h3>
    
        <p>The Daily Report weekly non submission list from the Department of ECE is as attached herewith.</p>
    
        <p>&nbsp;</p>
    
        
                {0}
    
        <p>&nbsp;</p>
    
        <p>Thanks &amp; Regards,</p>
    
        <p>Dr. Vishnu Rajan</p>
    
        <p>HOD, ECE</p>
    
        <p>&nbsp;</p>
    
        </body>
        
        </html>
        """.format(build_table(stafftable, 'blue_light'))
        
        py_mail('Weekly Daily Report Status - ECE', body, 'jointdirector@sahrdaya.ac.in', 'vishnurajanme@gmail.com')
        print(body)
        time.sleep(20)
        print(stafftable)
        print("Hey Vishnu, While you were away I just completed the daily report tabulation for you. I have also sent the same to sudha mam. Have a nice free time!")
        monitor.ping(state='complete')
        root.after(0,root.destroy)

# creating a label for  
# name using widget Label 
name_label = tk.Label(root, text = 'Username', 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating a entry for input 
# name using widget Entry 
name_entry = tk.Entry(root, 
                      textvariable = name_var
                      ,font=('calibre',10,'normal')) 

name_entry.insert(0, "fec1108")


   
# creating a label for password 
passw_label = tk.Label(root, 
                       text = 'Password', 
                       font = ('calibre',10,'bold')) 
   
# creating a entry for password 
passw_entry=tk.Entry(root, 
                     textvariable = passw_var, 
                     font = ('calibre',10,'normal'), 
                     show = '*') 

passw_entry.insert(0, "#")

      
# creating a label for  
# dates using widget Label 
date_label = tk.Label(root, text = 'No. of Dates to Verify', 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating a entry for input 
# dates using widget Entry 
date_entry = tk.Entry(root, 
                      textvariable = date_var
                      ,font=('calibre',10,'normal')) 

date_entry.insert(0, "6")
   
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(root,text = 'Verify', 
                  command = submit)

close_btn=tk.Button(text = "Quit", command = root.destroy)

   
# placing the label and entry in 
# the required position using grid 
# method 
name_label.grid(row=0,column=0, padx = 3, pady = 3) 
name_entry.grid(row=0,column=1, padx = 3, pady = 3) 
passw_label.grid(row=1,column=0, padx = 3, pady = 3) 
passw_entry.grid(row=1,column=1, padx = 3, pady = 3) 
date_label.grid(row=2,column=0, padx = 3, pady = 3) 
date_entry.grid(row=2,column=1, padx = 3, pady = 3) 
sub_btn.grid(row=3,column=0)
close_btn.grid(row=3,column=1) 

root.after(10000, submit)
   
# performing an infinite loop  
# for the window to display 
root.mainloop()    
    
    
    
    
    