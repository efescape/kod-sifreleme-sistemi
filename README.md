# 🔐 Kod Şifreleme Doğrulama Sistemi

Bu proje, bir **şifre korumalı sistem** oluşturmak isteyen kullanıcılar için hazırlanmış, **JustPaste.it** bağlantısı üzerinden alınan ve Base64 formatında saklanan bir şifreyi kontrol eden basit bir doğrulama sistemidir.

## 🧩 Özellikler

- Kullanıcıdan şifre girişi alır.  
- JustPaste.it üzerinde saklanan Base64 ile şifrelenmiş metni çeker.  
- Şifreyi çözümler ve girilen şifreyle karşılaştırır.  
- Doğruysa sistem çalışmasına izin verir.  
- Hatalıysa kullanıcıyı bilgilendirip çıkış yapar.  

## ⚙️ Kullanım

### 1. Gerekli Kütüphaneler

```bash
pip install requests
```

### 2. JustPaste.it Hazırlığı

- https://justpaste.it adresine girin.
- Şifrenizi Base64 formatına dönüştürün:

```python
import base64
sifre = "benimsifrem"
print(base64.b64encode(sifre.encode()).decode())
```

- Elde ettiğiniz kodu JustPaste.it üzerinde `<div class="jp-text">` etiketi içinde yayınlayın.
- `efescape` değişkenine JustPaste bağlantınızı girin:

```python
efescape = "https://justpaste.it/your_link"
```

### 3. Kodun Çalıştırılması

```bash
python main.py
```

Kullanıcıdan şifre istenir ve doğrulama yapılır. Başarılı olursa program çalışmasına devam eder.

## 🔐 Güvenlik Notları

- JustPaste linki herkese açık olmamalıdır.
- Şifreleme yöntemi yalnızca **Base64** olduğu için çok yüksek güvenlik sağlamaz; daha güçlü şifreleme yöntemleriyle entegre edilebilir.

### Discord: *kocalfa*
