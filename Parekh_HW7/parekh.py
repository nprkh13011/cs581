# Nidhi Parekh
# I pledge my honor that I have abided by the Stevens Honor System.

# Assignment 7
# To run from terminal window:   python3 parekh.py

"""
DESCRIPTION:
The idea of this assignment is using the data from Pew_Survey.csv,
    parekh.py processes an input file and prints results to the terminal window
    in both written/tabular and graph form.
Topic: Comparing Income Levels By Gender
    
"""
import csv
import matplotlib.pyplot as plt
import pprint
import tabulate
import numpy as np
print("\n----------------------------------------------ASSIGNMENT 7 - ANALYZE SOCIAL NETWORK DATA---------------------------------------------------\n")

# read the file
def process_file():
    #count for male with specific incomes
    count_Male_income1=0
    count_Male_income2=0
    count_Male_income3=0
    count_Male_income4=0
    count_Male_income5=0
    count_Male_income6=0
    count_Male_income7=0
    count_Male_income8=0
    count_Male_income9=0
    count_Male_income98=0
    count_Male_income99=0

    #count for female with specific incomes
    count_Female_income1=0
    count_Female_income2=0
    count_Female_income3=0
    count_Female_income4=0
    count_Female_income5=0
    count_Female_income6=0
    count_Female_income7=0
    count_Female_income8=0
    count_Female_income9=0
    count_Female_income98=0
    count_Female_income99=0

    with open('Pew_Survey.csv', mode='r', newline='') as file: # read the file
        csvreader = csv.reader(file)
        header = next(csvreader)
        rows = [] #list of list
        for row in csvreader:
            rows.append(row)

        #iterate through rows
        for i in range(0, len(rows)):
            income = rows[i][27] # they're strings --- data field #28
            #print("Income: " + income)
            sex = rows[i][22] #data field #23
            #print("sex:" + sex)
            #conditions for income -- males 
            if (income == '1' and sex == '1'): # male with income < $10k
                count_Male_income1 += 1
            if (income == '2' and sex == '1'): # male with $10 - 20K
                count_Male_income2 += 1
            if (income == '3' and sex == '1'): # male with $20 - 30K
                count_Male_income3 += 1
            if (income == '4' and sex == '1'): # male with $30 - 40K
                count_Male_income4 += 1
            if (income == '5' and sex == '1'): # male with $40 - 50K
                count_Male_income5 += 1
            if (income == '6' and sex == '1'): # male with $50 - 75K
                count_Male_income6 += 1
            if (income == '7' and sex == '1'): # male with $75 - 100K
                count_Male_income7 += 1
            if (income == '8' and sex == '1'): # male with $100 - 150K
                count_Male_income8 += 1
            if (income == '9' and sex == '1'): # male with $150 < 
                count_Male_income9 += 1
            if (income == '98' and sex == '1'): # Don't Know income for male
                count_Male_income98 += 1
            if (income == '99' and sex == '1'): # Male refused
                count_Male_income99 += 1

            #conditions for income -- females
            if (income == '1' and sex == '2'): # Female with income < $10k
                count_Female_income1 += 1
            if (income == '2' and sex == '2'): # Female with $10 - 20K
                count_Female_income2 += 1
            if (income == '3' and sex == '2'): # Female with $20 - 30K
                count_Female_income3 += 1
            if (income == '4' and sex == '2'): # Female with $30 - 40K
                count_Female_income4 += 1
            if (income == '5' and sex == '2'): # Female with $40 - 50K
                count_Female_income5 += 1
            if (income == '6' and sex == '2'): # Female with $50 - 75K
                count_Female_income6 += 1
            if (income == '7' and sex == '2'): # Female with $75 - 100K
                count_Female_income7 += 1
            if (income == '8' and sex == '2'): # Female with $100 - 150K
                count_Female_income8 += 1
            if (income == '9' and sex == '2'): # Female with $150 < 
                count_Female_income9 += 1
            if (income == '98' and sex == '2'): # Don't Know income for Female
                count_Female_income98 += 1
            if (income == '99' and sex == '2'): # Female refused
                count_Female_income99 += 1

        # Male's Incomes Before Taxes
        print("\n----------------------------------------------Data on Male Incomes (Before Taxes)---------------------------------------------------\n")
        print("----------------------------------------------Ranges of Income---------------------------------------------------\n")
        print("1. Income < $10K: " + str(count_Male_income1))
        print("2. Income Between $10K-$20K: " + str(count_Male_income2))
        print("3. Income Between $20K-$30K: " + str(count_Male_income3))
        print("4. Income Between $30K-$40K: " + str(count_Male_income4))
        print("5. Income Between $40K-$50K: " + str(count_Male_income5))
        print("6. Income Between $50K-$75K: " + str(count_Male_income6))
        print("7. Income Between $75K-$100K: " + str(count_Male_income7))
        print("8. Income Between $100K-$150K: " + str(count_Male_income8))
        print("9. Income > $150K: " + str(count_Male_income9))
        print("10. Males That Don't Know Income : " + str(count_Male_income98))
        print("11. Males Who Refused to Disclose Income: " + str(count_Male_income99))
        
        # Female's Incomes Before Taxes
        print("\n----------------------------------------------Data on Female Incomes (Before Taxes)---------------------------------------------------\n")
        print("----------------------------------------------Ranges of Income---------------------------------------------------\n")
        print("1. Income < $10K: " + str(count_Female_income1))
        print("2. Income Between $10K-$20K: " + str(count_Female_income2))
        print("3. Income Between $20K-$30K: " + str(count_Female_income3))
        print("4. Income Between $30K-$40K: " + str(count_Female_income4))
        print("5. Income Between $40K-$50K: " + str(count_Female_income5))
        print("6. Income Between $50K-$75K: " + str(count_Female_income6))
        print("7. Income Between $75K-$100K: " + str(count_Female_income7))
        print("8. Income Between $100K-$150K: " + str(count_Female_income8))
        print("9. Income > $150K: " + str(count_Female_income9))
        print("10. Females That Don't Know Income : " + str(count_Female_income98))
        print("11. Females Who Refused to Disclose Income: " + str(count_Female_income99))



        # create a bar graph for men and women per income
        # How many men and women earn the same range or
        Female = [float(count_Female_income1),float(count_Female_income2),
                 float(count_Female_income3),float(count_Female_income4),
                 float(count_Female_income5),float(count_Female_income6),
                 float(count_Female_income7),float(count_Female_income8),
                 float(count_Female_income9),float(count_Female_income98), float(count_Female_income99)]
        Male = [float(count_Male_income1),float(count_Male_income2),
                 float(count_Male_income3),float(count_Male_income4),
                 float(count_Male_income5),float(count_Male_income6),
                 float(count_Male_income7),float(count_Male_income8),
                 float(count_Male_income9),float(count_Male_income98), float(count_Male_income99)]

        #fig, ax = plt.subplots()
        x_labels=['Less than 10','10-20','20-30','30-40','40-50','50-75','75-100',
                  '100-150', 'More than 150', 'Unsure', 'Refused']
        # https://www.geeksforgeeks.org/plotting-multiple-bar-charts-using-matplotlib-in-python/
        n=11
        r = np.arange(n)
        width=0.25
        
        plt.bar(r, Female, color='pink', width=width, edgecolor='black', label='Female')
        plt.bar(r+width, Male, color='lightgreen', width=width, edgecolor='black', label='Male')
         
        plt.xticks(r+width/2, x_labels)
        plt.title('2018 Family Incomes Levels By Gender')
        plt.xlabel('Income Levels (in thousands $)')
        plt.ylabel('Number of Participants')
        plt.legend()
        plt.show()
        
process_file()















