class Planet:
	def __init__(self, name, planet_type, star):
		for attr in (name, planet_type, star):
			if not isinstance(attr, str):
				name = -1
				break
			elif attr == '':
				name = -2
				break
		if name == -1:
			raise TypeError('name, planet type, and star must be strings')
		elif name == -2:
			raise ValueError('name, planet_type, and star must be non-empty strings')

		self.name = name
		self.planet_type = planet_type
		self.star = star

	def orbit(self):
		return f'{self.name} is orbiting around {self.star}...'

	def __str__(self):
		return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'


planet_1 = Planet('Mercury', 'Terrestrial', 'Sun')
planet_2 = Planet('Venus', 'Terrestrial', 'Sun')
planet_3 = Planet('Earth', 'Terrestrial', 'Sun')

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())