#A function named hello() that prints a greeting to the user.

def hello():
    print("Hello, friend!")

#A function named pack() that accepts three arguments, and returns a single list

def pack(a,b,c):
    return [a,b,c]

#A function called eat_lunch() that accepts a list of any length, and print out a series of strings

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

hello()
print(pack("hey","hi","hello"))
eat_lunch([])
eat_lunch(["salad","pizza","pasta","canoli"])