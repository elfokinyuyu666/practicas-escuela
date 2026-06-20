import qrcode

url = "https://practicas-escuela-ak8zmu9jprg4zappbnudulr.streamlit.app"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("consultorio_streamlit_qr.png")

print("QR generado correctamente")
