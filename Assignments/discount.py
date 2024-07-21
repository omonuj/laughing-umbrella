def my_discount(price, discount):

	
	if price < 0 or discount < 0 or discount > 100:
		return "Invalid input. Price and discount should be non_negative and discount should be non-negative and discount should be at most 100."

	
	discount_amount = (discount / 100) * price
	final_price = price - discount_amount
	return final_price

if __name__ == "__main__":

	try: 
		price = float(input("Enter the original price: "))
		discount = float(input("Enter discount percentage: "))
	except ValueError:
		print("Invalid input. Please numeric values. ")
	else:
		
		final_price = my_discount(price, discount)
		print("The price after discount is:", final_price)
	
