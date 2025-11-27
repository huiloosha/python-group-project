import json
import sys

# Initialize user data with default values
user_dict = {"admins": [["admin", "admin"]], "operators": [["operator", "operator"]]}

# File name for storing user data
user_data_file = "userlist.txt"

# Load user data from a file or initialize with default values
def create_userlist():
    try:
        with open(user_data_file, "r") as file:
            user_data = json.load(file)
            return user_data
    except FileNotFoundError:
        # Initialize with default values if the file is not found
        return user_dict

# Save user data to a file
def save_data():
    with open(user_data_file, "w") as file:
        json.dump(user_dict, file)
        
user_dict = create_userlist()
admin_list = user_dict["admins"]
operator_list = user_dict["operators"]

##########################################


# File name for storing pricetable data
pricetable_file = "pricetable.txt"

# Initialize pricetable with default values
pricetable = {
    "below1kg": {
        "ZoneA": 8.00,
        "ZoneB": 9.00,
        "ZoneC": 10.00,
        "ZoneD": 11.00,
        "ZoneE": 12.00},
    "1kgto3kg": {
        "ZoneA": 16.00,
        "ZoneB": 18.00,
        "ZoneC": 20.00,
        "ZoneD": 22.00,
        "ZoneE": 22.00},
    "over3kg": {
        "ZoneA": 0.0,
        "ZoneB": 0.0,
        "ZoneC": 0.0,
        "ZoneD": 0.0,
        "ZoneE": 0.0}  #added placeholder for over3kg
        }


# Load pricetable data from a file or initialize with default values
def create_pricetable():
    try:
        with open(pricetable_file, "r") as file:
            pricetable_data = json.load(file)
            return pricetable_data
    except FileNotFoundError:
        # Initialize with default values if the file is not found
        return pricetable

# Save pricetable data to a file
def save_pricetable():
    with open(pricetable_file, "w") as file:
        json.dump(pricetable, file)


# Beginning of the program
pricetable = create_pricetable()

zones = ["ZoneA", "ZoneB", "ZoneC", "ZoneD", "ZoneE"]


# File paths
customer_file_name = "customers.txt"
parcel_file_name = "parcels.txt"
bills_file_name = "bills.txt"
parcel_number_file_path = "parcel_number.txt"


def create_bill_file():
    try:
        with open(bills_file_name, "r") as bill_file:
            pass  # File exists, do nothing
    except FileNotFoundError:
        # File doesn"t exist, create an empty bill file
        with open(bills_file_name, "w") as bill_file:
            empty_bill = [10000000]
            json.dump(empty_bill, bill_file)


# Checking if "parcels.txt" exists
def create_parcels_file():
    # Initializing parcels list
    parcels = []
    try:
        # Opening the "parcels.txt" file
        with open(parcel_file_name, "r") as parcel_file:
            try:
                # Loading parcels from the file
                parcels = json.load(parcel_file)
            except json.JSONDecodeError:
                # Handling JSON decoding error, possibly due to an empty file
               
                print("Empty or invalid parcels.txt. Initializing with an empty list.")
    except FileNotFoundError:
        pass  # File doesn"t exist yet
    
    # If the loaded data is not a list or "parcels.txt" doesn"t exist, initialize parcels as an empty list
    if not isinstance(parcels, list):
        parcels = []
    
    # Create "parcels.txt" if it doesn"t exist
    try:
        with open(parcel_file_name, "r"):
            pass  # File exists, do nothing
    except FileNotFoundError:
        with open(parcel_file_name, "w") as parcel_file:
            json.dump(parcels, parcel_file)

# Sample customer data structure
customers = []  # Initialize as an empty list
last_customer_id = 10000000  # Initialize with a starting value
last_parcel_num = 1  # Initialize with a starting value
price_table = {
    "A": {"1": 8.00, "3": 16.00},
    "B": {"1": 9.00, "3": 18.00},
    "C": {"1": 10.00, "3": 20.00},
    "D": {"1": 11.00, "3": 22.00},
    "E": {"1": 12.00, "3": 24.00},
}










#Administrator code
def admin_code():
    
    #Add new user
    def add_user():
        newlogin=input("Enter new login to add user: ").lower()
        newpassword=input("Enter new password to add user: ").lower()
        for user in operator_list:
          if user[0] == newlogin:
              print("-----------------------------------------------------------------")
              print("User already exists.")
              admin_menu()
              return
       
    
        operator_list.append([newlogin,newpassword])
        print("-----------------------------------------------------------------")
        print("The user was succesfully added")
        user_dict["operators"] = operator_list
        save_data()
        admin_menu()
        
    
    
    
                
    #Thank you
    def bye():
        print("-----------------------------------------------------------------")
        print("Thank You! Bye!")           
  
  
#Assign Admin
    def assign_admin():
        match="False"
        while match=="False":
            ans="Invalid"
            username=input("Enter the login: ")
            for user in operator_list:
                if user[0]==username:
                    admin_list.append(user)
                    operator_list.remove(user)
                    match="True"
                    break
                    
            if match=="True":
                print("-----------------------------------------------------------------")
                print("Yay! Admin was successfully assigned!")
                user_dict["admins"] = admin_list
                user_dict["operators"] = operator_list
                save_data()
                
            elif match=="False":
                while ans=="Invalid":
                    again=input("User was not found.Do you want to try again?(yes/no): ").lower()
                    if again=="no":
                        match="True"
                        ans="Valid"
                    elif again=="yes":
                        ans="Valid"
            
        admin_menu()
        
                
                
#Remove administrator
    def remove_admin():
        match = "False"
        ans = "Valid"
        username = input("Enter the login: ")
        for acc in admin_list:
            if acc[0] == username:
                match = "True"
                break
        if match == "True":
            confirm = input("Administrator was found. Are you sure you want to remove the administrator? (yes/no): ").lower()
            if confirm == "yes":
                operator_list.append(acc)
                admin_list.remove(acc)
                print("-----------------------------------------------------------------")
                print("The administrator was removed")
                user_dict["admins"] = admin_list
                user_dict["operators"] = operator_list
                save_data()
            else:
                print("-----------------------------------------------------------------")
                print("Removal canceled.")
                
        if match == "False":
            while ans == "Valid":
                again = input("Administrator was not found. Do you want to try again? (yes/no): ").lower()
                if again == "no":
                    match = "True"
                    ans = "Invalid"
                if again == "yes":
                    ans = "Invalid"
        admin_menu()
    
#Delete user
    def del_user():
        ans = "Valid"
        match = "False"
        username = input("Enter the login: ").lower()
        if username=="admin":
            print("-----------------------------------------------------------------")
            print("The user can't be deleted.")
            admin_menu()
        for x in admin_list:
            if x[0] == username:
                match = "True"
                break
        for y in operator_list:
            if y[0] == username:
                match = "True"
                break
        if match == "True":
            confirm = input("User was found. Are you sure you want to delete the user? (yes/no): ").lower()
            if confirm == "yes":
                for x in admin_list:
                    if x[0] == username:
                        admin_list.remove(x)
                        print("-----------------------------------------------------------------")
                        print("The user was deleted")
                        user_dict["admins"] = admin_list
                        user_dict["operators"] = operator_list
                        save_data()
                        break
                for y in operator_list:
                    if y[0] == username:
                        operator_list.remove(y)
                        print("-----------------------------------------------------------------")
                        print("The user was deleted")
                        user_dict["admins"] = admin_list
                        user_dict["operators"] = operator_list
                        save_data()
                        break
            else:
                print("-----------------------------------------------------------------")
                print("Deletion canceled.")
                
        if match == "False":
            while ans == "Valid":
                again = input("User was not found. Do you want to try again? (yes/no): ").lower()
                if again == "no":
                    match = "True"
                    ans = "Invalid"
                if again == "yes":
                    ans = "Invalid"
        admin_menu()
        
    
#View the list of users
    def view_list():
        s="False"
        while s=="False":
            final=input("Which list of users you would like to view?(all/operator/admin):")
            if final=="all":
                s="True"
                print("-----------------------------------------------------------------")
                print("List of all users:")
                print("\n")
                print(*operator_list,sep="\n")
                print(*admin_list,sep="\n")
            elif final=="admin":
                s="True"
                print("-----------------------------------------------------------------")
                print("Administrator list:")
                print("\n")
                print(*admin_list,sep="\n")
            elif final=="operator":
                s="True"
                print("-----------------------------------------------------------------")
                print("Operator list:")
                print("\n")
                print(*operator_list,sep="\n")
        admin_menu()
        
#####################################################################


    # add price to table over 3kg
    def add_price_over3kg():
        zones = ["ZoneA", "ZoneB", "ZoneC", "ZoneD", "ZoneE"]
        zone=input("Input zone:").upper()
        zone="Zone"+zone
        if zone in zones:
            price = float(input(f"Enter the price for {zone}: "))
            if price==0.00:
                print("-------------------------------------------------------------------------------")
                print("Hmmmm, are you sure you want to make the delivery free and be broke? I don't agree with you:(")
            else:
                if pricetable["over3kg"][zone]==0.00:
                    pricetable["over3kg"][zone] = price
                    save_pricetable()
                    print("-----------------------------------------------------------------")
                    print("Updated pricetable:")
                    print(pricetable)
                else:
                    print("-----------------------------------------------------------------------------------")
                    print("The price for this zone was already added. Please use modify to change the price:) ")
        else:
            print("-----------------------------------------------------------------")
            print("Invalid zone. Please try again.")
        admin_menu()

        
    
    # modify the price of parcel that is over 3kg
    def modify_price(zone,new_price):
        if zone in zones:
            pricetable["over3kg"][zone] = new_price
            save_pricetable()
            print("-----------------------------------------------------------------")
            print(f"Price modified for {zone} : {new_price:.2f}RM")
            print("-----------------------------------------------------------------")
        else:
            print("-----------------------------------------------------------------")
            print("Invalid zone. Can not modify price.")
        admin_menu()
            
        
    
    # delete the price of table that is over 3kg
    def delete_price(zone):
        if zone in zones:
            pricetable["over3kg"][zone]=0.0
            save_pricetable()
            print("-----------------------------------------------------------------")
            print(f"Price deleted for {zone} - over3kg")
        else:
            print("-----------------------------------------------------------------")
            print("Invalid zone. Can not delete price.")
        admin_menu()
            
        
    
    # function checks the price of a parcel based on its destination and weight
    def check_price(weight, zone):
        if zone in zones:
            if weight < 1.0:
                price = pricetable["below1kg"].get(zone, 0.0)
                print("-----------------------------------------------------------------")
                print(f"The price for {zone} - {weight}kg is: {price:.2f}RM")
                print("-----------------------------------------------------------------")
            elif 1.0 <= weight < 3.0:
                price = pricetable["1kgto3kg"].get(zone, 0.0)
                print("-----------------------------------------------------------------")
                print(f"The price for {zone} - {weight}kg is: {price:.2f}RM")
                print("-----------------------------------------------------------------")
            elif 3.0 <= weight:
                price = pricetable["over3kg"].get(zone, 0.0)           
                print("-----------------------------------------------------------------")
                print(f"The price for {zone} - {weight}kg is: {price:.2f}RM")
                print("-----------------------------------------------------------------")
            else:
                print("-----------------------------------------------------------------")
                print("Invalid weight or zone. Can not check price.")
                return 0.0
        else:
            print("-----------------------------------------------------------------")
            print("Invalid zone. Can not check price.")
            return 0.0
        admin_menu()
        
    
    # view all the price for all destination and weight
    def view_all_prices():
        for destination, prices in pricetable.items():
            print("-----------------------------------------------------------------")
            print(f"{destination}:")
            for weight, price in prices.items():
                print(f"{weight}: {price:.2f}RM")
        admin_menu()
        
                        
        
    def admin_menu ():
        choice="False"
        while choice=="False":
            create_userlist()
            create_pricetable()
            print("\n")
            print("----------MENU----------")
            print("a.Add user")
            print("b.Assign Administrator")
            print("c.Remove Administrator")
            print("d.Delete User")
            print("e.View List of Users")
            print("f.Add price for a parcel over 3kg")
            print("g.Modify Price(parcel>3kg) ")
            print("h.Delete price(parcel>3kg)")
            print("i.Check price")
            print("j.View all prices")
            print("k.Go back to the Welcome page")
            print("l.Exit")
            print("-----------------------------------------------------")
            choice=input("Which function you would like to call?(a-l): ").lower()
            if choice=="a":
                add_user()
            elif choice=="b":
                assign_admin()
            elif choice=="c":
                remove_admin()
            elif choice=="d":
                del_user()
            elif choice=="e":
                view_list()

            elif choice == "f":
                add_price_over3kg()
            elif choice == "g":
                zone = input("Input zone: ").upper()
                zone = "Zone"+zone
                new_price = float(input("Input new price: "))
                modify_price(zone,new_price)
            elif choice == "h":
                 zone = input("Input zone: ").upper()
                 zone = "Zone"+zone
                 delete_price(zone)
            elif choice == "i":
                 zone = input("Input zone: ").upper()
                 zone = "Zone"+zone
                 weight = float(input("Input weight: "))
                 check_price(weight, zone)
            elif choice == "j":
                 view_all_prices()
            elif choice=="k":
                 welcome()
            elif choice=="l":
                bye()
                user_dict["admins"] = admin_list
                user_dict["operators"] = operator_list
              
                save_pricetable()
                sys.exit()
            else:
                choice="False"  
    admin_menu()
                                
    
def operator_code():
    def load_last_customer_id():
        try:
            with open(customer_file_name, "r") as customer_file:
                data = json.load(customer_file)
                return data.get("last_customer_id", 10000000)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # Handle file not found or invalid JSON
            return 10000000
        
     #Thank you
    def bye():
        print("-----------------------------------------------------------------")
        print("Thank You! Bye!")           
         
    
    
    def load_data():
        global customers, last_customer_id, last_parcel_num, parcels
        try:
            if True:  # Check if the file exists
                with open(customer_file_name, "r") as customer_file:
                    try:
                        data = json.load(customer_file)
                    except (json.decoder.JSONDecodeError, ValueError):
                        data = {"customers": [], "last_customer_id": 10000000}
    
                    if isinstance(data, dict) and "customers" in data:
                        customers = data["customers"]
                        last_customer_id = data.get("last_customer_id", 10000000)
                    else:
                        customers = []  # Initialize as an empty list
                        last_customer_id = 10000000
            else:
                # Create the file if it doesn"t exist
                save_data()
    
            if True:  # Check if the file exists
                with open(parcel_file_name, "r") as parcel_file:
                    try:
                        data = json.load(parcel_file)
                    except json.decoder.JSONDecodeError:
                        data = [1, []]
    
                    if isinstance(data, list) and len(data) == 2:
                        last_parcel_num, parcels = data[0], data[1]
                    else:
                        last_parcel_num = 1
                        parcels = []
            else:
                # Create the file if it doesn"t exist
                save_data()
        except FileNotFoundError:
            # If the file doesn"t exist, initialize values and create the file
            customers = []  # Initialize as an empty list
            last_customer_id = 10000000
            last_parcel_num = 1
            parcels = []
            save_data()  # Create the files with initial data
        
    
    def save_data():
        try:
            with open(customer_file_name, "w") as customers_file:
                data = {"last_customer_id": last_customer_id, "customers": customers}
                json.dump(data, customers_file)
    
            with open(parcel_file_name, "w") as parcels_file:
                data = [last_parcel_num, parcels]
                json.dump(data, parcels_file)
            
        except Exception as e:
            print("-----------------------------------------------------------------")
            print(f"Error saving data: {e}")
    
    
    # Load existing customer and parcel data from file
    load_data()
    
    
    
    
    def add_customer(name, address, telephone):
        global last_customer_id
        last_customer_id = load_last_customer_id() + 1
    
        if not (telephone.startswith("60") and len(telephone) == 11):
            print("-----------------------------------------------------------------")
            print("Please enter a correct phone number starting with '60' and with 11 digits.")
            return None
    
        customer = {"id": last_customer_id, "name": name, "address": address, "telephone": telephone, "parcels": []}
        customers.append(customer)
        save_data()
        return last_customer_id

    
    
    def modify_cus_details(customer_id, cus_address, phone_num):
        for customer in customers:
            if customer["id"] == customer_id:
                # Validate phone number
                if not (phone_num.startswith("60") and len(phone_num) == 11):
                    print("-----------------------------------------------------------------")
                    print("Please enter a correct phone number starting with '60' and with 11 digits.")
                    return False  # Validation failed
                customer["address"] = cus_address
                customer["telephone"] = phone_num
                save_data()
                return True
        return False  # Customer not found
        operator_menu()
    
    
    def calculate_parcel_price(weight, destination):
        valid_destinations = ["A", "B", "C", "D", "E"]
        try:
            weight = float(weight)  # Convert to float
        except ValueError:
            print("-----------------------------------------------------------------")
            print("Invalid weight. Please enter a numeric value.")
            return None
        destination = destination.upper()  # Convert to uppercase
        if destination not in valid_destinations:
            return None
        if weight <= 1:
            return "{:.2f}".format(price_table[destination]["1"])
        elif weight <= 3:
            return "{:.2f}".format(price_table[destination]["3"])
        else:
            return None
        operator_menu()
    
    def parcels_received(date, destination):
        parcels_received = []
        for parcel in parcels:
            if parcel["date_received"] == date and parcel["destination"].upper() == destination.upper():
                parcels_received.append(parcel)
        return parcels_received
    
    

    
    def get_last_parcel_num(default=10000000):
        try:
            with open(parcel_number_file_path, "r") as file:
                return int(file.read().strip())
        except FileNotFoundError:
            return default
    
    
    def update_parcel_number(number):
        with open(parcel_number_file_path, "w") as file:
            file.write(str(number))
    
    
    def generate_parcel_num():
        global last_parcel_num
        parcel_number = f"P{last_parcel_num + 10000000:08d}"
        update_parcel_number(last_parcel_num + 1)
        return parcel_number
    
    
    # Function to save data to a file
    def save_toFile(file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file)
    
    
    def add_parcel(customer_id, receiver_name, receiver_address, receiver_telephone, destination, weight, date_received):
        global parcels, last_parcel_num, parcel_file_name, bills_file_name
    
        # Generate a unique parcel number
        parcel_number = generate_parcel_num()
    
        # Calculate the parcel price
        price = calculate_parcel_price(weight, destination)
        if price is None:
            print("-----------------------------------------------------------------")
            print("Invalid destination or weight. Unable to calculate parcel price.")
            return
    
        customer = next((c for c in customers if c["id"] == customer_id), None)
    
        # Create a new parcel
        parcel = {
            "parcel_number": parcel_number,
            "customer_id": customer_id,
            "receiver_name": receiver_name,
            "receiver_address": receiver_address,
            "receiver_telephone": receiver_telephone,
            "destination": destination,
            "weight": weight,
            "price": price,  # Include the calculated price
            "date_received": date_received
        }
    
        # Update the parcels file
        customer["parcels"].append(parcel)
        parcels.append(parcel)
        save_toFile(parcel_file_name, parcels)
        print("-----------------------------------------------------------------")
        print(f"Parcel added successfully. Parcel ID: {parcel_number}")
        
    
        # Update the parcels file
        with open(parcel_file_name, "r+") as parcel_file:
            parcels_data = json.load(parcel_file)
            parcels_data.append(parcel)
            parcel_file.seek(0)
            json.dump(parcels_data, parcel_file, indent=2)
    
        # Update the bills file
        with open(bills_file_name, "r+") as bills_file:
            bills_data = json.load(bills_file)
            for bill in bills_data[1:]:
                if bill["consignment_number"] == customer_id:
                    bill["customers"]["parcels"].append(parcel)
                    break
            bills_file.seek(0)
            json.dump(bills_data, bills_file)
    
        # Update the current parcel number
        last_parcel_num = get_last_parcel_num()
        update_parcel_number(last_parcel_num)
        save_data()
        operator_menu()
    
    
    def update_bills_file(customer_id, parcel):
        with open(bills_file_name, "r+") as bills_file:
            bills_data = json.load(bills_file)
            for bill in bills_data:
                if bill["customer"]["id"] == customer_id:
                    bill["customer"]["parcels"].append(parcel)
                    break
            bills_file.seek(0)
            json.dump(bills_data, bills_file, indent=2)
    
    
    
    # Function to create a bill for each consignment
    def create_bill():
        search = "notFound"
        final_Price = 0
        match = "ok"
        cus_name = input("Enter customer name:").lower()
    
        # Load customer data
        with open(customer_file_name, "r+") as customer_file:
            data = json.load(customer_file)
    
            for customer in data["customers"]:
                if cus_name == customer["name"].lower():
                    date = input("Enter today's date(DD/MM/YYYY):")
                    search = "found"  
    
                    con_num = 0
                    with open(bills_file_name, "r") as bill_file:
                        current_bill_data = json.load(bill_file)
                        con_num = int(current_bill_data[0] + 1)
                        current_bill_data[0] = con_num
    
                        # Update consignment number in the bill file
                        with open(bills_file_name, "w") as bill_file:
                            json.dump(current_bill_data, bill_file)
    
                    for parcel in customer["parcels"]:
                        zone = parcel["destination"]
                        weight = float(parcel["weight"])
    
                        if zone in ["A", "B", "C", "D", "E"] and 0 < weight <= 3:
                            price = cost(weight, zone)
                            parcel["price"] = price
                            final_Price += price
    
                            # Update customer file with new parcel information
                            with open(customer_file_name, "w") as customer_file:
                                json.dump(data, customer_file)
    
                            # Update parcel file with new price
                            with open(parcel_file_name, "r+") as parcel_file:
                                parcel_data = json.load(parcel_file)
                                for par in parcel_data[1:]:
                                    for p in par:
                                        if p["parcel_number"] == parcel["parcel_number"]:
                                            p.update({"price": price})
    
                                with open(parcel_file_name, "w") as parcel_file:
                                    json.dump(parcel_data, parcel_file)
                        else:
                            print("-----------------------------------------------------------------")
                            print("\nWeight or zone information is invalid. Please try again.")
                            match = "no"
                            break
    
                    if match == "ok" and search == "found":
                        final_Price = round(final_Price * 1.08, 2)
                        bill = {
                            "date": date,
                            "consignment_number": con_num,
                            "final_price": final_Price,
                            "customers": customer
                        }
    
                        try:
                            # Load existing bills
                            with open(bills_file_name, "r") as bills_file:
                                existing_bills = json.load(bills_file)
                        except FileNotFoundError:
                            existing_bills = []  
    
                        # Append the new bill to the existing bills
                        existing_bills.append(bill)
                        with open(bills_file_name, "w") as bills_file:
                            json.dump(existing_bills, bills_file)
                        print("-----------------------------------------------------------------")
                        print("\nA bill of the consignment:")
                        print('\n')
                        print(f"BillCreatedDate: {bill['date']}\nConsignmentNumber: {bill['consignment_number']}\nFinalPrice: {bill['final_price']}")
                        print("Customer_information:")
                        print(f"Customer ID: {bill['customers']['id']}\nName: {bill['customers']['name']}\nAddress: {bill['customers']['address']}\nTelephone: {bill['customers']['telephone']}")
                        print("Parcel_information:")
                        for parcel in bill['customers']['parcels']:
                            print(f"Parcel Number: {parcel['parcel_number']}\nReceiver Name: {parcel['receiver_name']}\nReceiver Address: {parcel['receiver_address']}\nReceiver Telephone: {parcel['receiver_telephone']}\nDestination: {parcel['destination']}\nWeight: {parcel['weight']}\nPrice: {parcel['price']}\nDate Received: {parcel['date_received']}")
                        print("\n")
    
                        break
    
            if search == "notFound":
                print("-----------------------------------------------------------------")
                print("\nThe customer name was not found.")
        operator_menu()    
    
    # Function to calculate the price of the parcel
    def cost(weight, zone):
        if 0.0 < weight < 1.0:
            price = {
                "A": 8,
                "B": 9,
                "C": 10,
                "D": 11,
                "E": 12
            }
            return price.get(zone, 0)
        elif 1.0 <= weight <= 3.0:
            price = {
                "A": 16,
                "B": 18,
                "C": 20,
                "D": 22,
                "E": 24
            }
            return price.get(zone, 0)
        operator_menu()
        
    # Function to delete a parcel from a bill
    def delete():
        match = False
        while not match:
            answer = "other"
            consignmentNumber = int(input("Enter consignment number you want to modify:"))
            parcelNumber = input("Enter parcel number you want to modify:")
            match = modify_parcel_file(consignmentNumber, parcelNumber, True)
    
            if not match:
                while answer == "other":
                    answer = input("The parcel number was not found. Do you want to try again? (yes or no)").lower()
                    if answer == "no":
                        match = True
                        operator_menu()
                    elif answer != "yes" and answer != "no":
                        answer = "other"
        operator_menu()
        
    # Function to modify customer file
    def modify_customer_file(file_name, consignment_number, parcel_number, new_Cusdetails, new_parcel_details, del_parcel):
        with open(bills_file_name, "r") as bill_file:
            bill_data = json.load(bill_file)
            for bill in bill_data[1:]:
                if bill["consignment_number"] == consignment_number:
                    custom_id = bill["customers"]["id"]
    
        with open(file_name, "r") as file:
            data = json.load(file)
            customer_found = False
    
            if del_parcel:
                for customer in data["customers"]:
                    if customer["id"] == custom_id:
                        for index, parcel in enumerate(customer["parcels"]):
                            if parcel["parcel_number"] == parcel_number:
                                customer["parcels"].pop(index)
                                break
            else:
                for customer in data["customers"]:
                    for parcel in customer["parcels"]:
                        if parcel["parcel_number"] == parcel_number:
                            if new_Cusdetails:
                                customer.update(new_Cusdetails)
                            if new_parcel_details:
                                parcel.update(new_parcel_details)
                            customer_found = True
                            break
                    if customer_found:
                        break
    
            # Write to file outside of the loop
            with open(file_name, "w") as file:
                json.dump(data, file)
    
            return customer_found
    
    # Function to modify bill file
    def modify_bill_file(file_name, consignment_number, parcel_number, new_Cusdetails, new_parcel_details, del_parcel):
        with open(file_name, "r") as file:
            data = json.load(file)
    
            if del_parcel:
                for bill in data[1:]:
                    if bill["consignment_number"] == consignment_number:
                        for index, parcel in enumerate(bill["customers"]["parcels"]):
                            if parcel["parcel_number"] == parcel_number:
                                bill["customers"]["parcels"].pop(index)
                                with open(file_name, "w") as file:
                                    json.dump(data, file)
                                break
    
            else:
                for bill in data[1:]:
                    if bill["consignment_number"] == consignment_number:
                        if new_Cusdetails:
                            bill["customers"].update(new_Cusdetails)
                        if new_parcel_details:
                            new_final_Price = new_parcel_details["price"] * 1.08
    
                            bill["final_price"] = new_final_Price
                            for parcel in bill["customers"]["parcels"]:
                                if parcel["parcel_number"] == parcel_number:
                                    parcel.update(new_parcel_details)
    
                        with open(file_name, "w") as file:
                            json.dump(data, file)
                            break
    
    # Function to modify parcel file
    def modify_parcel_file(consignment_number, parcel_number, del_parcel):
        with open(bills_file_name, "r") as bill_file:
            bill_data = json.load(bill_file)
            for bill in bill_data[1:]:
                if bill["consignment_number"] == consignment_number:
                    custom_id = bill["customers"]["id"]
                else:
                    return
    
        with open(customer_file_name, "r") as customer_file:
            customer_data = json.load(customer_file)
            match = False
            old_price = 0
    
            for customer in customer_data["customers"]:
                if customer["id"] == custom_id:
                    for parcel in customer["parcels"]:
                        if parcel["parcel_number"] == parcel_number:
                            old_price = parcel["price"]
                            match = True
                            break
    
            if match:
                with open(parcel_file_name, "r") as parcel_file:
                    parcel_data = json.load(parcel_file)
    
                    if del_parcel:
                        # Delete parcel
                        for index, parcel in enumerate(parcel_data[1]):
                            if parcel["parcel_number"] == parcel_number:
                                parcel_data[1].pop(index)
                                with open(parcel_file_name, "w") as parcel_file:
                                    json.dump(parcel_data, parcel_file)
                                print("-----------------------------------------------------------------")
                                print("The parcel was deleted")
                                break
    
                        modify_customer_file(customer_file_name, consignment_number, parcel_number, None, None, del_parcel)
                        modify_bill_file(bills_file_name, consignment_number, parcel_number, None, None, del_parcel)
                    else:
                        new_zone = input("Enter new zone(A-E):").upper()
                        new_weight = float(input("Enter new weight:"))
    
                        if new_zone in ["A", "B", "C", "D", "E"] and 0 < new_weight <= 3:
                            new_price = cost(new_weight, new_zone)
                            new_parcel_details = {
                                "destination": new_zone,
                                "weight": new_weight,
                                "price": new_price,
                            }
    
                            modify_customer_file(customer_file_name, consignment_number, parcel_number, None,
                                               new_parcel_details, None)
                            modify_bill_file(bills_file_name, consignment_number, parcel_number, None, new_parcel_details,
                                           None)
    
                            for parcel in parcel_data[1]:
                                if parcel["parcel_number"] == parcel_number:
                                    parcel.update(new_parcel_details)
    
                            with open(parcel_file_name, "w") as parcel_file:
                                json.dump(parcel_data, parcel_file)
    
                        else:
                            print("-----------------------------------------------------------------")
                            print("\nThe zone or weight is invalid. Please try again.")
                            operator_menu()
                    print("-----------------------------------------------------------------")
                    print("\nThe information was successfully updated.")
    
            return match
    
    # Function to modify customer details or parcel weight and destination
    def modify_details(option):
        if option == "a":  
            match = False
            while not match:
                answer = "other"
                consignment_number = int(input("Enter consignment number you want to modify:"))
                parcel_number = input("Enter parcel number you want to modify:")
                new_name = input("Enter new customer name:").lower()
                new_address = input("Enter new customer address:")
                new_num = input("Enter new customer phone number:")
                new_Cusdetails = {
                    "name": new_name,
                    "address": new_address,
                    "telephone": new_num
                }
    
                if modify_customer_file(customer_file_name, consignment_number, parcel_number, new_Cusdetails, None,
                                      False):
                    print("-----------------------------------------------------------------")
                    print("\nCustomer information was successfully updated.")
                    match = True
                    modify_bill_file(bills_file_name, consignment_number, parcel_number, new_Cusdetails, None, False)
    
                if not match:
                    while answer == "other":
                        answer = input("The parcel was not found. Do you want to try again? (yes or no)").lower()
                        if answer == "no":
                            match = True
                            operator_menu()
                        elif answer != "yes" and answer != "no":
                            answer = "other"
    
        if option == "b":  
            match = False
            while not match:
                answer = "other"
                consignment_number = int(input("Enter consignment number you want to modify:"))
                parcel_number = input("Enter parcel number you want to modify:")
    
                if modify_parcel_file(consignment_number, parcel_number, False):
                    match = True
                else:
                    while answer == "other":
                        answer = input("The parcel was not found. Do you want to try again? (yes or no)").lower()
                        if answer == "no":
                            match = True
                            operator_menu()
                        elif answer != "yes" and answer != "no":
                            answer = "other"
        operator_menu()
 
    
    
    # Function to view details of a bill for a consignment number
    def view_bill():
        match = False
        while not match:
            answer = "other"
            consignmentNumber = int(input("Enter consignment number of a bill you want to view:"))
            with open(bills_file_name, "r") as bills_file:
                bills_file = json.load(bills_file)
                for bill in bills_file[1:]:
                    if consignmentNumber == bill["consignment_number"]:
                        match = True
                        print("-----------------------------------------------------------------")
                        print("\nA bill of the consignment:")
                        print('\n')
                        print(f"BillCreatedDate: {bill['date']}\nConsignmentNumber: {bill['consignment_number']}\nFinalPrice: {bill['final_price']}")
                        print("Customer_information:")
                        print(f"Customer ID: {bill['customers']['id']}\nName: {bill['customers']['name']}\nAddress: {bill['customers']['address']}\nTelephone: {bill['customers']['telephone']}")
                        print("Parcel_information:")
                        for parcel in bill['customers']['parcels']:
                            print(f"Parcel Number: {parcel['parcel_number']}\nReceiver Name: {parcel['receiver_name']}\nReceiver Address: {parcel['receiver_address']}\nReceiver Telephone: {parcel['receiver_telephone']}\nDestination: {parcel['destination']}\nWeight: {parcel['weight']}\nPrice: {parcel['price']}\nDate Received: {parcel['date_received']}")
                        print("\n")
    
                        break
            if not match:
                while answer == "other":
                    answer = input("The consignment number was not found. Do you want to try again? (yes or no)").lower()
                    if answer == "no":
                        match = True
                        operator_menu()
                    elif answer != "yes" and answer != "no":
                        answer = "other"
        operator_menu()
    
    # Function to view details of bills for a customer
    def view_cus_bill():
        count = 1
        cus_total = 0
        match = False
        while not match:
            answer = "other"
            customer = input("Enter customer name of bills you want to check:").lower()
            with open(bills_file_name, "r") as bills_file:
                bills_file = json.load(bills_file)
                for bill in bills_file[1:]:
                    if customer == bill["customers"]["name"].lower():
                        match = True
                        if count == 1:
                            print("\n---------------------")
                            print("Bill of the customer:")
                            print("---------------------\n")
                            count = count - 1
                        print(f"BillCreatedDate: {bill['date']}\nConsignmentNumber: {bill['consignment_number']}\nFinalPrice: {bill['final_price']}")
                        print("Customer_information:")
                        print(f"Customer ID: {bill['customers']['id']}\nName: {bill['customers']['name']}\nAddress: {bill['customers']['address']}\nTelephone: {bill['customers']['telephone']}")
                        print("Parcel_information:")
                        for parcel in bill['customers']['parcels']:
                            print(f"Parcel Number: {parcel['parcel_number']}\nReceiver Name: {parcel['receiver_name']}\nReceiver Address: {parcel['receiver_address']}\nReceiver Telephone: {parcel['receiver_telephone']}\nDestination: {parcel['destination']}\nWeight: {parcel['weight']}\nPrice: {parcel['price']}\nDate Received: {parcel['date_received']}")
                        print("\n")
                        cus_total += bill["final_price"]
        if match:
            print("\n--------------------------------------------")
            print("Total amount of the customer:", "RM", cus_total)
            print("--------------------------------------------\n")
        else:
            answer = "other"
            while answer == "other":
                answer = input("The customer name was not found. Do you want to try again? (yes or no):").lower()
                if answer == "no":
                    operator_menu()
                elif answer != "yes" and answer != "no":
                    answer = "other"
        operator_menu()
    
    # Function to view details of bills for a date range
    def view_bill_byDate():
        count = 1
        dateTotal = 0
        answer = "yes"
        match = False
        dateRange = []
        while answer == "yes":
            add = "Invalid"
            theDate = input("Enter date of bills you want to view (DD/MM/YYYY):")
            dateRange.append(theDate)
            print(dateRange)
            while add == "Invalid":
                answer = input("Do you want to add another date? (yes or no):").lower()
                if answer == "yes" or answer == "no":
                    add = "valid"
    
        for i in dateRange:
            with open(bills_file_name, "r") as bills_file:
                bills_file = json.load(bills_file)
                for bill in bills_file[1:]:
                    if bill["date"] == i:
                        if count == 1:
                            print("\n-------------------------")
                            print("Bill created on the date:")
                            print("-------------------------\n")
                            count = count - 1
                        match = True
                        print(f"BillCreatedDate: {bill['date']}\nConsignmentNumber: {bill['consignment_number']}\nFinalPrice: {bill['final_price']}")
                        print("Customer_information:")
                        print(f"Customer ID: {bill['customers']['id']}\nName: {bill['customers']['name']}\nAddress: {bill['customers']['address']}\nTelephone: {bill['customers']['telephone']}")
                        print("Parcel_information:")
                        for parcel in bill['customers']['parcels']:
                            print(f"Parcel Number: {parcel['parcel_number']}\nReceiver Name: {parcel['receiver_name']}\nReceiver Address: {parcel['receiver_address']}\nReceiver Telephone: {parcel['receiver_telephone']}\nDestination: {parcel['destination']}\nWeight: {parcel['weight']}\nPrice: {parcel['price']}\nDate Received: {parcel['date_received']}")
                        print("\n")
                        dateTotal += bill["final_price"]
        if match:
            print("\n----------------------------------------")
            print("Total amount on the date:", "RM", dateTotal)
            print("----------------------------------------\n")
            operator_menu()
        else:
            answer = "other"
            while answer == "other":
                answer = input("There is no bill created on the date. Do you want to try again? (yes or no):").lower()
                if answer == "no":
                    operator_menu()
                elif answer != "yes" and answer != "no":
                    answer = "other"
        operator_menu()
    
    
    
    # Function to display the operator menu
    def operator_menu():
            create_bill_file()
            create_parcels_file()
            print("\n")
            print("----------MENU----------")
            print("1. Add customer data")
            print("2. Modify customer's address and telephone number")
            print("3. Add a parcel")
            print("4. View the customer list")
            print("5. Calculate parcel price")
            print("6. List of parcels received")
            print("7. Create a bill for each consignment")
            print("8  Modify details of each parcel")
            print("9. Delete a parcel from a bill")
            print("10.View a bill of a consignment")
            print("11.View a list of bills and total amount of all bills charged to a customer")
            print("12.View a list of bills and total amount of all bills in a range of date")
            print("13.Go back to welcome page")
            print("14.Exit")
            choice = input("Please enter your choice from 1-14: ")
    
            if choice == "1":
                # add customer details
                name = input("Enter customer name: ").lower()
                address = input("Enter customer address: ")
                telephone = input("Enter customer telephone: ")
                customer_id = add_customer(name, address, telephone)
                if customer_id is not None:
                    print("-----------------------------------------------------------------")
                    print(f"Customer added successfully. Customer ID: {customer_id}")
                operator_menu()
    
            elif choice == "2":
                # modify customer data
                customer_id = int(input("Please enter customer id: "))
                cus_address = input("Please enter customer's new address: ")
                phone_num_number = input("Please enter customer's new phone number: ")
                if modify_cus_details(customer_id, cus_address, phone_num_number):
                    print("-----------------------------------------------------------------")
                    print("Customer details modified successfully.")
                else:
                    print("-----------------------------------------------------------------")
                    print("Customer not found.")
                operator_menu()
    
            elif choice == "3":
                # add parcel
                customer_id = int(input("Enter customer ID: "))
                receiver_name = input("Enter receiver name: ")
                receiver_address = input("Enter receiver address: ")
                receiver_telephone = input("Enter receiver telephone: ")
                destination = input("Enter destination (A, B, C, D, E): ").upper()
                weight = input("Enter parcel weight (below 3kg): ")
                date_received = input("Enter date received (DD/MM/YYYY): ")
                parcel = add_parcel(customer_id, receiver_name, receiver_address, receiver_telephone, destination, weight, date_received)
                if parcel:
                    print("-----------------------------------------------------------------")
                    print(f"Parcel added successfully. Parcel Number: {parcel['number']}")
                    save_data()
                operator_menu()
    
            elif choice == "4":
                # view customer list
                if customers:
                    print("-----------------------------------------------------------------")
                    print("Customer List:")
                    for customer in customers:
                        print(
                            f"ID: {customer['id']}, Name: {customer['name']}, Address: {customer['address']}, Telephone: {customer['telephone']}")
                else:
                    print("-----------------------------------------------------------------")
                    print("No customers found.")
                operator_menu()
    
            elif choice == "5":
                # calculate parcel price
                weight = input("Enter parcel weight (below 3kg): ")
                destination = input("Enter destination (A, B, C, D, E): ").upper()
                price = calculate_parcel_price(weight, destination)
                if price is not None:
                    print("-----------------------------------------------------------------")
                    print(f"The price for a {weight}kg parcel to destination {destination} is RM{price}.")
                operator_menu()
    
            if choice == "6":
                date = input("Enter date received (DD/MM/YYYY): ")
                destination = input("Enter destination (zone): ")
                parcel_list = parcels_received(date, destination)
                if not parcel_list:
                    print("-----------------------------------------------------------------")
                    print(f"No parcels received on {date} to destination {destination}.")
                else:
                    print("-----------------------------------------------------------------")
                    print(f"Parcels received on {date} to destination {destination}:")
                    for parcel in parcel_list:
                        print(
                            f"Parcel Number: {parcel['parcel_number']}, Receiver Name: {parcel['receiver_name']}, Weight: {parcel['weight']}, Price: {parcel['price']}")
                operator_menu()
            
         
    
            elif choice == "7":
                create_bill()
    
            elif choice == "8":
                modify = "none"
                while modify == "none":
                    print("-----------------------------------------------------------------")
                    print("a: Modify sender name, address, and phone number")
                    print("b: Modify destination and weight")
                    modify = input("Enter a or b: ").lower()
                    if modify == "a" or modify == "b":
                        modify_details(modify)
                    else:
                        modify = "none"
            elif choice == "9":
                delete()
            elif choice == "10":
                view_bill()
            elif choice == "11":
                view_cus_bill()
            elif choice == "12":
                view_bill_byDate() 
            elif choice == "13":
                print("-----------------------------------------------------------------")
                print("Going back to welcome page.")
                save_data()
                welcome()
            elif choice == "14":
                print("-----------------------------------------------------------------")
                print("Exiting the program...")
                save_data()
                bye()
                sys.exit()
            else:
                True  
                
           
    # Call operator_menu() function 
    operator_menu()
                
    #Thank you
def bye():
    print("-----------------------------------------------------------------")
    print("Thank You! Bye!")           
  
def welcome():
    user="False"
    print("===================================")
    print("Hello, my friend!")
    print("Welcome to our own Shopee:)")
    print("=================================")
    ask=input("Do you have an account?(yes/no): ").lower()
    if ask=="yes":
        login=input("Enter your login: ").lower()
        password=input("Enter your password: ").lower()
        for item in admin_list:
            if login==item[0] and password==item[1]:
                user="True" 
                admin_code()
        for oper in operator_list:
            if login==oper[0] and password==oper[1]:
                user="True"
                operator_code()
        if user=="False"  :
            print("User was not found! Try again.")
            welcome() 
    elif ask=="no":
        print("Oops...Then you can't join the system!")
        bye()
        sys.exit()
            
#Beginning of the progrpam
welcome()

