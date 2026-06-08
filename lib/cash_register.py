#!/usr/bin/env python3

class CashRegister:
  # pass
    """
    A simple cash register that can:
    - Store purchased items
    - Calculate totals
    - Apply discounts
    - Void the most recent transaction
    """

    def __init__(self, discount=0):
        # Percentage discount (0 means no discount)
        self.discount = discount

        # Running total of all purchases
        self.total = 0

        # Stores all items purchased
        self.items = []

        # Stores transaction history
        self.previous_transactions = []

    def add_item(self, item_name, price, quantity=1):
        """
        Adds an item to the register.

        Parameters:
            item_name (str): Name of item
            price (float): Price of one item
            quantity (int): Number purchased
        """

        # Calculate the transaction value
        transaction_total = price * quantity

        # Update overall total
        self.total += transaction_total

        # Add item multiple times if quantity > 1
        self.items.extend([item_name] * quantity)

        # Save transaction details
        transaction = {
            "item": item_name,
            "price": price,
            "quantity": quantity
        }

        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """
        Applies the register discount to the total.
        """

        if self.discount <= 0:
            print("There is no discount to apply.")
            return

        # Calculate amount to subtract
        discount_amount = self.total * (self.discount / 100)

        # Reduce total
        self.total -= discount_amount

        print(
            f"After the discount, the total comes to ${self.total:.0f}."
        )

    def void_last_transaction(self):
        """
        Removes the most recent transaction.
        """

        if not self.previous_transactions:
            print("No transaction available to remove.")
            return

        # Get and remove the latest transaction
        last_sale = self.previous_transactions.pop()

        # Deduct its value from total
        self.total -= (
            last_sale["price"] * last_sale["quantity"]
        )

        # Remove corresponding items
        for _ in range(last_sale["quantity"]):
            if self.items:
                self.items.pop()

    def show_receipt(self):
        """
        Displays current register information.
        """

        print("\n------ RECEIPT ------")
        print(f"Items: {self.items}")
        print(f"Total: ${self.total}")
        print("---------------------\n")
"""
# Register without discount
register1 = CashRegister()
# discount should be 0 by default
print(register1.discount)  # 0
# total and items should be empty at initialization
print(register1.total)  # 0
print(register1.items)  # []

# Add one item
register1.add_item("Eggs", 0.98)
# After adding one item
print(register1.total)
print(register1.items)

# Add item with quantity
register1.add_item("Book", 5.00, 3)
# After adding item with quantity
print(register1.total)
print(register1.items)
# Multiple transactions
register1.add_item("Lucky Charms", 4.50)
register1.add_item("Ritz Crackers", 5.00)
register1.add_item("Peanut Butter Cups", 2.50, 2)
# After multiple transactions
print(register1.total)
print(register1.items)
# Void latest transaction
register1.void_last_transaction()
# After voiding last transaction
print(register1.total)
print(register1.items)

# Register with discount
register2 = CashRegister(20)

register2.add_item("MacBook Air", 1000)
# Before discount
print(register2.total)
register2.apply_discount()
# After discount
print(register2.total)
# Check transaction history
print(register2.previous_transactions)

# Show receipt
register2.show_receipt()
"""