# Blood Bank Management System

import mysql.connector as m

def connect_database():
    conn = m.connect(host="localhost", user="root", password="your_password", database="BloodBankDB")
    cursor = conn.cursor()
    return conn, cursor

def register_donor(conn, cursor):
    print("\n--- REGISTER NEW DONOR ---")
    name = input("Enter Donor Name: ")
    bg = input("Enter Blood Group (A+, O-, AB+, etc.): ").upper()
    units = int(input("Enter Units of Blood Donated: "))
    contact = input("Enter Contact Number: ")
    
    print("\nSelect Hospital Location:")
    print("1. Medanta - The Medicity")
    print("2. Fortis Memorial Research Institute")
    print("3. Artemis Hospital")
    print("4. Civil Hospital")
    
    hub_choice = input("Enter Hospital Choice (1-4): ")
    
    hubs = {"1": "Medanta The Medicity", "2": "Fortis Memorial", "3": "Artemis Hospital", "4": "Civil Hospital"}
    selected_hub = hubs.get(hub_choice, "General Medical Depot")

    query = "INSERT INTO donor_registry (donor_name, blood_group, units_available, contact_number, hospital_hub) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, bg, units, contact, selected_hub))
    conn.commit()
    print("Success: Record updated at " + selected_hub + " for donor " + name + ".")

def emergency_match_lookup(cursor):
    print("\n--- SEARCH AVAILABLE BLOOD STOCK ---")
    required_bg = input("Enter Required Blood Group: ").upper()
    
    query = "SELECT donor_name, units_available, contact_number, hospital_hub FROM donor_registry WHERE blood_group = %s"
    cursor.execute(query, (required_bg,))
    records = cursor.fetchall()
    
    print("\n============================================================")
    print("MATCHING DONORS FOR BLOOD GROUP: [" + required_bg + "]")
    print("============================================================")
    
    if not records:
        print("Alert: No blood units available for group " + required_bg + ".")
        return

    print("Donor Name | Available Units | Contact Number | Hospital Location")
    print("-" * 75)
    for row in records:
        print(str(row[0]) + " | " + str(row[1]) + " Units | " + str(row[2]) + " | " + str(row[3]))

def main_menu():
    conn, cursor = connect_database()

    while True:
        print("\n=============================================")
        print("        BLOOD BANK MANAGEMENT SYSTEM        ")
        print("=============================================")
        print("1. Register New Donor")
        print("2. Search for Matching Blood Group")
        print("3. Exit Program")
        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == '1':
            register_donor(conn, cursor)
        elif choice == '2':
            emergency_match_lookup(cursor)
        elif choice == '3':
            print("\nClosing connection. Goodbye!")
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main_menu()
