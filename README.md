Event Management System (Console-Based) – Python
Project Overview

This is a console-based Event Management System developed in Python.
The application follows the given flow chart and functional rules and supports role-based access for Admin and User.

Features

Role-based Login (Admin / User)

Maintenance Module (Admin only)

Add Membership

Update Membership

Reports Module

Transactions Module

Input Validations

Session handling till Logout

Membership duration selection with default option

User Roles & Access
Admin

Access Maintenance

Access Reports

Access Transactions

User

Access Reports

Access Transactions

No access to Maintenance

Login Credentials (for testing)
Admin:
Username: admin
Password: admin123

User:
Username: user
Password: user123

Modules Description
1. Login Module

Authenticates the user based on the username and password

Assigns role (Admin/User)

Maintains the session until logout

2. Maintenance Module (Admin Only)
Add Membership

All fields are mandatory

Membership duration options:

6 Months (Default)

1 Year

2 Years

Only one option can be selected

Update Membership

Membership Number is mandatory

Updates the member's name and duration

3. Reports Module

Displays membership details created in Maintenance

4. Transactions Module

Displays transaction summary based on membership data

Validations

Empty input is not allowed

The membership number must exist for the update

Role-based access is enforced

Technology Used

Language: Python

Type: Console Application

Data Storage: In-memory (Dictionary)

How to Run the Program

Open Command Prompt

Navigate to the project folder

Run the command:

python event_management.py

Conclusion

The application strictly follows the provided flow chart and instructions.
It implements all required modules with proper validations and access control using a simple and clean console-based approach.
