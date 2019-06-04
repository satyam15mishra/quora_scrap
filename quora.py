import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodecsv as csv

link = "https://www.quora.com/"
browser = webdriver.Chrome(executable_path='/Users/Satyam/Downloads/chromedriver')
browser.get(link)
form = browser.find_element_by_class_name('regular_login')
mail_button = form.find_element_by_name("email")
pass_button = form.find_element_by_name("password")
mail_button.send_keys("EMAIL_ID")
pass_button.send_keys("YOUR_PASSWORD")	
form.find_element_by_class_name("submit_button").send_keys(Keys.ENTER)

time.sleep(5)

elem1 = browser.find_element_by_tag_name("body").send_keys(Keys.CONTROL + 't')
link1 = "https://www.quora.com/topic/Job-Interviews/"
browser.get(link1)

elem = browser.find_element_by_tag_name('body')
qlinks = list()

with open('submission.csv','a') as file:
	    no_of_pagedowns = 1000
	    while no_of_pagedowns:
	        elem.send_keys(Keys.PAGE_DOWN)
	        time.sleep(0.2)
	        no_of_pagedowns-=1
	    post_elems =browser.find_elements_by_xpath("//a[@class='question_link']")
	    for post in post_elems:
	        qlink = post.get_attribute("href")
	        print(qlink)
	        qlinks.append(qlink)

	    for qlink in qlinks:
	        append_status=0
	        row = list()
	        browser.get(qlink)
	        time.sleep(1)
	        elem = browser.find_element_by_tag_name("body")
	        no_of_pagedowns = 1
	        while no_of_pagedowns:
	            elem.send_keys(Keys.PAGE_DOWN)
	            time.sleep(0.2)
	            no_of_pagedowns-=1

	        #Question Names
	        qname =browser.find_elements_by_xpath("//div[@class='question_text_edit']")
	        for q in qname:
	            print(q.text).encode('utf-8')
	            row.append(q.text)

	        #Question Link
	        ql = browser.current_url
	        row.append(ql)

	        #Answer Count    
	        no_ans = browser.find_elements_by_xpath("//div[@class='answer_count']")
	        for count in no_ans:
	            append_status = int(count.text[:2])

	            row.append(count.text)

	        #Follow Count
	        follows = browser.find_elements_by_class_name("ui_button_count_inner")
	        row.append(follows[0].text)
 
	        print('append_status',append_status)

	        if append_status >= 10 and follows[0].text > 40:
	            with open('submission.csv','a') as file:
	                writer = csv.writer(file)
	                writer.writerow(row)
