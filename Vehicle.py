from copy import copy

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
		self.position = copy(self._CurrPos)
		self._CurrPos.x += self.direction.x * n
		self._CurrPos.y += self.direction.y * n
		if self.is_rec:
			self._path.append(self.GetVector())

	def GetVector(self):	
		return Vector(self._CurrPos.x - self.position.x,self._CurrPos.y - self.position.y)
		
class Car(Vehicle):
	def __init__(self,position,gas,gpu):
		super().__init__(position)
		self.__gas = gas
		self.__gpu = gpu

	def SetGas(self,n):
		if isinstance(n, (int,float)):
			if n > self.GetGas():
				self.__gas = n

	def GetGas(self):
		return self.__gas

	def GetGPU(self):
		return self.__gpu

	def move(self,n=1):
		if isinstance(n, (int,float)):
			if self.GetGas() / self.GetGPU() >= self.direction.dist(self._CurrPos) * n: # GetGas() / GetGPU() - наш потенциал.
				self.__gas = self.GetGas() - self.GetGPU() * self.direction.dist(self._CurrPos) * n
				super(Car, self).move(n)

Porsche = Car(Point(0,0),0,1) # Gas Peer Unit = 1

Porsche.SetGas(20)

Porsche.is_rec = True

Porsche.direction = Vector(6,8)

Porsche.move(2)

Porsche.SetGas(30)

Porsche.direction = Vector(-6,-8)

Porsche.move()

Porsche.SetGas(1600)

Porsche.direction = Vector(-6,8)

Porsche.move(3)

for i in range(0,len(Porsche._path)):
	print('Vector №' + str(i + 1) + ':',Porsche._path[i])