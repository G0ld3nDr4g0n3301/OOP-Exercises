class Formula:
	def __init__(self,formula):
		self.operations = []
		self.numbers = []
		for i in formula.split()[::-1]:
			if i in '* / + -'.split():
				self.operations.append(i)
		for i in formula.split():
			if i not in '* / + -'.split():
				self.numbers.append(i)
		self.formula = self.numbers + self.operations
		print(' '.join(self.formula))

	def addElement(self,operation,number):
		self.formula.insert(-len(self.operations),operation)
		self.operations.insert(0,operation)
		self.formula.insert(-len(self.operations),number)
		self.numbers.append(number)
		print(' '.join(self.formula))

	def getOpOrNum(self,isoperation,index):
		if isinstance(isoperation, bool):
			try:
				if isoperation:
					return self.formula[-index]
				else:
					return self.formula[index - 1]
			except:
				print('Achtung!3rr0r!')
	def setOpOrNum(self,isoperation,index,newValue):
		if isinstance(isoperation, bool):
			try:
				if isoperation:
					if newValue in '+ - / *'.split():
						self.formula.pop(-index)
						self.formula.insert(-index + 1,newValue)
				else:
					self.formula.pop(index - 1)
					self.formula.insert(index - 1,newValue)
			except:
				print('Achtung!3rr0r!')


form = Formula('6 * 8 * 1 - 8')

form.addElement('+','3')

form.setOpOrNum(True,4,'-')

print(' '.join(form.formula))