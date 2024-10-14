def display_menu():
  print("""
        +----------------------------------------------------+
        | Pizza Type  |  Number of Slices  |  Price per Box  |
        +----------------------------------------------------+
        |  Sapa size  |         4          |  2000   Naira   |
        +----------------------------------------------------+
        | Small Money |         6          |  2400   Naira   |
        +----------------------------------------------------+
        |  Big Boys   |         8          |  3000   Naira   |
        +----------------------------------------------------+
        | Odogwu      |        12          |  4200   Naira   |
        +----------------------------------------------------+
  """)
def calculate_pizza_order(number_of_people, pizza_type):
  pizza_data = {
    "sapa size": {"slices": 4, "price": 2000},
    "small money": {"slices": 6, "price": 2400},
    "big boys": {"slices": 8, "price": 3000},
    "odogwu": {"slices": 12, "price": 4200}
  }

  slices_per_person = pizza_data[pizza_type]["slices"]
  price_per_box = pizza_data[pizza_type]["price"]

  boxes_needed = number_of_people // slices_per_person
  slices_leftover = number_of_people % slices_per_person

  if slices_leftover > 0:
    boxes_needed += 1
    slices_leftover = (boxes_needed * slices_per_person) - number_of_people

  total_price = boxes_needed * price_per_box

  return boxes_needed, slices_leftover, total_price

while True:
  try:
    display_menu()
    number_of_people_input = input("Enter number of people (or type 'Exit' to quit): ")
    if number_of_people_input.lower() == "exit":
      break  

    number_of_people = int(number_of_people_input)
    pizza_type = input("Enter pizza type: ").lower()

    if pizza_type not in ["sapa size", "small money", "big boys", "odogwu"]:
      raise ValueError("Invalid pizza type.")

    boxes_needed, slices_leftover, total_price = calculate_pizza_order(number_of_people, pizza_type)

    print(f"Number of boxes needed: {boxes_needed} boxes")
    print(f"Number of slices leftover: {slices_leftover} slices")
    print(f"Total price: {total_price} Naira")

  except ValueError as ve:
    print(f"Error: {ve}. please try again")
  except Exception as e:
    print(f"An error occurred: {e}. please try again")
    
  
    




  
