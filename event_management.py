
#GLOBAL STORAGE 
memberships = {}  
current_user = None
current_role = None

#LOGIN
def login():
    global current_user, current_role

    print("\n=== LOGIN PAGE ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == "admin" and password == "admin123":
        current_user = username
        current_role = "admin"
        print("\nLogin successful as ADMIN")
        return True

    elif username == "user" and password == "user123":
        current_user = username
        current_role = "user"
        print("\nLogin successful as USER")
        return True

    else:
        print("\nInvalid credentials!")
        return False

#MAINTENANCE 
def add_membership():
    print("\n--- Add Membership ---")

    mem_no = input("Membership Number: ").strip()
    name = input("Member Name: ").strip()

    if not mem_no or not name:
        print("All fields are mandatory!")
        return

    print("\nSelect Membership Duration:")
    print("1. 6 Months (Default)")
    print("2. 1 Year")
    print("3. 2 Years")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "2":
        duration = "1 Year"
    elif choice == "3":
        duration = "2 Years"
    else:
        duration = "6 Months"

    memberships[mem_no] = {
        "name": name,
        "duration": duration
    }

    print("Membership added successfully!")

def update_membership():
    print("\n--- Update Membership ---")

    mem_no = input("Enter Membership Number: ").strip()

    if mem_no not in memberships:
        print("Membership not found!")
        return

    name = input("Enter New Member Name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    print("\nSelect New Membership Duration:")
    print("1. 6 Months")
    print("2. 1 Year")
    print("3. 2 Years")

    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "2":
        duration = "1 Year"
    elif choice == "3":
        duration = "2 Years"
    else:
        duration = "6 Months"

    memberships[mem_no] = {
        "name": name,
        "duration": duration
    }

    print("Membership updated successfully!")

def maintenance_menu():
    while True:
        print("\n=== MAINTENANCE MENU (Admin Only) ===")
        print("1. Add Membership")
        print("2. Update Membership")
        print("3. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_membership()
        elif choice == "2":
            update_membership()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

# REPORTS
def reports():
    print("\n=== REPORTS ===")

    if not memberships:
        print("No records available.")
        return

    print("\nMembership Records:")
    for mem_no, data in memberships.items():
        print(f"Membership No: {mem_no}")
        print(f"Name         : {data['name']}")
        print(f"Duration     : {data['duration']}")
        print("-" * 30)

# TRANSACTIONS 
def transactions():
    print("\n=== TRANSACTIONS ===")
    print("Transaction module based on membership data.")
    print(f"Total memberships: {len(memberships)}")

#  MENUS
def admin_menu():
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. Maintenance")
        print("2. Reports")
        print("3. Transactions")
        print("4. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            maintenance_menu()
        elif choice == "2":
            reports()
        elif choice == "3":
            transactions()
        elif choice == "4":
            logout()
            break
        else:
            print("Invalid choice!")

def user_menu():
    while True:
        print("\n=== USER MENU ===")
        print("1. Reports")
        print("2. Transactions")
        print("3. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            reports()
        elif choice == "2":
            transactions()
        elif choice == "3":
            logout()
            break
        else:
            print("❌ Invalid choice!")

#LOGOUT 
def logout():
    global current_user, current_role
    current_user = None
    current_role = None
    print("\n Logged out successfully!")

#  APPLICATION START 
def main():
    print("=== EVENT MANAGEMENT SYSTEM ===")

    if login():
        if current_role == "admin":
            admin_menu()
        else:
            user_menu()

# RUN PROGRAM 
if __name__ == "__main__":
    main()
