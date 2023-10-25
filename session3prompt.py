#This code will define and print x**3+8 at a value of x=9 and print
#"YAY!"" if result is larger than 27

import numpy as np 
import sys

def f(x):      #define the function 
	return x**3 + 8

def main():   #main function
	x = 9   #inputs a value for f(x)
	result = f(x)   #defines the result 
	print(f"f({x}) = {result}")   #prints the result

	if result > 27:     #prints "YAY!" if value larger than 27
		print("YAY!")

if __name__ == '__main__':
	main()