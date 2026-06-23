import qrcode
url = input("enter the URL").strip()
qr = qrcode.QRCode()
qr.add_data(url)
img =qr.make_image()
img.save("qrcode.png")
print("QR generated successfully! 🎉")
print("Saved as qrcode.png")