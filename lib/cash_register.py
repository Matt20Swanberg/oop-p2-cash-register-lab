#!/usr/bin/env python3

class CashRegister:
  """A simple cash register for tracking purchases and discounts"""

  def __init__(self, discount=0):
    # Store the discount percentage (defaults to 0 if none is provided)
    self.discount = discount
    # Track the running total of all purchases
    self.total = 0
    # Store each purchased item
    self.items = []
    # Keep a history of transactions so they can be voided later
    self.previous_transactions = []

  def add_item(self, item, price, quantity=1):
    """Add an item purchase to the register"""

    # Increase the running total based on the quantity purchased
    self.total += price * quantity

    # Add each purchased item to the item list
    for _ in range(quantity):
      self.items.append(item)

    # Save the transaction details for potential reversal
    self.previous_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })

  def apply_discount(self):
    """Apply the configured discount to the current total"""

    # A discount of 0 means there is nothing to apply
    if self.discount == 0:
      print("There is no discount to apply.")
      return

    # Reduce the total by the configured percentage
    self.total *= (1 - self.discount / 100)

    print(f"After the discount, the total comes to ${self.total:g}.")

  def void_last_transaction(self):
    """Remove the most recent transaction from the register"""

    # Ensure there is a transaction available to remove
    if not self.previous_transactions:
      print("There is no transaction to void.")
      return

    # Retrieve and remove the last recorded transaction
    last_transaction = self.previous_transactions.pop()

    # Reverse the transaction's impact on the total.
    self.total -= (last_transaction["price"] * last_transaction["quantity"]
    )

    # Remove each purchased item from the item list.
    for _ in range(last_transaction["quantity"]):
      self.items.remove(last_transaction["item"])