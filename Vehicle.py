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
		self._CurrPos = Point(self.position.x,self.position.y)
		self._vector = self.GetVector()
		self._path = []
		self.is_rec = False

	def GetVector(self):
		return Vector(self._CurrPos.x + self.direction.x,self._CurrPos.y + self.direction.y)

	def move(self,n):
		self._CurrPos += n

	def GetVector(self):
		return (self._CurrPos.x + self.direction.x,self._CurrPos.y + self.direction.y)
		
class Car(Vehicle):
	def __init__(self,position,gas,gpu):
		super().__init__(position)
		self.__gas = gas
		self.__gpu = gpu

	def SetGas(self,n):
		if isinstance(n, (int,float)):
			if n > 0:
				self.__gas += n

	def GetGas(self):
		return self.__gas

	def GetGPU(self):
		return self.__gpu

	def move(self,n):
		if self.GetGas() / self.GetGPU() > 0 and self.GetGas() / self.GetGPU() >= n:
			self.move(n)

Porshe = Car(Point(0,0),0,1/5)

Porshe.SetGas(5)

print(Porshe.GetVector())

Porshe.move(25)

print(Porshe.GetVector())