class Place(object):
	def __init__(self, name, continent, country, is_coastal, language, distinction, typeof):
		self.name=name
		self.continent=continent
		self.country=country
		self.is_coastal=is_coastal
		self.language=language
		self.distinction=distinction
		self.typeof=typeof



class Person(object):
	def __init__(self, name, nationality, is_married, gender, occupation, distinction, typeof):
		self.name=name
		self.nationality=nationality
		self.gender=gender
		self.occupation=occupation
		self.distinction=distinction
		self.typeof=typeof	

class Animal(object):
	def __init__(self, name,kindofanimal, habitat, is_pet, distinction,typeof):
		self.name=name
		self.kindofanimal=kindofanimal
		self.habitat=habitat
		self.is_pet=is_pet
		self.typeof=typeof



