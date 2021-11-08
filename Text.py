class Text:
	def __init__(self,stringList):
		self.__textList = stringList,

	def GetLen(self):
		return len(self.__textList[0])

	def GetStr(self,n):
		try:
			return self.__textList[0][n - 1]
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



Text1 = Text(['Границы ключ переломлен пополам\n','А наш батюшка Ленин совсем усоп\n','Он разложился на плесень и на липовый мёд\n','А перестройка всё идёт и идёт по плану'])
print(Text1.GetWord(2,4))