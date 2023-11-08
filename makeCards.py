#to make this work, run "pip3 install Pillow"
#to make this work, run "pip3 install pandas"

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import textwrap

# Fonts on the card
partnerNameFont = ImageFont.truetype("fonts/BarlowCondensed-Medium.ttf", 64)
labelFont = ImageFont.truetype("fonts/BarlowCondensed-Medium.ttf", 35)
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

	#default line size
	conditionsFont = ImageFont.truetype("fonts/BioRhyme-Regular.ttf", 30)
	varSize = 38

	temp = conditionOne.split('\n')
	tempList = list()

	bullet1 = textwrap.wrap(conditionOne, width= varSize)

	if len(temp)>1:
		for line in temp:
			tempList = tempList + textwrap.wrap(line, width= varSize)
		bullet1 = tempList

	bullet2 = textwrap.wrap(conditionTwo, width= varSize)
	bullet3 = textwrap.wrap(conditionThree, width= varSize)
	bullet4 = textwrap.wrap(conditionFour, width= varSize)
	bullet5 = textwrap.wrap(conditionFive, width= varSize)

	if len(bullet1)+len(bullet2)+len(bullet3)+len(bullet4)+len(bullet5) >17:
		conditionsFont = ImageFont.truetype("fonts/BioRhyme-Regular.ttf", 26)
		varSize = 42

		bullet1 = textwrap.wrap(conditionOne, width= varSize)
		bullet2 = textwrap.wrap(conditionTwo, width= varSize)
		bullet3 = textwrap.wrap(conditionThree, width= varSize)
		bullet4 = textwrap.wrap(conditionFour, width= varSize)
		bullet5 = textwrap.wrap(conditionFive, width= varSize)

		if len(bullet1)+len(bullet2)+len(bullet3)+len(bullet4)+len(bullet5) >20:

			conditionsFont = ImageFont.truetype("fonts/BioRhyme-Regular.ttf", 24)
			varSize = 48

			bullet1 = textwrap.wrap(conditionOne, width= varSize)
			bullet2 = textwrap.wrap(conditionTwo, width= varSize)
			bullet3 = textwrap.wrap(conditionThree, width= varSize)
			bullet4 = textwrap.wrap(conditionFour, width= varSize)
			bullet5 = textwrap.wrap(conditionFive, width= varSize)

	# Calculate text size for wrapping
	conditionsFontSize = conditionsFont.getbbox(conditionOne);
	flavorFontSize = flavorFont.getbbox(partnerText);

	#Draw the black header
	draw.rectangle(xy = (0, 0, 826, 340), fill = (0, 0, 0), outline = (0, 0, 0), width = 0) 

	# Write the word "Conditions" on the image
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
		
	# Wrap the flavor text to the specified width
	partnerText = textwrap.wrap(partnerText, width= 62)

	#Set the height of the first condition and flavor text
	conditionHeight = 365  
	partnerTextHeight = 1270

	#Adjust the partner name height if it's 2 rows
	if "\n" in partnerName:
		nameHeight = 15
	else:
		nameHeight = 70

	# Draw the partner name on the image
	draw.text((60, nameHeight), partnerName, fill='white', font=partnerNameFont) 
	
	# Draw conditions in wrapped lines of text on the card 
	# The first line of each condition has a check mark
	onecounter = 0
	for line in bullet1:
		if onecounter == 0:
			Image.Image.paste(card, checkImage, (60, conditionHeight))
		draw.text((130, conditionHeight), line, fill='black', font=conditionsFont)
		conditionHeight += conditionsFontSize[3] # Move to the next line
		onecounter += 1

	twocounter = 0
	for line in bullet2:
		if twocounter == 0:
			Image.Image.paste(card, checkImage, (60, conditionHeight+30))
		draw.text((130, conditionHeight+30), line, fill='black', font=conditionsFont)
		conditionHeight += conditionsFontSize[3] # Move to the next line
		twocounter += 1

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

	# Save the card as a PNG file
	fileName = 'cards/'+str(row['scenario'])
	card.save(fileName.title().replace(" ",'')+'.png')
