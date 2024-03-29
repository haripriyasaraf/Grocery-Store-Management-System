import mysql.connector as sql
import getpass
import subprocess
import datetime
import sys
import os
import tabulate as t
import time
import sqlite3 as sql

from tkinter import *
from tkinter import messagebox

def connection():
    try:
      con=sql.connect(host="localhost",user="root",password="@Hari_7113",database="project1")
      if con.is_connected()==True:
          return con  
      else:
          print("Couldn't connect")
    except Exception as e:
      print(e)
      cur=con.cursor()


# Function to create a table
def create_table(table_name):
    try:
        con = connection()
        cur = con.cursor()
        query = f'''create table if not exists {table_name}
                (item_code int,
                item_name varchar(35),
                item_price float,
                gst float,
                discount_offer float,
                quantity float,
                stock int)'''
        cur.execute(query)
        print(f"Table '{table_name}' created successfully")
    except Exception as e:
        print(e)

# Function to perform insertion
def insertion(table_name):
    try:
        con = connection()
        cur = con.cursor()

        item_code = int(input("Enter CODE of product: "))
        item_name = input("Enter NAME of product: ")
        item_price = float(input("Enter MRP of product: "))
        gst = float(input("Enter GST Applied on product: "))
        discount_offer = float(input("Enter DISCOUNT Offer applicable on product: "))
        quantity = float(input("Enter QUANTITY of product: "))
        stock = int(input("Enter STOCK available of product: "))

        cur.execute(f"insert into {table_name}(item_code,item_name,item_price,gst,discount_offer,quantity,stock)values(?,?,?,?,?,?,?)",
                    (item_code, item_name, item_price, gst, discount_offer, quantity, stock))
        print("Data inserted successfully")
        con.commit()
    except sql.Error as er:
        print(er)

# Function to perform updation
def updation(table_name):
    try:
        con = connection()
        cur = con.cursor()

        code = int(input("Enter code of Product whose record is to be modified:"))
        query = f"select * from {table_name} where item_code={code}"
        cur.execute(query)
        rec = cur.fetchone()

        if not rec:
            print("No record exists for Product with item_code :", code)
        else:
            print("Existing Record:")
            print("Code :", rec[0])
            print("Name : ", rec[1])
            print("MRP :", rec[2])
            print("GST :", rec[3])
            print("Discount_Offer :", rec[4])
            print("Quantity :", rec[5])
            print("Stock :", rec[6])
            print("*" * 25)
            print("Type value to modify below or just press Enter for no change")

            item_name = input(f"Enter Name ({rec[1]}):") or rec[1]
            item_price = float(input(f"Enter MRP ({rec[2]}):") or rec[2])
            gst = float(input(f"Enter GST ({rec[3]}):") or rec[3])
            discount_offer = float(input(f"Enter Discount_Offer ({rec[4]}):") or rec[4])
            quantity = float(input(f"Enter Quantity ({rec[5]}):") or rec[5])
            stock = int(input(f"Enter Stock ({rec[6]}):") or rec[6])

            cur.execute(f"update {table_name} set item_name=?, item_price=?, gst=?, discount_offer=?, quantity=?, stock=? where item_code=?",
                        (item_name, item_price, gst, discount_offer, quantity, stock, code))

            print("Data updated successfully")
            con.commit()
    except sql.Error as er:
        print(er)

# Function to perform deletion
def deletion(table_name):
    try:
        con = connection()
        cur = con.cursor()

        item_code = int(input("Enter CODE of Product whose record you want to delete:"))
        cur.execute(f"delete from {table_name} where item_code=?", (item_code,))
        con.commit()
        if cur.rowcount > 0:
            print("Record Deleted successfully")
        else:
            print(f"Product with item_code {item_code} not found")

    except sql.Error as er:
        print(er)

# Function to delete all products
def delete_all_products(table_name):
    try:
        con = connection()
        cur = con.cursor()
        ch = input("Do you want to delete all the records (y/n): ")
        if ch.lower() == 'y':
            cur.execute(f"delete from {table_name}")
            con.commit()
            print("All records deleted")
    except Exception as e:
        print(e)

# Function to display one product
def display_one_product():
    try:
        con = connection()
        cur = con.cursor()
        item_code = int(input("Enter code of the product whose record is to be displayed:"))
        query = f"select * from {table_name} where item_code={item_code}"
        cur.execute(query)
        rec = cur.fetchone()
        if rec:
            print("Record Found:")
            print(t.tabulate([rec], headers=['Item_Code', 'Item_Name', 'Item_Price', 'GST', 'Discount_Offer', 'Quantity', 'Stock'], tablefmt='psql'))
        else:
            print("No record found for item_code", item_code)
    except Exception as e:
        print(e)

# Function to display all products
def display_all_products():
    try:
        con = connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM products")
        products = cur.fetchall()
        if products:
            print(t.tabulate(products, headers=['Item_Code', 'Item_Name', 'Item_Price', 'GST', 'Discount_Offer', 'Quantity', 'Stock'], tablefmt='psql'))
        else:
            print("No products found")
    except sql.Error as er:
        print(er)

def create_table_profile():
    try:
        con=connection()
        cur=con.cursor()
        sql='''create table if not exists profile
              (EmpCode int,
              EmpName varchar(30),
              Age integer,
              DateOfJoining varchar(10),
              Position varchar(20),
              Salary integer)'''
        cur.execute(sql)
    except Exception as e:
        print(e)    

#Employee main
def add():
    try:
        con=connection()
        cur=con.cursor()
        create_table_profile()

        EmpCode=int(input("Enter Employee Code :"))
        EmpName=input("Enter Employee Name : ")
        Age=input("Enter Employee Age : ")
        DateOfJoining=input("Enter Date Of Joining : ")
        Position=input("Enter Employee Position : ")
        Salary=input("Enter Employee Salary : ")
        cur.execute("insert into profile(EmpCode,EmpName,Age,DateOfJoining,Position,Salary)values('{}','{}','{}','{}','{}','{}')".format(EmpCode,EmpName,Age,DateOfJoining,Position,Salary))
        print()
        print("Data Inserted Successfully")
        con.commit()
    except sql.Error as er:
        print(er)
         
def display():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from employee")
        print(t.tabulate(cur,headers=['EmpCode','EmpName','Age','DateOfJoining','Position','Salary']))
        result=cur.fetchall()
        for i in result:
            print(i)
    except sql.Error as er:
        print(er)
                   
def delete():
    try:
        con=connection()
        cur=con.cursor()
        ch=input("Do you want to delete all the records (y/n) ")
        if ch=='y' or ch=="Y":
            cur.execute("delete from profile")
            con.commit()
            print("All records deleted ")
        else:
            EmpCode=int(input("Enter EmpCode whose record you want to delete :"))
            cur.execute("delete from spices_and_seasonings where item_code= %d"%(EmpCode))
            con.commit()
            c=cur.rowcount
            if c>0:
                print("Record Deleted successfully ")
            else:
                print("Employee with EmpCode ",EmpCode," not found")
       
    except sql.Error as er:
        print(er)
import mysql.connector as sql
import tabulate as t

# Function to generate bill for entire database
import mysql.connector as sql
import tabulate as t



#=================================================================================================================
def admin_menu():
    try:
        while True:
            print("\nAdmin Menu:")
            print("1. Product Information")
            print("2. Employee Information")
            print("3. Exit")
            choice = input("Enter Your Choice: ")

            if choice == '1':
                while True:
                    print("\nProduct Information Menu:")
                    print("1. Create Table")
                    print("2. Insertion")
                    print("3. Updation")
                    print("4. Deletion")
                    print("5. Delete All Products")
                    print("6. Display One Product")
                    print("7. Display All Products")
                    print("8. Back to Admin Menu")
                    option = input("Enter your choice: ")

                    if option == '1':
                        table_name = input("Enter table name: ")
                        create_table(table_name)
                    elif option == '2':
                        table_name = input("Enter table name: ")
                        insertion(table_name)
                    elif option == '3':
                        table_name = input("Enter table name: ")
                        updation(table_name)
                    elif option == '4':
                        table_name = input("Enter table name: ")
                        deletion(table_name)
                    elif option == '5':
                        table_name = input("Enter table name: ")
                        delete_all_products(table_name)
                    elif option == '6':
                        table_name = input("Enter table name: ")
                        display_one_product()
                    elif option == '7':
                        table_name = input("Enter table name: ")
                        display_all_products()
                    elif option == '8':
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")

            elif choice == '2':
                while True:
                    print("\nEmployee Information Menu:")
                    print("1. Enter Employee Details")
                    print("2. Display Employee Details")
                    print("3. Delete Employee Details")
                    print("4. Back to Admin Menu")
                    option = input("Enter Task No. : ")

                    if option == '1':
                        add()
                    elif option == '2':
                        display()
                    elif option == '3':
                        delete()
                    elif option == '4':
                        break
                    else:
                        print("Invalid choice. Please choose again.")

            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    except Exception as e:
        print(e)

def customer_menu():
    try:
        while True:
            print("\nCustomer Menu:")
            print("1. View Products")
            print("2. Exit")
            choice = input("Enter Your Choice: ")

            if choice == '1':
                display_all_products()  # Assuming customer can only view products
            elif choice == '2':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    except Exception as e:
        print(e)

def menu():
    root = Tk()
    root.geometry("400x200")
    root.title("Login")

    def admin_login():
        username = admin_username_entry.get()
        password = admin_password_entry.get()

        if username == "admin" and password == "dbms":
            admin_menu()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def customer_login():
        username = customer_username_entry.get()
        password = customer_password_entry.get()

        if username == "customer" and password == "hari":
            customer_menu()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    admin_frame = Frame(root)
    admin_frame.pack(pady=10)

    admin_username_label = Label(admin_frame, text="Admin Username: ")
    admin_username_label.grid(row=0, column=0)

    admin_username_entry = Entry(admin_frame)
    admin_username_entry.grid(row=0, column=1)

    admin_password_label = Label(admin_frame, text="Admin Password: ")
    admin_password_label.grid(row=1, column=0)

    admin_password_entry = Entry(admin_frame, show="*")
    admin_password_entry.grid(row=1, column=1)

    admin_login_button = Button(admin_frame, text="Login as Admin", command=admin_login)
    admin_login_button.grid(row=2, columnspan=2)

    customer_frame = Frame(root)
    customer_frame.pack(pady=10)

    customer_username_label = Label(customer_frame, text="Customer Username: ")
    customer_username_label.grid(row=0, column=0)

    customer_username_entry = Entry(customer_frame)
    customer_username_entry.grid(row=0, column=1)

    customer_password_label = Label(customer_frame, text="Customer Password: ")
    customer_password_label.grid(row=1, column=0)

    customer_password_entry = Entry(customer_frame, show="*")
    customer_password_entry.grid(row=1, column=1)

    customer_login_button = Button(customer_frame, text="Login as Customer", command=customer_login)
    customer_login_button.grid(row=2, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    menu()
