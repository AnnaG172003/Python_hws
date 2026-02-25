def convert_US_to_MPesos(US_dollar):
    money_rate = 1/0.058
    peso = US_dollar * money_rate
    return peso
money = float(input("US Dollar : $"))
convert_Mpesos = convert_US_to_MPesos(money)
print (f"Mexico Peso: ${convert_Mpesos:.2f}")