def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it meets the conditions.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage.
    
    Returns:
    float: The final price after applying the discount, or the original price if no discount is applied.
    """
    if discount_percent >= 20:  # Check if the discount is 20% or higher
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return the original price if discount is less than 20%

# Main program
try:
    # Prompt the user for input
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percentage)

    # Output the results
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount was applied. The original price is: ${original_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values for the price and discount.")
