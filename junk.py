import re
#definitely keep
newPrevChar = ''
stringOfResults = "poplzzzzyyyyttattattyysaoonn1a11zzzzyyyypoop"
newstringOfResults = ""
guessString = ''
alternativeString = ''
#might keep
semiFinalString = ''
finalString = ''


for currentChar in stringOfResults:
	# print('newPrevChar:' + newPrevChar +' currentChar:' + currentChar)
	newstringOfResults+=newPrevChar
	newPrevChar = currentChar
newstringOfResults+=newPrevChar
for currentCharIndex in range(len(newstringOfResults)//2):
	if(newstringOfResults[currentCharIndex * 2] == newstringOfResults[currentCharIndex * 2 + 1]):
		guessString += newstringOfResults[currentCharIndex * 2]
		alternativeString += newstringOfResults[currentCharIndex * 2]
	else:
		if(ord(newstringOfResults[currentCharIndex * 2]) > ord(newstringOfResults[currentCharIndex * 2+1])):
			guessString += newstringOfResults[currentCharIndex * 2]
			alternativeString += newstringOfResults[currentCharIndex * 2+1]
		else:
			guessString += newstringOfResults[currentCharIndex * 2+1]
			alternativeString += newstringOfResults[currentCharIndex * 2]
print(alternativeString)
print(guessString)
guessString = re.sub(r'.*zzyy(.+)zzyy.*', r'\1', guessString)
print(guessString)