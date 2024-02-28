cpf_user = "74682489070"
nine_digits = cpf_user[:9]  

count_1 = 10
loop_result_1 = 0

for digit in nine_digits:
    loop_result_1 += (int(digit) * count_1)   
    count_1 -= 1

final_result_1 = ((loop_result_1 * 10) % 11) 

final_result_1 = final_result_1 if final_result_1 <= 9 else 0


ten_digits = nine_digits + str(final_result_1)  

count_2 = 11
loop_result_2 = 0

for digit in ten_digits:
    loop_result_2 += (int(digit) * count_2)   
    count_2 -= 1

final_result_2 = ((loop_result_2 * 10) % 11) 

final_result_2 = final_result_2 if final_result_2 <= 9 else 0


new_cpf = f"{nine_digits}{final_result_1}{final_result_2}"

if cpf_user == new_cpf:
    print(f"{cpf_user} é valido.")
else:
    print("CPF inválido.")