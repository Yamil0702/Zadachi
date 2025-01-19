def calculate_structure_sum(data):
    total_sum = 0
    if isinstance(data, int):  # Если элемент — число, добавляем его к сумме
        total_sum += data
    elif isinstance(data, str):  # Если элемент — строка, добавляем её длину к сумме
        total_sum += len(data)
    elif isinstance(data, (list, tuple, set)):  # Если элемент — список, кортеж или множество, рекурсивно обрабатываем каждый элемент
        for item in data:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):  # Если элемент — словарь, рекурсивно обрабатываем ключи и значения
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)
    return total_sum
