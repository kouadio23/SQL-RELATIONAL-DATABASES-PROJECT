from tabulate import tabulate
import mysql.connector

print()
print("WELCOME TO THE MySQL blood donation database")
print("PLEASE CHOOSE A  NUMBER OPTION")
print()


# Prompt the user to chose options

choice = None
while choice != "7":
  print("1) Show Tables Name")
  print("2) Show Table Content")
  print("3) Insert Into Table")
  print("4) Delete Row From Table")
  print("5) Drop Table")
  print("6) Update Table")
  print("7) Quit")
  print()

  choice = input("Please choose number and press enter: ")
  print()

  if choice == "1":
    # Connect to MySql database
    mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")

    mycursor = mydb.cursor()
    # show tables in blood_donation_database database.
    mycursor.execute("SHOW TABLES FROM `blood_donation_database`")
    headers = ["Table Name"]
    print(tabulate(list(mycursor), headers, tablefmt="grid"))
    for x in mycursor.fetchall():
      print(x)
      print()
 # TABLE CONTENT
  elif  choice == "2":
    sub_choice = None
    while sub_choice != "quit":
      sub_choice = input("Enter Table Name :'blood_bank; blood_bank_has_staff; donor; patient; staff; staff_department; staff_has_staff_departement' and type quit to exit: ")

 # blood_bank content
      if sub_choice == "blood_bank":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM blood_bank")
        headers = ["id", "blood_group", "date_of_prelevement", "comment", "Patient_id", "Donor_id"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 

# blood_bank_has_staff  content
      elif sub_choice == "blood_bank_has_staff":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM blood_bank_has_staff ")
        headers = ["blood_bank_id", "staff_id"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 

#  donor content
      elif sub_choice == "donor":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM donor ")
        headers = ["id", "fname", "lname", "dob", "address", "phone_number", "gender", "medical_condition"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 


#  patient  content
      elif sub_choice == "patient":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM patient  ")
        headers = ["id", "fname", "lname", "dob", "blood_group", "address", "phone_number", "gender", "medical_condition"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 



#  staff  content
      elif sub_choice == "staff":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM staff  ")
        headers = ["id", "fname", "lname", "dob", "address", "phone_number"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 


#  staff_departement  content
      elif sub_choice == "staff_departement":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM staff_departement  ")
        headers = ["id", "category_description"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 



#  staff_has_staff_departement content
      elif sub_choice == "staff_has_staff_departement":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM staff_has_staff_departement ")
        headers = ["staff_id", "staff_departement_id"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 


#  INSERT
  elif choice == '3':
    mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
    mycursor = mydb.cursor()
    table_name = input('Which table to insert into? ')


# insert into blood_bank 
    if table_name == "blood_bank":
      id = input('blood_id: ')
      blood_group = input('blood group: ')
      date_of_prelevement = input("date of prelevemnt (yyy-MM-DD:")
      comment = input("comment: ")
      Patient_id = input("Patient ID: ")
      Donor_id = input("Donor ID: ")
      values = (id, blood_group, date_of_prelevement, comment, Patient_id, Donor_id)
      sql = "INSERT INTO blood_bank (id, blood_group, date_of_prelevement, comment, Patient_id, Donor_id) VALUES (%s, %s ,%s ,%s ,%s ,%s)"
      values = (id, blood_group, date_of_prelevement, comment, Patient_id, Donor_id)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()

# inserting in blood_bank_has_staff
    elif table_name == "blood_bank_has_staff":
      blood_bank_id = input('blood bank ID: ')
      staff_id = input('Staff ID: ')
      values = (blood_bank_id, staff_id)
      sql = "INSERT INTO blood_bank_has_staff (blood_bank_id, staff_id) VALUES (%s, %s)"
      values = (blood_bank_id, staff_id)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()

# inserting in donor
    elif table_name == "donor":

      id = input('donor ID: ')
      fname = input('first name: ')
      lname = input("last name: ")
      dob = input("day of birth (yyy-MM-DD: ")
      address = input("address: ")
      phone_number = input("Phone number (000-000-0000):")
      gender = input("gender: ")
      medical_condition = input("medical condition: ")
      values = (id, fname, lname, dob, address, phone_number, gender, medical_condition)
      sql = "INSERT INTO donor (id, fname, lname, dob, address, phone_number, gender, medical_condition) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
      values = (id, fname, lname, dob, address, phone_number, gender, medical_condition)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()


# inserting in patient
    elif table_name == "patient":
      id = input("patient ID:")
      fname = input("first name: ")
      lname = input("last name: ")
      dob = input("day of birth (yyy-MM-DD: ")
      blood_group = input("Blood group: ")
      address = input("address: ")
      phone_number = input("Phone number (000-000-0000):")
      gender = input("gender: ")
      medical_condition = input("medical condition: ")
      values = (id, fname, lname, dob, blood_group, address, phone_number, gender, medical_condition)
      sql = "INSERT INTO patient (id, fname, lname, dob, blood_group, address, phone_number, gender, medical_condition) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
      values = (id, fname, lname, dob, blood_group, address, phone_number, gender, medical_condition)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()


# inserting in staff
    elif table_name == "staff":
      id = input('staff ID: ')
      fname = input('first name: ')
      lname = input("last name")
      dob = input("Day of birth (yyy-MM-DD:")
      addrress = input("address: ")
      phone_number = input("phone number (000-000-0000):")
      values = (id, fname, lname, dob, address, phone_number)
      sql = "INSERT INTO staff (id, fname, lname, dob, address, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
      values = (id, fname, lname, dob, address, phone_number)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()

      # inserting in staff_departement

    elif table_name == "staff":
      id = input('staff ID: ')
      category_description = input("Category description: ")
      values = (id, category_description)
      sql = "INSERT INTO staff (id, category_description) VALUES (%s, %s)"
      values = (id, category_description)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()

      # inserting in staff_as_staff_department
    elif  table_name == "staff_as_staff_department":
      staff_id = input('staff ID: ')
      staff_departement_id = input('staff departement id: ')
      values = (staff_id, staff_departement_id)
      sql = "INSERT INTO staff (staff_id, staff_departement_id) VALUES (%s, %s)"
      values = (staff_id, staff_departement_id)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()

      # DELETE Row 
  elif choice == "4":
    mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
    mycursor = mydb.cursor()
    table_delete = input('Which table to delete From? ')

  # deleting in blood_bank table
    if table_delete == "blood_bank":
      blood = input('Blood_bank ID: ')
      sql = f"DELETE FROM blood_bank WHERE id = {blood}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()
    
    # deleting in blood_bank_has_staff table
    elif table_delete == 'blood_bank_has_staff':
      bbs = input('blood_bank_has_staff ID: ')
      sql = f"DELETE FROM blood_bank_has_staff WHERE blood_bank_id = {bbs}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()

      # deleting in donor table
    elif table_delete == 'donor':
      do = input('donor ID: ')
      sql = f"DELETE FROM donor WHERE id = {do}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()   

      # deleting in patient table
    elif table_delete == 'patient':
      pat = input('patient ID: ')
      sql = f"DELETE FROM patient WHERE id = {pat}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()


       # deleting in staff table
    elif table_delete == 'staff':
      staf = input('staff ID: ')
      sql = f"DELETE FROM staff WHERE id = {staf}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()

      # deleting in staff_departement table
    elif table_delete == 'staff_departement':
      sta_de = input('staff_departement ID: ')
      sql = f"DELETE FROM staff_departement WHERE id = {sta_de}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()   

      # deleting in staff_has_staff_departement table
    elif table_delete == 'staff_has_staff_departement':
      stade = input('staff_has_staff_departement ID: ')
      sql = f"DELETE FROM staff_has_staff_departement WHERE id = {stade}"
      mycursor.execute(sql)
      mydb.commit()
      print(mycursor.rowcount, "record(s) deleted.")
      print()


       # Drop table
  elif choice == "5":
    mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
    mycursor = mydb.cursor()
    table_drop = input('Which table to drop? Please consult Table Names: ')
    sql = f"DROP TABLE {table_drop}"
    mycursor.execute(sql)
    print(f"{table_drop} Droped")
    print()

     # Update Table
  elif choice == "6":
    mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
    mycursor = mydb.cursor()
    # prompt the user for info to update
    table_update = input('Which table to update from? ')
    column_update = input('which column to update? ')
    value_update = input('New Value(s): ')
    old_value = input('Old value(s): ')
    # run the query
    sql = f"UPDATE {table_update} SET {column_update} = {value_update} WHERE '{column_update}' = '{old_value}'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")
    print()
