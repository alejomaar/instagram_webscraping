#Link para Chromedriver: https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/
#Importar Selenium para aplicaciones basadas en la web para webscraping
from selenium import webdriver
from selenium.webdriver.common import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
 
#Ruta para el controlador de chrome 
path = r'D:\Descargas\chromedriver_win32\chromedriver.exe'
#Cargar el controlador en python
driver = webdriver.Chrome(executable_path = path)
#Establecer la pagina de objetivo
driver.get('https://www.instagram.com/')

#Guardar los objetos html por medio de selectores css
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#Limpiar y asignar los valores de los inputs seleccionados, para entrar a la cuenta de usuario
username.clear()
username.send_keys("user")
password.clear()
password.send_keys("password")

#Dar click a enviar formulario para entrar al perfil
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))

#Second Page
#Asignar la palabra clave
keyword = "#ivanduque"
#Seleccionar el campo de busqueda de instagram 
searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.XTCLo")))
#Limpiar el campo de busqueda
searchbox.clear()
#asignar la palabra clave al campo de texto de busqueda
searchbox.send_keys(keyword)

# Esperar 4 segundos para que cargue los resultados de la busqueda del hashtag de duque
time.sleep(4)
#Seleccionar el resultado del hashtag y ir hacia el resultado
my_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/"+keyword[1:]+"/')]")))
my_link.click()
#Third Page

#Moverse hacia abajo de la pagina para cargar mas resultados y repetir el proceso n_scroll veces
n_scrolls = 20
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

#Obtener todos los tag "a" de la pagina y por medio de una consulta...
#Javascript seleccionar el href(link) de todos ellos
anchors = driver.execute_script("return [...document.querySelectorAll('a')].map(a=> a.href)")

#Obtener todos los links que hagan referencia a publicaciones
anchors = [a for a in anchors if a.startswith("https://www.instagram.com/p/")]
#anchors= anchors[0:15] #Obtener cantidad limitida de elementos
Data = {'username':[], 'comment':[],'date':[], } 
print(len(anchors))
hashIndex = 0;
#para todos los links, obtener los datos de ellos y empezar a llenar la tabla
for page in anchors:
    #Cargar la pagina
    driver.get(page)
    #esperar 1 segundo que cargue
    time.sleep(1)
    #Obtener usuario, comentario, fecha y añadirlos a la tabla por medio de 
    #script javascript, por consultas de clases de html.
    #C4VMK: Clase que almacena los datos de la publicacion del usuario
    #_1o9PC: Clase de html donde se encuentra la fecha  
    username = driver.execute_script("return document.querySelector('.C4VMK').querySelector('span').innerText");
    comment = driver.execute_script("return document.querySelector('.C4VMK>span').textContent");
    date = driver.execute_script("return document.querySelector('._1o9PC').innerText");
    
    #Añadir a cada clave del diccionario
    Data['username'].append(username)
    Data['comment'].append(comment)
    Data['date'].append(date)

#Pasar el diccionario a un dataframe 
Dataframe = pd.DataFrame.from_dict(Data)
print(Dataframe)
#Exportar dataframe a xlsx
Dataframe.to_csv('export_dataframe2.csv', encoding='utf-16')

