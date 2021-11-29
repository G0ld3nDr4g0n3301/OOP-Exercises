def cache(func): # Ещё не доделал.Залью остальное вместе с ЭТИМ в репозиторий.
	d = {} 
	def wrap(*args,**kwargs):
		if len(args) == 1 and len(kwargs.keys()) == 0:
			if str(args[0]) in d.keys():
				print('Loading cache...')
				return d[str(args[0])]
			else:
				d[str(args[0])] = func(args[0])
				return d[str(args[0])]
		else:
			return func(*args,**kwargs)

	return wrap


@cache
def factorial(n):
	return n * factorial(n-1) if n else 1


# Можно создать строку kwstring = ''.join(str([kwargs.items()[i][1]) for i in range(len(kwargs.keys()))])
# Или можно создавать списки внутри списков,и в них хранить все аргументы...
# Ничего не придумывается... Сделаю пока простой вариант.

print(factorial(12))

print(factorial(10))

print(factorial(7))

print(factorial(5))

print(factorial(1))