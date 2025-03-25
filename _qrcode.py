# Import module
import wifi_qrcode_generator.generator as qr

# Use wifi_qrcode() to create a QR image
qr_code = qr.wifi_qrcode('EKS-Misafir', True, 'WPA', 'wezwap-cesGyh-8bojke')
qr_code.print_ascii()
qr_code.make_image().save('2.png')
