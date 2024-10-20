data = {'1232': 'value1', '4212': 'value2', '12234': 'value3', '21': 'value4'}
filtered_keys = [key for key in data if len(key) > 3]
print(filtered_keys)
filtered_keys = list(filter(lambda key: len(key) > 3, data))
print(filtered_keys)


input()
