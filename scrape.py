import requests
from bs4 import BeautifulSoup

# Web sayfasının URL'si
url = 'https://www.tefas.gov.tr/FonKarsilastirma.aspx'

# URL'den veri almak
response = requests.get(url)

# Durum kodunu kontrol etmek ve HTML içeriğini ayrıştırmak
if response.status_code == 200:
    # BeautifulSoup nesnesi oluşturmak
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Tüm başlık etiketlerini çıkarmak ve yazdırmak
    for tag in ['div']:
        for element in soup.find_all(tag):
            print(f"{tag}: {element.text.strip()}")
else:
    print("Web sayfasından veri alınamadı. Durum kodu:", response.status_code)

