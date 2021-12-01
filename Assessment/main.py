import requests

class BasePokemon:
	def __init__(self,name):
		self._name = name

	def __str__(self):
		return f'Name = {self._name}'.format()



class Pokemon(BasePokemon):

	def __init__(self,id,name,height,weight):
		super().__init__(name)
		self.__id = id
		self.__height = height
		self.__weight = weight

	def __str__(self):
		return f'ID = {self.__id}\nName = {self._name}\nHeight = {self.__height}\nWeight = {self.__weight}'.format()



class PokeAPI:

	def get_pokemon(Info):
		req = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(Info))
		lst = req.json()
		if Info == '':
			namelist = [lst['results'][i]['name'] for i in lst['results']]
			return namelist
		else:
			return Pokemon(lst['id'],lst['name'],lst['height'],lst['weight'])

	def get_all(get_full=False):
		if get_full:
			pass
		else:
			yield [BasePokemon(i) for i in PokeAPI.get_pokemon('')]

print([PokeAPI.get_all()])
