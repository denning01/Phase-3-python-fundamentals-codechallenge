def sort_by_age(tuples_list):
    # Sort the list of tuples by the second element (age) in each tuple
    sorted_list = sorted(tuples_list, key=lambda x: x[1])
    return sorted_list


# List of tuples with (name, age)
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

# Sort the list by age
sorted_people = sort_by_age(people)

print(sorted_people)  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
