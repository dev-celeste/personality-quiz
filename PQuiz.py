#this is the beginning prompt of the program that tells users its function with a call to action
print("What classic literature novel are you? Take this quiz to find out!")
#this variable stores the score of the user as the program runs. everyone starts at zero
res_num = 0
#this is the function that will be able to detect if an invalid response was input 
def bad_num(i):
    return i > 5 or i < 1

#this is the beginning of the series of questions. 
# First it will print the question, 
# then it will prompt the user to enter a response, 
# then it will analyze the response and if it's invalid, it will prompt them to enter another response
# if it is valid, it will add their response to their score stored in res_num 
# then it will move on to the next question and repeat the process all over again
print("Which color do you like best? red = 1, purple = 2, blue = 3, green = 4, yellow = 5")
res = int(input("enter response>"))
while bad_num(res):
    res = int(input("enter response>"))
else:
    res_num += res

print("Where would you rather spend your time? Type 1 for beach, 2 for library, 3 for forrest, 4 for party, 5 for bed: ")
res = int(input("enter response>"))
while bad_num(res):
    res = int(input("enter response>"))
else:
    res_num += res

print("What is your ideal vacation destination? Type 1 for Paris, 2 for Cancun, 3 for Toronto, 4 for Bali, 5 for Japan: ")
res = int(input("enter response>"))
while bad_num(res):
    res = int(input("enter response>"))
else:
    res_num += res

print("What was your favorite subject in school? Type 1 for Math, 2 for English, 3 for Science, 4 for History, 5 for Gym: ")
res = int(input("enter response>"))
while bad_num(res):
    res = int(input("enter response>"))
else:
    res_num += res

print("You have 1 minute to get dressed, which shoes do you reach for? Type 1 for boots, 2 for sneakers, 3 for heels, 4 for slides, 5 for barefoot: ")
res = int(input("enter response>"))
while bad_num(res):
    res = int(input("enter response>"))
else:
    res_num += res

#First i'll create a list that stores the strings associated with each personality type to be called withbthe final function Answer.
personalityString = ['', 'Pride and Prejudice', 'Wuthering Heights', 'Frankenstein', 'Les Liasons Dangereux', 'War and Peace']
#My function's intended use is to display the user's personality type determined after calculating their inputs.
#It takes in an integer and returns the string result depending on said integer.
def Answer(personalityType):
#There will be multiple if-statements that can run depending on the results from user input. 
#Each printed string will be different and provide an answer to the user.
    if personalityType < 10:
        #the input of personalityType will depend on the number calculated. It will first print the string followed by whichever words are designated to print per integer.
        print("Your personality type is: " + personalityString[1])
    elif 10 <= personalityType < 15:
        #for example, any integer under 10 may print "red" while an integer between 15 and 20 can print "blue" when personalityType is called.
        print("Your personality type is: " + personalityString[2])
    elif 15 <= personalityType < 20:
        print("Your personality type is: " + personalityString[3])
    elif 20 <= personalityType < 25:
        print("Your personality type is: " + personalityString[4])
    else:
        print("Your personality type is: " + personalityString[5])

#finally, we run the answer function to print the user's personality to the function
Answer(res_num)





























"""questionText = ["Which color do you like best? red = 1, purple = 2, blue = 3, green = 4, yellow = 5", 
"Where would you rather spend your time? Type 1 for beach, 2 for library, 3 for forrest, 4 for party, 5 for bed: ",
"What is your ideal vacation destination? Type 1 for Paris, 2 for Cancun, 3 for Toronto, 4 for Bali, 5 for Japan: ",
"What was your favorite subject in school? Type 1 for Math, 2 for English, 3 for Science, 4 for History, 5 for Gym: ",
"You have 1 minute to get dressed, which shoes do you reach for? Type 1 for boots, 2 for sneakers, 3 for heels, 4 for slides, 5 for barefoot: "]

def askQuestion(questions):
    for x in questions:
        print(x)"""

'''  
else:
   res_num += res

else:
    print("Which color do you like best? red = 1, purple = 2, blue = 3, green = 4, yellow = 5")
    res = int(input("enter response>"))
    if(int(res) > 5) or (int(res) < 1):
            raise "Oops! That wasn't a valid number, try again!"
res_num += res

try:
    print("Where would you rather spend your time? Type 1 for beach, 2 for library, 3 for forrest, 4 for party, 5 for bed: ")
    res = int(input("enter response>"))
    if(int(res) > 5) or (int(res) < 1):
        raise "Oops! That wasn't a valid number, try again!"
    #num2 = int(q2)
    #insert code that adds input number to score 
    res_num += res
except:
    print("Where would you rather spend your time? Type 1 for beach, 2 for library, 3 for forrest, 4 for party, 5 for bed: ")
    res = int(input("enter response>"))
    if(int(res) > 5) or (int(res) < 1):
        raise "Oops! That wasn't a valid number, try again!"
    res_num += res

try:
    print("What is your ideal vacation destination? Type 1 for Paris, 2 for Cancun, 3 for Toronto, 4 for Bali, 5 for Japan: ")
    res = int(input("enter response>"))
    if(int(res) > 5) or (int(res) < 1):
        raise "Oops! That wasn't a valid number, try again!"
    #num3 = int(q3)
    #insert code that adds input number to score 
    res_num += res

except:
    print("What is your ideal vacation destination? Type 1 for Paris, 2 for Cancun, 3 for Toronto, 4 for Bali, 5 for Japan: ")
    res = int(input("enter response>"))
    if(int(res) > 5) or (int(res) < 1):
        raise "Oops! That wasn't a valid number, try again!"
    res_num += res

try:
    print("What was your favorite subject in school? Type 1 for Math, 2 for English, 3 for Science, 4 for History, 5 for Gym: ")
    res = int(input("enter response>"))
    if(int(res) > 5) or (int(res) < 1):
        raise "Oops! That wasn't a valid number, try again!"
    #num4 = int(q4)
    #insert code that adds input number to score 
    res_num += res
except:
    print("What was your favorite subject in school? Type 1 for Math, 2 for English, 3 for Science, 4 for History, 5 for Gym: ")
    res = int(input("enter response>"))
    if(int(res) > 5) or (int(res) < 1):
        raise "Oops! That wasn't a valid number, try again!"
    res_num += res

try:
    print("You have 1 minute to get dressed, which shoes do you reach for? Type 1 for boots, 2 for sneakers, 3 for heels, 4 for slides, 5 for barefoot: ")
    res = int(input("enter response>"))
    if(int(res) > 5) or (int(res) < 1):
        raise "Oops! That wasn't a valid number, try again!"
    #num5 = int(q5)
    #insert code that adds input number to score 
    #insert code that makes total score equal to personalityType
    #insert code that causes Answer() function to run after question 5 is answered
    res_num += res
except:
    print("You have 1 minute to get dressed, which shoes do you reach for? Type 1 for boots, 2 for sneakers, 3 for heels, 4 for slides, 5 for barefoot: ")
    res = int(input("enter response>"))
    if(int(res) > 5) or (int(res) < 1):
        raise "Oops! That wasn't a valid number, try again!"
    res_num += res'''


"""next steps: 
1)decide what the personality types will be----
2)create a scanner variable----
3)make 5 prompts to ask user questions and gather their input----
4)write code that will add a certain number to their score depending on their answer 
5)calculate their total score depending on their input
6)call the answer function to print their personality to the terminal"""

"""Which color do you like best? red = 1, purple = 2, blue = 3, green = 4, yellow = 5
Where would you rather spend your time? beach = 1, library = 2, forrest = 3, party = 4, in bed = 5
What is your ideal vacation destination? Paris = 1, Cancun = 2, Toronto = 3, Bali = 4, Japan = 5 
What was your favorite subject in school? Math = 1, English = 2, Science = 3, History = 4, Gym = 5
You have 1 minute to get dressed, which shoes do you reach for? Boots = 1, sneakers = 2, heels = 3, slides = 4, barefoot = 5

I don't need each input to have a response but I need each input to trigger the next prompt and the last prompt input will trigger 
the Answer() function to activate which will print the answer to the terminal"""


"""personalityType = final answer (you have to make sure pt will absolutely always correlate to an index inside the list p strings)
    personalityStrings = ['', 'red', 'pruple', etc.]
    personalityStrings[personalityType]"""

"""1 + 1 + 1 + 1 + 1 = 5 = red
    2 + 2 + 2 + 2 + 2 = 10 = purple
    3 + 3 + 3 + 3 + 3 = 15 = blue
    4 + 4 + 4 + 4 + 4 = 20 = green
    5 + 5 + 5 + 5 + 5 = 25 = yellow"""

"""if personalityType < 10 = red
    if personalityType < 15 = purple
    if personalityType < 20 = blue
    if personalityType < 25 = green
    if personalityType == 25 = yellow"""
