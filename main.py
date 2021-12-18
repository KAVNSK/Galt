import telebot
import Knopli as kb

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

controller = {}
es = None
ek = None

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id,
                     """
                     Это Гальтон-бот! Здесь вы можете посмотерть на конкретное распределение шаров на доске Гальтона!
                     """,  reply_markup=kb.main_kb)
    user_id = message.from_user.id
    controller[user_id] = 'start'

@bot.message_handler(content_types=['text'])
def start(message):
    user_id = message.from_user.id
    user_choice = message.text
    user_state = controller.get(user_id, 'start') # Если вдруг такой user_id не сохранен, то считаем, что статус = start
    #answer = 'none'
    answer = start_handler(user_id, user_choice)
    if user_state == 'ready_to_play':
        galton_desk()


def start_handler(user_id, user_choice):

    if controller[user_id] == 'ball_count':
        es = int(user_choice)
        mes = 'Я получил число шаров = ' + str(es)
        bot.send_message(user_id, mes)

    if user_choice == "Ввести количество шаров":
        INVALID_CHOICE = "Введите, пожалуйста, число шаров, которых вы хотите распределить."
        bot.send_message(user_id, INVALID_CHOICE)
        controller[user_id] = 'ball_count'
    if user_choice == "Ввести число столбцов":
        INVALID_CHOICE: str = "Введите, пожалуйста, число столбцов, по которым вы хотите распределить шары."
        bot.send_message(user_id, INVALID_CHOICE)
    if user_choice == "Ввести номер интересующего столба":
        INVALID_CHOICE: str = "Введите, пожалуйста, номер конкретного столбца, который вы хотите посмотреть."
        bot.send_message(user_id, INVALID_CHOICE)

    if es != None and ek != None:
        controller[user_id] = 'ready_to_play'

def galton_desk():
    pass

bot.polling()
#nomerstolba():

'''
@bot.message_handler(func=lambda message: True)
def echo_message(message):
text = message.text
bot.reply_to(message, text)
bot.polling()
es = text #число шаров, задаётся пользователем"
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    bot.reply_to(message, text)
bot.polling()
ek = text #число столбцов, задаётся пользователем"
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    bot.reply_to(message, text)
bot.polling()
nk = text #номер конкретного столбца, вводится пользователем"

######################

n = ek-1 #глубина счёта"
e = 2**n #суммарный биноминальный коэффициент для глубины"

fn = 1 #хранение фаториала числа n"
if (n % 1 == 0 and n >= 0): #проверка на натуральность"
    # считаем факториал числа n
    for i in range(1, n + 1):
        fn = i * fn
# Если n - отрицательное или нецелое число, выводим сообщение об ошибке
else:
    print('Невозможно вычислить факториал нецелого и/или отрицательного числа!')
#так высчитали n!

ffk =nk-1 #нумерация столбов начинается с 0 по этому делаем сдвиг
fk = 1 #хранение фаториала числа nk
if (ffk % 1 == 0 and ffk >= 0): #проверка на натуральность"
    # считаем факториал числа nk!
    for i in range(1, ffk + 1):
        fk = i * fk
# Если n - отрицательное или нецелое число, выводим сообщение об ошибке
else:
    print('Невозможно вычислить факториал нецелого и/или отрицательного числа!')
#так высчитали nk!

ech = n - ffk #разница k-n в C из n по k
feach = 1 #хранение фаториала числа each
if (ech % 1 == 0 and ech >= 0): #проверка на натуральность"
    # считаем факториал числа nk!
    for i in range(1, ech + 1):
        feach = i * feach
# Если n - отрицательное или нецелое число, выводим сообщение об ошибке
else:
    print('Невозможно вычислить факториал нецелого и/или отрицательного числа!')

#Рассчёт биноминального коэффициента конкретного столбца
c= fn/(fk*feach)
#Рассчёт числа шаров через вероятность
nsk=es*c/e
print(nsk)
'''
