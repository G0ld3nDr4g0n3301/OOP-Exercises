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
		self.formula = ' '.join(self.numbers) + ' ' + ' '.join(self.operations)
		print(self.formula)

	def addElement(self,operation,number):
		self.formula = self.formula.split()
		self.formula.insert(-len(self.operations),operation)
		self.operations.insert(0,operation)
		self.formula.insert(-len(self.operations),number)
		self.numbers.append(number)
		self.formula = ' '.join(self.formula)
		print(self.formula)

form = Formula('6 * 8 * 1 - 8')

form.addElement('+','3')