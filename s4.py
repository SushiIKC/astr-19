#Write a Python program that declares a class describing 
#your favorite animal. Have the data members of the class 
#represent the following physical parameters of the animal: 
#length of the arms (float), length of the legs (float), 
#number of eyes (int), does it have a tail? (bool), is it furry? (bool). 
#Write an initialization function that sets the values of the data members 
#when an instance of the class is created. 
#Write a member function of the class to print out and describe the 
#data members representing the physical characteristics of the animal
import sys 

class FavoriteAnimal: 
	def print(self):
		print("Here is my favorite animal!")
		print(f"Length of the arms = {self.length_arms}")
		print(f"Length of the legs = {self.length_legs}")
		print(f"Number of eyes = {self.num_eyes}")
		print(f"Is it furry? = {self.furry}")
		print(f"Does it have a tail? = {self.tail}")

		if self.furry==True:
			print("I am furry!")
		else:
			print("I am not furry!")
		if self.tail==True:                   
			print("I have a tail!")
		else:
			print("I do not have a tail!")
		print("I am a polar bear :)")

	def __init__(self,arms=4.2, legs=4.7, neyes=2, furry=True, tail=True):   #Length in feet   
		self.length_arms = arms
		self.length_legs = legs 
		self.num_eyes    = neyes 
		self.furry       = furry
		self.tail        = tail

def main():
	arms = 4.2
	legs = 4.7 
	neyes = 2 
	furry = True
	tail = True

	if(len(sys.argv)>=2):
		arms = float(sys.argv[1])
	if(len(sys.argv)>=3):
		legs = float(sys.argv[2])
	if(len(sys.argv)>=4):
		neyes = float(sys.argv[3])	

	my_animal = FavoriteAnimal(arms=arms, legs=legs, neyes=neyes)

	my_animal.print()


if __name__ == '__main__':
	main()