# question 1 hello_Username

def hello_name(user_name):
    print("hello_USERNAME!")
user_name = "hello_USERNAME!"

hello_name(user_name)


#question 2 odds 1- 100

def first_odds():
    for numb in range(0,100):
        if numb % 2 == 1:   
            print(numb)
print(first_odds())

# question 3  return the max number of a given list
a_list = [1,2,3,4]
def max_num_in_list (a_list):
    
    return(max(a_list))

print((max_num_in_list(a_list[:])))


# question 4 is a given year a leap year
# leap year divisible by 4 but not 100 unless 400

a_year = int(input("give me a year: "))
def is_leap_year (a_year):
    """ is the given year a leap year?"""
    a_year = int(a_year)
    if ( a_year % 4 == 0 and a_year % 100 != 0):
        print(True)   
    elif ( a_year % 400 == 0):
        print(True) 
    else:
        print(False)


is_leap_year(a_year)

#question 5 checking if numbers in a given list are consecutive

a_list=[]

def is_consecutive(a_list):
    for i in range (len(a_list)):
        if (a_list[i+1]==a_list[i]+1):
            return True
        else:
            return False
 
print(is_consecutive(a_list))