# Python Projects Collection

This repository contains multiple Python projects that demonstrate a variety of functionalities and libraries. Each project is a standalone application, designed to serve a specific purpose such as generating QR codes, sending Telegram messages, automating tasks, and interacting with APIs. Below is a brief description of each project.

## Table of Contents

- [Wifi QR Code Generator](#wifi-qr-code-generator)
- [QR Code Generator for Website](#qr-code-generator-for-website)
- [Wifi Network Auto Connect](#wifi-network-auto-connect)
- [Telegram Message Sender](#telegram-message-sender)
- [Audio Message API](#audio-message-api)
- [Auto Typing Automation](#auto-typing-automation)
- [Scheduled WhatsApp Message Sender](#scheduled-whatsapp-message-sender)

## Wifi QR Code Generator

This project generates a WiFi QR code that can be scanned to easily connect to a WiFi network. The QR code is generated using the **wifi_qrcode_generator** Python library.

### Code:
```python
import wifi_qrcode_generator.generator as qr

# Generate a QR code for WiFi connection
qr_code = qr.wifi_qrcode('EKS-Misafir', True, 'WPA', 'wezwap-cesGyh-8bojke')
qr_code.print_ascii()
qr_code.make_image().save('2.png')
QR Code Generator for Website
This project generates a QR code that links to a specific website using the qrcode library. The QR code is saved as an SVG file.

Wifi Network Auto Connect
This project uses the pyzbar library to scan QR codes in real-time and automatically connect to a WiFi network using the credentials encoded in the QR code. The program uses OpenCV to capture and decode QR codes from the camera feed.


Telegram Message Sender
This project sends a message to a specific Telegram chat using a Telegram bot. The requests library is used to interact with the Telegram Bot API.

Telegram Message Sender
This project sends a message to a specific Telegram chat using a Telegram bot. The requests library is used to interact with the Telegram Bot API.


Auto Typing Automation
This project automates typing on your computer using the pyautogui library. It simulates typing a message repeatedly and pressing "Enter".


Scheduled WhatsApp Message Sender
This project uses pywhatkit to send a WhatsApp message at a scheduled time. The message and time are provided as input parameters.

How to Use

1.Clone this repository to your local machine:
git clone https://github.com/your-username/python-projects.git
2.Navigate into the project directory
cd python-projects
3.Run any individual project by executing the corresponding Python script:
python script_name.py
Feel free to contribute to any of these projects by forking this repository and submitting pull requests. Please ensure that your changes are well-documented.

License
This project is licensed under the MIT License - see the LICENSE file for details.




### Açıklamalar:
- **Wifi QR Code Generator**: WiFi QR kodu oluşturur.
- **QR Code Generator for Website**: Web sitesi için QR kodu oluşturur.
- **Wifi Network Auto Connect**: QR kodu ile WiFi'ye otomatik bağlanma.
- **Telegram Message Sender**: Telegram botu ile mesaj gönderir.
- **Audio Message API**: Audio mesaj gönderen bir API kullanır.
- **Auto Typing Automation**: Otomatik olarak yazı yazar ve Enter tuşuna basar.
- **Scheduled WhatsApp Message Sender**: Belirli bir saatte WhatsApp mesajı gönderir.

Bu README dosyasını, projelerinizi tanıtmak ve kullanıcıların nasıl kullanacaklarına dair bilgi sağlamak için kullanabilirsiniz.
