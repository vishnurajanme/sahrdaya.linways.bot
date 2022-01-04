# Program to make a simple  
# login screen   
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.ttk import *

   
root=tk.Tk() 
root.title('@#$%^&*$%^&*   Linways Daily Report Hacker for HODs   @#$%^&#$%^&*')
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
    driver.get("https://sahrdaya.linways.com/staff/staff.php?menu=staffDailyWorkLog&action=approval")
    # delay
    wait = WebDriverWait(driver, 600)
    #Defining messages:
    #Reading number of days to fill
    
    username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))) 
    password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))) 
    username.send_keys(user)
    password.send_keys(pasw + Keys.ENTER)
    
    
    for i in range(int(days)):
    	time.sleep(1)
    	try:
        	time.sleep(1)
        	wait.until(driver.find_element_by_xpath('//*[@id="pending-application-list"]/div[3]/table/thead/tr/th[1]/input').click())
    	except:
            print("Cannot find checkbox {}/{})".format(i,int(days)))
    	try:
            time.sleep(1)
            wait.until(driver.find_element_by_xpath('//*[@id="pending-application-list"]/div[3]/a').click())
    	except:
            print('Cannot find verify button')
    	try:
        	time.sleep(1)
        	wait.until(driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/div/div/div[2]/div[6]/div/div/div[3]/button[2]').click())
    	except:
            print('Cannot find okay button')
    	time.sleep(1);
    	driver.find_element_by_xpath('//*[@id="pending-application-list"]/div[1]/div[1]/div').click()

      
      
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
date_label = tk.Label(root, text = 'No. of Dates to Verify', 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating a entry for input 
# dates using widget Entry 
date_entry = tk.Entry(root, 
                      textvariable = date_var
                      ,font=('calibre',10,'normal')) 
   
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(root,text = 'Verify', 
                  command = submit)

close_btn=tk.Button(text = "Quit", command = root.destroy)

img = ImageTk.PhotoImage(Image.open("splash.png"))
panel = Label(root, image = img)
   
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
panel.grid(row = 0, column = 2, columnspan = 2,
           rowspan = 4, padx = 0, pady = 0) 
   
# performing an infinite loop  
# for the window to display 
root.mainloop()    
    
    
    
    
    