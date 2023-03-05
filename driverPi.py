import socket
import tqdm
import spidev as SPI
import ST7789
import time
from PIL import Image,ImageDraw,ImageFont
import os
# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5001
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# create the server socket
# TCP socket
# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 24
bus = 0
device = 0

# Display config
current = ""
lineNum = 1
row = 55
rowLimit = 195
charLim = 19
charCounter = 0

# 240x240 display with hardware SPI:
disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)

# Initialize library.
disp.Init()

# Clear display.
disp.clear()

# Create blank image for drawing.
display = Image.new("RGB", (disp.width, disp.height), "BLACK")
draw = ImageDraw.Draw(display)

# Setting the fonts for the display
largeFont = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 22)
smallFont = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBoldOblique.ttf', 18)
miniFont = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 12)
startupLarge = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 32)
startupMini = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 20)

# Wonderful startup init thing

draw.rectangle([(0,0),(240, 240)],fill = "BLACK")

image = Image.open('pic.jpg')
disp.ShowImage(image, 0, 0)

time.sleep(2)

# Reset plane
draw.rectangle([(0,0),(240, 240)],fill = "BLACK")

# Header
print ("Drew header box")
draw.rectangle([(0,0),(240,40)], fill = "WHITE")

print ("Drew header text")
draw.text((15, 10), ' Watch My Hands ', fill = "BLACK", font = largeFont, align = "center")

#Footer
print ("Drew footer box")
draw.rectangle([(0, 220), (240, 240)], fill = "WHITE")

print ("Drew footer text")
draw.text((10, 225), time.strftime("| Date: %m/%d/%y | Time: %H:%M |"), fill = "BLUE", font = miniFont, align = "right")


# Read from input.txt
with open('string.txt') as f:

    for line in f.readlines():

        line = line.strip()
        arrList = line.split()

        for i in range(len(arrList)):

            current += arrList[i].strip()

            if (len(current) > charLim):

                 row += 20
                 current = arrList[i]

                 if row == rowLimit:

                     row = 55
                     draw.rectangle([(0, 40), (240, 220)], fill = "BLACK")


            current += " "

            draw.text((15, row), (current + " "), font = smallFont, align = "left")

            disp.ShowImage(display,0,0)
            time.sleep(0.25)

time.sleep(3)
s = socket.socket()

# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.")

# receive the file infos
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)

# start receiving the file from the socket
# and writing to the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))

# close the client socket
client_socket.close()
# close the server socket
s.close()
