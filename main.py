import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def logo_blackjack():
    clear()
    print(logo)

def random_card():
    '''Return a random card from deck'''
    a = random.choice(cards)
    return a

def check_blackjack(l):
    '''Checking blackjack'''
    if sum(l) < 21:
        return 'min'
    elif sum(l) == 21:
        return 'black'
    else:
        return 'over'


while input('Do you want play BlackJack? (y/n): ').lower() == 'y':

    logo_blackjack()

    player_cards = []
    comp_cards = []

    for _ in range(2):
        player_cards.append(random_card())
        comp_cards.append(random_card())


    if check_blackjack(player_cards) == 'black' and check_blackjack(comp_cards) != 'black':
        print(f'Your final Hand: {player_cards}, final score: {sum(player_cards)}')
        print(f"Computer's final Hand: {comp_cards}, final score: {sum(comp_cards)}")
        print('You win, you got Blackjack')

    elif check_blackjack(player_cards) != 'black' and check_blackjack(comp_cards) == 'black':
        print(f'Your final Hand: {player_cards}, final score: {sum(player_cards)}')
        print(f"Computer's final Hand: {comp_cards}, final score: {sum(comp_cards)}")
        print('You lose, opponent has Blackjack')

    elif check_blackjack(player_cards) == 'black' and check_blackjack(comp_cards) == 'black':
        print('Game over, win win')

    else:
        print(f'Your cards {player_cards}, current score: {sum(player_cards)}')
        print(f"Computer's first card: {comp_cards[0]}")
        while input('Do you need more cards? (y/n): ').lower() == 'y':
            player_cards.append(random_card())
            print(player_cards)
            if sum(player_cards) > 21:
                if 11 in player_cards:
                    i = player_cards.index(11)
                    player_cards = player_cards[:i] + [1] + player_cards[i + 1:]
                else:
                    continue
            else:
                continue

            print(f'Your cards {player_cards}, current score: {sum(player_cards)}')
            print(f"Computer's first card: {comp_cards[0]}")

        while sum(comp_cards) < 18:
            comp_cards.append(random_card())

    print()

    if sum(player_cards) > 21:
        print('Lose, you over')

    elif (sum(player_cards) == sum(comp_cards)) and sum(player_cards) < 22 and sum(comp_cards) < 22 :
        print('win win')

    elif sum(player_cards) < 22 and sum(comp_cards) > 21:
        print('You win')

    elif sum(player_cards) > sum(comp_cards):
        print('You win')

    else:
        print('You lose')


    print(f'Your cards {player_cards}, current score: {sum(player_cards)}')
    print(f"Computer's cards: {comp_cards}, current score: {sum(comp_cards)}")