# Python Challenge
## Summary
This repository contains two seperate Python files, PyBank and PyPoll, with each folder containing its own CSV file for both its input and output.
PyBank evaluates a companys profits to corresponding dates, while PyPoll evaluates an election result.

## PyBank
The code for PyBank will read the data provided in an external CSV file, in this case labelled budget_data. This CSV file provides the user with a companies monthly profit/loss. Upon running the program, a result will output to a CSV file labelled analysis which contains the following information:
* total months of data
* total change in profit/loss over the whole time period provided
* average change to the monthly profit
* the month with the greatest profit increase, including value
* the month with the greatest profit decrease, including value

## PyPoll
PyPoll reads election data stored in a CSV file labelled election_data, which contains the votes Ballot ID, County, and Candidate name. It then returns the following information in the form of a CSV file named poll_results:
* total number of votes
* each candidate name, their percentage of votes received and actual number of votes received
* the winning candidate

## Running the code
This code is written in Python and runs using your computers Terminal (or similar) program. To view the inputs and outputs, a CSV reader is required. Common examples of this are Microsoft Excel or Visual Studio Code. 
