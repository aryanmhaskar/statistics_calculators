import math
from sigfig import round


data_set = [] # Set a list to hold all data points for any given scenario
while True:
    string_value = input("Enter single data value then hit enter\n When all data points entered, type 'quit': ") # Ask for each individual data point
    if string_value == 'quit': # Add way to break from loop after all data points entered
        break
    else:
        try: 
            data_value = float(string_value) # Convert data value from string to float
            data_set.append(data_value) # Add to list
            print(f"Current data set:\n {data_set}") # Allow user to see data values entered.
        except ValueError:
            print("Enter number or 'quit'") # In case user doesn't enter 'quit' or a number

while True:
    string_figs = input("Number of significant figures to round to: ") # Get number of sig figs to round to
    try:
        sig_figs = int(string_figs)
        break
    except ValueError: # Prevent ValueError convert the String input to an integer from occuring
        print("Enter an integer")

mean_sum = 0 
for value in data_set: # Add all the values to create the sum to calculate mean
    mean_sum += value 

mean = round(mean_sum/len(data_set), sigfigs=sig_figs) # Calculate the mean with significant figures

minimum = data_set[0]
for value in data_set: # Find the maximum for the range
    if value < minimum:
        minimum = value

maximum = data_set[0]
for value in data_set: # Find the minimum for the range
    if value > maximum:
        maximum = value

range = maximum-minimum # Calculate the range

squared_values = [] 
for value in data_set: # Subtract each value by the mean and square the result, then add to list.
    sqvalue = (value-mean)**2
    squared_values.append(sqvalue)

squared_sum = 0
for value in squared_values: # Add all squared values to be used to calculate the variance and standard deviation
    squared_sum += value

variance = float(squared_sum/(len(data_set) - 1)) # Calculate the variance
standard_deviation = math.sqrt(variance) # Calculate the standard deviation

# Calculate all the SD ranges, L means lower boud, H means upper bound. 
L1sd = mean-standard_deviation
H1sd = mean+standard_deviation
L2sd = mean-(2*standard_deviation)
H2sd = mean+(2*standard_deviation)
L3sd = mean-(3*standard_deviation)
H3sd = mean+(3*standard_deviation)


# Output all the values for a descriptive statistics table
output = f"""
mean: {mean}\n
range: {range}\n
maximum: {maximum}\n
minimum: {minimum}\n
variance: {variance}\n
standard deviation: {standard_deviation}\n
1SD: {L1sd}-{H1sd}
2SD: {L2sd}-{H2sd}
3SD: {L3sd}-{H3sd}
Number: {len(data_set)}
"""
print(output)