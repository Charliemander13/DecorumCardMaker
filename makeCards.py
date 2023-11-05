#to make this work, run "pip3 install Pillow"
#to make this work, run "pip3 install pandas"

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import textwrap

# Fonts on the card
partnerNameFont = ImageFont.truetype("fonts/BarlowCondensed-Medium.ttf", 64)
labelFont = ImageFont.truetype("fonts/BarlowCondensed-Medium.ttf", 35)
conditionsFont = ImageFont.truetype("fonts/BioRhyme-Regular.ttf", 30)
flavorFont = ImageFont.truetype("fonts/BarlowCondensed-LightItalic.ttf", 35)

# Size of the card
width, height = 826, 1417

# Load the CSV file into a DataFrame
csvFile = 'cardData.csv' 
df = pd.read_csv(csvFile)

df = df.fillna('')

# Repeat this process on each card in the CSV
for index, row in df.iterrows():

	# Create the white base card
	card = Image.new('RGB', (width, height), 'white')
	draw = ImageDraw.Draw(card)
	
	# Access data using row names
	partnerName = str(row['partner'])
	partnerText = str(row['text'])
	conditionOne = str(row['condition 1'])
	conditionTwo = str(row['condition 2'])
	conditionThree = str(row['condition 3'])
	conditionFour = str(row['condition 4'])
	conditionFive = str(row['condition 5'])

	# Calculate text size for wrapping
	partnerNameFontSize = partnerNameFont.getbbox(partnerName);
	conditionsFontSize = conditionsFont.getbbox(conditionOne);
	flavorFontSize = flavorFont.getbbox(partnerText);

	#Draw the black header
	draw.rectangle(xy = (0, 0, 826, 340), fill = (0, 0, 0), outline = (0, 0, 0), width = 0) 

	# Draw the word "Conditions" on the image
	draw.text((60, 265), 'CONDITIONS', fill='white', font=labelFont)

	# Find the stripe color
	if str(row['partner color']) == 'Red':
		stripeColor = 'red'

	elif str(row['partner color']) == 'Blue':
		stripeColor = 'blue'

	elif str(row['partner color']) == 'Green':
		stripeColor = 'green'

	elif str(row['partner color']) == 'Yellow':
		stripeColor = 'yellow'	
	
	else: 
		stripeColor = 'black'

	#Draw the color stripe 
	draw.rectangle(xy = (0, 177, 826, 206), fill = (stripeColor), outline = (0, 0, 0), width = 0) 

	#Import the partner icons and check mark image
	parterOneImage = Image.open(r"/Users/charliemackin/Documents/GitHub/DecorumCardMaker/Partner1Image.png")
	parterTwoImage = Image.open(r"/Users/charliemackin/Documents/GitHub/DecorumCardMaker/Partner2Image.png")
	checkImage = Image.open(r"/Users/charliemackin/Documents/GitHub/DecorumCardMaker/Check.png")
	# Find the partner number and paste the partner icons
	if str(row['partner number']) == '1':
		Image.Image.paste(card, parterOneImage, (576, 0))

	else:
		Image.Image.paste(card, parterTwoImage, (576, 0))
		
	# Wrap text to the specified width
	bullet1 = textwrap.wrap(conditionOne, width= 38)
	bullet2 = textwrap.wrap(conditionTwo, width= 38)
	bullet3 = textwrap.wrap(conditionThree, width= 38)
	bullet4 = textwrap.wrap(conditionFour, width= 38)
	bullet5 = textwrap.wrap(conditionFive, width= 38)
	partnerText = textwrap.wrap(partnerText, width= 62)

	#Set the hight of the first condition, will update as we print
	conditionHeight = 415
	partnerTextHeight = 1270

	if "\n" in partnerName:
		nameHeight = 15
	else:
		nameHeight = 70

	# Draw the partner name on the image
	draw.text((60, nameHeight), partnerName, fill='white', font=partnerNameFont) 
	
	# Draw wrapped lines of text on the image the first line of each condition has a check mark
	Image.Image.paste(card, checkImage, (60, conditionHeight))
	for line in bullet1:
		draw.text((130, conditionHeight), line, fill='black', font=conditionsFont)
		conditionHeight += conditionsFontSize[3] # Move to the next line

	Image.Image.paste(card, checkImage, (60, conditionHeight+30))
	for line in bullet2:
		draw.text((130, conditionHeight+30), line, fill='black', font=conditionsFont)
		conditionHeight += conditionsFontSize[3] # Move to the next line

	threecounter = 0
	for line in bullet3:
		if threecounter == 0:
			Image.Image.paste(card, checkImage, (60, conditionHeight+60))
		draw.text((130, conditionHeight+60), line, fill='black', font=conditionsFont)
		conditionHeight += conditionsFontSize[3] # Move to the next line
		threecounter += 1

	fourcounter = 0
	for line in bullet4:
		if fourcounter == 0:
			Image.Image.paste(card, checkImage, (60, conditionHeight+90))
		draw.text((130, conditionHeight+90), line, fill='black', font=conditionsFont)
		conditionHeight += conditionsFontSize[3] # Move to the next line
		fourcounter += 1
	
	fivecounter = 0
	for line in bullet5:
		if fivecounter == 0:
			Image.Image.paste(card, checkImage, (60, conditionHeight+120))
		draw.text((130, conditionHeight+120), line, fill='black', font=conditionsFont)
		conditionHeight += conditionsFontSize[3] # Move to the next line
		fivecounter += 1

	for line in partnerText:
		draw.text((60, partnerTextHeight), line, fill='black', font=flavorFont)
		partnerTextHeight += flavorFontSize[3] # Move to the next line

	# Save the image as a PNG file
	fileName = 'cards/'+str(row['scenario'])
	card.save(fileName.title().replace(" ",'')+'.png')
