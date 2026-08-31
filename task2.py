
products = {
    "P101": {"name": "Laptop", "category": "Electronics", "price": 1200.0, "quantity": 10},
    "P102": {"name": "Mouse", "category": "Electronics", "price": 25.0, "quantity": 0},
    "P103": {"name": "Keyboard", "category": "Electronics", "price": 50.0, "quantity": 5},
    "P104": {"name": "Desk Chair", "category": "Furniture", "price": 150.0, "quantity": 0}
}

def lookup_product(prod_id):
    return products.get(prod_id, "Product not found")

def update_price(prod_id, new_price):
    if prod_id in products:
        products[prod_id]["price"] = new_price
        print(f"Price for {prod_id} updated to ${new_price:.2f}")


def update_stock(prod_id, new_qty):
    if prod_id in products:
        products[prod_id]["quantity"] = new_qty
        print(f"Stock for {prod_id} updated to {new_qty}")


def get_out_of_stock():
    return [info["name"] for prod_id, info in products.items() if info["quantity"] == 0]


print("--- Product Lookup ---")
print("Lookup P101:", lookup_product("P101"))

print("\n--- Updates ---")
update_price("P101", 1150.0)
update_stock("P102", 12)

print("\n--- Out of Stock Products ---")
print("Out of stock items:", get_out_of_stock())
