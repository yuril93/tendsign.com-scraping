#Title
README file for tendsignSeleniumScrap.py python scritp.

##Description 
tendsignSeleniumScrap.py scrip automaticaly login in to https://tendsign.com/ site and checking below points,send an email in a headless mode:

1.	If data in site do not updated compered with existed tendsign.csv file: 
		Send an email to "daniel@connectivo.se" with attached existed "tendsign.csv" file which is located in script path.
		
2.	If data in site is updated compered with existed tendsign.csv file:
		Send an email to "daniel@connectivo.se" with attached "tendsign.csv" file which have new data scraped from https://tendsign.com/ site.

## Installation
1.	Install Python 3.6+
2.	Install Selenium "VERSION 3.141.0" or above
3.	Download webdriver for your browser (Google Chrome 12+,Internet Explorer 7,8,9,10,Safari 5.1+,Opera 11.5,Firefox 3+)
4. 	Copy tendsignSeleniumScrap.py file in your path.
5.	Touch new tendsign.csv file in same area

6.	Update following line in tendsignSeleniumScrap.py file:
	Line 13:	sender_email = "Your gmail" #gmail
    Line 14:	password = "Your gmail app password " # gmail App password
	
	line 63:	browser = webdriver.Chrome(executable_path=r"webdriver path",options=chrome_options)
				ex: browser = webdriver.Chrome(executable_path=r"C:\Users\yuril\Downloads\chromedriver.exe",options=chrome_options)

## Usage
run tendsignSeleniumScrap.py file.
ex: python tendsignSeleniumScrap.py
