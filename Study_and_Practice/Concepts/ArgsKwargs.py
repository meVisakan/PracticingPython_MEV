def order_pizza(size, *toppings, **details):
    print("Toppings is taken input as: ", toppings)
    print("Details are taken input as: ", details)

    print(f"Pizza of {size} size ordered with the following toppings: ")
    for top in toppings:
        print(f"-{top}")
    print("Details of the order are as below: ")
    for key, val in details.items():
        print(f"{key}: {val}")


# Input
size = "large"
order_pizza(size, "pepperoni", "cheese", "onion", delivery=True, tip=5)