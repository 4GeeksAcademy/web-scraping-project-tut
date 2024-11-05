import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

resource_url = "https://ycharts.com/companies/TSLA/revenues"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}

try:
    response = requests.get(resource_url, headers=headers)
    response.raise_for_status()
    html_content = response.text
    print("Página descargada con éxito.")

    # Crear el objeto BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    print("Contenido HTML transformado en BeautifulSoup.")
except requests.exceptions.RequestException as scrap:
    print("Error al descargar la página.")
    print(scrap)