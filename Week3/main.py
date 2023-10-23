from itertools import combinations


# Exercice 1 - Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)
def list_operations(a, b):
    # Convert the input lists to sets
    set_a = set(a)
    set_b = set(b)

    # Perform set operations
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    a_minus_b = set_a.difference(set_b)
    b_minus_a = set_b.difference(set_a)

    # Create a list of sets with the results
    result = [intersection, union, a_minus_b, b_minus_a]

    return result


#Exercice 2 - Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and
# the values are the number of occurrences of that character in the given text. Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
#{'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .
def count_characters(text):
    result = {}

    # Iterate through the string
    for character in text:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1

    return result


#Exercice 3 - Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)
def compare_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False

    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Recursively compare the values for each key
    for key in dict1.keys():
        value1 = dict1[key]
        value2 = dict2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dicts(value1, value2):
                return False

        elif isinstance(value1, list) and isinstance(value2, list):
            if len(value1) != len(value2):
                return False
            for item1, item2 in zip(value1, value2):
                if isinstance(item1, dict) and isinstance(item2, dict):
                    if not compare_dicts(item1, item2):
                        return False
                elif item1 != item2:
                    return False
        elif value1 != value2:
            return False

    return True


#Exerice 4 - The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML element.
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns the string = "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there ".
def build_xml_element(tag, content, **kwargs):
    result = "<" + tag

    for key, value in kwargs.items():
        result += " " + key + "=\"" + value + "\""

    result += ">" + content + "</" + tag + ">"

    return result

#Exercice 5 - The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that has strings as keys and values)
# and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix",
# "middle" is inside the value (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.
# Example: the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} and
# d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules are respected
# for "key1" and "key2" "key3" that does not appear in the rules.
def validate_dict(rules, dictionary):
    # Create a set to store keys that match the rules
    matched_keys = set()


    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            # Check if the value follows the rule
            if value.startswith(prefix) and middle in value[1:-1] and value.endswith(suffix):
                matched_keys.add(key)


    return len(matched_keys) == len(dictionary)


#Exercice 6 - Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in the list,
# and b representing the number of duplicate elements in the list (use sets to achieve this objective).
# 1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7 => (5, 2)
def count_unique_duplicates(input_list):
    unique_set = set()
    duplicate_set = set()

    for item in input_list:
        if item not in unique_set and item not in duplicate_set:
            unique_set.add(item)
        elif item in unique_set:
            unique_set.remove(item)
            duplicate_set.add(item)

    return len(unique_set), len(duplicate_set)


#Exercice 7 - Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -. Ex:
#{1,2}, {2, 3} =>
#{
#    "{1, 2} | {2, 3}":  {1, 2, 3},
#    "{1, 2} & {2, 3}":  { 2 },
#    "{1, 2} - {2, 3}":  { 1 },
#    ...
#}
def set_operations(*sets):
    result = {}

    for set1, set2 in combinations(sets, 2):
        key = f"{set1} | {set2}"
        result[key] = set1 | set2

        key = f"{set1} & {set2}"
        result[key] = set1 & set2

        key = f"{set1} - {set2}"
        result[key] = set1 - set2

        key = f"{set2} - {set1}"
        result[key] = set2 - set1

    return result


#Exercice 10(8) - Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start".
# Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value of the current key is the key for the next value, until you find a loop (a key that was visited before).
# The function must return the list of objects obtained as previously described.
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']
def loop(mapping):
    result = []
    visited_keys = set()

    current_key = mapping["start"]

    while current_key not in visited_keys:
        result.append(current_key)
        visited_keys.add(current_key)
        current_key = mapping[current_key]

    return result


#Exercice 11(9) - Write a function that receives a variable number of positional arguments and a variable number of keyword arguments and will return the
# number of positional arguments whose values can be found among keyword arguments values.
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return 3
def positional_vs_keyword_arguments(*args, **kwargs):
    result = 0

    for arg in args:
        if arg in kwargs.values():
            result += 1

    return result

if __name__ == "__main__":
    #Exercice 1
    print("Exercice 1")
    print(list_operations([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

    #Exercice 2
    print("Exercice 2")
    print(count_characters("Ana has apples."))

    #Exercice 3
    print("Exercice 3")
    print(compare_dicts({1: 2, 3: 4}, {1: 2, 3: 4}))
    print(compare_dicts({1: 2, 3: 4}, {1: 2, 3: 4, 5: 6}))

    #Exercice 4
    print("Exercice 4")
    print(build_xml_element("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))

    #Exercice 5
    print("Exercice 5")
    rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    dictionary = {
        "key1": "come inside, it's too cold out",
        "key2": "start the middle of winter",
        "key3": "this is not valid"
    }
    print(validate_dict(rules, dictionary))

    #Exercice 6
    print("Exercice 6")
    print(count_unique_duplicates([1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7]))

    #Exercice 7
    print("Exercice 7")
    print(set_operations({1, 2}, {2, 3}))

    #Exercice 8
    print("Exercice 8")
    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

    #Exercice 9
    print("Exercice 9")
    print(positional_vs_keyword_arguments(1, 2, 3, 4, x=1, y=2, z=3, w=5))
























