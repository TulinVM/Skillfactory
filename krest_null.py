import pyautogui


# Приветствие и правила игры.
def regulations():
    print()
    print('*' * 10, '\033[32m  Крестики - Нолики  \033[0m', '*' * 10)  # немного цвета в приветствие
    print('         Добро пожаловать друзья !')
    print()

    decision = input('Хотите прочитать правила?: ').lower()  # исключаем проблему ввода в различных регистрах
    while decision != 'да' and decision != 'нет':            # проверка на корректность ответа
        print('Введите корректный ответ ДА или НЕТ')
        decision = input('Хотите прочитать правила?: ').lower()

    if decision == 'да':
        res = pyautogui.confirm(text='* Игроки по очереди делают ход на свободные клетки поля.\n'
                                     '* Задача первым выставить 3 свои фишки по вертикали, горизонтали или диагонали.\n'
                                     '* Первый ход делает игрок, расставляющий крестик.\n'
                                     '* Для хода, необходимо ввести номер ячейки поля от 1 до 9 \n'
                                     ,
                                title='Правила игры «Крестики-нолики»',
                                buttons=['Начнем игру', 'В другой раз'])
        if res == 'В другой раз':
            print('Очень жаль, что вы передумали.\n''До новых встреч.')
            exit()
    elif decision == 'нет':
        print('Тогда начнем!')
        print()


regulations()
print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")
