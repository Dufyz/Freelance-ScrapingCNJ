# Pagina Mapa

# Selecionando estados
el_mapa_ufs_geral = waiter.until(EC.presence_of_element_located((By.XPATH, r'/html/body/div[2]/div[5]/fieldset/map')))
el_mapa_ufs = el_mapa_ufs_geral.find_elements(By.TAG_NAME, "area")

# for uf in el_mapa_ufs[1:]:
#     area.click()
#     time.sleep(2)
el_mapa_ufs[-10].click()

# Selecionando municipios
el_mapa_muns_geral = waiter.until(EC.presence_of_element_located((By.XPATH, r'//*[@id="cidade_serventia"]')))
el_mapa_muns = el_mapa_muns_geral.find_elements(By.TAG_NAME, "option")

# for mun in el_mapa_muns[1:]:
#     mun.click()
#     time.sleep(2)
el_mapa_muns[19].click()

# Pesquisar
el_pesquisar = waiter.until(EC.presence_of_element_located((By.XPATH, r'//*[@id="div_cidade"]/div/table/tbody/tr[2]/td/button[1]')))
el_pesquisar.click()