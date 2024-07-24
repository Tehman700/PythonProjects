from customtkinter import *
from PIL import Image
import json
import requests
from CTkTable import CTkTable
import pandas as pd
import psycopg2
import random
from tkinter import ttk


import CTkMessagebox

hostname = "localhost"
database = "inventory"
username = "postgres"
pwd  = "admin"
port_id = 5432
conn = None
cur = None

app = CTk()
app.title("Inventory Software")
app.geometry("800x600")

# Load images
img = Image.open("box.png")
img1 = Image.open("barcode.png")
img2 = Image.open("inventory.png")
img3 = Image.open("sales.png")
icon_image = Image.open("icon.png")
img4 = Image.open("shopping.png")
icon_image_size = (300, 50)
icon = CTkImage(dark_image=icon_image, size=icon_image_size)

# Create main frame
main_frame = CTkFrame(master=app)
main_frame.place(relwidth=1, relheight=1)

second_frame = CTkFrame(master=app)
second_frame.place(relwidth=1, relheight=1)

new_user_frame = CTkFrame(master=app)
new_user_frame.place(relwidth=1, relheight=1)

# Create add product frame
add_product_frame = CTkFrame(master=app)
add_product_frame.place(relwidth=1, relheight=1)


# Inventory Screen Frame

see_inventory_frame = CTkFrame(master=app)
see_inventory_frame.place(relwidth=1, relheight=1)

# Searching wali frame
see_searching_frame = CTkFrame(master=app)
see_searching_frame.place(relwidth=1, relheight=1)

today_frame = CTkFrame(master=app)
today_frame.place(relwidth=1, relheight=1)


# Function to show frames
def show_frame(frame):
    frame.tkraise()


# Login controlling mechansicam
def new_user():

    def register():
        conn = psycopg2.connect(
            host= hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
        )

        cur =conn.cursor()
        insert_register_details = 'INSERT INTO users (email,password) VALUES (%s,%s)'
        inserting_values =(email.get(),password.get())
        cur.execute(insert_register_details,inserting_values)

        conn.commit()

        conn.close()



    show_frame(new_user_frame)
    image_label = CTkLabel(master=new_user_frame, image=icon, text="")
    image_label.place(x=270, y=10)
    CTkLabel(master=new_user_frame, text="Enter Your Credentials Below", font=("Arial", 25)).place(x=50,y=90)

        
    CTkLabel(master=new_user_frame, text="Email:", font=("Arial", 25)).place(x=50,y=150)

    email = CTkEntry(master=new_user_frame,border_color="#D9534F", text_color="black", border_width=0, width=600,height=40,font=("Arial", 17) )
    email.place(x=50,y=200)

    CTkLabel(master=new_user_frame, text="Password:", font=("Arial", 25)).place(x=50,y=280)

    password = CTkEntry(master=new_user_frame, bg_color="white",border_color="blue", text_color="black",show="*", border_width=0, width=600,height=40,font=("Arial", 17))
    password.place(x=50,y=330)
        
    CTkButton(master=new_user_frame, text="Register",command=register, width=150,height=40, font=("Arial", 25), hover_color="#D9534F").place(x=50,y=420)
    CTkButton(master=new_user_frame, text="Login", width=150,height=40, font=("Arial", 25), hover_color="#D9534F", command=lambda: show_frame(main_frame)).place(x=280,y=420)







def login_handler():
    conn = psycopg2.connect(
        host= hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    cur =conn.cursor()

    checking_theory = 'SELECT * FROM users WHERE email = %s AND password = %s'
    cur.execute(checking_theory, (user_email.get(), user_password.get()))

    result = cur.fetchone()

    if result:
        CTkMessagebox.CTkMessagebox(title = "Success", message = "Login Success", icon="check")
        show_frame(second_frame)
    else:
        CTkMessagebox.CTkMessagebox(title="Error", message="Enter Correct Details", icon="cancel")
    
    cur.close()
    conn.close()


def alert_for_low_stock():
    conn = psycopg2.connect(
        host= hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor()
    checking_stock = 'SELECT * FROM products WHERE quantity < 5'
    cur.execute(checking_stock)
    
    answer = cur.fetchall()
    if answer:
        CTkMessagebox.CTkMessagebox(title ="Alert Khurram", message = "Khurram! Some Item quantity is less than 5", icon="cancel")
    else:
        cur.close()
        conn.close()






def combined():
    login_handler()
    alert_for_low_stock()




# ALL LOGIN MECHANISM UI FOR ENTRY WIDGETS AND BUTTONS


image_label = CTkLabel(master=main_frame, image=icon, text="")
image_label.place(x=270, y=10)
CTkLabel(master=main_frame, text="Enter Your Credentials Below", font=("Arial", 25)).place(x=50,y=90)

       
CTkLabel(master=main_frame, text="Email:", font=("Arial", 25)).place(x=50,y=150)

user_email = CTkEntry(master=main_frame,border_color="#D9534F", text_color="black", border_width=0, width=600,height=40,font=("Arial", 17) )
user_email.place(x=50,y=200)

CTkLabel(master=main_frame, text="Password:", font=("Arial", 25)).place(x=50,y=280)

user_password = CTkEntry(master=main_frame, bg_color="white",border_color="blue", text_color="black",show="*", border_width=0, width=600,height=40,font=("Arial", 17))
user_password.place(x=50,y=330)
       
CTkButton(master=main_frame, text="Login",command=(combined), width=150,height=40, font=("Arial", 25), hover_color="#D9534F").place(x=50,y=420)
CTkButton(master=main_frame, text="New User", width=150,height=40,command=new_user, font=("Arial", 25), hover_color="#D9534F").place(x=280,y=420)







# Changing the frame for adding product screen
def add():
    show_frame(add_product_frame)
    

# Fetching all details from entry widgets and saving them into variables
# Converting them to there specific datatypes


def add_to():
    conn = psycopg2.connect(
        host= hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    cur =conn.cursor()
    insert_product_details = 'INSERT INTO products (product_name,quantity,category,wholesale_price,your_price) VALUES (%s,%s,%s,%s,%s)'
    inserting_details =(product_name_entry.get(),quantity_entry.get(),category_entry.get(),wholesale_price_entry.get(),your_price_entry.get())

    cur.execute(insert_product_details,inserting_details)
    CTkMessagebox.CTkMessagebox(title = "Success", message = "Product Added Successfully", icon="check")
    


    conn.commit()

    conn.close()


    

# Deleting all the text in the entry widgets after clicking clear button

def delete_data():
    product_name_entry.delete(0,END)
    category_entry.delete(0,END)
    quantity_entry.delete(0,END)
    wholesale_price_entry.delete(0,END)
    your_price_entry.delete(0,END)





def barcode():
    print("barcodedesf")


# Seeing all the inventory using firebase API and showing it the table with seperate frame
tree = ttk.Treeview(see_inventory_frame, columns=("ID", "Product Name", "Quantity", "Category", "Wholesale Price", "Your Price"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Product Name", text="Product Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Category", text="Category")
tree.heading("Wholesale Price", text="Sale Price")
tree.heading("Your Price", text="Your Price")
# Set column widths
tree.column("ID", width=5)
tree.column("Product Name", width=150,anchor="center")
tree.column("Quantity", width=30, anchor="center")
tree.column("Category", width=100,anchor="center")
tree.column("Wholesale Price", width=100,anchor="center")
tree.column("Your Price", width=100,anchor="center")

tree.place(relwidth=1, relheight=0.8, x=20, y=100)



def delete_selected():
    selected_item = tree.selection()
    
    if not selected_item:
        CTkMessagebox.CTkMessagebox(title="Error", message="No item selected", icon="cancel")
        return
    
    item_id = tree.item(selected_item)["values"][0]
    
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        
        cur = conn.cursor()
        delete_query = 'DELETE FROM products WHERE id = %s'
        cur.execute(delete_query, (item_id,))
        conn.commit()
        cur.close()
        conn.close()

        for row in tree.get_children():
            tree.delete(row)
        see_inventory()

        CTkMessagebox.CTkMessagebox(title="Success", message="Product deleted successfully", icon="check")

    except Exception as e:
        CTkMessagebox.CTkMessagebox(title="Error", message=f"An error occurred: {e}", icon="cancel")

import customtkinter as ctk

def update_item():
    selected_item = tree.selection()


    item_id = tree.item(selected_item)["values"][0]
    top = ctk.CTkToplevel(app)
    top.title("Updating Product")
    top.geometry("500x300")

    product_name_label = ctk.CTkLabel(top, text="Product Name:", font=("Arial", 14))
    product_name_label.place(x=10, y=20)
    product_name_entry = ctk.CTkEntry(top, width=200, height=20)
    product_name_entry.place(x=120, y=20)

    quantity_label = ctk.CTkLabel(master=top, text="Quantity:", font=("Arial", 14))
    quantity_label.place(x=10, y=50)
    quantity_entry = ctk.CTkEntry(master=top, width=200, height=20)
    quantity_entry.place(x=120, y=50)

    category_label = ctk.CTkLabel(master=top, text="Category:", font=("Arial", 14))
    category_label.place(x=10, y=80)
    category_entry = ctk.CTkEntry(master=top, width=200, height=20)
    category_entry.place(x=120, y=80)

    wholesale_price_label = ctk.CTkLabel(master=top, text="Wholesale Price:", font=("Arial", 14))
    wholesale_price_label.place(x=10, y=110)
    wholesale_price_entry = ctk.CTkEntry(master=top, width=200, height=20)
    wholesale_price_entry.place(x=120, y=110)

    your_price_label = ctk.CTkLabel(master=top, text="Your Price:", font=("Arial", 14))
    your_price_label.place(x=10, y=140)
    your_price_entry = ctk.CTkEntry(master=top, width=200, height=20)
    your_price_entry.place(x=120, y=140)

    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        cur = conn.cursor()
        select_query = 'SELECT * FROM products WHERE id = %s'
        cur.execute(select_query, (item_id,))
        product = cur.fetchone()
        cur.close()
        conn.close()

        if product:
            product_name_entry.insert(0, product[1])
            quantity_entry.insert(0, product[2])
            category_entry.insert(0, product[3])
            wholesale_price_entry.insert(0, product[4])
            your_price_entry.insert(0, product[5])

    except Exception as tt:
        CTkMessagebox.CTkMessagebox(title="Error", message=f"An error occurred: {tt}", icon="cancel")
        return

    def save_all_data():
        product_name = product_name_entry.get()
        quantity = quantity_entry.get()
        category = category_entry.get()
        wholesale_price = wholesale_price_entry.get()
        your_price = your_price_entry.get()

        try:
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id
            )
            cur = conn.cursor()
            update_query = ''' UPDATE products SET product_name = %s, quantity = %s, category = %s, wholesale_price = %s, your_price = %s WHERE id = %s '''
            cur.execute(update_query, (product_name, quantity, category, wholesale_price, your_price, item_id))
            conn.commit()
            cur.close()
            conn.close()

            CTkMessagebox.CTkMessagebox(title="Success", message="Product updated successfully", icon="check")
            see_inventory()
            top.destroy() 

        except Exception as e:
            CTkMessagebox.CTkMessagebox(title="Error", message=f"An error occurred: {e}", icon="cancel")

    upt_button = ctk.CTkButton(top, text="Update Product", fg_color="red",
                               font=("Arial", 14), hover_color="#D9534F", command=save_all_data)
    upt_button.place(x=120, y=170)


def see_inventory():
    show_frame(see_inventory_frame)
    CTkLabel(master=see_inventory_frame, text="All Orders", font=("Arial", 25), text_color="black", fg_color="transparent").place(x=20,y=30)

    conn = psycopg2.connect(
        host= hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM products')
    rows = cur.fetchall()
    cur.close()
    conn.close()


    # Clear existing table data if any
    for row in tree.get_children():
        tree.delete(row)
    
    for row in rows:
        tree.insert("", "end", values=row)
        
    back_button = CTkButton(master=see_inventory_frame, text="Back to Main Menu", corner_radius=20, width=100,
                        height=40, font=("Arial", 20), hover_color="#F76935", command=lambda: show_frame(second_frame))
    back_button.place(x=550, y=30)

    delete_button = CTkButton(master=see_inventory_frame, text="Delete Selected", corner_radius=20, width=150, height=40,fg_color="red",
                             font=("Arial", 20), hover_color="#D9534F", command=delete_selected)
    delete_button.place(x=350, y=30)

    update_btn = CTkButton(master=see_inventory_frame, text="Update Selected", corner_radius=20, width=150, height=40,fg_color="green",command=update_item,
                             font=("Arial", 20), hover_color="#D9534F")
    update_btn.place(x=150,y=30)

import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import psycopg2

def todays():
    show_frame(today_frame)
    top = ctk.CTkToplevel(app)
    top.title("Today's Sale")
    top.geometry("1200x800")
    
    tree = ttk.Treeview(top, columns=("ID", "Product Name", "Quantity", "Category", "Wholesale Price", "Your Price"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Product Name", text="Product Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Category", text="Category")
    tree.heading("Wholesale Price", text="Sale Price")
    tree.heading("Your Price", text="Your Price")
    tree.column("ID", width=5)
    tree.column("Product Name", width=150, anchor="center")
    tree.column("Quantity", width=30, anchor="center")
    tree.column("Category", width=100, anchor="center")
    tree.column("Wholesale Price", width=100, anchor="center")
    tree.column("Your Price", width=100, anchor="center")
    tree.place(relwidth=.5, relheight=0.7, x=10, y=50)
    
    s_tree = ttk.Treeview(top, columns=("ID", "Product Name", "Quantity", "Category", "Wholesale Price", "Your Price"), show='headings')
    s_tree.heading("ID", text="ID")
    s_tree.heading("Product Name", text="Product Name")
    s_tree.heading("Quantity", text="Quantity")
    s_tree.heading("Category", text="Category")
    s_tree.heading("Wholesale Price", text="Sale Price")
    s_tree.heading("Your Price", text="Your Price")
    s_tree.column("ID", width=5)
    s_tree.column("Product Name", width=150, anchor="center")
    s_tree.column("Quantity", width=30, anchor="center")
    s_tree.column("Category", width=100, anchor="center")
    s_tree.column("Wholesale Price", width=100, anchor="center")
    s_tree.column("Your Price", width=100, anchor="center")
    s_tree.place(relwidth=.5, relheight=0.7, x=780, y=50)
    
    # Add Quantity Entry
    CTkLabel(master=top, text="Enter Quantity:", font=("Arial", 20), text_color="black", fg_color="transparent").place(x=30, y=7)
    quantity_entry = ctk.CTkEntry(master=top, width=100, height=20)
    quantity_entry.place(x=180, y=10)

    # Total sale label
    total_sale_label = CTkLabel(master=top, text="Total Sale for Today: 0", font=("Arial", 24), text_color="black", fg_color="transparent")
    total_sale_label.place(x=60 ,y=610)

    total_sale = 0
    total_wholesale_value = 0

    def update_right_table():
        nonlocal total_sale, total_wholesale_value  # Togdh update the total_sale variable in the outer scope
        selected_item = tree.selection()
        if not selected_item:
            return
        item_id = tree.item(selected_item)["values"][0]
        item_name = tree.item(selected_item)["values"][1]
        item_category = tree.item(selected_item)["values"][3]
        item_wholesale_price = tree.item(selected_item)["values"][4]
        item_your_price = tree.item(selected_item)["values"][5]
        try:
            quantity = int(quantity_entry.get())
        except ValueError:
            quantity = 0
        
        if quantity > 0:
            # Update right table
            s_tree.insert("", "end", values=(item_id, item_name, quantity, item_category, item_wholesale_price, item_your_price))
            
            # Update inventory quantity in the database
            conn = psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id
            )
            cur = conn.cursor()
            cur.execute('SELECT quantity FROM products WHERE id = %s', (item_id,))
            current_quantity = cur.fetchone()[0]
            new_quantity = current_quantity - quantity
            
            if new_quantity >= 0:
                cur.execute('UPDATE products SET quantity = %s WHERE id = %s', (new_quantity, item_id))
                conn.commit()
            cur.close()
            conn.close()
            
            # Update total sale
            total_sale += item_your_price * quantity
            total_wholesale_value += item_wholesale_price * quantity
            total_sale_label.configure(text=f"Total Sale for Today: {total_sale}")
            
            # for Refresh inventory display
            see_inventory()
    
    CTkButton(master=top, text="Select", command=update_right_table).place(x=300, y=8)
    
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM products')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    for row in tree.get_children():
        tree.delete(row)
    
    for row in rows:
        tree.insert("", "end", values=row)

    def profit_calc():
        profit = total_sale - total_wholesale_value 
        CTkLabel(master=top, text=f"Total Profit for Today: {profit}", font=("Arial", 24), text_color="black", fg_color="transparent").place(x=60 ,y=710)

    CTkButton(master=top, text="See Total Profit for Today", command=profit_calc, font=("Arial", 24)).place(x=60, y=660)



def searching():
    tree = ttk.Treeview(see_searching_frame, columns=("ID", "Product Name", "Quantity", "Category", "Wholesale Price", "Your Price"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Product Name", text="Product Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Category", text="Category")
    tree.heading("Wholesale Price", text="Sale Price")
    tree.heading("Your Price", text="Your Price")
    # Setting column widths
    tree.column("ID", width=5)
    tree.column("Product Name", width=150,anchor="center")
    tree.column("Quantity", width=30, anchor="center")
    tree.column("Category", width=100,anchor="center")
    tree.column("Wholesale Price", width=100,anchor="center")
    tree.column("Your Price", width=100,anchor="center")

    tree.place(relwidth=1, relheight=0.8, x=20, y=100)
    show_frame(see_searching_frame)
    CTkLabel(master=see_searching_frame, text="Enter Category:", font=("Arial", 20), text_color="black", fg_color="transparent").place(x=70, y=30)
    
    searched_item = CTkEntry(master=see_searching_frame, width=160, height=35)
    searched_item.place(x=240, y=30)
    
    def execute_search():
        category = searched_item.get()
        if not category:
            CTkMessagebox.CTkMessagebox(title="Error", message="Please enter a category", icon="cancel")
            return

        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        cur = conn.cursor()
        search_query = 'SELECT * FROM products WHERE category = %s'
        cur.execute(search_query, (category,))
        results = cur.fetchall()
        cur.close()
        conn.close()

        for row in tree.get_children():
            tree.delete(row)

        for row in results:
            tree.insert("", "end", values=row)
    
    CTkButton(master=see_searching_frame, text="Search", command=execute_search).place(x=410, y=30)

    back_button = CTkButton(master=see_searching_frame, text="Back to Main Menu", command=lambda: show_frame(second_frame))
    back_button.place(x=600, y=30)






# Main frame widgets
image_label = CTkLabel(master=second_frame, image=icon, text="")
image_label.place(x=270, y=10)

first = CTkButton(master=second_frame, text="Add Product", corner_radius=20, width=200,
                  height=100, font=("Arial", 35),
                  hover_color="#F76935", image=CTkImage(dark_image=img, size=(40,40)), command=add)
first.place(x=100, y=220)

second = CTkButton(master=second_frame, text="Add Product by Barcode", corner_radius=20, width=200,
                   height=100, font=("Arial", 27),
                   hover_color="#F76935", image=CTkImage(dark_image=img1, size=(30,30)), command=barcode)
second.place(x=100, y=350)

third = CTkButton(master=second_frame, text="See or Edit Entire Inventory", corner_radius=20, width=200,fg_color="#081339",
                  height=100, font=("Arial", 25),
                  hover_color="#F76935", image=CTkImage(dark_image=img2, size=(40,40)), command=see_inventory)
third.place(x=400, y=220)

fourth = CTkButton(master=second_frame, text="Today's Sale", corner_radius=20, width=200,fg_color="#081339",
                   height=100, font=("Arial", 27),
                   hover_color="#F76935", image=CTkImage(dark_image=img3, size=(40,40)), command=todays)
fourth.place(x=520, y=350)

fifth = CTkButton(master=second_frame, text="Search any Item", corner_radius=20, width=200,fg_color="#081339",
                   height=100, font=("Arial", 27),
                   hover_color="#F76935", image=CTkImage(dark_image=img4, size=(40,40)), command=searching)
fifth.place(x=100, y=480)






















# Add product frame widgets
product_name_label = CTkLabel(master=add_product_frame, text="Product Name:", font=("Arial",25))
product_name_label.place(x=100, y=70)
product_name_entry = CTkEntry(master=add_product_frame, width=400,height=35)
product_name_entry.place(x=300, y=70)

quantity_label = CTkLabel(master=add_product_frame, text="Quantity:", font=("Arial",25))
quantity_label.place(x=100, y=130)
quantity_entry = CTkEntry(master=add_product_frame, width=400,height=35)
quantity_entry.place(x=300, y=130)

category_label = CTkLabel(master=add_product_frame, text="Category:", font=("Arial",25))
category_label.place(x=100, y=190)
category_entry = CTkEntry(master=add_product_frame, width=400,height=35)
category_entry.place(x=300, y=190)

wholesale_price_label = CTkLabel(master=add_product_frame, text="Wholesale Price:", font=("Arial",25))
wholesale_price_label.place(x=100, y=240)
wholesale_price_entry = CTkEntry(master=add_product_frame, width=400,height=35)
wholesale_price_entry.place(x=300, y=240)

your_price_label = CTkLabel(master=add_product_frame, text="Your Price:", font=("Arial",25))
your_price_label.place(x=100, y=290)
your_price_entry = CTkEntry(master=add_product_frame, width=400,height=35)
your_price_entry.place(x=300, y=290)




back_button = CTkButton(master=add_product_frame, text="Back to Main Menu", corner_radius=20, width=100,
                        height=40, font=("Arial", 20), hover_color="#F76935", command=lambda: show_frame(second_frame))
back_button.place(x=460, y=370)



add_product_button = CTkButton(master=add_product_frame, text="Add Product", corner_radius=20, width=100,fg_color="#F76935",
                        height=40, font=("Arial", 20), hover_color="black", command = add_to)
add_product_button.place(x=260,y=370)

clear_data_button = CTkButton(master=add_product_frame, text="Clear Data", corner_radius=20, width=100,hover_color="#D9534F",
                        height=40, font=("Arial", 20), command = delete_data)
clear_data_button.place(x=70,y=370)    


# Initialize by showing the main frame
show_frame(main_frame)

app.mainloop()
