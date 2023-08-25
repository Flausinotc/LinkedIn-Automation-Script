# Importar as bibliotecas necessárias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Definir o termo a ser pesquisado / Login / Senha
termo_pesquisa = 'Desenvolvedor'
login=''
senha=''

# Inicializar o driver do Chrome
driver = webdriver.Chrome()

# Acessar o site desejado
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
sleep(3)

# Preencher o Login
campo_preencher = driver.find_element(By.XPATH,"//input[@id='username']")
campo_preencher.send_keys(login)

# Preencher a senha
campo_preencher = driver.find_element(By.XPATH,"//input[@id='password']")
campo_preencher.send_keys(senha)

# Clicar no botão de ENTRAR
botaopesquisar = driver.find_element(By.XPATH,"//button[@class='btn__primary--large from__button--floating']")
botaopesquisar.click()
sleep(3)


# Entra no link que só seria possivel entrar logado
campo_pesquisar = driver.find_element(By.XPATH,"//input[@class='search-global-typeahead__input']")
campo_pesquisar.send_keys(termo_pesquisa)

driver.get('https://www.linkedin.com/search/results/people/?keywords=desenvolvedor&origin=CLUSTER_EXPANSION&searchId=5e6e7a10-937e-4306-893b-49726791854d&sid=T!f')
sleep(3)


#Desenvolver botão clica conectar
try:
    # Encontrar o botão pelo XPath com base na classe e no texto
    botao_conectar = driver.find_element(By.XPATH, "//span[@class='artdeco-button__text' and text()='Conectar']")
    
    # Clicar no botão 
    botao_conectar.click()
    #Verifica se realmente foi clicado ou se deu algum tipo de erro
    print("Botão clicado com sucesso!")
    
except Exception as e:
    print("Ocorreu um erro:", e)

#Desenvolver botão clica adicionar nota(Mensagem)

try:
    # Encontrar o botão pelo XPath com base na classe e no texto
    botao_conectar = driver.find_element(By.XPATH, "//span[@class='artdeco-button__text' and text()='Adicionar nota']")
    
    # Clicar no botão 
    botao_conectar.click()
    #Verifica se realmente foi clicado ou se deu algum tipo de erro
    print("Botão clicado com sucesso!")
    
except Exception as e:
    print("Ocorreu um erro:", e)

#Digita a mensagem desejada

mensagem_desejada = "Olá, me Chamo Thiago, tudo bem? É um prazer entrar em contato! Estou em busca de expandir minha rede de contatos com profissionais tão qualificados quanto você. Desejo conectar-me para trocar ideias, compartilhar experiências e potencialmente explorar oportunidades colaborativas."
campo_mensagem = driver.find_element(By.ID, "custom-message")
campo_mensagem.clear()  # Limpa o campo (opcional, se quiser substituir o conteúdo anterior)
campo_mensagem.send_keys(mensagem_desejada)

#Desenvolver botão Enviar 

botao_conectar = driver.find_element(By.XPATH, "//span[@class='artdeco-button__text' and text()='Enviar']")
botao_conectar.click()
sleep(7)