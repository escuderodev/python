# identificar o valor do desconto
valor_produto = float(input("\nInforme o valor do produto R$: "))
porcentagem_desconto = int(input("Informe a porcentagem de desconto: "))
desconto = (valor_produto / 100) * porcentagem_desconto

# descobrir o valor com desconto
valor_com_desconto = valor_produto - desconto

# descobrir o valor do troco
valor_pago = float(input("Informe o valor pago R$: "))
troco = valor_pago - valor_com_desconto

# resultado
print(f"""
      === Resultado ===
      Valor do Produto: R$ {valor_produto:.2f}
      Desconto de {porcentagem_desconto}%
      Valor do Desconto: R$ {desconto:.2f}
      Novo valor do Produto: R$ {valor_com_desconto:.2f}
      Valor Pago: R$ {valor_pago:.2f}
      Troco: R$ {troco:.2f}
      """)