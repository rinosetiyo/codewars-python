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

  class Day5():
    # python loops
    def average_height():
      student_heights = [180, 124, 165, 173, 189, 169, 146]
      student = 0
      number = 0
      for student_byone in student_heights:
        student += student_byone
        number += 1
      average = student / number
      print(round(average))

    def high_score():
      student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
      high_score = 0
      for student in student_scores:
        if student > high_score:
          high_score = student
      print(high_score)
        
    def even_number():
      for even in range(2, 101, 2):
        even
        print(even)

    def fizzbuzz():
      for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
          print("FizzBuzz")
        elif number % 5 == 0:
          print("Buzz")
        elif number % 3 == 0:
          print("Fizz")
        else:
          print(number)

class kumite():
  def odd_number():
    for x in range(1,21):
      if x % 2 != 0:
        print("odd number")
      else:
        print(x)
kumite.odd_number()    
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

  def rock_scissors_paper():
    import random as r

    welcome = "Welcome to rock scissors and paper, for play this game you have choose one \n rock(0), scissors(2), and paper(1) \n"
    print(welcome)
    
    your_turn = int(input("you have to choose one ! "))
    computer = r.randint(0,2)

    if your_turn == 0 and computer == 1:
      print("You choose rock, computer choose paper, computer win")
    elif your_turn == 0 and computer == 2:
      print("You choose rock, computer choose scissors, you win")
    elif your_turn == 1 and computer == 0:
      print("You choose paper, computer choose rock, you win")
    elif your_turn == 1 and computer == 2:
      print("You choose paper, computer choose scissors, computer win")
    elif your_turn == 2 and computer == 0:
      print("You choose scissors, computer choose rock, computer win")
    elif your_turn == 2 and computer == 1:
      print("You choose scissors, computer choose paper, you win")
    elif your_turn == computer:
      print("Draw")
      if your_turn == 1:
        print("You choose paper and computer choose paper")
      elif your_turn == 2:
        print("You choose scissors and computer choose scissors")
      elif your_turn == 0:
        print("You choose rock and computer choose rock")
    else:
      print("Your input is invalid")

  def pass_generator():
    import random
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['!','@','#','$','%','^','&','*']
    many_letter = int(input("How many letters did you want to generate: "))
    many_number = int(input("How many numbers did you want to generate: "))
    many_symbol = int(input("How many symbols did you want to generate: "))
    generate = []
    for ran_letter in range(0, many_letter):
      chosen_letter = random.choice(letters)
      generate.append(chosen_letter)
 
    for ran_number in range(0, many_number):
      chosen_number = random.choice(numbers)
      generate.append(chosen_number)
   
    for ran_symbol in range(0, many_symbol):
      chosen_symbol = random.choice(symbols)
      generate.append(chosen_symbol)
    random.shuffle(generate)
    print(generate)
  def hangman():
    import random as r
    word_list = ["ardvark","baboon","camel"]
    random_word = r.choice(word_list)
    for slice_word in random_word:
      print(slice_word)