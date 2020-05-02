from selenium import webdriver
import time
import smtplib

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://amazon.in')
time.sleep(1)

keyword = '#name of the product'
flag=0

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('#sender_mail','#receiver_mail')
    subject = 'THE PRICE OF YOUR CHOOSEN PRODUCT FELL DOWN UNDER #price_assigned'
    body = 'PRODUCT ADDED TO YOUR CART. GO CHECK IT NOW BY THIS LINK \n https://www.amazon.in/cart/ebooks?&ref=ebook_dp_buybox_vc_btn'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail('#sender_mail','#receiver_mail',msg)
    print("Email has been sent!")
    server.quit

search_box = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
time.sleep(1)
search_box.send_keys(keyword)
time.sleep(1)
srch_btn = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
time.sleep(1)
book = driver.find_element_by_link_text('The Pragmatic Programmer: From Journeyman to Master')
time.sleep(1)
book.click()
new_tab=driver.window_handles
for tab in new_tab:
    driver.switch_to_window(tab)
    if(driver.current_url=='https://www.amazon.in/Pragmatic-Programmer-Journeyman-Master-ebook/dp/B003GCTQAE/ref=sr_1_2?dchild=1&keywords=the+pragmatic+programmer&qid=1588277242&sr=8-2'):
     break
g = driver.find_element_by_xpath('//*[@id="a-autoid-11-announce"]/span[2]/span')
price = g.text
price = float(price[2:])
time.sleep(1)
if(price<=#price_assigned):
   cart = driver.find_element_by_xpath('//*[@id="add-to-ebooks-cart-button"]').click()
   send_mail()
