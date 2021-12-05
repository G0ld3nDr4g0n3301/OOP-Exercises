import requests
from typing import Union, Iterator
from json.decoder import JSONDecodeError
from dataclasses import dataclass

class PokeError(Exception):
	pass

@dataclass(repr = False,eq = False,frozen = True)
class BasePokemon:
	name: str

	def __str__(self) -> str:
		return f'Name = {self._name}'.format()


@dataclass(repr = False,eq = False,frozen=True)
class Pokemon(BasePokemon):
	id: int
	name: str
	height: int
	weight: int

	def __str__(self) -> str:
		return f'ID = {self.id}\nName = {self.name}\nHeight = {self.height}\nWeight = {self.weight}'.format()

	def __gt__(self,other) -> bool: # Я пытался указать тут Pokemon для other,но не получилось,извините.
		return self.weight > other.weight


class PokeAPI:

	PokeCacheDict: dict = {}

	def get_pokemon(Info: str ='') -> Union[list,Pokemon]:
		if Info in PokeAPI.PokeCacheDict.keys():
			print('**************')
			print('Loading Cache')
			print('**************')
			return PokeAPI.PokeCacheDict[Info]
		try:
			req = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(Info))
		except:
			raise PokeError('Bad c....ect..n...pshhhhhhhh......')
		if req.status_code == 404:
			raise PokeError('Pokemon not found!')
		try:
			lst: list = req.json()
		except JSONDecodeError:
			raise PokeError('Something\'s wrong with your JSON...')
		if Info == '':
			while len(lst['results']) != lst['count']:
				new = requests.get(lst['next']).json()
				lst['next'] = new['next']
				for i in new['results']:
					lst['results'].append(i)
			namelist: list = [lst['results'][i]['name'] for i in range(lst['count'])]
			PokeAPI.PokeCacheDict[Info] = namelist
			return namelist
		else:
			try:
				PokeAPI.PokeCacheDict[Info] = Pokemon(lst['id'],lst['name'],lst['height'],lst['weight'])
			except:
				raise PokeError('You can only load one pokemon(or all of them)')
			return PokeAPI.PokeCacheDict[Info]

	def get_all(get_full: bool = False): # Генератор аннотировать тоже не получилось без аргументов.
		if get_full:
			for i in PokeAPI.get_pokemon(''):
				yield PokeAPI.get_pokemon(i)
		else:
			for i in PokeAPI.get_pokemon(''):
				yield BasePokemon(i)






print(PokeAPI.get_pokemon('ditto'))


print('*******************************')

first50: Iterator = PokeAPI.get_all(True)
weightList: list = []

for i in range(50):
	weightList.append(next(first50))

print(max(weightList))

'''

# Test for cache

print(PokeAPI.get_pokemon('ditto'))

itr = PokeAPI.get_all(True)

for i in range(55):
	print(next(itr))

itr = PokeAPI.get_all(True)

for i in range(55):
	print(next(itr))
print(PokeAPI.get_pokemon('ditto'))

'''