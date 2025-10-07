#Name: John Paul Taguinod
#School: FEU-TECH
#Machine Problem -1



class Rectangle:
    def __init__(self):
        self.length = None
        self.width = None

    def get_input(self):
        length_input = input("Enter Length value:")
        width_input = input("Enter the width of the rectangle:")

        if length_input.isdigit() and int(length_input) > 0:
            if width_input.isdigit() and int(width_input) > 0:
                self.length = int(length_input)
                self.width = int(width_input)
            else:
                print("The number is not a positives integer:")
                return False
        else:
            print("Input the correct data format is not a Positive integer.")
            return False

        return True

    def calculate_area(self):
        return self.length * self.width

    def display_area(self):
        area = self.calculate_area()
        print(f"The Area of the Rectangle is:{area}")


# Main program using the Rectangle class
rectangle = Rectangle()

if rectangle.get_input():
    rectangle.display_area()









# Name: John PauL S. Taguinod
# School: FEU-TECH
# Machine Problem number - 2

#class Circle:
 #   def __init__(self):
  #      self.radius = None

   # def get_input(self):
    #    radius_input = input("Enter radius:")
     #   if radius_input.isdigit() and int(radius_input) > 0:
      #      self.radius = int(radius_input)
       #     return True
        #else:
            # Check if it's a negative or decimal value
         #   try:
          #      radius = float(radius_input)
           #     if radius < 0:
            #        print("You use enter positive number")
             #   else:
              #      print("You use input whole number value:")
            #except ValueError:
             #   print("Invalid input.")
            #return False

    # def calculate_area(self):
      #  return 3.14 * self.radius ** 2

    # def calculate_perimeter(self):
      #  return 2 * 3.14 * self.radius

   # def display_results(self):
    #    area = self.calculate_area()
     #   perimeter = self.calculate_perimeter()
      #  print(f"The answer is {area}")
       # print(f"Here is the Answer: {perimeter}")


# Main Program
#circle = Circle()

#if circle.get_input():
 #   circle.display_results()
    
    
    
    
    
    
    
    
    
    
    
# John Paul S. Taguinod
# FEU-TECH



class RomanConverter:
    def __init__(self):
   
        self.roman_numerals = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]

    def int_to_roman(self, number):
        result = ''
        for numeral, value in self.roman_numerals:
            while number >= value:
                result += numeral
                number -= value
        return result

    def roman_to_int(self, roman):
        roman = roman.upper()
        index = 0
        result = 0
        for numeral, value in self.roman_numerals:
            while roman[index:index+len(numeral)] == numeral:
                result += value
                index += len(numeral)
                if index >= len(roman):
                    break
        return result

# Main Program
def main():
    converter = RomanConverter()

    while True:
        print("\nMENU")
        print("1. convert an integer to a roman numeral")
        print("2. convert a roman numeral to an integer")
        print("3. exit")

        choice = input("Enter your choice:")

        if choice == '1':
            num = int(input("\nEnter Integer - "))
            roman = converter.int_to_roman(num)
            print(f"Output in Roman numerals is: {roman}")

        elif choice == '2':
            roman_input = input("\nEnter Roman Numeral - ")
            integer = converter.roman_to_int(roman_input)
            print(f"Output in Integer is: {integer}")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
