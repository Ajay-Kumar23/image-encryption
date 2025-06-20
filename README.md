# 🖼️ Image Encryption Tool 🔒  
**Simple Image Encryption using Pixel Manipulation with Python & PIL**

---

## 🚀 PRODIGY_CS_02  
**Image Encryption & Decryption Tool (CLI with PIL)**  

This project was developed as part of my internship at **Prodigy InfoTech**, under the role of **Cyber Security Intern**.  
The task was to build a basic image encryption/decryption system using **Python**, utilizing the **Pillow (PIL)** and **NumPy** libraries.

---

## ✨ Features

- 🔐 Encrypts and decrypts images using a custom pixel manipulation technique  
- 🖼️ Supports all standard image formats (JPG, PNG, etc.)  
- 🔁 Adjustable encryption key (integer-based)  
- 💡 Ensures pixel value wrapping with modular arithmetic  
- 📂 Saves encrypted/decrypted images with descriptive filenames

---

## 🧠 How It Works

This tool manipulates the RGB pixel values of an image:

- **Encryption**: Adds the key value to each RGB pixel component and takes modulo 256  
- **Decryption**: Subtracts the same key and applies modulo 256 again  
- Works on any RGB image format and preserves image dimensions and quality

---

## 📌 Example

```text
Original Image:        myphoto.jpg  
Encryption Key:        50  
Encrypted Output:      myphoto_encrypted.png  
Decrypted Output:      myphoto_decrypted.png
