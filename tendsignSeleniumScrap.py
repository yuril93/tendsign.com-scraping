import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(subject):
    #subject# = "tendsign.com CSV data"
    body = "tendsign.com CSV data"
    sender_email = "Your gmail" #gmail
    password = "Your gmail app password " # gmail App password
    receiver_email = "daniel@connectivo.se"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "tendsign.csv"  # In same directory as script

    # Open CSV file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

with open('tendsign.csv', newline='') as f:
  reader = csv.reader(f)
  row1 = next(reader)
f.close()

chrome_options = Options()
chrome_options.add_argument("--headless")

# chromedriver.exe path
browser = webdriver.Chrome(executable_path=r"C:\Users\Ashunik\Downloads\chromedriver.exe",options=chrome_options)
import smtplib, ssl


browser.get("https://tendsign.com/")

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


if row1==[(((browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-itemstyle']/td[1]")+browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-alternatingitemstyle']/td[1]"))[0]).text), ((browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-itemstyle']/td[2]")+browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-alternatingitemstyle']/td[2]"))[0]).text, ((browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-itemstyle']/td[3]")+browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-alternatingitemstyle']/td[3]"))[0]).text, ((browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-itemstyle']/td[4]")+browser.find_elements_by_xpath("//tbody/tr[@class='datagrid-alternatingitemstyle']/td[4]"))[0]).text]:
    subject = "No updates in tendsign.com CSV data"
    print ("Sending email ...")
    sendEmail(subject)
    print("Done")
    exit()
else:
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
                break
            except:
                browser.refresh()#
                time.sleep(10)

    data = [column_1, column_2, column_3, column_4]

    with open('tendsign.csv', 'w', newline='') as z:
        writer = csv.writer(z)
        for x in range(len(column_1)):
             data = [[column_1[x], column_2[x], column_3[x], column_4[x]]]
             writer.writerows(data)
    z.close()
    print ("Sending email ...")
    sendEmail(subject="tendsign.com CSV data")
    print("Done")




