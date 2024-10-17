 The program takes a dictionary and checks if a given key exists in a dictionary or not. 
...
def check_key_in_dict(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
key_to_check = 'age'

if check_key_in_dict(my_dict, key_to_check):
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")
...
Key 'age' exists in the dictionary.
