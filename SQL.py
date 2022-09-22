from tabulate import tabulate
import mysql.connector

print()
print("WELCOME TO THE MySQL HOSPITAL DATABASE")
print("PLEASE CHOOSE A  NUMBER OPTION")
print()


# Prompt the user to chose options

choice = None
while choice != "8":
  print("1) Show Tables Name")
  print("2) Show Table Content")
  print("3) Insert Into Table")
  print("4) Delete Row From Table")
  print("5) Drop Table")
  print("6) Update Table")
  print("8) Quit")
  print()

  choice = input("Please choose number and press enter: ")
  print()

 