import csv
import time

# Count of lines with no value
wrong_values = 0
# Count of lines with correct value
correct_values = 0
# List for values
list_of_values = []

wrong_list = []

# Start counting time
start_time = time.time()

# Opening data file and reading each line
with open('projekt2_dane.csv', 'r', encoding="utf8") as data_file:
    csv_reader = csv.reader(data_file)
    # If there is acceptable value in third column, we put it at the end of "list_of_values"
    # We also convert that value from to "float" and then, to "int"
    for line in csv_reader:
        if (line[2] == '1.0' or line[2] == '2.0' or line[2] == '3.0' or line[2] == '4.0' or line[2] == '5.0' or
                line[2] == '6.0' or line[2] == '7.0' or line[2] == '8.0' or line[2] == '9.0' or line[2] == '10.0'):
            correct_values += 1
            list_of_values.append(int(float(line[2])))
        # If that value is empty or is actually a name e.g. "Gate (2011–2015)"
        else:
            wrong_values += 1

# Calculating time required for loading and writing values
duration_time = time.time() - start_time

# Create lists with different sizes
list_of_values_100 = list_of_values[:100]
list_of_values_10k = list_of_values[:10000]
list_of_values_100k = list_of_values[:100000]
list_of_values_500k = list_of_values[:500000]
list_of_values_max = list_of_values

print('-----------------------------------------')
print('Lines with correct values:', correct_values)
print('Lines with wrong values:', wrong_values)
print('Loading and writing to time:', '%.2f' % duration_time)
print('Size of list:', len(list_of_values))
print('-----------------------------------------')
