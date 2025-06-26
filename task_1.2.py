def sort_dicts_by_key(dicts_list, sort_key, reverse=False):
    """
    Sorts a list of dictionaries by a specific key.

    Args:
        dicts_list (list): List of dictionaries to sort.
        sort_key (str): The key to sort the dictionaries by.
        reverse (bool): Whether to sort in descending order.

    Returns:
        list: New list of dictionaries sorted by the given key.
    """
    return sorted(dicts_list, key=lambda x: x.get(sort_key), reverse=reverse)

# Example usage:
data = [
    {"name": "Alice", "age": 34},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 40}
]

sorted_data = sort_dicts_by_key(data, "name")
print(sorted_data)
# Output: [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 34}, {'name': 'Charlie', 'age': 40}]