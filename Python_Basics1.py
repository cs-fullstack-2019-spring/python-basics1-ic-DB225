def main():
    problem1()
    problem2()
    problem3()
    problem4()

#Create a function that asks for a student's name.
# Then ask for another student's name.
# Print [first student] and [second student] went to class.
def problem1():
    student1 = input("User1, enter your name: ")
    student2 = input("User2, enter your name: ")

    print(student1 + " and "+student2+ " went to class")


#############################################################
#Create a function to ask the user for a grade.
# Then ask the user how much extra credit they earned.
# Print the grade plus extra credit.
def problem2():
    userGrade = int(input("Put your grade: "))
    credit = int(input("How much extra credit you earned?"))
    print(str(userGrade + credit))
#############################################################
#Create a function to ask the user for three numbers.
# Print the sum as it would be written in
def problem3():
    myNumber1 = int(input("Put the first number: "))
    myNumber2 = int(input("Put the first number: "))
    myNumber3 = int(input("Put the first number: "))
    total = str(myNumber1 + myNumber2 + myNumber3)
    print(str(myNumber1)+ "+ "+str(myNumber2)+"+ "+str(myNumber3)+ " ="+ total)
#############################################################
#Create a function to ask the user for a number.
# If the number is negative print "Negative!".
# If the number is positive, print "Positive!.
# Otherwise print the only other number it can be.
def problem4():
    myNumber = int(input("Put a number: "))

    if (myNumber<0):
        print("Negative")
    elif(myNumber>0):
         print("Positive")
    else:
        print("ZERO")
########################################################################################
if __name__ == '__main__':
    main()