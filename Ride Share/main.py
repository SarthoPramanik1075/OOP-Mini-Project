from ride import Ride, RideRequest, RideMatching, RideSharing
from user import Rider, Driver
from vehicle import Car, Bike


RideVerse = RideSharing("RideVerse")

print("🚖 Welcome to RideVerse Ride Sharing 🚖")

while True:
    print("\nChoose an option:")
    print("1. Register Rider")
    print("2. Register Driver")
    print("3. Request Ride (Rider)")
    print("4. Complete Ride (Driver)")
    print("5. Show Rider's Current Ride")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Register Rider
        name = input("Enter rider name: ")
        email = input("Enter rider email: ")
        nid = int(input("Enter rider NID: "))
        location = input("Enter rider current location: ")
        balance = int(input("Enter rider balance: "))
        rider = Rider(name, email, nid, location, balance)
        RideVerse.add_rider(rider)
        print(f"✅ Rider {name} registered.")

    elif choice == "2":
        # Register Driver
        name = input("Enter driver name: ")
        email = input("Enter driver email: ")
        nid = int(input("Enter driver NID: "))
        location = input("Enter driver current location: ")
        driver = Driver(name, email, nid, location)
        RideVerse.add_driver(driver)
        print(f"✅ Driver {name} registered.")

    elif choice == "3":
        # Rider requests ride
        rider_name = input("Enter rider name: ")
        destination = input("Enter destination: ")
        vehicle_type = input("Enter vehicle type (car/bike): ")

        rider = RideVerse.find_rider(rider_name)   # you need to implement find_rider in RideSharing
        if rider:
            rider.request_ride(RideVerse, destination, vehicle_type)
        else:
            print("❌ Rider not found!")

    elif choice == "4":
        # Driver completes ride
        driver_name = input("Enter driver name: ")
        rider_name = input("Enter rider name: ")

        driver = RideVerse.find_driver(driver_name)   # implement find_driver in RideSharing
        rider = RideVerse.find_rider(rider_name)

        if driver and rider and rider.current_ride:
            driver.reach_destination(rider.current_ride)
            print(f"✅ Ride completed for {rider.name}")
        else:
            print("❌ Either driver/rider not found or no active ride.")

    elif choice == "5":
        rider_name = input("Enter rider name: ")
        rider = RideVerse.find_rider(rider_name)
        if rider:
            rider.show_current_ride()
        else:
            print("❌ Rider not found!")

    elif choice == "6":
        print("👋 Thank you for using RideVerse!")
        break

    else:
        print("⚠️ Invalid choice! Try again.")
