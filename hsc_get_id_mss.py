from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

f = open("list_id_werke.txt", "r")
list_id_werke = f.read().split("\n")
f.close()

# Durch \n gibt es eine leere Zeile am Ende. Diese wird durch folgenden Befehl entfernt:
list_id_werke.pop()
# Um das Scraping unauffälliger zu machen, wird die Reihenfolge in der Liste zufällig verändert:
random.shuffle(list_id_werke)

driver = webdriver.Firefox()
list_url_mss = []
for item in list_id_werke:
    driver.get("https://www.handschriftencensus.de/werke/" + str(item))
    time.sleep(2)
    list = driver.find_elements(By.XPATH, "//ol//a[@href]")
    for id in list:
        if id.get_attribute("href") not in list_url_mss:
            if id.get_attribute("href") != "https://www.handschriftencensus.de/abkverz":
                list_url_mss.append(id.get_attribute("href"))
    print(str(list_id_werke.index(item)+1) + "/" + str(len(list_id_werke)))
driver.close()

list_id_mss = [id[35:] for id in list_url_mss]

f2 = open("list_id_mss.txt", "w")
for item in list_id_mss:
   f2.write(item + "\n")
f2.close()

print("Done!")