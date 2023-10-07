# Exercice 1 - Find The greatest common divisor of multiple numbers read from the console.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd_of_numbers(numbers):
    if len(numbers) < 2:
        return numbers[0]

    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])

    return result


# Exercice 2 - Write a script that calculates how many vowels are in a string.
def count_vowels_in_string(string):
    vowels = "aeiou"
    counter = 0
    for char in string:
        if char in vowels:
            counter += 1
    return counter


# Exercice 3 - Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def count_occurrences_of_string_in_string(string1, string2):
    counter = 0
    for i in range(len(string2)):
        if string2[i:].startswith(string1):
            counter += 1
    return counter


# Exercice 4 - Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
def convert_upper_camel_case_to_lowercase_with_underscores(input_str):
    result = ""
    for char in input_str:
        if char.isupper():
            if result:
                result += "_" # pentru a nu avea underscore la inceput
            result += char.lower()
        else:
            result += char
    return result


#Exercice 5 - Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order:
def spiral_matrix(matrix):
    result = ""
    while matrix:
        result += "".join(matrix.pop(0))
        for row in matrix:
            result += row.pop()
        if matrix:
            result += "".join(matrix.pop()[::-1])
        for row in matrix[::-1]: # [::-1] - inverseaza lista
            result += row.pop(0)
    return result


# Exercice 6 - Write a function that validates if a number is a palindrome.
def is_palindrome(number):
    ogl = 0
    aux = number
    while aux > 0:
        ogl = ogl * 10 + aux % 10
        aux = aux // 10
    if number == ogl:
        print(f"The number {number} is a palindrome.")
    else:
        print(f"The number {number} is not a palindrome.")


# Exercice 7 - Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
def extract_number_from_text(text):
    result = ""
    flag_found = False
    for char in text:
        if char.isdigit():
            result += char
            flag_found = True
        elif result:
            break # daca am gasit un numar, nu mai cautam
    if flag_found:
        return int(result)
    else:
        return None


# Exercice 8 - Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
def count_bits_with_value_1(number):
    result = 0
    while number:
        result += number & 1 # daca ultimul bit este 1, atunci rezultatul va fi 1, altfel 0
        number >>= 1 # shiftare la dreapta cu o pozitie
    return result


# Exercice 9 - Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.
def most_common_letter(input_str):
    input_str = input_str.lower()

    letter_count = {} # dictionar in care cheia este litera, iar valoarea este numarul de aparitii al literei

    for char in input_str:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    # Find the most common letter and its count.
    max_count = 0
    most_common = None

    for letter, count in letter_count.items():
        if count > max_count:
            most_common = letter
            max_count = count
        elif count == max_count and letter < most_common:
            most_common = letter


    return most_common, max_count


# Exercice 10 - Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.
def count_words_in_text(text): # mergea si cu split()
    counter = 0
    for i in range(len(text)):
        if text[i] == " " and text[i-1] != " ":
            counter += 1
    if text[-1] != " ":
       counter += 1
    return counter

if __name__ == "__main__":

    #Exercice 1
    input_numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in input_numbers]
    gcd_result = find_gcd_of_numbers(numbers)
    print(f"The GCD of the numbers is: {gcd_result}")

    #Exercice 2
    input_string = input("Enter a string: ")
    print(f"The number of vowels in the string is: {count_vowels_in_string(input_string)}")

    #Exercice 3
    input_string1 = input("Enter the first string: ")
    input_string2 = input("Enter the second string: ")
    print(f"The number of occurrences of the first string in the second is: {count_occurrences_of_string_in_string(input_string1, input_string2)}")
    
    #Exercice 4
    input_string = input("Enter a string in UpperCamelCase: ")
    print(f"The string converted to lowercase_with_underscores is: {convert_upper_camel_case_to_lowercase_with_underscores(input_string)}")
    
    #Exercice 5
    input_matrix = input("Enter a matrix of characters: ").split() # formatul : firs n_lt oba_ htyp
    matrix = [list(row) for row in input_matrix]
    print(f"The string obtained by going through the matrix in spiral order is: {spiral_matrix(matrix)}")

    #Exercice 6
    input_number = int(input("Enter a number: "))
    is_palindrome(input_number)

    #Exercice 7
    input_text = input("Enter a text: ")
    print(f"The number extracted from the text is: {extract_number_from_text(input_text)}")
    
    #Exercice 8
    input_number = int(input("Enter a number: "))
    print(f"The number of bits with value 1 is: {count_bits_with_value_1(input_number)}")
    
    #Exercice 9
    input_string = input("Enter a string: ")
    most_common, count = most_common_letter(input_string)
    print(f"The most common letter is {most_common} and it appears {count} times.")

    #Exercice 10
    input_text = input("Enter a text: ")
    print(f"The number of words in the text is: {count_words_in_text(input_text)}")






