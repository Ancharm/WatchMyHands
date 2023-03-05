import socket
import tqdm
import os

import cv2
import numpy as np
import onnxruntime as ort

file = open('string.txt', 'w')
file.close()
file = open('string.txt', 'w')

def center_crop(frame):

    h, w, _ = frame.shape
    start = abs(h - w) // 2

    if h > w:

        return frame[start: start + w]
    
    return frame[:, start: start + h]


def main():

    index_to_letter = list('ABCDEFGHIKLMNOPQRSTUVWXY')
    mean = 0.485 * 255.
    std = 0.229 * 255.

    ort_session = ort.InferenceSession("signlanguage.onnx")

    cap = cv2.VideoCapture(0)

    tempLetter = ""

    while True:
        
        ret, frame = cap.read()

        frame = center_crop(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        x = cv2.resize(frame, (28, 28))
        x = (x - mean) / std

        x = x.reshape(1, 1, 28, 28).astype(np.float32)
        y = ort_session.run(None, {'input': x})[0]

        index = np.argmax(y, axis = 1)
        letter = index_to_letter[int(index)]
    
        if (letter != tempLetter):
                
            tempLetter = letter
            file.write(letter)

        cv2.putText(frame, letter, (5, 55), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), thickness=2)
        cv2.imshow("Sign Language Translator", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):

            break

    cap.release()
    cv2.destroyAllWindows()

main()

################
#sends data

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = "172.20.10.2"
# the port, let's use 5001
port = 5001
# the name of file we want to send, make sure it exists
filename = "input.txt"
# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()
