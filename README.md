# Daily Pay Calculator
## About the Project
The Daily Pay Calculator is a program that calculates how much someone is to be paid based on the hours worked in the day and their payrate. The calculator accounts for weekends and applies a multiplier on the pay rate, depending on if it's Saturday or Sunday.
## How to Use
This program works using any Python interpreter. The user enters the hours worked, payrate and date of payment into the input fields and the program will calculate how much someone will be paid for their work during that day.
## How it Works
The datetime module is imported to allow use of the datetime functions. The variables saturdayRate and sundayRate are editable to allow workplaces to change them as per their industry award rate. The hours, payrate and dateStr variables take input data from the user. 

The dateStr string is split at each '/' and the values are assigned to three new variables; day, month and year. The dateInt variable is created to format the variables into a date that can be read by the datetime.date function. The strings that were inside the day, month and year variables are converted into integers so the datetime.date function can read the values. The weekday variable is created to get the name of the weekday from the date entered.

To ensure the variables are holding valid data, the majority of the program is wrapped inside a try/except statement. If the data is valid, the program will run otherwise a print statement will appear advising there was an invalid character or date entered.

An if/else statement checks the value of the weekday variable to see if it's Saturday or Sunday and apply the weekend rate where possible. If it's not Saturday or Sunday, the program will calculate the total pay normally and a result will be printed in the console.
