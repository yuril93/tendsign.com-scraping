import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
#chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'`

browser = webdriver.Chrome(executable_path=r"C:\Users\yuril\Downloads\chromedriver.exe",options=chrome_options)
import smtplib, ssl


browser.get("https://tendsign.com/")

#time.sleep(5) # Let the user actually see something!

browser.find_element_by_id("txt_UserName").send_keys("info@swedishasongroup.se")
browser.find_element_by_id("UcomLogin_txt_Password").send_keys("Blomma12")
browser.find_element_by_id("UcomLogin_btn_Submit").click()
a=browser.get("https://tendsign.com/supplier/s_publications.aspx")
browser.find_element_by_link_text("Annonseringsdatum").click()
time.sleep(2)
browser.find_element_by_link_text("Annonseringsdatum").click()

column_1 = []
column_2 = []
column_3 = []
column_4 = []

while len(browser.find_elements_by_link_text("Nästa"))>0:
    c1 = browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-itemstyle']/td[1]")+browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-alternatingitemstyle']/td[1]")
    c2 = browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-itemstyle']/td[2]")+browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-alternatingitemstyle']/td[2]")
    c3 = browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-itemstyle']/td[3]")+browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-alternatingitemstyle']/td[3]")
    c4 = browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-itemstyle']/td[4]")+browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-alternatingitemstyle']/td[4]")

    for ca in c1:
        column_1.append(ca.text)
    for cb in c2:
        column_2.append(cb.text)
    for cc in c3:
        column_3.append(cc.text)
    for cd in c4:
        column_4.append(cd.text)


    while True:
        try:
            browser.find_elements_by_link_text("Nästa")[0].click()
            print("next pacge")
            break
        except:
            browser.refresh()#
            time.sleep(10)

data = [column_1, column_2, column_3, column_4]

with open('seleniumData.csv', 'w', newline='') as z:
    writer = csv.writer(z)
    for x in range(len(column_1)):
        data = [[column_1[x], column_2[x], column_3[x], column_4[x]]]
        writer.writerows(data)
z.close()



password = input("yura123321")
# Create a secure SSL context
context = ssl.create_default_context()

#with smtplib.SMTP_SSL("smtp.gmail.com", 465, context="string") as server:
#    server.login("yuraledyaev93@gmail.com", password)
#    server.sendmail(yuraledyaev93@gmail.com, yuraledyaev93@gmail.com, context)

# TODO: Send email here

