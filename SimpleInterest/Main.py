#for simple interest = (Principal* Rate * Time) / 100

def calculate_simple_interest(principal,rate, time):
    simple_interest = (principal * rate *time)/100
    return simple_interest

print(calculate_simple_interest(1000,3,2))

#compound interest
#A = P * (1 + R/n)^n*T

def collect_values():
    principal = float(input("Enter your principal amount"))
    rate = float(input("Enter the rate in %"))
    time = int(input("Enter your time period"))
    number = int(input("Enter the number of times interest is compounded per year"))
    return [principal, rate,time,number]


def calculate_compound_interest():
    values = collect_values()
    compounding_interest = values[0] *(1 + (values[1]/values[3]))** (values[3]*values[2])
    print(compounding_interest)

calculate_compound_interest()