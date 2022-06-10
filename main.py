# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


users = ["alivia", "behnam", "bettina", "diadora", "esther", "susanne"]
search_terms = ["opioid abuse intervention", "opioid abuse management",
                "opioid abuse therapy", "opioid abuse treatment", "opioid abuse", "opioid addiction recovery",
                "opioid addiction", "opioid misuse", "opioid use disorder",
                "prescription opioid abuse", "prescription opioid misuse"]

import csv
import statistics
# csv file name
input_folder = "./input_task2/"
filename_suffix = "200_ios.csv"

def read_all_files():
    all_user_results = []
    for user in users:
        user_search_results_per_term = []
        for term in search_terms:

            file = f'{input_folder}{user}_{term}_{filename_suffix}'
            rows_for_user_and_term = read_a_file(file)
            num_results_for_user_and_term = len(rows_for_user_and_term)
            # print(f'{num_results_for_user_and_term} results for user:{user} and search term:{term}')
            user_search_results_per_term.append(num_results_for_user_and_term)
        all_user_results.append(user_search_results_per_term)

    mins_row = []
    maxes_row = []
    means_row = []
    for c in range(len(search_terms)):
        col = column(all_user_results, c)

        minimum = min(col)
        maximum = max(col)
        mean = statistics.mean(col)

        mins_row.append(minimum)
        maxes_row.append(maximum)
        means_row.append(mean)

    all_user_results.append(mins_row)
    all_user_results.append(maxes_row)
    all_user_results.append(means_row)
    write_output_csv(all_user_results)


def column(matrix, i):
    return [row[i] for row in matrix]

def write_output_csv(array):
    filename = "./output/out.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        #csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(array)

def read_a_file(filename):
    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)
        # get total number of rows
        # print("Total no. of rows for file : %d" % (len(rows)))
    return rows
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    read_all_files()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
