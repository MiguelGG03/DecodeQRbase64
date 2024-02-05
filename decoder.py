from PIL import Image
import pyzbar.pyzbar as pyzbar

# Function to decode QR codes from an image
def decode(image_path):
    # Open the image file
    image = Image.open(image_path)
    # Use pyzbar to decode the QR code
    decoded_objects = pyzbar.decode(image)
    return decoded_objects

if __name__ == "__main__":
    # Path to the image file
    image_path = "flag.png"
    # Print the decoded objects
    print(decode(image_path))
