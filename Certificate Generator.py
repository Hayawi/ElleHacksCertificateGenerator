import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import openpyxl as xw

wbOne = xw.load_workbook('ElleHacks-Participant-Confirmation-Responses.xlsx')
sht1 = wbOne['Sheet1']

font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 25)
for registrants in range(1, sht1.max_row):
	img = Image.open("Participants.png")
	draw = ImageDraw.Draw(img)
	name = str(sht1['A' + str(registrants)].value) + ' ' + str(sht1['B' + str(registrants)].value)
	print(name)
	xLocation = 570 - len(name) * 7
	draw.text((xLocation,515), name, (0,0,0), font=font)
	draw = ImageDraw.Draw(img)
	del draw
	img.save(name + " Certificate.png")