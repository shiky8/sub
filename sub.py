#!/bin/bash/python3
# by shiky
from time import sleep
import csv as cs
from selenium import webdriver
#browser=webdriver.Chrome()
browser=webdriver.Firefox(executable_path="./geckodriver")

def gloin(em,passed):
    #browser.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    browser.get("https://gmail.com")
    browser.find_element_by_id("identifierId").send_keys(em)
    browser.find_element_by_id("identifierNext").click()
    sleep(5)
    browser.find_element_by_name("password").send_keys(passed)
    browser.find_element_by_id("passwordNext").click()
    sleep(5)

def glogout():
    browser.get("https://accounts.google.com/SignOutOptions?hl=en&continue=https://mail.google.com/mail&service=mail")
    browser.find_element_by_xpath('//button[normalize-space()="Sign out"]').click()

def add_lis(f):
    dlist=[]
    em = cs.reader(f)
    for r in em:
        dlist.append(r)
    return dlist

looges=open("email.txt",'r')
passer=open("pass.txt",'r')
email_list=add_lis(looges)
pass_list=add_lis(passer)
c=len(pass_list)
s=0
channel=str(input("Enter the youtube channel link here : "))
while c!=0:
    gloin(email_list[s],pass_list[s])
    #browser.get("https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw")
    browser.get(channel)
    Sub = browser.find_element_by_id("subscribe-button")
    Sub.click()
    glogout()
    s+=1
    c-=1
browser.close()