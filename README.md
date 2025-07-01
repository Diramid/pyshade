# **`pyshade`**  
### *An Unbreakable, Lightning-Fast Encryption Library for Python*  
**Version 1.0.0**  
<sub>Built on the **CryptoShade** reversible algorithm</sub>  

---

`pyshade` is a minimalist yet powerful encryption library for Python, designed to **obfuscate and restore text** effortlessly using a unique, per-run character map. With zero dependencies and pure Python (3.8+), it integrates seamlessly into any project.  

---

## **✨ Key Features**  
✅ **Reversible symmetric cipher** – Decrypt *exactly* what you encrypted.  
✅ **Full ASCII support** – Works with all standard characters.  
✅ **Randomized per-run keys** – Fresh numeric mapping for every encryption.  
✅ **Blazing fast** – O(n) complexity, ideal for any payload size.  
✅ **Zero dependencies** – Pure Python, no external libraries.  
✅ **JSON key export/import** – Securely store or transmit keys.  

---

## **⚡ Quickstart**  
### Installation  
```bash
pip install pyshade
```

### Import  
```python
from pyshade.interface import Pyshade
```

---

## **🔐 Usage**  
> [!NOTE]  
> Currently supports **strings only** (lists/dicts coming soon!).  

### **1. Encryption & Decryption (Standard Key)**  
#### **Encrypt**  
```python
encrypted_data = Pyshade.encrypt("hello world")
```  
Returns a `dict` with:  
- **`data`**: Obfuscated string (e.g., `"364/830/978/978/377/..."`)  
- **`key`**: One-time numeric mapping (e.g., `{"a": 253, "b": 721, ...}`)  

#### **Decrypt**  
```python
decrypted = Pyshade.decrypt(encrypted_data["data"], encrypted_data["key"])
print(decrypted)  # "hello world"
```  

### **2. Encryption & Decryption (JSON Key)**  
#### **Encrypt**  
```python
encrypted_data = Pyshade.encrypt_jsonkey("hello world")
```  
Returns:  
- **`data`**: Same obfuscated string.  
- **`key`**: Key as a JSON string (e.g., `'{"a": 253, "b": 721, ...}'`).  

#### **Decrypt**  
```python
decrypted = Pyshade.decrypt_jsonkey(encrypted_data["data"], encrypted_data["key"])
```  

> ⚠️ **WARNING**  
> The key is **one-time use only**. Lose it, and decryption is *impossible*!  

---

## **💡 Pro Tips**  
- **Never reuse keys**: Each `encrypt()` call generates a *unique* cipher.  
- **Use JSON keys for transmission**: Safer for APIs/networked data.  
- **Static methods**: No need to instantiate `Pyshade`—just call the methods directly!  

---

## **👥 Contribute**  
We welcome contributions! Here’s how to help:  

### **🔧 Setup Development Environment**  
1. Fork the repository and clone it locally.  
  
2. Create a branch for your feature/fix:  
   ```bash
   git checkout -b feature/your-feature-name
   ```  

### **📌 Contribution Guidelines**  
- **Report bugs** via [GitHub Issues](https://github.com/diramid/pyshade/issues).  
- **Suggest features** by opening a discussion.  
- **Submit PRs** for:  
  - Bug fixes (with tests).  
  - New features (documented and tested).  
  - Documentation improvements.  

### **🧪 Testing**  
Ensure all tests pass before submitting:  
```bash
pytest tests/
```  

---

### **📜 License**  
[MIT](LICENSE) – Free for any use.  