import random

def game():
    while True:
        player_choice = input("Выберите вариант: камень, ножницы, бумага (для выхода напишите end): ").lower()
        while player_choice not in ["камень", "ножницы", "бумага", "end"]:
            print("Некорректный ввод. Пожалуйста, попробуйте еще раз.")
            
            
        choices = ["камень", "ножницы", "бумага"]
        computer_choice = random.choice(choices)
        
        print(f"\nВы выбрали {player_choice}, компьютер выбрал {computer_choice}.\n")
        if player_choice == computer_choice:
            print("Ничья!")
        elif (player_choice == "камень" and computer_choice == "ножницы") or \
             (player_choice == "ножницы" and computer_choice == "бумага") or \
             (player_choice == "бумага" and computer_choice == "камень"):
            print("Победа!")
        else:
            print("Поражение!")
        play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        if play_again != "да":
            break
game()
       
