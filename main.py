from art import logo
import random
print(logo)
# Get difficulty value


def restart_game():
    restart = input('Do you need to play again? [y] or [n] ').lower()
    need_to_restart = False
    if restart == 'y':
        print('The game in restarted')
        print('Good luck')
        need_to_restart = True
    elif restart == 'n':
        print("See you soon. Thank you so much")
        need_to_restart = False
    else:
        need_to_restart = False
    print(f'The value pf restart is {need_to_restart}')
    print("#"*80)
    return need_to_restart


def game_guess():
    invalid_diff = False
    chance = 0
    while not invalid_diff:
        difficult = input("Entre difficulty by typing [hard] or [easy] ").lower()
        if difficult == 'hard':
            chance = 5
            invalid_diff = True
        elif difficult == 'easy':
            chance = 10
            invalid_diff = True
        else:
            print(f'{difficult} is invalid value for difficulty level. Try again!!')
            print('='*70)
        cpu_choose = random.choice(range(1, 101))
        remaining_chance = True
        while remaining_chance:
            print(f'You have {chance} attempts remaining to guess the number ')
            user_guess = int(input("Make a guess: "))
            if user_guess == cpu_choose:
                print(f'You guess {user_guess} and is correct . You win')
                # ask to play again
                if restart_game():
                    game_guess()
                else:
                    break
            elif user_guess > cpu_choose:
                print(f'{user_guess} too hight')
                chance -= 1
            elif user_guess < cpu_choose:
                print(f'{user_guess} too low')
                chance -= 1
            if chance == 0:
                remaining_chance = False
                print('You lose')
                if restart_game():
                    game_guess()


game_guess()
