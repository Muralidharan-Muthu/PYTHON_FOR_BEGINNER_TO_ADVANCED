# Match case in python

# 1. Why Match case used in python?
""" Before Python 3.10, we used if-elif-else for everything."""

choice = "Pizza"

if choice == "Pizza":
    print("You Ordered Pizza")
elif choice == "Burger": 
    print("You Ordered Burger")
elif choice == "Pasta":
    print("You Ordered Pasta")
else:
    print("Invalid Choice")

# 2. Syntax for Match case

"""match variable:
    case value1:
        # code block
    case value2:
        # code block 2
    case value3:
        # code block 3
        #.... """

# 3. Default case ( _ ) in match case

color = "Green"

match color:
    case "Red":
        print("Stop")
    case "Green":
        print("Go")
    case "Yellow":
        print("Wait")
    case _: #default case (else)
        print("Unknown traffic signal color")


# 4. Nested match-case in python

user = ("Admin", "Active")

match user:
    case ("Admin", "Active"):
        print("Welcome Active Admin")
    case ("Admin", "Inactive"):
        print("Admin account is inactive")
    case ("Guest", _):
        print("Welcome Guest")
    case _:
        print("Unknown user")


# 5. Lets see an example for match in python (week days)

day = 6

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:
        print("weekend")
    case _:
        print("Invalid day")

# Next Video - Array in Python

Thank you guys .....
