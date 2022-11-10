import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# QRコード生成
img = qrcode.make('https://pypi.org/project/qrcode/')
img.save("image/QRcode1.png")


# 高度な生成
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=2,
)
qr.add_data('https://pypi.org/project/qrcode/')
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="black")
# img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
img.save("image/QRcode2.png")


# QRコードに画像を埋め込む
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('https://www.youtube.com/c/%E3%82%8F%E3%81%84%E3%82%8F%E3%81%84/videos?app=desktop&view=0&sort=dd&shelf_id=0')
img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="わいわいアイコン.jpg")
img.save("image/QRcode3.png")


# 独特なQRコード生成
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('https://www.youtube.com/c/%E3%82%8F%E3%81%84%E3%82%8F%E3%81%84/videos?app=desktop&view=0&sort=dd&shelf_id=0')
img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_1.save("image/QRcode4.png")
img_2.save("image/QRcode5.png")