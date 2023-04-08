from random import randint
from os import remove, rename

separator = ','
operand_list = []
for num in range(5):
    operand_list[num] = randint(1, 9)

operator_list = []
operator_dictionary = {
    '1': '+',
    '2': '-',
    '3': '',
    '4': '*'
}
for num in range(4):
    random_operator = operator_dictionary[randint(1, 4)]
    if (operator_list and operand_list[num - 1] == '**') and random_operator == '**':
        continue
    else:
        operator_list[num] = random_operator



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
