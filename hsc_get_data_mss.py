from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv

csv_file = open("hsc_data_mss.csv", 'w')
#reicht es, writer hier einmal zu definieren?
writer = csv.DictWriter(
    csv_file, fieldnames=["id", "time", "lang", "place"], delimiter="$")
writer.writeheader()
csv_file.close()

f = open("list_id_mss.txt", "r")
list_id_mss = f.read().split("\n")
f.close()

# Durch \n gibt es eine leere Zeile am Ende. Diese wird durch folgenden Befehl entfernt:
list_id_mss.pop()

driver = webdriver.Firefox()

for item in list_id_mss:
    driver.get("https://www.handschriftencensus.de/" + str(item))
    time.sleep(2)
    try:
        driver.find_element(By.XPATH, "//th[contains(text(),'Entstehungszeit')]/following-sibling::td")
    except NoSuchElementException:
        a = ''
    else:
        a = driver.find_element(By.XPATH, "//th[contains(text(),'Entstehungszeit')]/following-sibling::td").text
    try:
        driver.find_element(By.XPATH, "//th[contains(text(),'Schreibsprache')]/following-sibling::td")
    except NoSuchElementException:
        b = ''
    else:
        b = driver.find_element(By.XPATH, "//th[contains(text(),'Schreibsprache')]/following-sibling::td").text
    try:
        driver.find_element(By.XPATH, "//th[contains(text(),'Schreibort')]/following-sibling::td")
    except NoSuchElementException:
        c = ''
    else:
        c = driver.find_element(By.XPATH, "//th[contains(text(),'Schreibort')]/following-sibling::td").text
    csv_file = open("hsc_data_mss.csv", 'a', errors="replace")
    writer = csv.DictWriter(
        csv_file, fieldnames=["id", "time", "lang", "place"], delimiter="$")
    writer.writerow({"id": item, "time": a, "lang": b, "place": c})
    csv_file.close()
    print(str(list_id_mss.index(item)+1) + "/" + str(len(list_id_mss)))

driver.close()

print("Done!")

