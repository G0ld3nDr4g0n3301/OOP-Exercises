class Text:
	def __init__(self,stringList):
		self._textList = stringList,

	def GetLen(self):
		return len(self._textList[0])

	def GetStr(self,n):
		try:
			return self._textList[0][n - 1]
		except:
			print('Ошибка')

	def GetWordsNum(self,n):
		firstSplit = self.GetStr(n).split()
#		for i in firstSplit:
#			if len(i.split(',')) > 1:
#				firstSplit.pop(firstSplit.index(i))
#				for x in i.split(','):
#					firstSplit.append(i.split(',')[i.split(',').index(x)]) 
			

		return len(firstSplit)

	def GetWord(self,stringNum,wordNum):
		try:
			return self.GetStr(stringNum).split()[wordNum - 1]
		except:
			print('Ашипка!')

class EditableText(Text):
	def replaceStr(self,stringNum,string):
		if isinstance(string, str):
			try:
				self._textList[0][stringNum - 1] = string
			except:
				print('Вы точно правильный номер строки ввели?')

	def replaceWord(self,stringNum,wordNum,word):
		self.replaceStr(stringNum,self.GetStr(stringNum).replace(self.GetStr(stringNum).split()[wordNum - 1],word))

	def __str__(self):
		string = ' '
		for i in range(self.GetLen()):
			string += self.GetStr(i + 1) + ' '
		return string

	def GetWordPos(self,word):
		wordsList = []
		for i in range(self.GetLen()):
			for x in range(len(self.GetStr(i + 1).split())):
				wordsList.append(self.GetStr(i + 1).split()[x])
		return wordsList.index(word) + 1

Text1 = EditableText(['Границы ключ переломлен пополам\n','А наш батюшка Ленин совсем усоп\n','Он разложился на плесень и на липовый мёд\n','А перестройка всё идёт и идёт по плану'])

print(Text1.GetWord(2,4))

Text1.replaceWord(2,4,'Вася')

print(Text1.GetWordsNum(2))

print(Text1.GetWordPos('Вася'))

print(Text1)