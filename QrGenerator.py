# Creating a qrcode with desired link under 10 lines of code
# must have qrcode and pillow packages installed
# can be easily done using pip install
# a png file "QR.png" will be saved in the same folder

import qrcode

qr = qrcode.QRCode(version=1, box_size=15, border=5)

data = 'https://github.com/21Siddhantjain'
# adding data (here my github profile link) in the qrcode
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill='black', back_color='white')
image.save('QR.png')
