try:
                pagina = 1
                while True:
                    if pagina > 1:
                        clickable_element = waiter.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='display_next']")))
                        clickable_element.click()

                    el_100 = waiter.until(EC.presence_of_element_located((By.XPATH, '//*[@id="display_length"]/label/select/option[4]')))
                    el_100.click()

                    el_infos_geral = waiter.until(EC.presence_of_element_located((By.XPATH, r'//*[@id="display"]/tbody')))
                    el_infos = el_infos_geral.find_elements(By.TAG_NAME, 'a')

                    for info in el_infos:
                        info.click()
                        try:
                            info.click()
                        except StaleElementReferenceException:
                            pass

                        # Realize ação getDados() para obter os dados
                        nova_linha_df = getDados()
                        df = pd.concat([df, nova_linha_df], ignore_index=True)

                        # browser.back()

                    try:
                        clickable_element = waiter.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='display_next']")))
                        clickable_element.click()
                        
                        pagina += 1
                    except Exception as e:
                        break

            except Exception as e:
                error = True