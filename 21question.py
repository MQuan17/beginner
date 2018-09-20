import random
from classes import Place, Person, Animal
from sys import exit 


NY=Place("New York", "America", "America", "inland", "English", "North America","place")
P=Place("Paris","Europe", "France", "inland", "French", "Western Europe","place")
S=Place("Singapore", "Asia", "Singapore", "coastal", "English or Chinese or Tamil", "South East Asia","place")

DT=Person("Donal Trump", "American", "married", "male", "president", "billionare","person")
ES=Person("Emma Wastion", "English", "single", "female", "actress", "Harry Potter","person" )
TS=Person("Taylor Swift", "American", "single", "female", "singer", "famous" ,"person")

lion=Animal("lion", "mamal", "Africa", "wildlife", "carnivore","animal")
snake=Animal("snake", "reptile", "every continent", "wildlife", "nocturnal","animal")
owl=Animal("owl", "bird", "every continent","pet", "nocturnal","animal")

list= [NY, Place, S, DT, ES,TS, lion, snake, owl]
answer=random.choice(list)

list_of_values=answer.__dict__.values()

def start():
	print "Wellcome to 21question"

	raw_input()

	for i in range(1,22): 
		ask_n_answer(i)
	
	print "you false.Wanna see the relsut??"
	raw_input()
	
	print answer.name





def again():
	ans=raw_input()
	if "e" in ans:
		start()
	else:
		exit(0)


def ask_n_answer(i):
	input=raw_input(str(i))

	list_of_answer=input.split()

	for x in list_of_answer:
		
		if x in list_of_values:
			
			if x== answer.name:
				print "you won!!! So lucky.Wanna play again?"
				again()
			else:
				print True

		else:
			print False



start()












