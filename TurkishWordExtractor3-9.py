import requests
from bs4 import BeautifulSoup

def kelime_listesi_ceker(url, harf_sayisi):
    header = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-9,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }

    response = requests.get(url, headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        kelime_listesi = []

        # Kelime listesi ul/li elementleri içinde bulunuyor
        for li in soup.find_all("li"):
            kelime = li.get_text().strip()
            if kelime and len(kelime) == harf_sayisi and kelime.islower():
                kelime_listesi.append(kelime)
        
        return kelime_listesi
    else:
        print(f"Kelime listesi çekilemedi. Durum kodu: {response.status_code}")
        return []

# Vikisözlük'teki harf bazlı kelime listesi URL'leri
base_url = "https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_({letter})"

# Tüm harfler ve harf sayıları için kelime listesi çekme
tum_kelime_listesi = {i: [] for i in range(3, 10)}
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"

for harf in harfler:
    url = base_url.format(letter=harf.upper())
    for harf_sayisi in range(3, 10):
        kelime_listesi = kelime_listesi_ceker(url, harf_sayisi)
        tum_kelime_listesi[harf_sayisi].extend(kelime_listesi)
        print(f"{harf.upper()} harfi için {harf_sayisi} harfli {len(kelime_listesi)} kelime çekildi.")

# Toplam kelime sayısını yazdır
for harf_sayisi in range(3, 10):
    print(f"Toplam {harf_sayisi} harfli {len(tum_kelime_listesi[harf_sayisi])} kelime çekildi.")

# Çekilen kelimeleri ayrı dosyalara yazma
for harf_sayisi in range(3, 10):
    dosya_adi = f"{harf_sayisi}_harfli_turkce_kelime_listesi.txt"
    with open(dosya_adi, "w", encoding="utf-8") as f:
        for kelime in tum_kelime_listesi[harf_sayisi]:
            f.write(kelime + "\n")
