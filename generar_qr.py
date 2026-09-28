"""Genera qr.png para imprenta.  Uso:  python3 generar_qr.py https://cata.midominio.com
Requiere:  pip install "qrcode[pil]"
"""
import sys
import qrcode
from qrcode.constants import ERROR_CORRECT_H

url = sys.argv[1] if len(sys.argv) > 1 else sys.exit("Indica la URL: python3 generar_qr.py https://...")
qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=40, border=4)  # corrección alta, margen de 4 módulos
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("1")  # 1 bit: negro puro sobre blanco
img.save("qr.png", dpi=(600, 600))
print(f"qr.png creado: {img.size[0]}x{img.size[1]} px  ->  {url}")
