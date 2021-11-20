from typing import Union

class Point:
	x: Union[int,float]
	y: Union[int,float]

	def __init__(self,x: Union[int,float],y: Union[int,float]) -> None:
		if isinstance(x, (int,float)):
			if isinstance(y, (int,float)):
				self.x = x
				self.y = y
		else:
			print('He')
	
	def dist(self,other: Point) -> Union[int,float]:
			try:
				return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
			except AttributeError:
				print('Другая точка должна иметь атрибуты x и y.')

