import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.handschriftencensus.de/werke") # Aufrufen der Werke-Seite
time.sleep(5) # Pause
#content = driver.find_element(By.CLASS_NAME, "content") # Findet das Content-Element
#list = content.find_elements(By.XPATH, "//a[@href]") # findet die URL-Klasse
list = driver.find_elements(By.XPATH, "//li[@id]")

# Erstellt eine Liste der Klassen-IDs = URLs
list_id = []
for id in list:
    list_id.append(id.get_attribute("id"))

# Schreibt die Liste in Datei
f = open("list_id_werke.txt", "w")
for item in list_id:
   f.write(item[2:] + "\n")
f.close()

driver.close()