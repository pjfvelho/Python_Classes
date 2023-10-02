
def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax

# We call this function the same way we called the first function. The next code cell calculates the paycheck, based on working 40 hours. (After taxes, it is $528.)

# Calculate pay based on working 40 hours
pay_fulltime = get_pay(40)
print(pay_fulltime)

# To quickly calculate pay based on a different number of hours worked, you need to supply the function with a different number. For instance, say your friend works 32 hours. (Then, they get $422.40.)

pay_parttime = get_pay(32)
print(pay_parttime)

