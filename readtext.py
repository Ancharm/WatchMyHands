import spidev as SPI
import ST7789
import time

from PIL import Image,ImageDraw,ImageFont

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
 
