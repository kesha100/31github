"""
try:
    some code 1
except:
    some code 2
else:
    some code 3 (works when no exception)
finally:
    some code 4 (always works)
"""

try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 / num2
except ZeroDivisionError:                                      # bare exception
    print('You cannot divide to 0')
except ValueError:
    print('You entered not int')
else:
    print(result)
finally:
    print('Girl it is so great to live this life!')

dict_ = dict.fromkeys(('makers', 'bootcamp'), 0)
dict_ = {key: len(key) for key,val in dict_.items()}
dict_.update({'except': 'Exception'})
print(dict_)

while True:
    try:
        key = input('Enter word: ')
        if key == 'exit':
            break
        dict_[key] += 2
    except (KeyError, TypeError):
        print('This key doesn\'t exist or This key isn\'t integer')
    else:
        print(dict_[key])
    finally:
        print(dict_)

"""
Task with catching exception

you enter the file name, this function counts and shows the lines in this file
"""


def count_lines_in_files(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f'The number of lines if {file_path}: {lines}')
    except FileNotFoundError:
        print('Couldn\'t find this file')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')


file_path = input('Enter the file path: ')
count_lines_in_files(file_path)

def safe_division():
    try:
        numerator = float(input('Enter the numerator: '))
        denominator = float(input('Enter the denominator: '))
        result = numerator / denominator
        print(f'The result of dividing: {result}')
    except ValueError:
        print('Enter numeric type of data.')
    except ZeroDivisionError:
        print('Denominator cannot be zero.')
    except Exception as e:
        print(f'Some error has occurred: {e}')
    finally:
        print('The program finished.')

safe_division()