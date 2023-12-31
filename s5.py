import numpy as np
import math

def main():
    x_values = np.linspace(0, 2 * math.pi, 1000)   #generating x values 

    print("x      | sin(x)")   #make a table for looks 
    print("-------|-------")
    for x in x_values:
        sin_x = math.sin(x)
        print(f"{x:.4f} | {sin_x:.4f}")  #use a for loop to continuously print x and sin(x) values

if __name__ == "__main__":
    main()

