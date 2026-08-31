# Data representation: {product_name: {"price": price, "quantity": quantity}}
cart = {}


def add_product(name, price, quantity=1):
    if name in cart:
        cart[name]["quantity"] += quantity
        print(f"Updated {name} quantity to {cart[name]['quantity']}")
    else:
        cart[name] = {"price": price, "quantity": quantity}
        print(f"Added {name} to cart.")


def modify_quantity(name, new_quantity):
    if name in cart:
        if new_quantity > 0:
            cart[name]["quantity"] = new_quantity
            print(f"Updated {name} quantity to {new_quantity}")
        else:
            remove_product(name)
    else:
        print(f"Item '{name}' not found in cart.")


def remove_product(name):
    if name in cart:
        del cart[name]
        print(f"Removed {name} from cart.")
    else:
        print(f"Item '{name}' not found in cart.")


def calculate_total():
    total = sum(item["price"] * item["quantity"] for item in cart.values())
    return total


print("--- Cart Operations ---")
add_product("Laptop", 1000.0, 1)
add_product("Mouse", 25.0, 2)


add_product("Mouse", 25.0, 1)

modify_quantity("Laptop", 2)
remove_product("Mouse")

print("\n--- Final Cart & Total ---")
print("Cart Contents:", cart)
print(f"Total Price: ${calculate_total():.2f}")
