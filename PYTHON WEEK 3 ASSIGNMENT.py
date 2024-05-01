def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# Original price of the shoes,
original_price = 437

# Discount percentage from the coupon
discount_percent = 30

# CalculatING the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Output of  the final price,
if final_price == original_price:
    print("No discount applied. Original price: $", final_price)
else:
    print("Final price after applying the discount: $", final_price)

