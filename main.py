import telebot
API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)
controller = {}

@bot.message_handler(commands=['start'])

INVALID_CHOICE = "Введите, пожалуйста, число шаров, которых вы хотите распределить."
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    bot.reply_to(message, text)
bot.polling()
es = text #число шаров, задаётся пользователем"

INVALID_CHOICE = "Введите, пожалуйста, число столбцов, по которым вы хотите распределить шары."
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    bot.reply_to(message, text)
bot.polling()
ek = text #число столбцов, задаётся пользователем"

INVALID_CHOICE = "Введите, пожалуйста, номер конкретного столбца, который вы хотите посмотреть."
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    text = message.text
    bot.reply_to(message, text)
bot.polling()
nk = text #номер конкретного столбца, вводится пользователем"

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
