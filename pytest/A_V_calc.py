'''
 TPRG 2131 Fall 2024 Assignment 1
 Chamath Kulathilaka (100889193)
 COMP4131
 October 10, 2024
 This program is strictly my own work. Any material
 beyong course learning materials that is taken from
 the Web or other sources is properly cited, giving
 credit to original author (s).
 This program operates as follows,
 

*********
A/V calculator

(Level 0)
Enter Q/q to quit – select either will gracefully close the application and cancel the calculated view option.
Enter V/v to change the calculated view(just the answer) or D/d for default view (equation).

	(Level 1)
    1.	First Area/Volume* calulation
    2.	Second Area/Volume* calculation
    3.	Third Area/Volume* calculation
    4.	Fourth Area/Volume* calculation
    5.	Fifth Area/Volume* calculation

*********

The above menu style (inside the asterix's) is expected, only 2 key entries to use the calculator.

The menu Level 1 , options 1...5 should be modified from the above to reflect the
function you selected.

After selection at level 1, the calculator expects data to entered (use appropiate data types).

(The Level 0 & 1 labels are for indication purpose and are not
to be included)

'''
import math
  
def decision(equation, result, choice):  #main definition to change views to answer only or equation with answer.
    if choice == "V" or choice == "v":
        return f"Answer: {result}" # just the result
    elif choice == "D" or choice == "d":
        return f"Equation: {equation}\nAnswer: {result}" #equation and result both

def cylinder_cal(height, radius): #calculation for cylinder Volume
    Volume1 = math.pi * radius**2 * height
    Volume = round(Volume1, 2)
    return Volume

def circle_cal(radius): # calculation for circle area
    Area1 = math.pi * radius ** 2
    Area = round(Area1, 2) 
    return Area

def sphere_cal(radius): # calculation for sphere volume
    Volume1 = (4/3) * math.pi * radius ** 3
    Volume = round(Volume1, 2)
    return Volume

def cuboid_cal(length, width, height): # calculation for cuboid area
    Area1 = 2 * length * width + 2 * length * height + 2 * height * width
    Area = round(Area1, 2)
    return (Area)

def prism_cal(base, base_height, height): # calculation for prism volume
    Volume1 = ((1/2) * base * base_height) * height
    Volume = round(Volume1, 2)
    return Volume

if __name__ == "__main__":
    view = 'D' # default view is D

    while True:
        q = input("\nEnter Q/q to quit, \nV/v for answer-only view, \nD/d for answer with equation.\n[Q/V/D]? ").lower() # given choices to quit or change the view
        
        if q == "q": 
            exit("Thank you for using A_V Calculator") # exiting program
        
        elif q == "v":
            view = 'V'
        
        elif q == "d":
            view = 'D'
        
        else:
            print("Invalid choice, please try again.")
            continue  # when a wrong answer is give it goes back to the loop without continuing further.
        
        while True: # start of the second loop
             # 5 choices to calculate       
            print("\n1) Volume of a Cylinder") 
            print("\n2) Area of a Circle")
            print("\n3) Volume of a Sphere")
            print("\n4) Area of a Cuboid")
            print("\n5) Volume of a Prism")
            print("\n6) Previous menu")
            
            choice = input("\nSelect a calculation (1-6): ") #prompting to get a selection out of above
            
            if choice == '1':
                r = float(input("Enter the Radius: ")) #input radius
                h = float(input("Enter the height: ")) #inout height
                answer = cylinder_cal(h, r) 
                equation = f"\u03c0 * {r}^2 * {h}" #equation that is gonna be printed for the given calculation
                output = decision(equation, answer, view)
                print(output+"\u33A5") 
                
            elif choice == '2':
                r = float(input("Enter the Radius: ")) #input radius
                result = circle_cal(r)
                equation = f"\u03c0 * {r}^2" #equation that is gonna be printed for the given calculation
                output = decision(equation, result, view)
                print(output+"\u33A1")
                
            elif choice == '3':
                r = float(input("Enter the Radius: ")) #input radius
                result = sphere_cal(r)
                equation = f"(4/3) * \u03c0 * {r}^3" #equation that is gonna be printed for the given calculation
                output = decision(equation, result, view)
                print(output+"\u33A5")

            elif choice == '4':
                l = float(input("Enter the Length: ")) #input length
                w = float(input("Enter the Width: ")) #input width
                h = float(input("Enter the Height: ")) #input height
                result = cuboid_cal(l, w, h)
                equation = f"2 * {l} * {w} + 2 * {l} * {h} + 2 * {h} * {w}" #equation that is gonna be printed for the given calculation
                output = decision(equation, result, view)
                print(output+"\u33A1")

            elif choice == '5':
                b = float(input("Enter the Base Length: ")) #input length
                h = float(input("Enter the Base Height: ")) #input Base Height
                H = float(input("Enter the Height: ")) #input height
                result = prism_cal(b, h, H) 
                equation = f"((1/2 * {b} * {h}) * {H}" #equation that is gonna be printed for the given calculation
                output = decision(equation, result, view)
                print(output+"\u33A5")
                
            elif choice == '6':
                print("Back to main menu.")
                break # stops the second loop to go back to change views

            else:
                print("Invalid selection, please try again.") #any pther input error message comes up
                
            


