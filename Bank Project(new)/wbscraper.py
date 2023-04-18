from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
from array import *
from sys import argv

def main(username, password):
    driver = webdriver.Chrome(executable_path="G:\chromedriver\chromedriver.exe")
    driver.maximize_window()
    driver.get('https://fridaystudentportal.com/oldbridge')  
    userbox = driver.find_element("name", "username")
    userbox.send_keys(username)
    passbox = driver.find_element("name", "password")
    passbox.send_keys(password)
    time.sleep(1)
    passbox.submit()
    time.sleep(1)
    driver.get('https://fridaystudentportal.com/portal/index.cfm?f=grades.cfm')
    htmlsource = driver.page_source
    time.sleep(1)
    global gradespage
    gradespage = BeautifulSoup(htmlsource, 'html.parser')
    time.sleep(1)
    driver.quit()
    global finalgpa
    finalgpa = 0.0
    variables()
    finalgpa = finalcalc()
    return round(finalgpa, 3)

def variables():
    i = 0
    global grade
    grade = {}
    grades = 0
    counter = 0
    for el in gradespage.find_all("span", class_="main-grade-display notranslate"):
        counter += 1
        grades += int(el.get_text())
        if counter == 3:
            counter = 0
            grade[i] = int(grades/3)
            #$print(grade[i])
            grades = 0
            i += 1
    i = -1
    global subject
    subject = []
    for el in gradespage.find_all("font"):
        i += 1
        if "LAB-DRUGS & ALC - 11" in el.get_text():
            continue
        else:
            subject.append(el.get_text())
        #print('subject[' + str(i) + ']' + subject[i])


def finalcalc():
    #print(subject)
    points = 0.00
    credits = 0
    x = 0
    for y in subject:
        subjectinfo = subjectarray(y)
        point = pointcalc(grade[x])
        points += (point + subjectinfo[1]) * subjectinfo[2]
        credits += subjectinfo[2]
        x += 1
    gpa = points/credits
    print(gpa)
    finalgpa = round((((4.653 * 2)+ gpa)/3), 3)
    return (finalgpa)
        

def subjectarray(el):
    subjectlist = []
    compsi = ["AP COMPUTER SCIENCE", 2, 5]
    lang = ["AP ENGLISH COMP", 2, 5]
    calc = ["AP CALCULUS BC", 2, 10]
    health = ["LAB-DRUGS & ALC - 11", 0, 1]
    chem = ["AP CHEMISTRY", 2, 10]
    gov = ["AP GOVT & POLITICS", 2, 5]
    gym = ["PHYS ED - 11", 0, 4]
    subjectlist.append(compsi)
    subjectlist.append(lang)
    subjectlist.append(calc)
    #subjectlist.append(health)
    subjectlist.append(chem)
    subjectlist.append(gov)
    subjectlist.append(gym) 
    for sbj in subjectlist:
        if sbj[0] in el:
            return sbj


def pointcalc(gradenum):
    point = 0.00
    if(gradenum >= 97):
        point = (4.33)
    elif(gradenum >= 93):
        point = (4.0)
    elif(gradenum >= 90):
        point = (3.67)
    elif(gradenum >= 87):
        point = (3.33)
    elif(gradenum >= 83):
        point = (3.0)
    elif(gradenum >= 80):
        point = (2.67)
    elif(gradenum >= 77):
        point = (2.33)
    elif(gradenum >= 73):
        point = (2.0)
    elif(gradenum >= 70):
        point = (1.67)
    elif(gradenum >= 67):
        point = (1.33)
    elif(gradenum >= 63):
        point = (1.0)
    elif(gradenum >= 60):
        point = (0)
    return point

if __name__ == '__main__':
    main()
    variables()
    pointcalc()


