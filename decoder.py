import pyzbar.pyzbar as pyzbar

def decode(image):
    decoded_objects = pyzbar.decode(image)
    return decoded_objects

