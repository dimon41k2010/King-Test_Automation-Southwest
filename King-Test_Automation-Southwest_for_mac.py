from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math

print("Logs:")

url="https://www.southwest.com/"

input_val={'Departing_code':'PVR',
            'Arrive_code':'LAX',
            'Date':'5/20'}

fields_id={'DEPART':'LandingPageAirSearchForm_originationAirportCode',
            'ARRIVE':'LandingPageAirSearchForm_destinationAirportCode',
            'DEPART_DAY':'LandingPageAirSearchForm_departureDate',
            'SEARCH':'LandingPageAirSearchForm_submit-button'}

icons={'flight':'span.actionable-tab--content'}

elements={'checkbox':'label.checkbox_button.checkbox.filters--filter-area-nonstop',
        'yellow_button':'.fare-button.fare-button_primary-yellow.select-detail--fare',
        'to_detailed_page':'air-booking-product-1',
        'pre_price':'fare-button--value-total',
        'post_price':'span.currency.currency_dollars',
        'post_date':'span.flight-detail--heading-date',
        'd-a-code':'span.flight-segments--airport-code'}

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
driver.get(url)

if str(url) == str(driver.current_url):
    print("The browser is on the correct URL.") 

time.sleep(3) #for correct work if connection is slow
driver.execute_script('window.scrollTo(0, 300)') 
time.sleep(2) #to be elegant
l = driver.find_element_by_css_selector(icons['flight']) 
l.click()
print("'Flight' tab selected.")
time.sleep(2) #to be elegant
l=driver.find_element_by_xpath("//input[@value='oneway']"); 
l.click()
print("Checkbox filled.")
time.sleep(2) #to be elegant
l=driver.find_element_by_id(fields_id['DEPART'])
l.send_keys(input_val['Departing_code'])
l.send_keys(Keys.RETURN)
print("Departing_code inputed.")
time.sleep(2) #to be elegant
l=driver.find_element_by_id(fields_id['ARRIVE'])
l.send_keys(input_val['Arrive_code'])
l.send_keys(Keys.RETURN)
print("Arrive_code inputed.")
time.sleep(2) #to be elegant
l=driver.find_element_by_id(fields_id['DEPART_DAY'])
for i in range(5):
    l.send_keys(Keys.BACKSPACE)
l.send_keys(input_val['Date'])
print("Date inputed.")
time.sleep(2) #to be elegant
l=driver.find_element_by_id(fields_id['SEARCH'])
l.click()

time.sleep(10)
try:
    l=driver.find_element_by_css_selector(elements['checkbox'])
    #l=driver.find_element_by_xpath("//button[@aria-label='Display only Nonstop flights.']"); #only nonstop if aviable
    l.click()
    print("Button 'Nonstop' clicked.")
except:
    try:

        time.sleep(5)
        l=driver.find_element_by_xpath("//button[@aria-label='Display only Nonstop flights.']"); #only nonstop if aviable
        l.click()
    except:
        print("No button 'Nonstop'.")

time.sleep(2) #to be elegant
l=driver.find_element_by_css_selector(elements['yellow_button'])
l.click()
print("Yellow box clicked.")
time.sleep(2) #to be elegant

l=driver.find_elements_by_class_name(elements['pre_price'])
temp_cost=int(l[2].text)
time.sleep(2) #to be elegant

l=driver.find_element_by_id(elements['to_detailed_page'])
l.click()
print("Step to detailed page.")
time.sleep(2)

l=driver.find_element_by_css_selector(elements['post_date'])

if input_val['Date'] in l.text:
    print("Date is the same: " + input_val['Date'])

time.sleep(2)

l=driver.find_element_by_css_selector(elements['post_price'])
temp_cost2=math.ceil(float(l.text.replace('$','')))

if temp_cost == temp_cost2:
    print("Price is the same! - " + str(temp_cost) + "$")
time.sleep(2)
l=driver.find_elements_by_css_selector(elements['d-a-code'])

if l[0].text in input_val['Departing_code']:
    print("Departing_code match up: " + input_val['Departing_code'])


if l[1].text in input_val['Arrive_code']:
    print("Arrive_code match up: " + input_val['Arrive_code'])

time.sleep(6)
driver.quit()