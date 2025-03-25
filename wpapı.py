import http.client
import ssl

# Güvenli bir SSL bağlamı oluştur
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False  # Hostname kontrolünü devre dışı bırakır
context.verify_mode = ssl.CERT_NONE  # Sertifika doğrulamasını devre dışı bırakır (test amaçlı)

# API bağlantısı
conn = http.client.HTTPSConnection("api.alvochat.com", context=context)

# Gönderilecek veri
payload = "token=YourToken&to=16315555555&audio=https://alvochat-example.s3-accelerate.amazonaws.com/audio/1.mp3&priority=&message_id="
payload = payload.encode('utf8')  # Veriyi uygun biçimde kodla

# Başlıklar
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
}

# POST isteği
conn.request("POST", "/instance1199/messages/audio", payload, headers)

# Yanıtı al ve yazdır
