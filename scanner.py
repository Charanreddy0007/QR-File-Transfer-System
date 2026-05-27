import cv2
import base64
import json
from pyzbar.pyzbar import decode

# store

recived_chunk = {}

total = None
last_qr = None
file_name = None

# Camera 

camera = cv2.VideoCapture(1)

while True:

    success, frame = camera.read()

    qr_code  = decode(frame)

    for qr in qr_code:

        qr_text = qr.data.decode("utf-8")

        if last_qr == qr_text:
            continue

        print("NEW QR")

        last_qr = qr_text

        packet = json.loads(qr_text)

        total = packet["total"]
        file_name = packet["filename"]
        seq  = packet["seq"]

        decoded_data = base64.b64decode(packet["data"])

        recived_chunk[seq] = decoded_data
        print(f"Stored: {seq}/{total}")

        if len(recived_chunk) == total:
            print("All resived")

            re_created = b""

            for i in range(total):
                re_created += recived_chunk[i] 
        
            with open(f"recived_{file_name}", "wb") as f:
                f.write(re_created)
                print(f"File saved as recived_{file_name}")

            camera.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("Scanner", frame)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()