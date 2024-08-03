from PIL import Image
import numpy as np


def encrypt_image(input_path, output_path, key):
    # Open the image and convert it to a NumPy array
    image = Image.open(input_path)
    image_array = np.array(image)

    # Get image dimensions
    rows, cols, channels = image_array.shape

    # Create a random permutation based on the key
    np.random.seed(key)
    permutation = np.random.permutation(rows * cols)

    # Flatten the image array and apply the permutation
    flat_image_array = image_array.reshape(-1, channels)
    encrypted_flat_image = flat_image_array[permutation]

    # Reshape the encrypted flat image back to the original shape
    encrypted_image_array = encrypted_flat_image.reshape(rows, cols, channels)

    # Create and save the encrypted image
    encrypted_image = Image.fromarray(encrypted_image_array)
    encrypted_image.save(output_path)


def decrypt_image(input_path, output_path, key):
    # Open the encrypted image and convert it to a NumPy array
    encrypted_image = Image.open(input_path)
    encrypted_image_array = np.array(encrypted_image)

    # Get image dimensions
    rows, cols, channels = encrypted_image_array.shape

    # Create the same permutation based on the key
    np.random.seed(key)
    permutation = np.random.permutation(rows * cols)

    # Create an inverse permutation
    inverse_permutation = np.argsort(permutation)

    # Flatten the encrypted image array and apply the inverse permutation
    flat_encrypted_image_array = encrypted_image_array.reshape(-1, channels)
    decrypted_flat_image = flat_encrypted_image_array[inverse_permutation]

    # Reshape the decrypted flat image back to the original shape
    decrypted_image_array = decrypted_flat_image.reshape(rows, cols, channels)

    # Create and save the decrypted image
    decrypted_image = Image.fromarray(decrypted_image_array)
    decrypted_image.save(output_path)


# Function to test the encryption and decryption
def test_image_encryption():
    input_image_path = r'C:\Users\Meghana\PycharmProjects\encryptor\img.jpg'  # Path to the input image
    encrypted_image_path = r'C:\Users\Meghana\PycharmProjects\encryptor\encrypted_image.png'  # Path to save the encrypted image
    decrypted_image_path = r'C:\Users\Meghana\PycharmProjects\encryptor\decrypted_image.png'  # Path to save the decrypted image
    key = 10  # Encryption key

    encrypt_image(input_image_path, encrypted_image_path, key)
    print(f"Image encrypted and saved as {encrypted_image_path}")

    decrypt_image(encrypted_image_path, decrypted_image_path, key)
    print(f"Image decrypted and saved as {decrypted_image_path}")


# Run the test function
test_image_encryption()
