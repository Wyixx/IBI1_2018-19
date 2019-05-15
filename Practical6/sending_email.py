# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:29:23 2019

@author: Wyxx
"""
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#read email body
xfile1=open('body.txt','r')
body=xfile1.read()
print(body)
xfile1.close

#test the address
xfile=open('address_information.csv','r')
namelist=[]
addresslist=[]
subjectlist=[]
for line in xfile:
    mylist=re.split(',',str(line))
    if re.search(r'(@)',mylist[1])==None:#overlook titles(in the first list) 
        continue
    if re.match(r'(\S+@\S+com)',mylist[1]):
        #add the information of the correct address into the list
        namelist += [mylist[0]]
        addresslist += [mylist[1]]
        subjectlist += [mylist[2]]
        print(mylist[1],'correct address')
    else:
        print(mylist[1],'wrong address')
xfile.close

#send emails
from_addr=input('please enter the sender address:')
password=input('password:')

for i in range(0,len(addresslist)):
    body1=re.sub(r'User',namelist[i],body) #correct the recipient's name
#At first I did not creat a new name 'body1' (still used 'body')
#then the users' name were all 'Anna'
    
    to_addr=addresslist[i]
    subject=subjectlist[i]
    
    msg = MIMEText(body1,'plain','utf-8')
    msg['From'] = Header('WangYixuan','utf-8')
    msg['To'] = Header(to_addr,'ascii')
    msg['Subject'] = Header(subject,'utf-8')
    
    try:
        server = smtplib.SMTP('smtp.zju.edu.cn',25)#setup SMTP object, port for server is 25
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print('Mail sent successfully!')
    except smtplib.SMTPException:
        print('Mail delivery failed')




