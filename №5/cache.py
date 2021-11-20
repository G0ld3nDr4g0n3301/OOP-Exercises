def cache(func): # Ещё не доделал.Залью остальное вместе с ЭТИМ в репозиторий.
	d = {} 
	def wrap(*args,**kwargs):
		print(args,kwargs.items(),kwargs)
		if len(args) == 1:
			if args[0] in d.keys():
				return d[args[0]]
			else:
				d.fromkeys(args[0],func(args[0]))
				return d[args[0]]

		elif len(kwargs.keys()) == 1:
			if kwargs.items() in d.keys():
				return d[kwargs.items()]
			else:
				d.formkeys(kwargs.items(),func(**kwargs))
				return d[kwargs.items()]

		else:
			return func(*args,**kwargs)

		name = f'{args,kwargs}'.format()
		print(name)

		if name in d.keys():
			return d[name]

		else:
			d.fromkeys(name, func(*args,**kwargs))
			return result

	return wrap


@cache
def factorial(n):
	return n * factorial(n-1) if n else 1


print(factorial(5))