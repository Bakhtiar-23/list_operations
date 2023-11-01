# File name:                              list_operations.py
# Author:                                 Bakhtiar Khider Ismail
# Description:                            List operations: search, add, remove, sort, and list functions.

def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def search_element(lst, element):
    found = False
    if is_float(element):
        element = float(element)
    for item in lst:
        if isinstance(item, (int, float)) and (isinstance(element, (int, float)) and abs(item - element) < 1e-6):
            found = True
            break
        if isinstance(item, str) and item == element:
            found = True
            break

    if found:
        return f"{element} found in the list."
    else:
        return f"{element} not found in the list."


def add_element(lst, element):
    lst.append(element)
    return f"{element} added to the list."


def remove_element(lst, element):
    found = False
    if element.isdigit():
        element = int(element)
    try:
        element = float(element)
    except ValueError:
        pass

    if isinstance(element, (int, float)):
        if element in lst:
            lst.remove(element)
            found = True
    elif isinstance(element, str):
        if element in lst:
            lst.remove(element)
            found = True

    if found:
        return f"{element} removed from the list."
    else:
        return f"{element} not found in the list."


def sort_list(lst, ascending=True):
    numeric_elements = [x for x in lst if isinstance(x, (int, float))]
    non_numeric_elements = [x for x in lst if not isinstance(x, (int, float))]

    if ascending:
        numeric_elements.sort()
    else:
        numeric_elements.sort(reverse=True)

    sorted_lst = numeric_elements + non_numeric_elements
    return sorted_lst


def list_elements(lst):
    return lst


if __name__ == "__main__":
    my_list = [10, 5.5, "Hello", 20, 15.5, "World", 30, 25.5,
               "Python", 40, 35.5, "Program", 60, 55.5, "List", 70, 65.5, "Example",
               80, 75.5, "AI", 90, 85.5, "OpenAI", 100, 95.5, "GPT-3", 110, 105.5, "Sample Text"]

    while True:
        print("\nChoose an option:")
        print("1. Search for an element")
        print("2. Add an element")
        print("3. Remove an element")
        print("4. Sort the list")
        print("5. List all elements")
        print("6. Stop the program")

        choice = input("Enter your choice: ")

        if choice == '1':
            element = input("Enter the element to search: ")
            result = search_element(my_list, element)
            print(result)
        elif choice == '2':
            element = input("Enter the element to add: ")
            result = add_element(my_list, element)
            print(result)
        elif choice == '3':
            element = input("Enter the element to remove: ")
            result = remove_element(my_list, element)
            print(result)
        elif choice == '4':
            ascending = input("Sort in ascending order? (y/n): ").lower()
            ascending = ascending == 'y'
            result = sort_list(my_list, ascending)
            print(result)
        elif choice == '5':
            elements = list_elements(my_list)
            print("List elements:", elements)
        elif choice == '6':
            print("Program stopped.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
