import qrcode
import cv2

def generate(data, save_path):
    qr = qrcode.QRCode(version=1,
                        error_correction=qrcode.ERROR_CORRECT_L,
                        box_size=2,
                        border=2)

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)
generate("{\"id_of_product\": 18 }",'d:/Downloads/images/Voda.png')