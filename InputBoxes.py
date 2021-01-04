from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
driver=webdriver.Chrome()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
inputboxes=driver.find_elements(By.CLASS_NAME,'text_field') #capture all input boxes in the which have the same class name
print(len(inputboxes)) # 6 input boxes
status_D=driver.find_element_by_id('RESULT_TextField-1').is_enabled()
print("displayed or not: ",status_D)
status_E=driver.find_element_by_id('RESULT_TextField-1').is_enabled()
print("Enabled or not: ",status_E)
driver.find_element_by_id('RESULT_TextField-1').send_keys("tarek")
driver.find_element_by_id('RESULT_TextField-2').send_keys("chrigui")
driver.find_element_by_id('RESULT_TextField-3').send_keys("+216 23 787 766")
driver.find_element_by_id('RESULT_TextField-4').send_keys("Tunisia")
driver.find_element_by_id('RESULT_TextField-5').send_keys("kairouan")
driver.find_element_by_id('RESULT_TextField-6').send_keys("tarekchrigui@gmail.com")

# working Radio button (expl: male/female)

driver.implicitly_wait(5) #implicit wait (from selenuim)
Status_male=driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").is_selected()
print(Status_male)
wait = WebDriverWait(driver,10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='q26']/table/tbody/tr[1]/td/label")))
element.click()
Status_male=element.is_selected() #problem here to be checked
print(Status_male)

# working with check boxes

driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").click()
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[7]/td/label").click()
print("sunday is selected or not: ", driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").is_selected()) #problem here to be checked


time.sleep(5)
driver.quit()

