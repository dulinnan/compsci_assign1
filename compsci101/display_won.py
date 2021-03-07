def display_has_won_feedback(player_name, number_of_guesses):
    line1 = ""
   
    if number_of_guesses == 1:
        output = "guess"
    else:
        output = "guesses"
 
    line3 = print("   Congratulations ", player_name, ", You guessed the letters in ", number_of_guesses," ", output,".", sep="")
 
    player_name_legnth = len(player_name)
    output_legnth = len(output)
    number_of_guesses_legnth = len(str(number_of_guesses))
    legnth = number_of_guesses_legnth + output_legnth + player_name_legnth
   
    total_legnth = 49 + legnth
    star_amount = "*" * total_legnth
 
    line2 =  star_amount
    line4 =  star_amount
 
    print(line1)
    print(line2)
    print(line3)
    print(line4)


if __name__ == "__main__":
    display_has_won_feedback("Lia", 1)