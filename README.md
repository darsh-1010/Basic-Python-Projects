# Description of the projects 

## Project 1 :Event Management System

This Python project is a simple Event Management System that allows users to create new events, store participant and sponsor details, and fetch event details. The system provides a basic command-line interface with different options.

Features:
Create a New Event:

Users can input the name of the event, specify the number of participants and sponsors, and set a total budget.
Event details are stored in a text file with participant and sponsor names, sorted alphabetically.
Fetch Event Details:

Users can retrieve details of an existing event by entering the event name.
Event details, including participants, sponsors, and budget, are displayed on the console.
Advanced Menu:

Offers additional functionalities like listing all events and searching for a specific event.
Users can navigate through the advanced menu to access these features.
List All Events:

Displays a list of all available events, showing the user a numbered menu.
Search for an Event:

Enables users to search for a specific event by entering its name.
Displays event details if the event exists; otherwise, it provides an error message.
How to Use:
Run the script.
Choose options from the main menu to create events, fetch event details, or access the advanced menu for additional features.
Follow the prompts to provide necessary information for event creation.
Retrieve event details by searching for an existing event.

This repository contains two projects developed using Python and Tkinter for creating a simple IRCTC (Indian Railways Catering and Tourism Corporation) ticket booking system. The projects are organized as follows:



## Project 2:Enhanced Event Management System

This Python project is an enhanced version of the Event Management System. It now incorporates the use of Excel files to store event details, providing a more structured and organized approach.

Features:
Create a New Event:

Users can input the name of the event, specify the number of participants and sponsors, and set a total budget.
Event details are stored in both a text file and an Excel file.
The Excel file includes separate columns for participants, sponsors, and total budget.
Fetch Event Details:

Users can retrieve details of an existing event by entering the event name.
Event details, including participants, sponsors, and budget, are displayed on the console.
How to Use:
Run the script.
Choose options from the main menu to create events, fetch event details, or exit the program.
Follow the prompts to provide necessary information for event creation.
Retrieve event details by searching for an existing event.
The enhanced version now utilizes Excel files for better organization and easier data manipulation. Enjoy managing your events with this improved Event Management System!


## Project 3:Loan Calculator

This Python project is a simple GUI-based Loan Calculator that allows users to calculate both simple and compound interest. The calculator is built using the Tkinter library, providing an easy-to-use interface.

#### Features:

1. **Simple Interest Calculator:**
   - Users can enter the principle amount, annual interest rate, and time in years.
   - The calculator displays the calculated interest and the total amount.

2. **Compound Interest Calculator:**
   - Similar to the simple interest calculator, users input the principle amount, annual interest rate, and time in years.
   - The calculator calculates compound interest and the total amount.

3. **User-Friendly Interface:**
   - The application utilizes Tkinter for the graphical user interface, making it accessible and visually appealing.

#### How to Use:

1. Run the script.
2. The main window welcomes users and offers a choice between simple and compound interest.
3. Select the interest type from the dropdown menu.
4. Click the "Submit" button to open the respective interest calculator window.
5. In the calculator window, input the required values and click the "Calculate" button to get the results.

Enjoy the convenience of calculating simple and compound interest with this Loan Calculator!



## Project 4: IRCTCApp (Train Schedule Viewer)

### Description
The `IRCTCApp` project is a Tkinter-based application that allows users to view the train schedule. It provides an interface to select between viewing the train schedule and booking train tickets.

### Files
- `irctc_schedule.py`: Contains the `IRCTCApp` class for viewing the train schedule.

### How to Run
Run the `irctc_schedule.py` file to launch the application. Follow the on-screen instructions to navigate through the menu and view the train schedule.



## Project 5: TicketBookingApp (Train Ticket Booking System)

### Description
The `TicketBookingApp` project is a Tkinter-based application for booking train tickets. Users can input details such as the source station, destination, number of passengers, passenger details, and payment information to book tickets.

### Files
- `irctc_ticket_booking.py`: Contains the `TicketBookingApp` class for booking train tickets.

### How to Run
Run the `irctc_ticket_booking.py` file to launch the application. Follow the on-screen instructions to input the required details and book train tickets.

## Instructions for Running the Projects

1. Make sure you have Python installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the project directory using the terminal or command prompt.
4. Run the respective Python file for the project you want to use.

## Project 6 : Coin Note analysis 

I'd be glad to craft a response that incorporates the best aspects of the previous ones, addresses their shortcomings, and leverages insights from the ratings:

Short GitHub Description:

Coin Note Denomination Calculator

This Python code calculates the optimal combination of coins and notes required to dispense a given currency amount.

Description:

This code provides a straightforward solution for determining the number of coins and notes needed to represent a specific monetary value. It's particularly useful for:

Cash register systems: Calculate the appropriate change to provide to customers based on their payment and purchase amount.
Financial calculations: Gain insights into cash flow management and optimal denomination combinations.
Educational purposes: Demonstrate basic concepts of money and denomination systems.
Functionalities:

Denomination Calculation: Accepts a user-defined currency amount as input and efficiently calculates the required number of coins and notes for each denomination.
Flexibility: Supports various Indian denominations (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1 rupees) and can be adapted to other currencies by modifying the denominations list.
User-Friendly Interface: Employs a simple input function to retrieve the desired amount from the user.
Clear Output: Presents the calculated breakdown of coins and notes in a readable format.
Getting Started:

Clone the repository: git clone https://github.com/<your-username>/coin-note-analysis.git
Run the code: Execute the Python script (e.g., coin_note_analysis.py). You'll be prompted to enter the currency amount.
Observe the results: The code will display the calculated number of coins and notes for each denomination.
Example Usage:

Python
# Assuming the script is named coin_note_analysis.py
amount = int(input("Enter the currency amount: "))

# Function to calculate denominations (replace with your actual implementation)
def calculate_denominations(amount):
  denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]  # Indian denominations
  coins_notes = {denomination: 0 for denomination in denominations}

  for denomination in denominations:
    coins_notes[denomination] = amount // denomination
    amount %= denomination

  return coins_notes

# Calculate and print results
results = calculate_denominations(amount)
for denomination, count in results.items():
  if count > 0:
    print(f"No. of Rs.{denomination} notes/coins: {count}")
Use code with caution.
Additional Notes:

Consider error handling for invalid user input (e.g., negative values).
Explore advanced techniques like dynamic programming for potentially larger amounts.
Feel free to enhance the code's readability with comments and docstrings.

Note: Ensure that you have the necessary dependencies installed. You can install them using the following command:
```bash


pip install tk
Contribution Guidelines
Feel free to contribute to the project by submitting bug reports, feature requests, or directly contributing code through pull requests. Please follow the guidelines in the CONTRIBUTING.md file.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Happy coding!


In this template:

- Each project is described briefly under its respective heading.
- Instructions for running the projects are provided.
- Contribution guidelines and licensing information are mentioned.
- Feel free to customize the template further based on your project-specific details and preferences.
