import os
from datetime import datetime, timedelta

# Set the borrowing period for student
# Set the daily penalty
period_stu = 7
period_sta = 21

# File paths for storing data
user_file = 'users.txt'
staff_file = 'staff.txt'
admin_file = 'admin.txt'

# Initialize lists to store data
user_name = []
user_id = []
user_pw = []
staff_name = []
staff_id = []
staff_pw = []
admin_name = []
admin_id = []
admin_pw = []
books = []
reservation = []

def load_data():
    # Load data from user, staff, and admin files into respective lists.
    # Load users
    if os.path.exists('users.txt'):
        with open('users.txt', 'r') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    stu_name, stu_id, stu_pw = line.strip().split(',')
                    user_name.append(stu_name)
                    user_id.append(stu_id)
                    user_pw.append(stu_pw)

    # Load staff
    if os.path.exists('staff.txt'):
        with open('staff.txt', 'r') as file:
            for line in file:
                if line.strip():
                    tc_name, tc_id, tc_pw = line.strip().split(',')
                    staff_name.append(tc_name)
                    staff_id.append(tc_id)
                    staff_pw.append(tc_pw)

    # Load admin
    if os.path.exists('admin.txt'):
        with open('admin.txt', 'r') as file:
            for line in file:
                if line.strip():
                    ad_name, ad_id, ad_pw = line.strip().split(',')
                    admin_name.append(ad_name)
                    admin_id.append(ad_id)
                    admin_pw.append(ad_pw)


def main_menu():
    # Display the main menu and handle user's choice.
    print('''
WELCOME TO UTAR LIBRARY SYSTEM
=====================================================
[1] Login    [2] Registration    [Q] Quit System
    ''')
    option1 = input("Option >> ").strip().upper()
    while option1 not in ['1', '2', 'Q']:
        print("Please enter ONLY 1/2/Q.")
        option1 = input("Option >> ").strip().upper()

    if option1 == '1':
        login_phase()
    elif option1 == '2':
        registration_phase()
    else:
        print("Thank you for using UTAR Library System. Goodbye!")


def login_phase():
    # Handle the login phase for User, Staff, and Admin roles.
    print('''
What role are you?
User [U]    Staff [S]   Admin [A]
    ''')
    role_select = input("Option >>> ").strip().upper()
    while role_select not in ['U', 'S', 'A']:
        print("Please enter ONLY U/S/A.")
        role_select = input("Option >>> ").strip().upper()

    if role_select == 'U':
        user_login(role_select)
    elif role_select == 'S':
        staff_login(role_select)
    else:
        admin_login()


def user_login(role_select):
    # Handle user login.
    stu_id = input("Please enter your user id: ")
    stu_pw = input("Please enter your user password: ")

    if stu_id not in user_id:
        print("Invalid user id. Please try again.")
        main_menu()
    else:
        idx = user_id.index(stu_id)
        if user_pw[idx] == stu_pw:
            print(f'''
====================================================
UTAR Library System (User View) - Main Menu
User: {user_name[idx]}  | User ID: {user_id[idx]}
====================================================
<1> Enter Library

<L> Logout
====================================================
            ''')
            option2 = input("Option>>> ").upper()
            if option2 == '1':
                library_menu(role_select, user_id[idx])
            else:
                print('Log out successfully.')
                main_menu()

        else:
            print("Invalid password. Please try again.")
            main_menu()

def staff_login(role_select):
    # Handle staff login.
    tc_id = input("Please enter your staff id: ")
    tc_pw = input("Please enter your staff password: ")

    if tc_id not in staff_id:
        print("Invalid staff id. Please try again.")
        main_menu()
    else:
        idx = staff_id.index(tc_id)
        if staff_pw[idx] == tc_pw:
            print(f'''
====================================================
UTAR Library System (Staff View) - Main Menu
Staff: {staff_name[idx]}  | Staff ID: {staff_id[idx]}
====================================================
<1> Enter Library System

<L> Logout
====================================================
            ''')
            option2 = input("Option>>> ").upper()
            if option2 == '1':
                library_menu(role_select, staff_id[idx])
            else:
                print('Log out successfully.')
                main_menu()

        else:
            print("Invalid password. Please try again.")
            main_menu()

def admin_login():
    # Handle admin login.
    ad_id = input("Please enter your admin id: ")
    ad_pw = input("Please enter your admin password: ")

    if ad_id not in admin_id:
        print("Invalid admin id. Please try again.")
        main_menu()
    else:
        idx = admin_id.index(ad_id)
        if admin_pw[idx] == ad_pw:
            print(f'''
====================================================
UTAR Library System (Admin View) - Main Menu
Admin ID: {admin_id[idx]}
====================================================
<1> Manage User Profiles
<2> Book Management    
<3> Book Transaction Tracking 

<L> Logout
====================================================
            ''')
            option2 = input("Option>>> ").upper()
            if option2 == '1':
                admin_management()
            elif option2 == '2':
                admin_book_tracking()
            elif option2 == '3':
                admin_book_transaction()
            else:
                print('Log out successfully.')
                main_menu()
        else:
            print("Invalid password. Please try again.")
            main_menu()

def registration_phase():
    # Handle the registration phase for User and Staff.
    print('''
WELCOME TO UTAR LIBRARY SYSTEM - Registration
=====================================================
[1] User    [2] Staff
    ''')
    reg_role = input('Enter your role: ').strip()
    while reg_role not in ['1', '2']:
        print("Error - Please enter ONLY 1 or 2.")
        reg_role = input('Enter your role: ').strip()

    if reg_role == '1':
        user_registration()
    else:
        staff_registration()

def user_registration():
    # Handle user registration.
    stu_name = input('Enter your name: ')
    stu_id = input('Please enter your user id: ')
    stu_pw = input('Please enter new password: ')

    if stu_id in user_id:  # Prevent duplicate IDs
        print("This user ID already exists. Please try again.")
        main_menu()

    with open('users.txt', 'a') as file:
        file.write(f"\n{stu_name},{stu_id},{stu_pw}")
        user_name.append(stu_name)
        user_id.append(stu_id)
        user_pw.append(stu_pw)
        print('-' * 50)
        print(f"User registration successful! Welcome, {stu_name}.")
        print('-' * 50)
        main_menu()


def staff_registration():
    # Handle staff registration.
    tc_name = input('Please enter your staff name: ')
    tc_id = input('Please enter your staff id: ')
    tc_pw = input('Please enter new password: ')

    if tc_id in staff_id:  # Prevent duplicate IDs
        print("This staff ID already exists. Please try again.")
        main_menu()

    with open('staff.txt', 'a') as file:
        file.write(f"\n{tc_name},{tc_id},{tc_pw}")
        staff_name.append(tc_name)
        staff_id.append(tc_id)
        staff_pw.append(tc_pw)
        print('-' * 50)
        print(f'Staff registration is successful! Welcome, {tc_name}.')
        print('-' * 50)
        main_menu()

def load_books():
    global books  # Make sure we are modifying the global books list
    books = []  # Initialize the list to be empty before loading
    try:
        with open('books.txt', 'r') as file:
            for line in file:
                # Split the line into fields and strip any extra spaces
                fields = line.strip().split(',')
                if len(fields) == 8:  # Ensure there are enough fields for a valid book
                    book = {
                        'Book ID': fields[0],
                        'Title': fields[1],
                        'Author': fields[2],
                        'Genre': fields[3],
                        'Publisher': fields[4],
                        'Year': int(fields[5]),
                        'Copies Available': int(fields[6]),
                        'Status': fields[7]
                    }
                    books.append(book)
    except FileNotFoundError:
        print("Error: The books.txt file was not found.")
    except Exception as e:
        print(f"Error: {e}")


def save_books():
    # Save book data to the books file.
    with open('books.txt', 'w') as file:
        for book in books:
            file.write(f"{book['Book ID']},{book['Title']},{book['Author']},{book['Genre']},\
{book['Publisher']},{book['Year']},{book['Copies Available']},{book['Status']}\n")


def library_menu(role_select, identifier):
    # Display the library menu for borrowing and returning books.
    print(f'''
============================================================
UTAR Library System - Main Menu
============================================================
<1> Borrow book
<2> Return book
<3> Search book
<4> Reserve book
<5> View Reservations

<L> Logout
============================================================
    ''')

    action = input("Enter your choice: ").strip().upper()
    while action not in ['1','2','3','4','5','L']:
        print("Error - Please enter ONLY 1/2/3/4/5/L.")
        action = input("Enter your choice: ").strip().upper()
    if action == '1':
        borrow_book(identifier, role_select)
    elif action == '2':
        return_book(role_select)
    elif action == '3':
        user_search_book(role_select, identifier)
    elif action == '4':
        reserve_book(identifier, role_select)
    elif action == '5':
        view_reservations(identifier, role_select)
    else:
        print('Log out successfully.')
        main_menu()


def borrow_book(role_select, identifier):
    # Ensure role_select is valid
    role_select = role_select.strip().upper()
    if role_select not in ['U', 'S']:
        print("Invalid role. Cannot proceed with borrowing. Please check the role and try again.")
        return

    if not books:
        load_books()

    if not books:
        load_books()

    # Display available books
    print("\nAvailable Books:")
    available_books = [book for book in books if book['Copies Available'] > 0]

    if not available_books:
        print("No books are currently available for borrowing.")
        library_menu(role_select, identifier)
        return

    print(f"{'Book ID':<12}{'Title':<50}{'Copies Available':<15}")
    print("-" * 80)
    for book in available_books:
        print(f"{book['Book ID']:<12}{book['Title']:<50}{book['Copies Available']:<15}")

    # Prompt user to select a book
    book_id = input("\nEnter the Book ID you want to borrow (press Enter if do not borrow book): ").strip().upper()
    if book_id == '':
        print("No book borrowed. Returning to library menu.")
        library_menu(role_select, identifier)
        return

    selected_book = next((b for b in books if b['Book ID'] == book_id), None)
    if not selected_book:
        print("Invalid Book ID. Please try again.")
        return

    if int(selected_book['Copies Available']) == 0:
        print("Sorry, this book is currently unavailable.")
        return

    # Link borrower (prompt for Student/Staff ID)
    if role_select == 'U':
        stu_id = input("Enter your Student ID: ").strip()
        if not stu_id:
            print("Student ID cannot be empty. Please try again.")
            return
        borrower_id = stu_id
    elif role_select == 'S':
        tc_id = input("Enter your Staff ID: ").strip()
        if not tc_id:
            print("Staff ID cannot be empty. Please try again.")
            return
        borrower_id = tc_id
    else:
        print("Invalid role. Cannot proceed with borrowing.")
        return

    # Update book details
    selected_book['Copies Available'] -= 1
    selected_book['Status'] = 'borrowed' if selected_book['Copies Available'] == 0 else 'available'
    save_books()

    # Calculate the due date based on role
    borrow_date = datetime.today()
    if role_select == 'U':
        due_date = borrow_date + timedelta(days=period_stu)
    elif role_select == 'S':
        due_date = borrow_date + timedelta(days=period_sta)
    else:
        print("Invalid role. Cannot assign due date.")
        return

    print(f"Borrow Date: {borrow_date.strftime('%d-%m-%Y')}")
    print(f"Due Date: {due_date.strftime('%d-%m-%Y')}")

    # Save borrowing record with specific borrower details
    try:
        with open('borrowed_books.txt', 'a') as file:
            file.write(f"{book_id},{selected_book['Title']},{borrower_id},{role_select},{due_date.strftime('%d-%m-%Y')}\n")
        print(f"You have successfully borrow {selected_book['Title']}!")
        print(f"Due date: {due_date.strftime('%d-%m-%Y')}. Penalty applies for late returns (RM 0.50 per day).")
    except IOError as e:
        print(f"Error in saving borrow record: {e}")

    # Return to library menu
    library_menu(role_select, identifier)


def return_book(role_select):
    # Determine role
    print('''
---------------------------------------
<U> User
<S> Staff
---------------------------------------
    ''')
    role = input("Choose your role to return book >>> ").strip().upper()
    while role not in ['U', 'S']:
        print("Please enter ONLY U/S")
        role = input("Are you a User (U) or Staff (S)? Please enter 'U' or 'S': ").strip().upper()

    # Define file paths
    borrowed_records_path = 'borrowed_books.txt'
    returned_records_path = 'returned_books.txt'
    books_path = 'books.txt'
    reservations_path = 'reservations.txt'

    book_id = input("Enter the Book ID you want to return: ").strip().upper()

    # Check if borrowed_books.txt exists
    if not os.path.exists(borrowed_records_path):
        print("No borrowed records found.")
        return

    # Read borrowed records
    with open(borrowed_records_path, 'r') as file:
        borrowed_records = file.readlines()

    borrow_record = None
    for record in borrowed_records:
        record_parts = record.strip().split(',')
        if len(record_parts) == 5 and record_parts[0] == book_id and record_parts[3] == role:
            borrow_record = record_parts
            break

    if not borrow_record:
        print("No borrowing record found for this book. Please check and try again.")
        return

    # Extract details from the borrowing record
    _, title, borrower_id, _, due_date_str = borrow_record
    try:
        due_date = datetime.strptime(due_date_str, '%d-%m-%Y')
    except ValueError:
        print(f"Invalid due date format in record: {due_date_str}")
        return

    # Get the return date
    return_date_str = input("Please enter the return date (DD-MM-YYYY): ").strip()
    try:
        return_date = datetime.strptime(return_date_str, '%d-%m-%Y')
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return

    # Calculate late days and penalty
    late_days = max(0, (return_date - due_date).days)
    penalty_fee = late_days * 0.50

    if late_days > 0:
        print(f"Returned late by {late_days} days. Penalty fee: RM{penalty_fee:.2f}")
    else:
        print("Returned on time. No penalty.")

    # Read books data
    try:
        with open(books_path, 'r') as file:
            book_lines = file.readlines()

        updated_book_lines = book_lines[:]

    except IOError as e:
        print(f"Error in reading books file: {e}")
        return

    # Automatically assign the book to the first user in the reservation list
    try:
        with open(reservations_path, 'r') as file:
            reservations = file.readlines()

        updated_reservations = []
        next_user = None
        for res in reservations:
            res_parts = res.strip().split('|')
            if len(res_parts) == 4 and res_parts[0] == book_id:
                if not next_user or int(res_parts[3]) < int(next_user[3]):
                    next_user = res_parts
            else:
                updated_reservations.append(res)

        # Remove the specific borrowed record
        with open(borrowed_records_path, 'w') as file:
            for record in borrowed_records:
                if not (record.startswith(book_id) and record.split(',')[2] == borrower_id):
                    file.write(record)

        if next_user:
            # Do NOT update the book count in books.txt, as the book is still unavailable
            # Log the borrowed record for the next user
            try:
                with open(borrowed_records_path, 'a') as file:
                    new_due_date = (return_date + timedelta(days=14)).strftime('%d-%m-%Y')
                    file.write(f"{book_id},{title},{next_user[2]},U,{new_due_date}\n")
                print(f"The book has been automatically borrowed by User ID: {next_user[2]}")

            except IOError as e:
                print(f"Error in updating borrowed_books.txt: {e}")
                return
        else:
            # Update the books.txt to mark the book as available
            try:
                with open(books_path, 'r') as file:
                    book_lines = file.readlines()

                updated_book_lines = []
                for line in book_lines:
                    book_data = line.strip().split(',')
                    if book_data[0] == book_id:
                        book_data[6] = str(int(book_data[6]) + 1)  # Increase available copies
                        book_data[7] = 'available'
                        updated_book_lines.append(','.join(book_data))
                    else:
                        updated_book_lines.append(line.strip())

                with open(books_path, 'w') as file:
                    file.writelines('\n'.join(updated_book_lines) + '\n')

            except IOError as e:
                print(f"Error in updating book: {e}")
                return

            print("No reservations for this book. It is now available.")

        # Update reservations.txt
        with open(reservations_path, 'w') as file:
            file.writelines('\n'.join(updated_reservations))

    except IOError as e:
        print(f"Error in processing reservations: {e}")
        return



    # Log the return in returned_books.txt
    try:
        with open(returned_records_path, 'a') as file:
            file.write(f"\n{book_id},{title},{borrower_id},{role},{due_date.strftime('%d-%m-%Y')},\
    {return_date.strftime('%d-%m-%Y')},{late_days},RM{penalty_fee:.2f}")
    except IOError as e:
        print(f"Error in saving return record: {e}")
        return

def user_search_book(role_select, identifier):
    print('''
==================================================
Book Searching System
==================================================
<1> Search by Book ID
<2> Search by Title
<3> Search by Author
<4> Search by Genre

<B> Back to previous menu
==================================================
        ''')

    option9 = input("Option >>> ").strip().upper()

    while option9 not in ['1', '2', '3', '4', 'B']:
        print("Please select ONLY 1/2/3/4/B.")
        option9 = input("Option >>> ").strip().upper()

    if option9 == 'B':
        library_menu(role_select, identifier)
        return

    # Ensure books are loaded before searching
    load_books()

    query = input("Enter your search query: ").strip()

    # Search based on the selected option
    if option9 == '1':  # Search by Book ID
        results = [book for book in books if book['Book ID'].lower() == query.lower()]
    elif option9 == '2':  # Search by Title
        results = [book for book in books if query.lower() in book['Title'].lower()]
    elif option9 == '3':  # Search by Author
        results = [book for book in books if query.lower() in book['Author'].lower()]
    elif option9 == '4':
        results = [book for book in books if query.lower() in book['Genre'].lower()]
    else:
        results = []

    # Display results
    if results:
        print("\nSearch Results:")
        print(f"{'Book ID':<12}{'Title':<50}{'Author':<25}{'Genre':<20}{'Copies Available':<20}{'Status':<12}")
        print("-" * 150)

        for book in results:
            print(f"{book['Book ID']:<12}{book['Title']:<50}{book['Author']:<25}{book['Genre']:<27}\
    {book['Copies Available']:<13}{book['Status']:<12}")

    else:
        print("\nNo books found matching your search query.")

    print()  # Blank line for better formatting
    library_menu(role_select, identifier)


def staff_search_book():
    print('''
    ==================================================
    Book Searching System
    ==================================================
    <1> Search by Book ID
    <2> Search by Title
    <3> Search by Author
    <4> Search by Genre

    <B> Back to previous menu
    ==================================================
        ''')

    option9 = input("Option >>> ").strip().upper()

    while option9 not in ['1', '2', '3', '4', 'B']:
        print("Please select ONLY 1/2/3/4/B.")
        option9 = input("Option >>> ").strip().upper()

    if option9 == 'B':
        library_menu(role_select='S')

    # Ensure books are loaded before searching
    load_books()

    query = input("Enter your search query: ").strip()

    # Search based on the selected option
    if option9 == '1':  # Search by Book ID
        results = [book for book in books if book['Book ID'].lower() == query.lower()]
    elif option9 == '2':  # Search by Title
        results = [book for book in books if query.lower() in book['Title'].lower()]
    elif option9 == '3':  # Search by Author
        results = [book for book in books if query.lower() in book['Author'].lower()]
    elif option9 == '4':
        results = [book for book in books if query.lower() in book['Genre'].lower()]
    else:
        results = []

    # Display results
    if results:
        print("\nSearch Results:")
        print(f"{'Book ID':<12}{'Title':<50}{'Author':<25}{'Genre':<20}{'Copies Available':<20}{'Status':<12}")
        print("-" * 150)

        for book in results:
            print(f"{book['Book ID']:<12}{book['Title']:<50}{book['Author']:<25}{book['Genre']:<27}\
    {book['Copies Available']:<13}{book['Status']:<12}")

    else:
        print("\nNo books found matching your search query.")

    print()  # Blank line for better formatting
    library_menu(role_select='S')


def admin_management():
    print('''
==================================================
Manage User and Staff Profiles
==================================================
<1> View All Users and Staff
<2> Add User or staff
<3> Edit User or staff
<4> Delete User or staff

<L> Logout
==================================================
    ''')
    option3 = input("Option >>> ").strip().upper()
    while option3 not in ['1', '2', '3', '4', 'L']:
        print('Please enter ONLY 1/2/3/4/L.')
        option3 = input("Option >>> ").strip().upper()
    if option3 == '1':
        view_user_staff1()
    elif option3 == '2':
        add_user_staff1()
    elif option3 == '3':
        edit_user_staff1()
    elif option3 == '4':
        dlt_user_staff1()
    else:
        print('Log out successfully.')
        main_menu()

def view_user_staff1():
    print('''
==================================================
All Registered Users:
==================================================
    ''')

    # Display all users
    if user_id:   # Check if user data is available
        print(f"{'Name':<15}{'User ID':<15}{'Password':<15}")
        print('-' * 50, end = ' ')
        for name, uid, pw in zip(user_name, user_id, user_pw):
            print(f"\n{name:<15}{uid:<15}{pw:<15}")
    else:
        print("No users registered.")

    print('''\n
==================================================
All Registered Staff:
==================================================
    ''')

    # Display all staff
    if staff_id:  # Check if staff data is available
        print(f"{'Name':<15}{'Staff ID':<15}{'Password':<15}")
        print('-' * 50, end = ' ')
        for name, sid, pw in zip(staff_name, staff_id, staff_pw):
            print(f"\n{name:<15}{sid:<15}{pw:<15}")
    else:
        print("No staff registered.")

    print('='*50, end = ' ')
    print('\n')
    admin_management()

def add_user_staff1():
    print('''
==================================================
Add User or Staff
==================================================
<1> Add User
<2> Add Staff

<B> Back to Previous Menu
==================================================
    ''')

    option4 = input("Option >>> ").strip().upper()
    while option4 not in ['1', '2', 'B']:
        print("Error - Please enter ONLY 1/2/B.")
        option4 = input("Option >>> ").strip().upper()

    if option4 == '1':  # Add User
        stu_name = input('Enter user name: ').strip()
        stu_id = input('Enter user ID: ').strip()
        stu_pw = input('Enter user password: ').strip()

        if stu_id in user_id:  # Prevent duplicate IDs
            print("This user ID already exists. Please try again.")
            admin_management()
        else:
            with open(user_file, 'a') as file:
                file.write(f"\n{stu_name},{stu_id},{stu_pw}")
            user_name.append(stu_name)
            user_id.append(stu_id)
            user_pw.append(stu_pw)
            print(f"User {stu_name} has been added successfully!\n")
            admin_management()

    elif option4 == '2':  # Add Staff
        tc_name = input('Enter staff name: ').strip()
        tc_id = input('Enter staff ID: ').strip()
        tc_pw = input('Enter staff password: ').strip()

        if tc_id in staff_id:  # Prevent duplicate IDs
            print("This user ID already exists. Please try again.")
            admin_management()
        else:
            with open(staff_file, 'a') as file:
                file.write(f"\n{tc_name},{tc_id},{tc_pw}")
            user_name.append(tc_name)
            user_id.append(tc_id)
            user_pw.append(tc_pw)
            print(f"User {tc_name} has been added successfully!\n")
            admin_management()

def edit_user_staff1():
    print('''
==================================================
Edit User or Staff Information
==================================================
<1> Edit User
<2> Edit Staff

<B> Back to Previous Menu
==================================================
    ''')
    option5 = input("Option >>> ").strip().upper()
    while option5 not in ['1', '2', 'B']:
        print("Error - Please enter ONLY 1/2/B.")
        option5 = input("Option >>> ").strip().upper()

    if option5 == '1':
        edit_user1a()
    elif option5 == '2':
        edit_staff1b()
    else:
        admin_management()

def edit_user1a():
    print('''
==================================================
Edit User Information
==================================================
''')
    user_view = input('Display users information? (Y/N) >>> ')
    while user_view not in ['Y','N']:
        print("Please enter ONLY Y or N.")
        user_view = input('Display the users information? (Y/N) >>> ')
    if user_view == 'Y':
        view_user_staff1()
        edit_user_staff1()
    else:
        stu_id = input('Enter the User ID of the user you want to edit: ').strip()
        if stu_id not in user_id:
            print("This User ID does not exist. Please check and try again.")
            return admin_management()

    # Get the index of the user to be edited
    idx = user_id.index(stu_id)

    print(f'''
Current Details:
Name: {user_name[idx]}
User ID: {user_id[idx]}
User Password: {user_pw[idx]}
    ''')

    # Prompt for new details
    new_name = input('Enter new name (press Enter to keep unchanged): ').strip()
    new_password = input('Enter new password (press Enter to keep unchanged): ').strip()

    # Update details
    user_name[idx] = new_name if new_name else user_name[idx]
    user_pw[idx] = new_password if new_password else user_pw[idx]

    # Save updated details to the file
    with open(user_file, 'w') as file:
        for name, uid, pw in zip(user_name, user_id, user_pw):
            file.write(f"{name},{uid},{pw}\n")

    print("User details have been successfully updated!")
    admin_management()


def edit_staff1b():
    print('''
==================================================
Edit Staff Information
==================================================
''')

    staff_view = input('Display the staff information? (Y/N) >>> ')
    while staff_view not in ['Y','N']:
        print("Please enter ONLY Y or N.")
        staff_view = input('Display staff information? (Y/N) >>> ')
    if staff_view == 'Y':
        view_user_staff1()
    else:
        tc_id = input('Enter the Staff ID of the staff you want to edit: ').strip()
        if tc_id not in staff_id:
            print("This Staff ID does not exist. Please check and try again.")
            return admin_management()

    # Get the index of the staff to be edited
    idx = staff_id.index(tc_id)

    print(f'''
Current Details:
Name: {staff_name[idx]}
Staff ID: {staff_id[idx]}
Staff Password: {staff_pw[idx]}''')

    # Prompt for new details
    new_name = input('Enter new name (press Enter to keep unchanged): ').strip()
    new_password = input('Enter new password (press Enter to keep unchanged): ').strip()

    # Update details
    staff_name[idx] = new_name if new_name else staff_name[idx]
    staff_pw[idx] = new_password if new_password else staff_pw[idx]

    # Save updated details to the file
    with open(staff_file, 'w') as file:
        for name, sid, pw in zip(staff_name, staff_id, staff_pw):
            file.write(f"{name},{sid},{pw}\n")

    print("Staff details have been successfully updated!")
    admin_management()

def dlt_user_staff1():
    print('''
==================================================
Delete User or Staff
==================================================
<1> Delete User
<2> Delete Staff

<B> Back to Previous Menu
==================================================
    ''')
    option6 = input("Option >>> ").strip().upper()
    while option6 not in ['1', '2', 'B']:
        print("Error - Please enter ONLY 1/2/B.")
        option6 = input("Option >>> ").strip().upper()

    if option6 == '1':  # Delete User
        user_id_to_delete = input('Enter the User ID of the user to delete: ').strip()
        if user_id_to_delete not in user_id:
            print("This User ID does not exist. Please check and try again.")
            return admin_management()
        else:
            # Remove user from lists
            idx = user_id.index(user_id_to_delete)
            del user_name[idx]
            del user_id[idx]
            del user_pw[idx]

            # Save updated list to file
            with open(user_file, 'w') as file:
                for name, uid, pw in zip(user_name, user_id, user_pw):
                    file.write(f"{name},{uid},{pw}\n")
            print(f"User with ID {user_id_to_delete} has been deleted.")
            admin_management()


    elif option6 == '2':  # Delete Staff
        staff_id_to_delete = input('Enter the Staff ID of the staff to delete: ').strip()
        if staff_id_to_delete not in staff_id:
            print("This Staff ID does not exist. Please check and try again.")
            return admin_management()
        else:
            # Remove staff from lists
            idx = staff_id.index(staff_id_to_delete)
            del staff_name[idx]
            del staff_id[idx]
            del staff_pw[idx]

            # Save updated list to file
            with open(staff_file, 'w') as file:
                for name, sid, pw in zip(staff_name, staff_id, staff_pw):
                    file.write(f"{name},{sid},{pw}\n")
            print(f"Staff with ID {staff_id_to_delete} has been deleted.")
            admin_management()

    else:
        admin_management()

def admin_book_tracking():
    print('''
==================================================
Manage Book Records
==================================================
<1> View All Books
<2> Add New Book
<3> Edit Book
<4> Delete Book

<L> Logout
==================================================
    ''')
    option7 = input("Option >>> ").strip().upper()
    while option7 not in ['1', '2', '3', '4', 'L']:
        print("Please enter ONLY 1/2/3/4/L.")
        option7 = input("Option >>> ").strip().upper()

    if option7 == '1':
        view_books2()
    elif option7 == '2':
        add_book2()
    elif option7 == '3':
        edit_book2()
    elif option7 == '4':
        dlt_book2()
    else:
        main_menu()

def view_books2():
    print('''
==================================================
All Books in the Library
==================================================
    ''')

# Reload books from the file to ensure up-to-date data
    if not books:
        load_books()
    book_list = [book for book in books if book['Copies Available'] >= 0]
    for book in book_list:
        print(f"{book['Book ID']} - {book['Title']} (Copies Available: {book['Copies Available']})")


    print('=' * 70)
    print()
    admin_book_tracking()


def add_book2():
    print('''
==================================================
Add a New Book
==================================================
    ''')

    load_books()  # Ensure that books are loaded first before adding a new book
    book_id = input("Enter Book ID: ").strip()
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    genre = input("Enter Genre: ").strip()
    publisher = input("Enter Publisher: ").strip()
    year = input("Enter Year of Publication: ").strip()
    copies = input("Enter Number of Copies Available: ").strip()
    status = input("Enter Status (Available/Unavailable): ").strip()

    # Check for duplicate Book ID.
    for book in books:
        if book['Book ID'] == book_id:
            print("This Book ID already exists. Please try again.")
            admin_book_tracking()

    # Append the new book
    books.append({
        'Book ID': book_id,
        'Title': title,
        'Author': author,
        'Genre': genre,
        'Publisher': publisher,
        'Year': int(year),
        'Copies Available': int(copies),
        'Status': status
    })

    # Save to file.
    save_books()  # This will save the updated list to the file
    print(f"Book {title} has been added successfully!\n")
    admin_book_tracking()

def edit_book2():
    print('''
==================================================
Edit Book Details
==================================================
    ''')

    load_books()  # Ensure that books are loaded first before editing a book

    book_id = input("Enter the Book ID to edit: ").strip()

    # Check if the book exists
    found = False
    for book in books:
        if book['Book ID'] == book_id:
            found = True
            # Show current details and allow editing
            print(f"Current details of the book {book_id}:")
            print(f"Title: {book['Title']}")
            print(f"Author: {book['Author']}")
            print(f"Genre: {book['Genre']}")
            print(f"Publisher: {book['Publisher']}")
            print(f"Year: {book['Year']}")
            print(f"Copies Available: {book['Copies Available']}")
            print(f"Status: {book['Status']}")

            # Allow editing of each field
            book['Title'] = input("Enter new Title (press Enter to keep unchanged): ").strip() or book['Title']
            book['Author'] = input("Enter new Author (press Enter to keep unchanged): ").strip() or book[
                'Author']
            book['Genre'] = input("Enter new Genre (press Enter to keep unchanged): ").strip() or book['Genre']
            book['Publisher'] = input("Enter new Publisher (press Enter to keep unchanged): ").strip() or \
                                book['Publisher']
            book['Year'] = input("Enter new Year (press Enter to keep unchanged): ").strip() or str(book['Year'])
            book['Copies Available'] = input("Enter new Copies Available \
(press Enter to keep unchanged): ").strip() or str(book['Copies Available'])
            book['Status'] = input("Enter new Status (press Enter to keep unchanged): ").strip() or book['Status']

            # Save updated books list to file
            save_books()  # This saves the modified books list
            print(f"Book {book_id} has been successfully updated.\n")
            admin_book_tracking()
            break

    if not found:
        print(f"Book ID {book_id} not found. Please check and try again.\n")
        admin_book_tracking()

def dlt_book2():
    print(''' 
    ==================================================
    Delete a Book
    ==================================================
    ''')
    load_books()  # Ensure books are loaded before deletion
    book_id = input("Enter the Book ID to delete: ").strip()

    found = False  # Flag to check if the book was found
    for book in books:
        if book['Book ID'] == book_id:
            books.remove(book)
            save_books()
            print(f"Book {book_id} has been deleted.\n")
            found = True
            break  # Exit the loop once the book is deleted

    if not found:
        print("Book ID not found. Please check and try again.\n")
    admin_book_tracking()

def admin_book_transaction():
    print('''
==================================================
Manage Book Transactions
==================================================
<1> View Book Borrowing Record
<2> View Book Returning Record
<3> Book Searching

<L> Logout
==================================================
    ''')
    option8 = input("Option >>> ").strip().upper()

    while option8 not in ['1', '2', '3', 'L']:
        print("Please enter ONLY 1/2/3/L.")
        option8 = input("Option >>> ").strip().upper()

    if option8 == '1':
        borrowed_record3()
    elif option8 == '2':
        returned_record3()
    elif option8 == '3':
        admin_search_book()
    else:
        main_menu()  # Logout or return to the main menu

def borrowed_record3():
    borrowed_records_path = 'borrowed_books.txt'

    print("\n==================================================")
    print("Borrowed Book Records")
    print("==================================================")

    # Check if borrowed_books.txt exists
    if not os.path.exists(borrowed_records_path):
        print("No borrowed book records found.")
        admin_book_transaction()

    # Read and display borrowed book records
    try:
        with open(borrowed_records_path, 'r') as file:
            borrowed_records = file.readlines()

        if not borrowed_records:
            print("No borrowed book records found.")
            admin_book_transaction()
        else:
            print(f"{'Book ID':<12}{'Title':<50}{'Borrower ID':<20}{'Role':<10}{'Due Date':<15}")
            print("-" * 110)
            for record in borrowed_records:
                record_parts = record.strip().split(',')
                if len(record_parts) == 5:
                    book_id, title, borrower_id, role, due_date = record_parts
                    print(f"{book_id:<12}{title:<50}{borrower_id:<20}{role:<10}{due_date:<15}")
            admin_book_transaction()
    except IOError as e:
        print(f"Error reading borrowed book records: {e}")

def returned_record3():
    returned_records_path = 'returned_books.txt'

    print("\n==================================================")
    print("Returned Book Records")
    print("==================================================")

    # Check if returned_books.txt exists
    if not os.path.exists(returned_records_path):
        print("No returned book records found.")
        admin_book_transaction()
        return

    # Read and display returned book records
    try:
        with open(returned_records_path, 'r') as file:
            returned_records = file.readlines()

        if not returned_records:
            print("No returned book records found.")
            admin_book_transaction()
        else:
            print(f"{'Book ID':<12}{'Title':<50}{'Borrower ID':<20}{'Role':<10}{'Due Date':<15}{'Return Date':<15} \
{'Late Days':<15}{'Penalty Fee':<15}")
            print("-" * 150)
            for record in returned_records:
                record_parts = record.strip().split(',')
                if len(record_parts) == 8:
                    book_id, title, borrower_id, role, due_date, return_date, late_days, penalty_fee = record_parts
                    print(f"{book_id:<12}{title:<50}{borrower_id:<20}{role:<10}{due_date:<15}{return_date:<15} \
{late_days:<15}{penalty_fee:<15}")
            admin_book_transaction()
    except IOError as e:
        print(f"Error reading returned book records: {e}")

def admin_search_book():
    print('''
==================================================
Book Searching System
==================================================
<1> Search by Book ID
<2> Search by Title
<3> Search by Author
<4> Search by Genre

<B> Back to previous menu
==================================================
    ''')

    option9 = input("Option >>> ").strip().upper()

    while option9 not in ['1', '2', '3', '4', 'B']:
        print("Please select ONLY 1/2/3/4/B.")
        option9 = input("Option >>> ").strip().upper()

    if option9 == 'B':
        admin_book_transaction()

    # Ensure books are loaded before searching
    load_books()

    query = input("Enter your search query: ").strip()


    # Search based on the selected option
    if option9 == '1':  # Search by Book ID
        results = [book for book in books if book['Book ID'].lower() == query.lower()]
    elif option9 == '2':  # Search by Title
        results = [book for book in books if query.lower() in book['Title'].lower()]
    elif option9 == '3':  # Search by Author
        results = [book for book in books if query.lower() in book['Author'].lower()]
    elif option9 == '4':
        results = [book for book in books if query.lower() in book['Genre'].lower()]
    else:
        results = []

    # Display results
    if results:
        print("\nSearch Results:")
        print(f"{'Book ID':<12}{'Title':<50}{'Author':<25}{'Genre':<20}{'Copies Available':<20}{'Status':<12}")
        print("-" * 150)

        for book in results:
            print(f"{book['Book ID']:<12}{book['Title']:<50}{book['Author']:<25}{book['Genre']:<27}\
{book['Copies Available']:<13}{book['Status']:<12}")

    else:
        print("\nNo books found matching your search query.")

    print()  # Blank line for better formatting
    admin_book_transaction()


def load_reservations():
    # Load reservation data from a text file.
    reservations = []
    try:
        with open("reservations.txt", "r") as file:
            for line in file:
                book_id, identifier, role_select, order = line.strip().split("|")
                reservations.append({"Book ID": book_id, "Identifier": identifier, "ID": role_select, "Order": int(order)})
    except FileNotFoundError:
        # If the file doesn't exist, no reservations are loaded
        pass
    return reservations


def save_reservations(reservations):
    # Save reservation data to a text file.
    with open("reservations.txt", "w") as file:
        for res in reservations:
            file.write(f"{res['Book ID']}|{res['Identifier']}|{res['ID']}|{res['Order']}\n")


def reserve_book(identifier,role_select):
    # Allow users to reserve a book.
    load_books()
    reservations = load_reservations()

    book_id = input("Enter the Book ID you want to reserve: ").strip()

    # Check if the book exists
    book = next((b for b in books if b["Book ID"] == book_id), None)
    if not book:
        print("Book not found.")
        return

    # Check if the book is available
    if int(book["Copies Available"]) > 0 and book["Status"].lower() == "available":
        print("The book is available and does not need to be reserved.")
        return

    # Check if the user already has a reservation
    if any(res for res in reservations if res["Book ID"] == book_id and res["ID"] == role_select):
        print("You have already reserved this book.")
        return

    # Add the reservation
    reservation_order = len([res for res in reservations if res["Book ID"] == book_id]) + 1
    reservations.append({"Book ID": book_id, "Identifier": identifier, "ID": role_select, "Order": reservation_order})
    save_reservations(reservations)

    # Change the book status from 'borrowed' to 'reserved'
    for book in books:
        if book["Book ID"] == book_id:
            book["Status"] = "reserved"
            break

    # Save the updated book list after changing status
    save_books()

    print(f"Reservation added successfully. You are number {reservation_order} in the queue. The book status is now 'reserved'.")

def notify_user(book_id):
    # Notify the next user in the reservation queue when a book becomes available.
    reservations = load_reservations()

    # Find the first user in the queue
    queue = [res for res in reservations if res["Book ID"] == book_id]
    if not queue:
        # No one is in the queue
        return

    # Notify the first user
    first_reservation = sorted(queue, key=lambda x: x["Order"])[0]
    print(f"Notification: {first_reservation['Role']} {first_reservation['Identifier']}, the book (ID: {book_id}) is now available.")

    # Remove the user from the queue
    reservations.remove(first_reservation)
    save_reservations(reservations)


def view_reservations(identifier, role_select):
    reservations = load_reservations()
    user_reservations = [res for res in reservations if res["Identifier"] == identifier and res["ID"] == role_select]

    if not user_reservations:
        print("You have no active reservations.")
        return

    print("\nYour Reservations:")
    print('-'*30)
    print(f"{'Book ID':<10}{'Queue Position':<15}")
    for res in sorted(user_reservations, key=lambda x: x["Order"]):
        print(f"{res['Book ID']:<10}{res['Order']:<15}")

# Main program execution
if __name__ == "__main__":
    load_data()
    main_menu()
    load_books()