import csv

def readStopwords(stopwordsFileName):

	#Reading stopwords file and storing each word into 'stopwords' array 
	stopwordsFile = open(stopwordsFileName, "r")
	stopwords = stopwordsFile.read()
	stopwords = stopwords.split('\n')
	return stopwords

def removeStopwords(sentence):

	stopwordsArray = readStopwords("stopwords.txt")
	sentenceWithNoStopWords = []
	for word in sentence:
		flag = 0
		for stopword in stopwordsArray:
			if word == stopword:
				flag = 1
				break
		
		if flag == 0:
			sentenceWithNoStopWords.append(word)
			
	return sentenceWithNoStopWords


def tokenizeSentence(sentence):

	#splitting sentence by spaces
	sentence = sentence.split(' ')
	
	#removing '.' and ','
	for i in range (0, len(sentence)):
		sentence[i] = sentence[i].strip('.')
		sentence[i] = sentence[i].strip(',')
		sentence[i] = sentence[i].lower()
			
	return sentence

def sentenceFilter(table, mySentence, option):

	wordGivenOption = 0
	
	for line in table:
		for myWord in mySentence:
			if line["option"] == option:
				for word in line["words"]:
					if myWord == word:
						wordGivenOption += 1
						print(line)
	
	return wordGivenOption

#Driver Code
if __name__ == "__main__":

	table = []
	dataSetFile = "Dataset.csv"
	with open(dataSetFile, mode='r') as csv_file:
		
		csv_reader = csv.DictReader(csv_file)
		sentenceCount = 0
		
		totalSpam = 0
		totalNotSpam = 0
		
		for row in csv_reader:
			node = {"option": "", "words": []}
			sentence = tokenizeSentence(row['v2'])	
			sentenceWithNoStopWords = removeStopwords(sentence)
			
			if (row['v1'] == "spam"):
				totalSpam += 1
			else:
				totalNotSpam += 1
			
			node['option'] = row['v1']
			node['words'] = sentenceWithNoStopWords
			table.append(node)
			
			#counting number of sentences
			sentenceCount += 1
			
			#if(sentenceCount == 40):
				#break
	
		print("\nTotal Spam Emails: ", totalSpam)
		print("Total Not Spam Emails: ", totalNotSpam)
		
	while 1:
	
		#taking input
		mySentence = input("\nEnter a sentence: ")
		
		#exit condition
		if mySentence == "exit":
			break
		
		#tokenizing and removing stopwords from my sentence
		mySentence = tokenizeSentence(mySentence)	
		mySentence = removeStopwords(mySentence)
		
		print("\nSentence after removing Stopwords", mySentence)
		
		lines = sentenceFilter(table, mySentence, "spam")
		print("\nTotal sentence found in spam Emails: ", round(((lines/totalSpam) * 100), 2))
		
		lines = sentenceFilter(table, mySentence, "notSPAM")
		print("\nTotal sentence found in not spam Emails: ",  round(((lines/totalNotSpam) * 100), 2))
	