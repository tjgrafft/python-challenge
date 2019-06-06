import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
month = []
profit_loss = []

# with open(budget_data, newline="", encoding='utf-8') as csvfile:
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        # Add month
        month.append(row[0])

        # Add profit/loss
        profit_loss.append(int(row[1]))

def month_count(mon):
    print("Total Months: " + str(len(mon)))
    return ("Total Months: " + str(len(mon)))
    
def PF_sum(PL):
    total_sum = sum(profit_loss)
    print(f"Total: $" + str(total_sum))
    return f"Total: $" + str(total_sum)

# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total_change = 0
    great_increase = 0
    great_decrease = 0
    increase_index = 0
    decrease_index = 0
    change = 0

    for number in numbers:
        if numbers.index(number) == 0:
            last_value = number
        else:
        
            change = number - last_value
            if change > great_increase: 
                great_increase = change
                increase_index = numbers.index(number)          
            elif change < great_decrease : 
                great_decrease = change
                decrease_index = numbers.index(number)
            total_change += change
            last_value = number

    for x in month:
        if month.index(x) == increase_index:
            month_in = x
        elif month.index(x) == decrease_index:
            month_de = x


    
    average_change = str(round(float(total_change / (length-1)), 2))
    print("Average Change: $" + average_change)
    print("Greatest Increase in Profits: "  + str(month_in) + " ("  + str(great_increase) + ")")
    print("Greatest Decrease in Profits: " + str(month_de) + " (" + str(great_decrease) + ")")
    return ("Average Change: $" + average_change) + '\n' + ("Greatest Increase in Profits: "  + str(month_in) + " ("  + str(great_increase) + ")") + '\n' + ("Greatest Decrease in Profits: " + str(month_de) + " (" + str(great_decrease) + ")")


#Print output for terminal
print("Financial Analysis")
print("----------------------------")
month_count(month)
PF_sum(profit_loss)
average(profit_loss)


##Write to text file
with open("results.txt","w") as file1: 
    file1.write("Financial Analysis" + '\n')
    file1.write("------------------------" + '\n')
    file1.write(str(month_count(month)) + '\n')
    file1.write(str(PF_sum(profit_loss)) + '\n')
    file1.write(str(average(profit_loss)) + '\n')
    file1.close()
