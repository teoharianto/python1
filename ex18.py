# Belajar fungsi di python
def print_two(*args) :
    arg1, arg2 = args
    print (f"arg1 : {arg1}, arg2 : {arg2}")

# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2) :
    print (f"arg1 : {arg1}, arg2 : {arg2}")

# fungsi berikut hanya memiliki satu argumen
def print_one(arg1) :
    print (f"arg1: {arg1}")

# fungsi berikut tidak memiliki argumen
def print_none() :
    print ("I got nothin'.")

print_two("hello", "panda")
print_two_again("hello", "panda")
print_one("hello")
print_none()