# Exercice 1 - Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci_list(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        fib = [0,1]
        for i in range(2,n):
            fib.append(fib[i-1]+fib[i-2])
        return fib


# Exercice 2 - Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def prime_list(list):
    prime = []
    for i in list:
        if i > 1:
            for j in range(2,int(i/2+1)):
                if (i % j) == 0:
                    break
            else: # else de la for loop
                prime.append(i)
    return prime


# Exercice 3 - Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def list_operations(list_a, list_b):
    intersect = []
    union = []
    a_minus_b = []
    b_minus_a = []
    for i in list_a:
        if i in list_b:
            intersect.append(i)
        else:
            a_minus_b.append(i)
    for i in list_b:
        if i not in list_a:
            b_minus_a.append(i)
    union = list_a + b_minus_a
    return intersect, union, a_minus_b, b_minus_a

# Exercice 4 - Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
def compose(list_notes, list_moves, start_position):
    song = []
    song.append(list_notes[start_position])
    for i in range(len(list_moves)):
        start_position = (start_position + list_moves[i]) % len(list_notes)  # % len pentru a nu depasi marginile listei
        song.append(list_notes[start_position])
    return song


# Exercice 5 - Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
def matrix_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix


# Exercice 6 - Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists.
def list_count(lists, x):
    count = {}
    for i in lists:
        for j in i:
            if j in count:
                count[j] += 1
            else:
                count[j] = 1
    result = []
    for i in count:
        if count[i] == x:
            result.append(i)
    return result


# Exercice 7 - Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
def palindrome(list):
    count = 0
    max_palindrome = 0
    for i in list:
        if str(i) == str(i)[::-1]:
            count += 1
            if i > max_palindrome:
                max_palindrome = i
    return count, max_palindrome


# Exercice 8 - Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
#
#  Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must return list of lists.
def ascii_divisible(x=1, list=[], flag=True):
    result = []
    for i in list:
        temp = []
        for j in i:
            if flag == True:
                if ord(j) % x == 0:
                    temp.append(j)
            else:
                if ord(j) % x != 0:
                    temp.append(j)
        result.append(temp)
    return result


# Exercice 9 - Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.
#
# 	Example:
#
# # FIELD
#
# [[1, 2, 3, 2, 1, 1],
#
# [2, 4, 4, 3, 7, 2],
#
# [5, 5, 2, 5, 6, 4],
#
# [6, 6, 7, 6, 7, 5]]
#
# Will return : [(2, 2), (3, 4), (2, 4)]

def find_obstructed_seats(matrix):
    obstructed_seats = []
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            current_height = matrix[row][col]

            # Check if there is a taller spectator in front
            obstructed = False
            for r in range(row + 1, rows):
                if matrix[r][col] > current_height:
                    obstructed = True
                    break

            if obstructed:
                obstructed_seats.append((row, col))

    return obstructed_seats


# Exercice 10 - Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].
def list_to_tuple(*lists):
    result = []
    for i in range(max([len(x) for x in lists])):
        temp = []
        for j in lists:
            if i < len(j):
                temp.append(j[i])
            else:
                temp.append(None)
        result.append(tuple(temp))
    return result


# Exercice 11 - Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def order_tuples_by_3rd(tuples_list):
    key_tuplu = lambda x: x[1][2] if len(x[1]) > 2 else None

    sorted_tuples = sorted(tuples_list, key=key_tuplu)
    return sorted_tuples


# Exercice 12 - Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
def group_by_rhyme(words):

    rhyme_groups = {}

    for word in words:
        rhyme = word[-2:]

        if rhyme not in rhyme_groups:
            rhyme_groups[rhyme] = []

        rhyme_groups[rhyme].append(word)

    grouped_words = list(rhyme_groups.values())

    return grouped_words


if __name__ == "__main__":

    #Exercice 1
    print(fibonacci_list(10))

    #Exercice 2
    print(prime_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))

    #Exercice 3
    print(list_operations([1,2,3,4,5,6,7,8,9,10],[5,6,7,8,9,10,11,12,13,14,15]))

    #Exercice 4
    print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

    #Exercice 5
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    for i in matrix_diagonal(matrix):
        print(i)

    #Exercice 6
    print(list_count([[1,2,3],[2,3,4],[4,5,6],[4,1,"test"]], 2))

    #Exercice 7
    print(palindrome([1,2,121,232,343,454,9009,901,101102]))

    #Exercice 8
    print(ascii_divisible(2, ["test", "hello", "lab002"], False))

    #Exercice 9
    stadium = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
              ]
    obstructed = find_obstructed_seats(stadium)
    print(obstructed)

    #Exercice 10
    print(list_to_tuple([1,2,3,4], [5,6,7], ["a", "b", "c"]))

    #Exercice 11
    tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
    print(order_tuples_by_3rd(tuples_list))

    #Exercice 12
    words = ['ana', 'banana', 'carte', 'arme', 'parte']
    print(group_by_rhyme(words))



















