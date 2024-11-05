def func2():
	param = 4

	def inner(var):
		var += 1

	inner(param)
	return param

#возвращает 4