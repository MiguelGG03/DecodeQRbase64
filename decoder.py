import pyzbar.pyzbar as pyzbar

def decode(image):
    decoded_objects = pyzbar.decode(image)
    return decoded_objects

if __name__ == "__main__":
    
    
    """
    N = int(input("Enter the number of times to decode: "))
    image = "flag.png"
    for i in range(N):
        image = decode(image)
        print(image)
    """