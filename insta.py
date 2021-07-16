import os
from os import wait
from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup as bs

# FUNKCJA KASOWANIA ŚMIECI Z KONSOLI

def clear(): os.system('clear')
 
# DANE LOGOWANIA DO KONTA INSTAGRAM

nazwa = input("Podaj nazwę konta: ")
haslo = input("Podaj hasło do konta: ")

# KOMENTARZE

comment1 = """Perfect photo! 😃"""
comment2 = """WOW! 😮"""
comment3 = """Nice! 😃"""
comment4 = """Beautiful! 😍"""

# PRZERWA TECHNICZNA INFORMACJA

time.sleep(1)
clear()
time.sleep(2)
print("FUNKCJA KOMENTARZY JEST TYMCZASOWO WYŁĄCZONA.")
time.sleep(2)
clear()

# OTWORZENIE PRZEGLĄDARKI

driver = webdriver.Chrome()

time.sleep(5)

# OTWORZENIE STRONY

driver.get("https://www.instagram.com/")

# AKCEPTOWANIE COOKIES

driver.find_element_by_xpath("/html/body/div[3]/div/div/button[1]").click()
time.sleep(1)

# WPROWADZENIE WCZEŚNIEJ PODANYCH DANYCH

driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[1]/div/label/input""").send_keys(nazwa)
time.sleep(0.2)
driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[2]/div/label/input""").send_keys(haslo)
time.sleep(0.5)
driver.find_element_by_xpath("""//*[@id="loginForm"]/div/div[3]/button/div""").click()
time.sleep(3)

# AKCEPTACJA POWIADOMIEŃ I PROŚBY O ZAPISANIA HASŁA

driver.find_element_by_xpath("""//*[@id="react-root"]/section/main/div/div/div/div/button""").click()
time.sleep(4)
driver.find_element_by_xpath("""/html/body/div[4]/div/div/div/div[3]/button[2]""").click()
time.sleep(4)

# OTWORZENIE HASHTAGU

driver.get("https://www.instagram.com/explore/tags/likeforlikes/")
time.sleep(4)

# OTWORZENIE LOSOWEGO ZDJĘCIA

driver.left = random.randint(1,3)
driver.left = str(driver.left)
driver.downIndex = random.randint(1,3)
driver.downIndex = str(driver.downIndex)
driver.photo = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div['+ driver.left + ']/div['+ driver.downIndex +']/a/div')
driver.photo.click()

# LOSOWANIE I SYSTEM LIKE

time.sleep(3)
siuras = 1
while(True):
    siuras = (random.randint(1,2))
    print(siuras)
    if (siuras == 1):
        print("zero akcji")
        time.sleep(random.randint(10,30))
    else:
        print("like")
        time.sleep(random.randint(2,7))
        time.sleep(0.5)
        like_button = driver.find_element_by_class_name('fr66n')
        time.sleep(0.5)
        get_name = driver.find_element_by_class_name('e1e1d')
        time.sleep(0.5)
        get_name.text
        print('liked photo: {}'.format(get_name.text))
        like_button.click()    
        time.sleep(random.randint(10,30))
    
    # KLIKNIĘCIE PRZYCISKU DALEJ
    
    driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div/div/a[2]""").click()