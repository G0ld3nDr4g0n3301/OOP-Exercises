class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def dist(self,other):
		if isinstance(other,Point):
			return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

class Vector(Point):
	def length(self,other):
		if isinstance(other,Vector):
			return self.dist(other.x,other.y)

	def __str__(self):
		return f'x = {self.x},y = {self.y}'

	def __add__(self,other):
		if isinstance(other,Vector):
			return Vector(self.x + other.x,self.y + other.y)

	def __sub__(self,other):
		if isinstance(other,Vector):
			return Vector(self.x - other.x,self.y - other.y)

	def __mul__(self,other):
		if isinstance(other,(int,float)):
			return Vector(self.x * other,self.y * other)
		elif isinstance(other,Vector):
			return self.x * other.x + self.y * self.y
	def __rmul__(self,other):
		self * other

class Vehicle:
	def __init__(self,position):
		if isinstance(position,Point):
			self.position = position
		self.direction = Point(0,0)
		self._CurrPos = position
		self._vector = self.GetVector()
		self._path = []
		self.is_rec = False

	def move(self,n):
		self.position = self._CurrPos
		print(self.position.x,self.position.y,'<- position from move()')
		self._CurrPos.x += self.direction.x * n
		self._CurrPos.y += self.direction.y * n
		print(self._CurrPos.x,self._CurrPos.y,'<- _CurrPos from move()')

	def GetVector(self):
		print(self.position.x,self.position.y,'<- position from GetVector()')		
		return Vector(self._CurrPos.x - self.position.x,self._CurrPos.y - self.position.y)
		
class Car(Vehicle):
	def __init__(self,position,gas,gpu):
		super().__init__(position)
		self.__gas = gas
		self.__gpu = gpu

	def SetGas(self,n):
		if isinstance(n, (int,float)):
			if n > self.GetGas():
				self.__gas += n

	def GetGas(self):
		return self.__gas

	def GetGPU(self):
		return self.__gpu

	def move(self,n):
		if isinstance(n, (int,float)):
			if self.GetGas() / self.GetGPU() >= self.direction.dist(self._CurrPos) * n: # GetGas() / GetGPU() - наш потенциал.
				self.__gas = self.GetGas() - self.GetGPU() * self.direction.dist(self._CurrPos) * n
				super(Car, self).move(n)

Porsche = Car(Point(0,0),0,1) # GPU = 1

Porsche.SetGas(20) # Gas = 20

print(Porsche.GetVector()) # Всегда (0,0).Это для контроля.

Porsche.direction = Vector(6,8) # Мы должны проехать 10.

Porsche.move(2) # 2 раза

print(Porsche.GetVector())

print(Porsche.GetGas())