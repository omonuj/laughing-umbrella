from datetime import datetime, timedelta

def calculate_cycle(last_period, cycle_length):
    last_period = datetime.strptime(last_period, "%d-%m-%Y")
    ovulation_date = last_period + timedelta(days=cycle_length // 2)
    next_period_start_date = last_period_start_date + timedelta(days=cycle_length)
    
    menstrual_end_date = last_period + timedelta(days = 6)
    safe_period_start = last_period - timedelta(days = 7)
    safe_period_end = ovulation_date - timedelta(days = 2)
    
    print(f"Menstrual Phase: {last_period.date()} to {menstrual_end_date.date()}")
    print(f"Ovulation Date: {ovulation_date.date()}")
    print(f"Safe Period: {safe_period_start.date()} to {safe_period_end.date()}")
    print(f"Next Period Start Date: {next_period_start_date.date()}")

def main():
    digit = input("Enter last period date: ")
    digits = input("Enter period duraion: ")

calculate_cycle(digit, digits)
print(f"The rsult is: ", calculate_cycle(digit, digits))