#  QR File Transfer Experiment

> “What if two laptops could transfer files just by staring at each other?” 👀

This project is a fun Python experiment that transfers files using dynamically changing QR codes.

It is **NOT practical for large files** 😅  
It is **NOT faster than WiFi, Bluetooth, USB, or literally anything modern** 😂

But it *does* prove that data can be transferred visually through QR codes between two systems.

---

# 🎥 How This Weird Thing Works

One laptop becomes the **Sender** 📤  
Another laptop becomes the **Receiver** 📥

The sender:
- Reads a file
- Splits it into chunks
- Converts chunks into QR codes
- Continuously changes the QR image

The receiver:
- Uses webcam to scan QR codes
- Collects chunks
- Rebuilds the original file

Basically:

```text
Laptop A 👁️ ---> 👁️ Laptop B
```

The laptops literally need to **see each other** for this to work 😂

---

# ⚠️ Important Reality Check

This project is:
- A learning experiment
- A computer vision + encoding demo
- A fun idea

This project is NOT:
- Production ready
- Efficient
- Secure
- Fast
- Smart enough for huge files

Trying to transfer a movie file with this is basically self-torture 💀

---

# 📂 Project Structure

```bash
├── encode_qr.py      # Sender script
├── scanner.py        # Receiver script
├── text.txt          # File to transfer
├── QR.png            # Dynamic QR output
├── First_img.png     # Generated QR frames
```

---

# 🛠️ Requirements

Install dependencies:

```bash
pip install qrcode opencv-python pyzbar pillow numpy
```

---

# 🚀 Setup Guide

# 🖥️ Sender System

The system that wants to SEND the file should run:

```bash
python encode_qr.py
```

Inside the script:

```python
file = "text.txt"
```

Change this to your target file.

The script:
- Splits the file into chunks
- Encodes them
- Generates QR codes dynamically

QR codes are saved into:

```text
QR.png
```

and continuously updated.

---

#  Receiver System

The system that wants to RECEIVE the file should run:

```bash
python scanner.py
```

---

#  Camera Setup

Inside `scanner.py`:

```python
camera = cv2.VideoCapture(1)
```

You may need to change:

```python
0
1
2
```

depending on your webcam.

Example:

```python
camera = cv2.VideoCapture(0)
```

---

#  Very Important

The receiver camera must physically SEE the sender's QR code screen.

YES.  
The laptops literally need eye contact. 😂

You can:
- Point one laptop camera at another screen
- Use two monitors
- Use a phone camera
- Even print the QR if you're patient enough

---

# ▶️ How To Run

## Step 1 — Start Sender

```bash
python encode_qr.py
```

You will see:

```text
file_name: text.txt
file_size: 1234
total_chunks: 2
```

Type:

```text
go
```

to begin QR streaming.

---

## Step 2 — Start Receiver

```bash
python scanner.py
```

The webcam window opens and starts scanning QR codes.

---

## Step 3 — Wait Patiently 😅

As QR codes are scanned:

```text
NEW QR
Stored: 0/5
Stored: 1/5
...
```

Once complete:

```text
All received
File saved as recived_text.txt
```

---

# 🧠 What This Project Demonstrates

This experiment combines:

- QR Codes
- Base64 Encoding
- Computer Vision
- Webcam Scanning
- File Chunking
- Data Reconstruction

It’s basically a tiny visual data transmission system.

---

# 🐢 Why It’s Slow

Because:
- QR codes have size limits
- Cameras miss frames
- Encoding is heavy
- Screens refresh slowly
- Reality exists

---

# 🔮 Future Improvements

Maybe someday this can become:

- Animated QR streaming
- Error correction
- Faster chunk handling
- GUI application
- Multi-threaded transfer
- Live video QR broadcasting

Or maybe it remains a cursed science experiment forever 

---

# 💡 Fun Fact

This is technically a form of:
- Optical data transfer
- Visual communication
- Human-visible networking 😂

---

# ❤️ Final Note

This project was made for:
- Learning
- Experimenting
- Having fun with Python

Not for replacing:
- USB drives
- Cloud storage
- WiFi
- Common sense

---

# 📜 License

Free to use, modify, break, and experiment with.