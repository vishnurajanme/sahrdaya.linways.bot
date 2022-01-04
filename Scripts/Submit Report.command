#!/usr/bin/env python

# Program to make a simple  
# login screen   
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.ttk import *
import cronitor
cronitor.api_key = '#'

cronitor.Monitor.put(
    key='mydailyreport',
    type='job'
)

monitor = cronitor.Monitor('mydailyreport')
monitor.ping(state='run')
   
root=tk.Tk() 
root.title('@#$%^&*$%^&*   Linways Daily Report Hacker   @#$%^&#$%^&*')
# setting the windows size 
root.geometry("450x300") 


   
# declaring string variable 
# for storing name and password 
name_var=tk.StringVar() 
passw_var=tk.StringVar() 
date_var=tk.StringVar() 

   
# defining a function that will 
# get the name and password and  
# print them on the screen 
def submit(): 
    import time
    from selenium import webdriver 
    from selenium.webdriver.support.ui import WebDriverWait 
    from selenium.webdriver.support import expected_conditions as EC 
    from selenium.webdriver.common.keys import Keys 
    from selenium.webdriver.common.by import By 
    from random import randrange
    user = name_entry.get()
    pasw = passw_var.get()
    days = date_entry.get()
    #chrome driver path
    driver = webdriver.Chrome('/Users/vishnurajan/Documents/Developer/Python/Linways/chromedriver') 
    #opening website
    driver.get("https://sahrdaya.linways.com/staff/staff.php?menu=myworkhrs&action=workLog")
    # delay
    wait = WebDriverWait(driver, 600)
    #Defining messages:
    msglist = ["Dept work", "Project Development", "Meeting", "Class Preparation",
               "Interaction with Students", "Project", "Subject Preparation", "Request letter submission", "PR & Media",
               "Work Allocation"]
    #Reading number of days to fill
    
    username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))) 
    password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))) 
    username.send_keys(user)
    password.send_keys(pasw + Keys.ENTER)
    
    
    for i in range(int(days)):
        try:
            for j in range(1,8):
                time.sleep(1);
                typer = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="work-desc-{}"]'.format(j))))
                typer.send_keys(msglist[randrange(len(msglist))])
            typer = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="work-desc-8"]')))
            typer.send_keys("Wrap up & Daily Report Submission")
            wait.until(driver.find_element_by_xpath('//*[@id="submitButton"]').click())
        except:
            print("Seems, it was already done :P ({}/30)".format(i))
        time.sleep(2);
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/span[1]').click()
    print("Hey Vishnu, While you were away I just completed the daily report submission for you. Have a nice free time!")
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


   
# creating a label for password 
passw_label = tk.Label(root, 
                       text = 'Password', 
                       font = ('calibre',10,'bold')) 
   
# creating a entry for password 
passw_entry=tk.Entry(root, 
                     textvariable = passw_var, 
                     font = ('calibre',10,'normal'), 
                     show = '*') 


      
# creating a label for  
# dates using widget Label 
date_label = tk.Label(root, text = 'No. of Dates to Hack', 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating a entry for input 
# dates using widget Entry 
date_entry = tk.Entry(root, 
                      textvariable = date_var
                      ,font=('calibre',10,'normal')) 
   
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(root,text = 'Submit', 
                  command = submit)

name_entry.insert(0, "fec1108")
passw_entry.insert(0, "#")
date_entry.insert(0, "1")


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
    
    
    
    
    