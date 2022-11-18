import json
import string

def add_cases(user_input: list[str]):
    """
    Add upper and lower cases to the input
    """
    new_input = []

    for element in user_input:
        if not element.isalpha():
            continue

        if element.isupper():
            new_input.append(element.lower())
            new_input.append(element.title())
        elif element.islower():
            new_input.append(element.upper())
            new_input.append(element.title())
        elif element.istitle():
            new_input.append(element.upper())
            new_input.append(element.lower())

    user_input.extend(new_input)
def mix_inputs(user_input: list[str]):
    """
    Mix the input with each other
    """
    new_input = []
    for left_element in user_input:
        for right_element in user_input:
            if left_element == right_element:
                continue
            new_input.append(left_element + right_element)

    user_input.extend(new_input)
def add_numbers(user_input: list[str]):
    """
    Add numbers from config/numbers.json to the input
    """
    numbers = json.loads(open('config/numbers.json', 'r').read())

    new_input = []
    for element in user_input:
        for number in numbers:
            new_input.append(element + number)
            new_input.append(number + element)
    user_input.extend(new_input)
def add_punctuation(user_input: list[str]):
    """
    Add punctuation from string.punctuation to the input
    """
    new_input = []
    for element in user_input:
        for p in string.punctuation:
            new_input.append(element + p)
            new_input.append(p + element)
    user_input.extend(new_input)

def load_input() -> list[str]:
    """
    Load the input from input.txt
    """
    user_input = []
    with open('input.txt', 'r') as f:
        for line in f:
            user_input.extend(line.split())
    return user_input
def generate_passwords(user_input: list[str]) -> None:
    """ Generate passwords from the input """
    add_cases(user_input)
    mix_inputs(user_input)
    add_punctuation(user_input)
    add_numbers(user_input)
    add_punctuation(user_input)


def main():
    user_input = load_input()
    generate_passwords(user_input)
    
    with open('output.txt', 'w') as f:
        for password in user_input:
            f.write(f'{password}\n')

    print(f'Done! {len(user_input)} words generated')

if __name__ == '__main__':
    main()