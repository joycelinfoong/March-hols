name = input("What is your name? ")

# If length of name is greater than 20,
# print something

if len(name) > 20:
    print("Length greater than 20")

age = input("What is your age? ")

# If age is less than 10, print "Smol"
# ELse if age is between 10 and 20, print "Big boi"
# Else, print "Big big boi"

if age < "10":
    print("Smol")
elif "10" < age < "20":
    print("Big boi")
else:
    print("Big big boi")

coolness = input("Rate your coolness out of 100.0 = ")

# If coolness is more than 100.0, just print some error

if float(coolness) > 100.0:
    print("ERROR")

# Now print a string like
# My name is Arnold Tan, I am 69 and I'm Really Cool

print ("My name is "+name,", I am " + age, "and I'm Really Cool")