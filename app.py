#Headers File
LINK_MAIN = "https://www.cnj.jus.br/corregedoria/justica_aberta/?"

#Browser File
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from headers import LINK_MAIN

# Criando folders que serão utilizados para salvar os arquivos
PATH_DESKTOP = str(Path.home()) + "\Desktop"

browser = webdriver.Chrome()

browser.headless = True 
wait = WebDriverWait(browser, 2)

def getBrowserDriver():
    browser.get(LINK_MAIN)
    browser.maximize_window()
    return browser, wait



# Main File
import re
import pandas as pd

from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import  NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from browser import getBrowserDriver

browser, waiter = getBrowserDriver()

# Pagina Inicial
el_extrajudicial = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/div/div/div/ul/li[2]/a')))
el_extrajudicial.click()

el_serventias_extrajudicial = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/div/div/div/ul/li[2]/ul/li[1]/a')))
el_serventias_extrajudicial.click()

# Criando dataframe
data = {
    'Denominacao': [""],
    'Situacao': [""],
    'Atribuicoes': [""],
    'Responsavel': [""],
    'Substituto': [""],
    'UF': [""],
    'Municipio': [""],
    'Telefone Principal': [""],
    'Telefone Secundario': [""],
    'Email': [""],
}

df = pd.DataFrame(data)


def getEstados():
    el_mapa_ufs_geral = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset/map')))
    el_mapa_ufs = el_mapa_ufs_geral.find_elements(By.TAG_NAME, "area")

    return el_mapa_ufs

def getMunicipios():
    el_mapa_muns_geral = waiter.until(EC.presence_of_element_located((By.XPATH, r'//*[@id="cidade_serventia"]')))
    el_mapa_muns = el_mapa_muns_geral.find_elements(By.TAG_NAME, "option")

    return el_mapa_muns

def getDados():
    #Dados cartorio
    try:
        denominacao = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/fieldset[1]/table/tbody/tr[2]/td[2]').text
    except NoSuchElementException:
        denominacao = None
    
    try:
        situacao = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/fieldset[1]/table/tbody/tr[5]/td[2]').text
    except NoSuchElementException:
        situacao = None

    #Atribuições
    try:
        atribuicoes = ""
        element_temp = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset[2]/table/tbody')))
        elements_temp = element_temp.find_elements(By.TAG_NAME, 'td')
        for c in range(0, len(elements_temp)):
                if(c % 2 == 1 and c != 1):
                    atribuicoes += f"{elements_temp[c].text[1:]} ;"
    except:
        atribuicoes = None

    #Responsaveis
    try:
        responsavel = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset[3]/table/tbody/tr[1]/td[2]'))).text
        responsavel = re.sub(r"\n.*", "", responsavel)
    except:
        responsavel = None

    try:
        substituto = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset[3]/table/tbody/tr[3]/td[2]'))).text
        substituto = re.sub(r"\n.*", "", substituto)
    except:
        substituto = None

    #Localização
    try:
        uf = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset[4]/table/tbody/tr[1]/td[2]'))).text
    except:
        uf = None
    
    try:
        municipio = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset[4]/table/tbody/tr[2]/td[2]'))).text
    except:
        municipio = None
    
    try:
        telefone_principal = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset[4]/table/tbody/tr[6]/td[2]'))).text
    except:
        telefone_principal = None
    
    try:
        telefone_secundario = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/fieldset[4]/table/tbody/tr[7]/td[2]').text
    except NoSuchElementException:
        telefone_secundario = None

    try:
        email = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/fieldset[4]/table/tbody/tr[7]/td[2]').text
    except NoSuchElementException:
        email = None

    #Atribuições
    try:
        atribuicoes = ""
        element_temp = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset[2]/table/tbody')))
        elements_temp = element_temp.find_elements(By.TAG_NAME, 'td')
        for c in range(0, len(elements_temp)):
                if(c % 2 == 1 and c != 1):
                    atribuicoes += f"{elements_temp[c].text[1:]} ;"
    except:
        atribuicoes = None

    #Arrecadações
    try:
        arrecadacoes = []
        datas = []
        element_temp = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset[6]/table[2]/tbody')))
        elements_temp = element_temp.find_elements(By.TAG_NAME, 'td')
        i = 0
        for c in range(0, len(elements_temp)):
            i += 1
            if i == 3:
                arrecadacoes.append(elements_temp[c].text)
                i = 0
            elif i == 1:
                titulo = elements_temp[c].text
                datasss = re.findall(r'\d{2}/\d{2}/\d{4}', titulo)
                ultima_data = datasss[-1] if datasss else None
                datas.append(ultima_data)

    except:
        arrecadacoes = []

    element_temp = browser.find_element(By.XPATH, '/html/body/div[2]/div[5]/fieldset[4]/table/tbody')
    element_temp = element_temp.find_elements(By.TAG_NAME, 'tr')

    if len(element_temp) == 7:
        email = telefone_secundario
        telefone_secundario = None

    nova_linha = {
        'Denominacao': denominacao,
        'Situacao': situacao,
        'Atribuicoes': atribuicoes,
        'Responsavel': responsavel,
        'Substituto': substituto,
        'UF': uf,
        'Municipio': municipio,
        'Telefone Principal': telefone_principal,
        'Telefone Secundario': telefone_secundario,
        'Email': email,
        **{f'{datas[i]}': valor for i, valor in enumerate(arrecadacoes)}  # Colunas de arrecadação
    }

    nova_linha_df = pd.DataFrame([nova_linha])  # Criar um novo DataFrame com a nova linha

    return nova_linha_df

# Pagina Mapa
error = False
el_mapa_ufs = getEstados()

# Selecionando estados
for uf in range(1, 27):
    # for num in range(1, 2):
    num = 1
    while(True):
        try:
            el_mapa_ufs = getEstados()
            el_mapa_ufs[uf].click()
            el_mapa_muns = getMunicipios()
            el_mapa_muns[num].click()

            browser.implicitly_wait(3)
            el_pesquisar = waiter.until(EC.presence_of_element_located((By.XPATH, r'//*[@id="div_cidade"]/div/table/tbody/tr[2]/td/button[1]')))
            el_pesquisar.click()

            # Pagina Cartorios
            # Selecionando x quantidade de dados em um municipio
            try:
                el_infos_geral = waiter.until(EC.presence_of_element_located((By.XPATH, r'//*[@id="display"]/tbody')))
                el_infos = el_infos_geral.find_elements(By.TAG_NAME, 'a')

                for info in range(len(el_infos) - 1, len(el_infos)):
                    el_infos[info].click()
                    try:
                        el_infos[info].click()
                    except StaleElementReferenceException:
                        pass

                    browser.implicitly_wait(1)
                    nova_linha_df = getDados()
                    df = pd.concat([df, nova_linha_df], ignore_index=True)  # Concatenate DataFrames

                    browser.back()
                    browser.implicitly_wait(1)

                    el_infos_geral = waiter.until(EC.presence_of_element_located((By.XPATH, r'//*[@id="display"]/tbody')))
                    el_infos = el_infos_geral.find_elements(By.TAG_NAME, 'a')
            except:
                error = True

            # Resetando para conseguir clicar novamente
            browser.back()
            browser.back()

            if(error):
                el_serventias_extrajudicial = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/div/div/div/ul/li[2]/ul/li[1]/a')))
                el_serventias_extrajudicial.click()

            browser.implicitly_wait(1)
            error = False
        except StaleElementReferenceException:
            ...
        
        num += 1

        if(num == len(el_mapa_muns)):
            break

df = df.drop(index = 0)

df.to_excel("scraping.xlsx")
