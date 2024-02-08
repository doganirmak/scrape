import requests

url = 'https://www.tefas.gov.tr/FonKarsilastirma.aspx'
response = requests.get(url)
with open('sayfa.html', 'w', encoding='utf-8') as file:
    file.write(response.text)
