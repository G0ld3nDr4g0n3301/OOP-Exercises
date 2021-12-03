import requests
from typing import Union

class BasePokemon:
	name: str

	def __init__(self,name: str) -> None:
		self._name = name

	def __str__(self) -> str:
		return f'Name = {self._name}'.format()



class Pokemon(BasePokemon):
	id: int
	name: str
	height: int
	weight: int


	def __init__(self,id: int,name: str,height: int,weight: int) -> None:
		super().__init__(name)
		self.__id = id
		self.__height = height
		self.__weight = weight

	def __str__(self) -> str:
		return f'ID = {self.__id}\nName = {self._name}\nHeight = {self.__height}\nWeight = {self.__weight}'.format()

	def __gt__(self,other: Pokemon) -> bool:
		return self.__weight > other.__weight



class PokeAPI:

	def get_pokemon(Info='': str) -> Union(list,Pokemon):
		req = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(Info))
		lst: list = req.json()
		if Info == '':
			while len(lst['results']) != lst['count']:
				new = requests.get(lst['next']).json()
				lst['next'] = new['next']
				for i in new['results']:
					lst['results'].append(i)
			namelist: list = [lst['results'][i]['name'] for i in range(lst['count'])]
			return namelist
		else:
			return Pokemon(lst['id'],lst['name'],lst['height'],lst['weight'])

	def get_all(get_full=False: bool):             #Как аннотировать генераторы???
		if get_full:
			for i in PokeAPI.get_pokemon(''):
				yield PokeAPI.get_pokemon(i)
		else:
			for i in PokeAPI.get_pokemon(''):
				yield BasePokemon(i)


print(PokeAPI.get_pokemon('ditto'))


print('*******************************')

first50 = PokeAPI.get_all(True)
weightList: list = []

for i in range(50):
	weightList.append(next(first50))

print(max(weightList))