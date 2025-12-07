# improve my mind

def menu_simple():
    print(" - - - - MENU - - - -\n" + '=' * 30)
    print("[1] ADD CAR\n" + '=' * 30)
    print("[2] SEARCH CAR\n" + '=' * 30)
    print("[3] SEE CARS\n" + '=' * 30)
    print("[4] LEAVE\n" + '=' * 30)

def add_cars():
    plate = input("license plate: ")
    car_name = input("car: ")

    if plate == "" or car_name == "":
        print("ERROR, write something please")
        return None


    cars_storage = {
        'plate': plate,
        'car_name': car_name
    }
    return cars_storage

power = True
plate_storage = []

while power:
    menu_simple()
    try:
        write_cars = int(input("choose your option: "))
    except ValueError:
        print("not have this opition")

    if write_cars == 1:
        cars_storage = add_cars()
        if cars_storage:
            plate_storage.append(cars_storage)
        else:
            print("it's a ilegal plate or name")

    elif write_cars == 2:
        search_car = input("car name: ")
        car_found = False
        for car in plate_storage:
            if car['car_name'] == search_car:
                print(f"name: {car['car_name']}")
                print(f"name: {car['car_name']} | plate: {car['plate']}")
                car_found = True
        if not car_found:
            print("No have this car sorry")


    elif write_cars == 3:
        for car in plate_storage:
            print(f"name: {car['car_name']} | plate: {car['plate']}")

    elif write_cars == 4:
        power = False

    else:
        print("no have this option sorry")
        continue

print("thank you for using my program")

