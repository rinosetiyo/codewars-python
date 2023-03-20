class InteractiveCoding():
  class Day1():
    # Working with variables to manage data
    def print_function():
      print("Day 1 - Python Print Function")
      print("The function is declared like this:")
      print("print('what to print')")
    
    def string_manipulation():
      print("Day 1 - String Manipulation")
      print('String Concatenation is done with the "+" sign.')
      print('e.g. print("Hello " + "world")')
      print("New lines can be created with a backslash and n.")
    
    def length_function():
      print(len(input("What is your name? ")))
    def switch_values(a, b):
    # logic to switch
      c = a
      a = b
      b = c
      print("a: " + a)
      print("b: " + b)

  class Day2():
    # Understanding Data types and how to manipulate strings
    def data_types(digit_number):
      # logic using slicing
      a = digit_number[0]
      b = digit_number[1]
      sum_digit = int(a) + int(b)
      print(sum_digit)

    def bmi_calculator(height, weight):
      # math operator
      bmi = int(weight) / (float(height) * float(height))
      print(round(bmi))
      
    def life_in_weeks(age):
      years_remaining = 90 - int(age)
      days = years_remaining * 365
      months = years_remaining * 12
      weeks = years_remaining * 52
      print(f"You have {days} days. {weeks} weeks, and {months} months left.")

  class Day3():
    # control flow and logical operators
    def odd_or_even(number):
      if number % 2 == 0:
        print("This is an even number.")
      else:
        print("This is an odd number.")

    def bmi_2(height, weight):
      # math operator
      bmi = round(int(weight) / (float(height) * float(height)))

      if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are underweight")
      elif bmi > 18.5 and bmi <= 25:
        print(f"Your BMI is {bmi}, you have a normal weight")
      elif bmi > 25 and bmi <= 30:
        print(f"Your BMI is {bmi}, you are slightly overweight")
      elif bmi > 30 and bmi <= 35:
        print(f"Your BMI is {bmi}, you are obese")
      else:
        print(f"Your BMI is {bmi}, you are clinically obese")

    def leap_year(years):
      if years % 4 == 0:
        print("Leap year.")
      elif years % 100 == 0:
        print("Not leap year.")
      elif years % 400 == 0:
        print("Leap year.")
      else:
        print("Not leap year.")

    def pizza_order():
      print("Welcome to Python Pizza Deliveries! ")
      size = input("What size pizza do you want? S, M, or L ").lower()
      add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
      extra_cheese = input("Do you want extra cheese? Y or N ").lower()

      if size == 's':
        harga = 15
        if add_pepperoni == 'y':
          total = harga + 2
          if extra_cheese == 'y':
            extra = total + 1
            print(f"Your final bill is ${extra}")
          else:
            print(f"Your final bill is ${total}")
        elif add_pepperoni == 'n' and extra_cheese == 'y':
          extra = harga + 1
          print(f"Your final bill is ${extra}")
        else:
          print(f"Your final bill is ${harga}")

      elif size == 'm':
        harga = 20
        if add_pepperoni == 'y':
          total = harga + 3
          if extra_cheese == 'y':
            extra = total + 1
            print(f"Your final bill is ${extra}")
          else:
            print(f"Your final bill is ${total}")
        elif add_pepperoni == 'n' and extra_cheese == 'y':
          extra = harga + 1
          print(f"Your final bill is ${extra}")

      elif size == 'l':
        harga = 25
        if add_pepperoni == 'y':
          total = harga + 3
          if extra_cheese == 'y':
            extra = total + 1
            print(f"Your final bill is ${extra}")
          else:
            print(f"Your final bill is ${total}")
        elif add_pepperoni == 'n' and extra_cheese == 'y':
          extra = harga + 1
          print(f"Your final bill is ${extra}")
        else:
          print(f"Your final bill is ${harga}")
      else:
        print("Your input is invalid")
      
    def love_calculator():
      name1 = input("input your name : ")
      name2 = input("input her / his name : ")

      combined = name1 + name2
      T = combined.lower().count("t")
      R = combined.lower().count("r")
      U = combined.lower().count("u")
      E = combined.lower().count("e")
      TRUE = T + R + U + E

      L = combined.lower().count("l")
      O = combined.lower().count("o")
      V = combined.lower().count("v")
      E = combined.lower().count("e")
      LOVE = L + O + V + E
      lovescore = str(TRUE) + str(LOVE)

      if int(lovescore) <= 10 or int(lovescore) >= 90:
        print(f"Your score is {lovescore}, you go together like coke and mentos.")
      elif int(lovescore) >= 40 and int(lovescore) <= 50:
        print(f"Your score is {lovescore}, you are alright together.")
      else:
        print(f"Your score is {lovescore}.")
        
  class Day4():
    # Ramdomisation and python lists
    def heads_or_tails():
      import random as r
      int_random = r.randint(0,1)
      if int_random == 1:
        print("Heads")
      else:
        print("Tails")
      
    def banker_roulete():
      import random
      # Split string method
      names_string = input("Give me everybody's names, separated by a comma. ")
      names = names_string.split(", ")
      # 🚨 Don't change the code above 👆
      box = len(names)
      random_number = random.randint(0, box - 1)
      random_name = names[random_number]
      print(f"{random_name} is going to pay the bill !")
      
InteractiveCoding.Day4.banker_roulete()
class Projects():
# Project of 100 Day code python
  def band_name_generator():
    city = input("What's name of the city you grew up in? \n")
    pet = input("What's your pet's name? \n")
    print(city + ' ' + pet)

  def tip_calculator():
    total_bill = float(input("What was the total bill? "))
    percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    split_bill = int(input("How many people to split bill? "))
    bill_after_percentage = total_bill * (percentage_tip / 100)

    pay = (total_bill + bill_after_percentage ) / split_bill
    print(round(pay, 2))

  def treasure_island():
    answer = input("Your are in front of gate, choose left(l) or right(r)? ").lower()

    if answer == "l":
      answer2 = input("In front of you there is river, choose swim(s) or wait(w) a boat? ").lower()
      if answer2 == "w":
        answer3 = input("In front of you there is 3 gate, blue(b), yellow(y), and red(r), you can choose one of them? ").lower()
        if answer3 == "y":
          print("You win")
        elif answer3 == "b":
          print("Eaten by beasts. Game over.")
        elif answer3 == "r":
          print("Burned by fire. Game over.")
        else:
          print("your input is invalid.")
      elif answer2 == "s":
        print("Attacked by trout. Game over.")
      else:
        print("your input is invalid.")
    elif answer == "r":
      print("Fall into a hole. Game over.")
    else:
      print("your input is invalid.")

