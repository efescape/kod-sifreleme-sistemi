import requests
import sys
import re
import base64
from datetime import datetime

efescape = "" # Şifrenin alınacağı JustPaste linkini buraya girin.

ksifre = input("Lütfen şifreyi girin: ")

try:
    response = requests.get(efescape)
    if response.status_code == 200:
        sifre = response.text

        match = re.search(r'<div class="jp-text">(.*?)</div>', sifre, re.DOTALL)
        if match:
            smetin = match.group(1).strip()

            try:
                cozuldu = base64.b64decode(smetin)
                csifre = cozuldu.decode('utf-8').strip()
            except Exception as e:
                print("Hata B64:", str(e))
                sys.exit()

            if ksifre != csifre:
                print("Hatalı şifre. Tekrar deneyin.")
                sys.exit()

            print("Şifre doğrulandı.")
            # Buraya kodunuzu yazın. 

        else:
            print("Şifre metni sayfada bulunamadı.")
            sys.exit()

    else:
        print("Sayfa alınamadı, bağlantı hatası:", response.status_code)
        sys.exit()

except Exception as e:
    print("Hata oluştu:", str(e))
    sys.exit()
