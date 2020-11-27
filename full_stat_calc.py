from itertools import count
import math
import itertools
from sigfig import round

def create_data_set():
    data_set = [] # Set a list to hold all data points for any given scenario
    data_set_name = input("Name of data set:") # Allow user to name each data set
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
    data_set.append(data_set_name) # Make the name of the data set the last item in the list
    return data_set

while True:
    try:
        string_sets = input("Number of data sets: ") # Ask for the number of data sets to be processed
        number_of_data_sets = int(string_sets) 
        break
    except ValueError:
        print("Enter an integer")    

data_sets = []
for x in range(0, number_of_data_sets): # Create a 2-dimensional list that holds all data sets
    data_sets.append(create_data_set())

while True:
    string_figs = input("Number of significant figures to round to: ") # Get number of sig figs to round to
    try:
        sig_figs = int(string_figs)
        break
    except ValueError: # Prevent ValueError convert the String input to an integer from occuring
        print("Enter an integer")

mean_list = [] # Add all means to this number to perform a t-test
variance_list = [] # Add all variances to this number to perform a t-test
number = None
for data_set in data_sets: # Do statistical analysis for each data set

    number = len(data_set) - 1 # Create the number for statistical operations, subtract 1 because last in index is the name

    mean_sum = 0 
    for value in data_set[:-1]: # Add all the values to create the sum to calculate mean, remove last because last is the name
        mean_sum += value 

    mean = round(mean_sum/number, sigfigs=sig_figs) # Calculate the mean with significant figures
    mean_list.append(mean)

    minimum = data_set[0]
    for value in data_set[:-1]: # Find the maximum for the range subtract because last element is name
        if value < minimum:
            minimum = value

    maximum = data_set[0]
    for value in data_set[:-1]: # Find the minimum for the range subtract because last element is name
        if value > maximum:
            maximum = value

    stat_range = maximum-minimum # Calculate the range

    squared_values = [] 
    for value in data_set[:-1]: # Subtract each value by the mean and square the result, then add to list subtract because last element is name
        sqvalue = (value-mean)**2
        squared_values.append(sqvalue)

    squared_sum = 0
    for value in squared_values: # Add all squared values to be used to calculate the variance and standard deviation
        squared_sum += value

    variance = float(squared_sum/(number - 1)) # Calculate the variance, subtract 1 because formula is n-1
    variance_list.append(variance) # Add variance to variance list to later calculate t-test
    standard_deviation = math.sqrt(variance) # Calculate the standard deviation

    # Calculate all the SD ranges, L means lower boud, H means upper bound. 
    L1sd = mean-standard_deviation
    H1sd = mean+standard_deviation
    L2sd = mean-(2*standard_deviation)
    H2sd = mean+(2*standard_deviation)
    L3sd = mean-(3*standard_deviation)
    H3sd = mean+(3*standard_deviation)

    # Output all the values for a descriptive statistics table
    # The data_set[-1] is to access the name of the data set
    descriptive_stats = f"""___________________________________
{data_set[-1]}:
mean: {mean}

range: {stat_range}
    maximum: {maximum}
    minimum: {minimum}

variance: {variance}
standard deviation: {standard_deviation}
    1SD: {L1sd}-{H1sd}
    2SD: {L2sd}-{H2sd}
    3SD: {L3sd}-{H3sd}

Number: {number} 
___________________________________
    """
    print(descriptive_stats)

mean_differences = []
for a, b in itertools.permutations(mean_list, 2): # Part one of t-test, calculate the differences of the means for each t-test needed to be performed
    mean_difference = a-b
    mean_differences.append(mean_difference) # Log the values in order in a t-test so that the correct values are used for each corresponding t-test

variance_processes = []
for a, b in itertools.permutations(variance_list, 2): # Part 2 of the t-test, calculate the variances summed and rooted for each t-test needed to be performed
    variance_process = math.sqrt((a+b)/number)
    variance_processes.append(variance_process) # Log the values in order in a t-test so that the correct values are used for each corresponding t-test

t_values = []
for x in range(0, len(mean_differences)): # Since the two lists should be the same, use the length for one to increment the x counter 
    t_value = abs(mean_differences[x]/variance_processes[x]) # Since values stored in order, the same counter can be used to index both lists to get the t-value
    t_values.append(t_value) # Log the values in order in a t-test so that the correct values are used for each corresponding t-test

t_outputs = []
counter = 0
for a, b in itertools.permutations(data_sets, 2):
    t_out = f"{a[-1]} vs {b[-1]}: {t_values[counter]}" # Since the values are stored in order, uses the indexes to acces names to return the t-value for the specified t-test
    t_outputs.append(t_out) # Add to list of formatted strings
    counter += 1


print("""______________________
Results of t-test:""")
for out in t_outputs:
    print(out)
print("______________________")