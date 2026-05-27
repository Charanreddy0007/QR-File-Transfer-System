import math
import os 
import base64
import qrcode
import json
import time
import numpy as np

# Settings

file = "text.txt"
nuber_chunk = 1000

# Read file 

with open(file, "rb") as f:
    file_data = f.read()

# Info

file_name = os.path.basename(file)
file_size = len(file_data)
total_chunks = math.ceil(file_size/nuber_chunk)

print("file_name:",file_name)
print("file_size:",file_size)
print("total_chunks:",total_chunks)

# Spliting into chunks 

packets = []

for i in range(total_chunks):

    start = i * nuber_chunk
    end   = start + nuber_chunk

    chunk = file_data[start:end]

    encoded_chunk = base64.b64encode(chunk).decode()

    # metadata

    packet = {
        "filename": file_name,
        "seq": i,
        "total": total_chunks,
        "size": file_size,
        "data": encoded_chunk
    }

    json_text = json.dumps(packet)

    packets.append(json_text)


img = qrcode.make(packets[int(0)])
img.save("QR.png")
go = input("""Enter "go" to start: """)
    
for i in range(total_chunks):

    if go == "go":

        img = qrcode.make(packets[int(i)])
        time.sleep(0.5)
        img.save("First_img.png")

