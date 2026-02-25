
test_cases = []
t_test = int(input())  
#input
for i in range(t_test):
    parts_input = input()
    parts = parts_input.split()
    k_cookie = float(parts[0])  
    n_numberofCookies = float(parts[1])  
    moneyofJohn = float(parts[2])  
    test_cases.append((k_cookie,n_numberofCookies ,moneyofJohn ))
#ouput
for i in range(t_test):
    k_cookie,n_numberofCookies ,moneyofJohn = test_cases[i]
    total_cost =  k_cookie* n_numberofCookies
    if total_cost > moneyofJohn:
        s_shortfall = total_cost - moneyofJohn
    else:
        s_shortfall = 0
    
    print(f"{s_shortfall:.2f}")