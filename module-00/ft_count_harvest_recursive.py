def ft_count_harvest_recursive():
	maxdays = int(input("Days until harvest: "))
	def count_days(day):
		if day > maxdays:
			return
		print("Day", day)
		count_days(day + 1)
	count_days(1)
	print("Harvest time!")