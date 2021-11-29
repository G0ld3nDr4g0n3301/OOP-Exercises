from time import perf_counter # Пойдём по простому пути - будем мерять время.
from math import log2 # Для усложнения измеряемой ф-ции я решил перемножать логаримфмы аргументов по основанию 2.
from functools import reduce


def time_it(func):
	def wrap(*args,**kwargs):
		start: float = perf_counter()
		print('Засекаем...')
		print('Результат выполнения Функции --> ' + str(func(*args,**kwargs)))
		print(f'Функция выполнилась за {perf_counter() - start} секунды.'.format())
	return wrap


@time_it
def test_func(a=0,b=0,c=0,d=1,e=3,f=4,g=128) -> float:
	try:
		lst: list = [a,b,c,d,e,f,g]
		for i in range(len(lst)):
			lst[i] = log2(lst[i])
		return reduce(lambda x,y: x * y, lst)
	except:
		return None


test_func(2,4,8,d = 16,e = 32,f = 64)