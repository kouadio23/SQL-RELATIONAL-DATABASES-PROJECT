from tabulate import tabulate
import mysql.connector

print()
print("WELCOME TO THE MySQL HOSPITAL DATABASE")
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
      elif sub_choice == "blood_bank_has_staff ":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM blood_bank_has_staff ")
        headers = ["blood_bank_id", "staff_id"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 

#  donor content
      elif sub_choice == "donor ":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM donor ")
        headers = ["id", "fname", "lname", "dob", "address", "phone_number", "gender", "medical_condition"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 


#  patient  content
      elif sub_choice == "patient  ":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM patient  ")
        headers = ["id", "fname", "lname", "dob", "blood_group", "address", "phone_number", "gender", "medical_condition"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 



#  staff  content
      elif sub_choice == "staff  ":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM staff  ")
        headers = ["id", "fname", "lname", "dob", "address", "phone_number"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 


#  staff_departement  content
      elif sub_choice == "staff_departement ":
        mydb = mysql.connector.connect(host="localhost",user="root",password="KKF23091989kkf",database="blood_donation_database")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM staff_departement  ")
        headers = ["id", "category_description"]
        print(tabulate(list(mycursor), headers, tablefmt="grid" ))
        for x in mycursor.fetchall():
          print(x) 
          print() 



#  staff_has_staff_departement content
      elif sub_choice == "staff_has_staff_departement ":
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
      "id", "blood_group", "date_of_prelevement", "comment", "Patient_id", "Donor_id"
      id = input('blood_id: ')
      blood_group = input('blood group: ')
      date_of_prelevement = input("date of prelevemnt")
      comment = ("comment")
      Patient_id = ("Patient ID")
      Donor_id = ("Donor ID")
      values = (id, blood_group, date_of_prelevement, comment, Patient_id, Donor_id)
      sql = "INSERT INTO blood_bank (id, blood_group, date_of_prelevement, comment, Patient_id, Donor_id) VALUES (%s, %s ,%s ,%s ,%s ,%s)"
      values = (id, blood_group, date_of_prelevement, comment, Patient_id, Donor_id)
      mycursor.execute(sql, values)
      mydb.commit()
      print(mycursor.rowcount, "record inserted.")
      print()