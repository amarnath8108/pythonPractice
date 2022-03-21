# initialize the lists
Correct_Answers_list = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D',
                        'A']
Exam_Answers_list = []
Incorrect_Answers_list = []

# read file values to temp
# temp = open('C:/Users/AmarnathMaddala/Desktop/numbers.txt').read()

# Read values from file to list
temp = open('C:/Users/AmarnathMaddala/Desktop/Driver.txt').read().splitlines()
for i in temp:
    Exam_Answers_list.append(i)

Total_correct_answers = 0
# Compare two lists to get correct answers count
for i in range(20):
    if Correct_Answers_list[i] == Exam_Answers_list[i]:
        Total_correct_answers = Total_correct_answers + 1
    else:
        Incorrect_Answers_list.append(i+1)

# display the exam results based on total correct answers
# If correct answers are greater than or equal to 15 it is pass else fail
if Total_correct_answers >= 15:
    print("Congratulations!!! you passed the License exam")
else:
    print("You Failed License exam, Better luck next time!!")


# display total correct answers
print("Total correct answers count : {0}".format(Total_correct_answers))

# display total in correct answers
print("Total incorrect answers : {0}".format(20 - Total_correct_answers))

# display incorrectly answered question numbers
print("The list shows the wrong answered questions {0}".format(Incorrect_Answers_list))


