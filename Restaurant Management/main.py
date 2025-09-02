from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurent import Restaurent
from users import Admin, Employee, Customer

res=Restaurent('Mama Aso')
def customer_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone: ")
    address=input("Enter your address: ")

    customer=Customer(name, email, phone, address)

    while True:
        print(f'Welcome {customer.name}')
        print("1. View Menu")
        print("2. add to cart")
        print("3. View to cart")
        print("4. PayBill")
        print("5. exit")

        choice=int(input('Enter your choice: '))
        if choice==1:
            customer.view_menu(res)
        elif choice==2:
            item_name=input('Enter item name: ')
            quantity=int(input("Enter quantity: "))
            customer.add_to_cart(res, item_name, quantity)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            break
        else:
            print("Invalid Input!")


def admin_menu():
    name=input("Enter your name: ")
    email=input("Enter your email: ")
    phone=input("Enter your phone: ")
    address=input("Enter your address: ")

    admin=Admin(name, email, phone, address)

    while True:
        print(f'Welcome {admin.name}')
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Item")
        print("6. Exit")



        choice=int(input('Enter your choice: '))
        if choice==1:
            item_name=input('Enter item name: ')
            item_price=int(input("Enter item price: "))
            item_quantity=int(input("Enter item quantity: "))
            item=FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(res, item)

        elif choice==2:
            name=input("Enter Employee Name: ")
            email=input("Enter Employee Email: ")
            phone=input("Enter Employee Phone: ")
            address=input("Enter Employee Address: ")
            designation=input("Enter Employee Designation: ")
            age=input("Enter Employee Age: ")
            salary=input("Enter Employee Salary: ")
            emp=Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(res, emp)
            
        elif choice==3:
            admin.view_employee(res)
        elif choice==4:
            admin.view_menu(res)
        elif choice==5:
            item_name=input("Enter item name that you want to delete: ")
            admin.remove_item(res,item_name)
        elif choice==6:
            break
        else:
            print("Invalid Input!")

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        customer_menu()
    elif choice==2:
        admin_menu()
    elif choice==3:
        break
    else:
        print("Invalid Input!!")
