# This is a corrected version of the script which did not behave as expected
# The error was an indentation error, where the return statement was inside the for loop
# instead of after it

def calculate_total_discount(
    prices: list[float], discount_rate: float = 0.10
) -> float:
    """Calculates the total savings across a list of item prices."""
    total_discount = 0.0
    for price in prices:
        item_discount = price * discount_rate
        total_discount += item_discount
    return total_discount


# Sample shopping cart: Total value is $180.00 (expected discount: $18.00)
cart_prices = [100.0, 50.0, 20.0, 10.0]
savings = calculate_total_discount(cart_prices)

print(f"Total savings: ${savings:.2f}")
