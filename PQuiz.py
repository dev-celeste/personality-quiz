#First i'll create a list that stores the strings associated with each personality type to be called withbthe final function Answer.
personalityString = ['', 'red', 'purple', 'blue', 'green', 'yellow']
#My function's intended use is to display the user's personality type determined after calculating their inputs.
#It takes in an integer and returns the string result depending on said integer.
def Answer(personalityType):
#There will be multiple if-statements that can run depending on the results from user input. 
#Each printed string will be different and provide an answer to the user.
    if personalityType < 10:
        #the input of personalityType will depend on the number calculated. It will first print the string followed by whichever words are designated to print per integer.
        print("Your personality type is: " + personalityString[1])
    if 10 < personalityType < 15:
        #for example, any integer under 10 may print "red" while an integer between 15 and 20 can print "blue" when personalityType is called.
        print("Your personality type is: " + personalityString[2])
    if 15 < personalityType < 20:
        print("Your personality type is: " + personalityString[3])
    if 20 < personalityType < 25:
        print("Your personality type is: " + personalityString[4])
    if personalityType == 25:
        print("Your personality type is: " + personalityString[5])

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
