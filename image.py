import qrcode 
import streamlit as st
from PIL import Image

title = "QR Code Generator"

url_text = st.text_input("Enter URL to generate QR Code")
img_name = st.text_input("Enter image name")
size = st.number_input("Enter image size")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=50/size,
)
qr.add_data(url_text)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{img_name}.png")
st.image(f"{img_name}.png",caption=img_name)