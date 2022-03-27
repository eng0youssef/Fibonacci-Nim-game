# take number of coins from the players
number_of_coins = int(input('enter number of coins: '))

# the first player takes the number he wants,
# provided that he takes less than the number of coins
the_first_player = int(input('player1 enter number of coins you want to take it: '))
while the_first_player > number_of_coins or the_first_player<0:
    the_first_player = int(input('again player1 enter number of coins you want to take it: '))

# the number of coins decreases by the number chosen by the first player
number_of_coins -= the_first_player

# the game ends when the number of coins is zero
while number_of_coins != 0:

    # the second player takes the number he wants,
    # provided that he takes less than double the number of coins for the first player
    the_second_player = int(input('player2 enter number of coins you want to take it: '))
    while the_second_player > number_of_coins or the_second_player > 2*the_first_player or the_second_player<0:
        the_second_player = int(input('again player2 enter number of coins you want to take it: '))

    # the number of coins decreases by the number chosen by the second player
    number_of_coins -= the_second_player

    # if the number of coins becomes zero,the second player wins
    if number_of_coins == 0:
        print("plyer2 is winner")
        break

    # the first player takes the number he wants,
    # provided that he takes less than double the number of coins for the second player
    the_first_player = int(input('player1 enter number of coins you want to take it: '))
    while the_first_player > number_of_coins or the_first_player > 2*the_second_player or the_first_player<0:
        the_first_player = int(input('again player1 enter number of cons you want to take it:'))

    # the number of coins decreases by the number chosen by the first player
    number_of_coins -= the_first_player

    # if the number of coins becomes zero,the first player wins
    if number_of_coins == 0:
        print("plyer1 is winner")
        break