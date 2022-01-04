# Program to make a simple  
# login screen   
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.ttk import *
import smtplib
from email.message import EmailMessage


def send_email_gmail(subject, message, destination):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    #This is where you would replace your password with the app password
    server.login('vishnurajanme@gmail.com', 'yourownapppassword')

    msg = EmailMessage()

    message = f'{message}\n'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = 'vishnurajanme@gmail.com'
    msg['To'] = destination
    server.send_message(msg)
   
root=tk.Tk() 
root.title('@#$%^&*$%^&*   Linways Daily Report Hacker for HODs   @#$%^&#$%^&*')
# setting the windows size 
root.geometry("450x300") 


   
# declaring string variable 
# for storing name and password 
name_var=tk.StringVar() 
passw_var=tk.StringVar() 
date_var=tk.StringVar() 

staff = ['Binet Rose Devassy', 'Chinchu Jose', 'Deepak Joseph Babu', 'Dr. Arun Thomas', 'Dr. G.R.Gnana King', 'Dr. K.R.Joy', 'Jisha Jacob', 'Priyanka Menon A S', 'Santhosh Kumar M S', 'Silpa P A', 'Vidyamol K', 'Ambily Francis'] 

monday = []
tuesday = []
wednesday = []
thursday = []
friday = []

date1 = ""
date2 = ""
date3 = ""
date4 = ""
date5 = ""

message = ""


   
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
         	rows=len(driver.find_elements_by_xpath('//*[@id="pending-application-list"]/div[3]/table/tbody/tr'))
         	cols=len(driver.find_elements_by_xpath('//*[@id="pending-application-list"]/div[3]/table/tbody/tr/td'))
         	if (i == 0):
                     date5 = (driver.find_element_by_xpath('//*[@id="pending-application-list"]/div[1]/div[2]/input[2]').get_attribute('value'))
         	elif (i == 1):
                     date4 = (driver.find_element_by_xpath('//*[@id="pending-application-list"]/div[1]/div[2]/input[2]').get_attribute('value'))    
         	elif (i == 2):
                     date3 = (driver.find_element_by_xpath('//*[@id="pending-application-list"]/div[1]/div[2]/input[2]').get_attribute('value'))
         	elif (i == 3):
                     date2 = (driver.find_element_by_xpath('//*[@id="pending-application-list"]/div[1]/div[2]/input[2]').get_attribute('value'))
         	elif (i == 4):
                     date1 = (driver.find_element_by_xpath('//*[@id="pending-application-list"]/div[1]/div[2]/input[2]').get_attribute('value'))          
    
         	for r in range(1, rows):
                 value = driver.find_element_by_xpath(
                     "//*[@id='pending-application-list']/div[3]/table/tbody/tr["+str(r)+"]/td[3]").text
                 print(value)
                 if (i == 0):
                     friday.append(value)
                 elif (i == 1):
                     thursday.append(value)        
                 elif (i == 2):
                     wednesday.append(value)
                 elif (i == 3):
                     tuesday.append(value)
                 elif (i == 4):
                     monday.append(value)             
         	
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

    #print("\nThe following staff members has kept the daily report on the corresponding days.",
     #           "\n{}: {} \n{}: {} \n{}: {} \n{}: {} \n{}: {}\n\n\n".format(date1, ",".join(monday), date2, ",".join(tuesday), date3, ",".join(wednesday), date4, ",".join(thursday), date5, ",".join(friday)),
      #          "\nThe following staff members failed to submit the daily report on the corresponding days",
       #         "\n{}: {} \n{}: {} \n{}: {} \n{}: {} \n{}: {} \n\n\n".format(date1, ",".join(list(set(staff) - set(monday))), date2, ",".join(list(set(staff)-set(tuesday))), date3, ",".join(list(set(staff)-set(wednesday))), date4, ",".join(list(set(staff)-set(thursday))),date5, ",".join(list(set(staff)-set(friday)))))  
    mailmatter = "Respected madam,\n\nThe following staff members has kept the daily report on the corresponding days.\n" \
    + date5 + " : " + (",".join(friday)) + "\n" \
    + date4 + " : " + (",".join(thursday)) + "\n" \
    + date3 + " : " + (",".join(wednesday)) + "\n" \
    + date2 + " : " + (",".join(tuesday)) + "\n" \
    + date1 + " : " + (",".join(monday)) + "\n" \
    + "\n\n\nThe following staff members failed to submit the daily report on the corresponding days.\n" \
    + date5 + " : " + (",".join(list(set(staff) - set(friday)))) + "\n" \
    + date4 + " : " + (",".join(list(set(staff) - set(thursday)))) + "\n" \
    + date3 + " : " + (",".join(list(set(staff) - set(wednesday)))) + "\n" \
    + date2 + " : " + (",".join(list(set(staff) - set(tuesday)))) + "\n" \
    + date1 + " : " + (",".join(list(set(staff) - set(monday)))) + "\n" \
    + "\nThanks and Regards\nDr. Vishnu Rajan\nHOD, ECE"
    
    print(mailmatter)
    send_email_gmail('Weekly Daily Report Status - ECE', mailmatter, 'hodece@sahrdaya.ac.in')
      
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

passw_entry.insert(0, "yourownpassword")

      
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

date_entry.insert(0, "5")
   
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
    
    
    
    
    