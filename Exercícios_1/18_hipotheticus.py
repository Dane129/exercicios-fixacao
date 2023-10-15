horanormal = float(input("Quantas horas normais trabalhadas?"))
horaextra = float(input("Quantas horas extras trabalhadas?"))
horanormal = horanormal * 10
horaextra = horaextra * 15
bruto = horanormal + horaextra
bruto2 = bruto *  0.10
liquido = bruto - bruto2
print("O salário bruto é", bruto, " o líquido é", liquido)
