import requests
from bs4 import BeautifulSoup

def kelime_listesi_ceker(url):
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
            if kelime and kelime[0].islower():
                kelime_listesi.append(kelime)
        
        return kelime_listesi
    else:
        print(f"Kelime listesi çekilemedi. Durum kodu: {response.status_code}")
        return []

base_url = "https://tr.wiktionary.org/wiki/Vikisözlük:Sözcük_listesi_({letter})"

tum_kelime_listesi = []
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
for harf in harfler:
    url = base_url.format(letter=harf.upper())
    kelime_listesi = kelime_listesi_ceker(url)
    tum_kelime_listesi.extend(kelime_listesi)
    print(f"{harf.upper()} harfi için {len(kelime_listesi)} kelime çekildi.")

print(f"Toplam {len(tum_kelime_listesi)} kelime çekildi.")
print(tum_kelime_listesi[:50]) 

with open("turkish_words.txt", "w", encoding="utf-8") as f:
    for kelime in tum_kelime_listesi:
        f.write(kelime + "\n")
