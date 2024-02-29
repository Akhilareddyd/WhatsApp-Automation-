def add_contact_to_group(group_name, contact_to_add):
    #find chat with the correct title
    el_target_chat = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[@title='%s']" % (group_name))))
    el_target_chat.click()
        
    #wait for it to load by detecting that the header changed with the new title
    el_header_title = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='main']//header//span[@title='%s']" % (group_name))))
    
    #click on the menu button
    el_menu_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='main']//div[@data-testid='conversation-menu-button']")))
    el_menu_button.click()
    
    #click on the Group Info button
    el_group_info = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='app']//li//div[@aria-label='Group info']")))
    el_group_info.click()    
    
    #click on the Add Participant button
    el_add_participant = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='drawer-right']//div[text() = 'Add participant']")))
    el_add_participant.click()    
    
    #click on the Search
    el_modal_popup = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-animate-modal-body='true']")))    
    el_modal_popup.find_element(By.XPATH, "//div[contains(@title, 'Search')]").send_keys(contact_to_add)
    
    #click on the Contact
    el_contact_to_add = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-animate-modal-body='true']//span[@title='%s']" % (contact_to_add))))
    el_contact_to_add.click()    
    