def should_serve_customer(customer_age, on_break, time):
    age_ok = customer_age >= 21
    time_ok = 5 <= time <= 10
    return age_ok and time_ok and not on_break