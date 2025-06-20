from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    """
    Encrypts an image by performing pixel manipulation
    :param image_path: Path to the input image
    :param key: Encryption key (integer value)
    :return: Encrypted image as a PIL Image object
    """
    # Open the image using PIL
    img = Image.open(image_path)
    
    # Convert image to RGB mode if it's not already
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Convert image to numpy array for easier manipulation
    img_array = np.array(img)
    
    # Perform encryption by adding the key to each pixel value and modulo 256
    # This ensures the pixel values wrap around if they exceed 255
    encrypted_array = (img_array + key) % 256
    
    # Convert back to PIL Image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    
    return encrypted_img

def decrypt_image(encrypted_img, key):
    """
    Decrypts an encrypted image by reversing the pixel manipulation
    :param encrypted_img: Encrypted image as PIL Image object
    :param key: Encryption key (same integer used for encryption)
    :return: Decrypted image as a PIL Image object
    """
    # Convert encrypted image to numpy array
    encrypted_array = np.array(encrypted_img)
    
    # Perform decryption by subtracting the key and modulo 256
    # Adding 256 before modulo ensures we don't get negative values
    decrypted_array = (encrypted_array - key + 256) % 256
    
    # Convert back to PIL Image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    
    return decrypted_img

def main():
    print("Simple Image Encryption Tool using Pixel Manipulation")
    print("---------------------------------------------------")
    
    # Get user input
    image_path = input("Enter the path to the image file: ")
    operation = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    key = int(input("Enter the encryption/decryption key (integer): "))
    
    try:
        if operation == 'E':
            # Encrypt the image
            encrypted_img = encrypt_image(image_path, key)
            output_path = image_path.split('.')[0] + "_encrypted.png"
            encrypted_img.save(output_path)
            print(f"Image encrypted and saved as {output_path}")
        elif operation == 'D':
            # Decrypt the image
            encrypted_img = Image.open(image_path)
            decrypted_img = decrypt_image(encrypted_img, key)
            output_path = image_path.split('.')[0] + "_decrypted.png"
            decrypted_img.save(output_path)
            print(f"Image decrypted and saved as {output_path}")
        else:
            print("Invalid operation. Please choose 'E' or 'D'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if _name_ == "_main_":
    main()
