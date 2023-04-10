import math
from random import randint
from os import remove, rename

separator = ','
question_string = ''
operand_list = []
for num in range(5):
    number = randint(1, 9)
    operand_list.append(number)
# print(operand_list)
operator_list = []
operator_dictionary = {
    '1': '+',
    '2': '-',
    '3': '/',
    '4': '*'
}
for num in range(4):
    random_operator = operator_dictionary[f'{randint(1, 4)}']
    print(f'List: {operator_list}')
    if operator_list and operator_list[-1] == '**' and random_operator == '**':
        print(f'####{operand_list[num - 1]} AND {random_operator}#####')
        print(f'Skipped {num - 1}')
        continue
    else:
        operator_list.append(random_operator)
        print(f'appended {random_operator}')
        print(operator_list)

for operand in operand_list:
    print(f'question_string: {operand}{operator_list[randint(0, 3)]}')
    question_string = question_string + f'{operand}{operator_list[randint(0, 3)]}'
print(f'before: {question_string}')
question_string = question_string.replace("**", "^").removesuffix(question_string[-1])
result = math.floor(eval(question_string))
print(f"res: {result}")
print(f'What will be the result {question_string} 🤣🤣🤣🤣? ')
user_guess = input("Enter your answer: ")
if user_guess is not character:
    if int(user_guess) == result:
        print("Congrats🎉🎉🎉 you pass.")
    else:
        print("Sorry! You didn't pass😥. Please try again!")
else:
    print("Please enter digits only.")



def get_user_point(user_name):
    try:
        file = open('userScores.txt', 'r')
        user_data = []
        for f in file:
            user_data.append(f)
        for user in user_data:
            if user_name == user.split(separator)[0]:
                file.close()
                return user.split(separator)[1]
            else:
                file.close()
                return '-1'
    except IOError as error:
        print(error)
        file = open('userScores.txt', 'w')
        file.close()
        return '-1'


def update_user_score(new_user, user_name, score):
    if new_user:
        file = open('userScores.txt', 'a')
        file.write(f'{user_name}, {score}\n')
    else:
        tmp_file = open('userScores.tmp', 'w')
        file = open('userScores.txt', 'r')
        for f in file:
            splitted_data = f.split(separator)
            if user_name == splitted_data[0]:
                splitted_data[1] = score
                tmp_file.write(separator.join(splitted_data))
            else:
                tmp_file.write(f)
        file.close()
        tmp_file.close()
        remove('userScores.txt')
        rename('userScores.tmp', 'userScores.txt')
