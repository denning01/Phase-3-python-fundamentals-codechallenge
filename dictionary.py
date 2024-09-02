def merge_dicts(dict1, dict2):
    # Create a new dictionary that starts as a copy of dict1
    merged_dict = dict1.copy()

    # Iterate over the second dictionary
    for key, value in dict2.items():
        # If the key is already in the merged dictionary, sum the values
        if key in merged_dict:
            merged_dict[key] += value
        else:
            # If the key is not in the merged dictionary, add the key-value pair
            merged_dict[key] = value

    return merged_dict

# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

# Call the merge_dicts function and print the result
merged = merge_dicts(dict1, dict2)
print(merged)  # Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
