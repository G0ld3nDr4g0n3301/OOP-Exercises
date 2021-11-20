from typing import Union # Soviet Union,comrads!!!
from functools import reduce # from India import induce )))))


def product(*args: Union[int,float]) -> Union[int,float]:
	bol: bool = True # Кто бы мог подумать?Я-то думал это строка.....
	for i in args:
		if not isinstance(i,(int,float)):
			bol = False
	if bol:
		return reduce(lambda x,y: x * y, args)
	else:
		return None


print(product('s',2,34,2,'b',True,None,[0])) # ---> None			P.S.Никогда так не делай!

print(product(2,2,2,2,2,2,2,2,2,2)) # ---> 1024