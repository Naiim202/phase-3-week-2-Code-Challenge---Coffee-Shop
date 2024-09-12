# test_coffee_shop.py

from customer import Customer
from coffee import Coffee
from order import Order

def main():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    # Create orders
    alice.create_order(espresso, 2.5)
    alice.create_order(latte, 3.5)
    bob.create_order(espresso, 2.5)
    bob.create_order(espresso, 2.5)

    # Test customer methods
    print(f"{alice.name}'s orders: {len(alice.orders())}")
    print(f"{alice.name}'s coffees: {[coffee.name for coffee in alice.coffees()]}")

    # Test coffee methods
    print(f"{espresso.name} orders: {espresso.num_orders()}")
    print(f"{espresso.name} average price: ${espresso.average_price():.2f}")

    # Test most_aficionado method
    aficionado = Customer.most_aficionado(espresso)
    if aficionado:
        print(f"Biggest {espresso.name} aficionado: {aficionado.name}")
    else:
        print(f"No aficionado found for {espresso.name}")

if __name__ == "__main__":
    main()