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
row = 60
rowLimit = 220

# 240x240 display with hardware SPI:
disp = ST7789.ST7789(SPI.SpiDev(bus, device),RST, DC, BL)

# Initialize library.
disp.Init()

# Clear display.
disp.clear()

# Create blank image for drawing.
image1 = Image.new("RGB", (disp.width, disp.height), "BLACK")
draw = ImageDraw.Draw(image1)
largeFont = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
smallFont = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBoldOblique.ttf', 18)

#print ("***draw line")
#draw.line([(0,0),(240,0)], fill = "BLUE",width = 5)
#draw.line([(240,0),(240,240)], fill = "BLUE",width = 5)
#draw.line([(240,240),(0,240)], fill = "BLUE",width = 5)
#draw.line([(0,240),(0,0)], fill = "BLUE",width = 5)
print ("***draw rectangle")
draw.rectangle([(0,0),(240,40)],fill = "WHITE")

print ("***draw text")

draw.text((15, 10), 'TRANSLATING... ', fill = "BLACK", font = largeFont, align = "center")

with open('input.txt') as f:

    for line in f.readlines():

        if row == rowLimit:

            row = 60
            draw.rectangle([(0, 40), (240, 240)], fill = "BLACK")

        current = line.strip()
        draw.text((15, row), (current + " "), font = smallFont, align = "left")

        row += 20

        time.sleep(0.25)

#draw.text((15, 60), '1234512345123451234 ', fill = "WHITE", font = smallFont, align = "left")
#draw.text((15, 80), '1234512345123451234 ', fill = "WHITE", font = smallFont, align = "left")
#draw.text((15, 100), '1234512345123451234 ', fill = "WHITE", font = smallFont, align = "left")
#draw.text((15, 120), '1234512345123451234 ', fill = "WHITE", font = smallFont, align = "left")
#draw.text((15, 140), '1234512345123451234 ', fill = "WHITE", font = smallFont, align = "left")
#draw.text((15, 160), '1234512345123451234 ', fill = "WHITE", font = smallFont, align = "left")
#draw.text((15, 180), '1234512345123451234 ', fill = "WHITE", font = smallFont, align = "left")
#draw.text((15, 200), '1234512345123451234 ', fill = "WHITE", font = smallFont, align = "left")
#draw.text((15, 220), '1234512345123451234 ', fill = "WHITE", font = smallFont, align = "left")

disp.ShowImage(image1,0,0)
time.sleep(3)

#image = Image.open('pic.jpg')
#disp.ShowImage(image,0,0)
