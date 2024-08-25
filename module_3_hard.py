def calculate_structure_sum(value):
    global sum_value
    if isinstance(value, int):
        sum_value += float(value)
    elif isinstance(value, str):
        sum_value += float(len(value))
    elif isinstance(value, float):
        sum_value += value
    elif isinstance(value, dict):
        for item in value:
            calculate_structure_sum(value[item])
            calculate_structure_sum(item)
    elif not isinstance(value, bool):
        for item in value:
            calculate_structure_sum(item)
    return sum_value


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_value = 0.0
result = calculate_structure_sum(data_structure)
print(result)
