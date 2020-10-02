def main():
prompt_amount = -1
prompt_instalments = 0
while (prompt_amount < 1 or prompt_amount > 1000):
    prompt_amount = int(input("Enter a donation amount (up to 1000): "))
while prompt_instalments < 1:
    prompt_instalments = int(input("Enter the number of payment instalmets: "))
amount_installments = prompt_amount // prompt_instalments
amount_payed = prompt_amount / amount_installments
amount_payed = int(amount_payed)
print("You will donate", prompt_amount, "dollars in", amount_payed, "instalments of", amount_installments, "dollars.")



if __name__ == "__main__":
    main()