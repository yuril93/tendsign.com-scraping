import time
import csv
from selenium import webdriver
browser = webdriver.Chrome(executable_path=r"C:\Users\Ashunik\Downloads\chromedriver.exe")

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

yuril=0
#while len(browser.find_elements_by_link_text("Nästa"))>0:
while yuril <3:


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



    browser.find_elements_by_link_text("Nästa")[0].click()
    yuril=yuril+1

print(column_1,"\n",column_2,"\n",column_3,"\n",column_4)

data = [column_1, column_2, column_3, column_4]

with open('seleniumData.csv', 'w', encoding='utf-8') as z:
    writer = csv.writer(z)
    for x in range(len(column_1)):
        data = [[column_1[x], column_2[x], column_3[x], column_4[x]]]
        writer.writerows(data)
z.close()
   # for x in range(len(column_1)):
#        z.write([column_1[x],column_2[x],column_3[x],column_4[x]]))
#        z.write('\n')

