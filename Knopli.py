from telebot import types
from aiogram.types import ReplyKeyboardRemove
#button_1 = types.KeyboardButton('Старт')
button_2 = types.KeyboardButton('Сброс')
button_3 = types.KeyboardButton('Ввести количество шаров')
button_4 = types.KeyboardButton('Ввести число столбцов')
button_5 = types.KeyboardButton('Ввести номер интересующего столба')
#надо ввести ввод строки или будет показывать какая строка по счёту
# или ввести массив и по нему искать число, которое хочет спросить пользоватеь.
main_kb = types.ReplyKeyboardMarkup()
main_kb.add(button_2).add(button_3).add(button_4).add(button_5)
