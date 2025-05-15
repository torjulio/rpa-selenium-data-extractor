from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from utils import salvar_csv

def executar_processo():
    options = Options()
    options.add_argument('--headless')
    servico = Service('drivers/chromedriver')
    navegador = webdriver.Chrome(service=servico, options=options)

    navegador.get("https://quotes.toscrape.com/login")
    sleep(1)

    navegador.find_element(By.ID, "username").send_keys("admin")
    navegador.find_element(By.ID, "password").send_keys("admin" + Keys.ENTER)
    sleep(2)

    navegador.get("https://quotes.toscrape.com")
    sleep(1)

    resultados = []

    while True:
        quotes = navegador.find_elements(By.CLASS_NAME, "quote")
        for quote in quotes:
            texto = quote.find_element(By.CLASS_NAME, "text").text
            autor = quote.find_element(By.CLASS_NAME, "author").text
            resultados.append({"Frase": texto, "Autor": autor})

        try:
            proxima = navegador.find_element(By.PARTIAL_LINK_TEXT, "Next")
            proxima.click()
            sleep(1)
        except:
            break

    navegador.quit()
    salvar_csv(resultados, "dados/resultados.csv")
