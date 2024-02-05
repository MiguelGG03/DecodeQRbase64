from PIL import Image
import pyzbar.pyzbar as pyzbar
import base64

# Function to decode QR codes from an image
def decode(image_path):
    # Open the image file
    image = Image.open(image_path)
    # Use pyzbar to decode the QR code
    decoded_objects = pyzbar.decode(image)
    return decoded_objects

    """
    def decode_base64(encoded_data):
        # Decode the Base64 encoded data
        decoded_bytes = base64.b64decode(encoded_data)
        # Convert to string
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string

    """
def do(path="flag.png"):
    # Path to the image file
    N = int(input("Enter the number of decodes: "))
    image_path = path
    decoded = decode(image_path)
    if N == 1:
        return decoded
    elif N >= 1:
        image = decoded[0].data
        for _ in range(N):
            image = base64.b64decode(image)
        return image
    else:
        return "Invalid number of decodes"
    
def main():
    print(do("flag.png"))
    

if __name__ == "__main__":
    main()
