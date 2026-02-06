import telebot
from telebot import types

bot = telebot.TeleBot('8308118957:AAEOCISDb8qxL5D2vi35d6xS0ciAq1_8tQQ')

mp = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
item1 = types.KeyboardButton('🚚Как заказать?')
item2 = types.KeyboardButton('🎯Отзывы')
item3 = types.KeyboardButton('📲Связь с менеджером')
item4 = types.KeyboardButton('🔔Группа')
item5 = types.KeyboardButton('💵Рассчитать стоимость')
item6 = types.KeyboardButton('')
mp.add(item1, item2, item3, item4, item5, item6)

mp2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
item7 = types.KeyboardButton('👟Обувь')
item8 = types.KeyboardButton('👕Верхняя/нижняя одежда')
mp2.add(item7, item8)

mp3 = types.InlineKeyboardMarkup()
item9 = types.InlineKeyboardButton('вернуться к меню', callback_data='menu')
mp3.row(item9)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!' '\n' '\n'
                                'Тут ты можешь рассчитать сумму своего заказа💵''\n'
                                'Связаться с менеджером' '\n'
                                '@DostavkaDewu' '\n'
                                'Получить ответы на все свои вопросы🤔'

                     .format(message.from_user), reply_markup=mp)
    bot.register_next_step_handler(message, button_menu)


@bot.message_handler(types=['text'])
def button_menu(message):
    if message.text.strip() == '💵Рассчитать стоимость':

        bot.send_message(message.chat.id, 'Выберите категорию товара' '\n'
        'От правильного выбора категории зависит стоимость доставки', reply_markup=mp2)
        bot.register_next_step_handler(message, cost_function)
    elif message.text.strip() == '🚚Как заказать?':
        bot.send_message(message.chat.id, '1.Выберите желаемую вами позицию' '\n' '\n'

'2.Откройте меню с размерами, а также стоимостью в юанях''\n' '\n'

'3.Нажмите линейку, дабы определить ваш конечный размер' '\n' '\n'

'4.После успешного выбора размера вам остаётся лишь узнать его цену в юанях, для этого просто нажмите на него' '\n' '\n'

'P.S. Не забудьте скопировать ссылку или артикул желаемого товара' '\n' '\n' '\n'


'КАК СКОПИРОВАТЬ ССЫЛКУ?' '\n'
'После перехода на страницу позиции вам необходимо нажать на кнопку сверху справа (зачастую она зелёная), во всплывающем окне выбрать пункт "скопировать"')
        photo3 = open(r"C:\Users\Андрей\Desktop\BOT\3.jpg", 'rb')
        photo4 = open(r"C:\Users\Андрей\Desktop\BOT\4.jpg", 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_photo(message.chat.id, photo4)
        bot.register_next_step_handler(message, button_menu)
    elif message.text.strip() == '📲Связь с менеджером':
        bot.send_message(message.chat.id, f'📲Связь с менеджером: @DostavkaDewu')
        bot.register_next_step_handler(message, button_menu)
    elif message.text.strip() == '💰Выкупы':
        bot.send_message(message.chat.id, f'💰Выкупы:    https://t.me/STORESTREETBASE')
        bot.register_next_step_handler(message, button_menu)
    elif message.text.strip() == '🎯Отзывы':
        bot.send_message(message.chat.id, f'🎯Отзывы:     https://t.me/STREETBASEOTZIV')
        bot.register_next_step_handler(message, button_menu)
    elif message.text.strip() == '🔔Группа':
        bot.send_message(message.chat.id, f'🔔Группа: https://t.me/STORESTREETBASE')
        bot.register_next_step_handler(message, button_menu)
    else:
        bot.send_message(message.chat.id, 'Упс! Что то пошло не так', reply_markup=mp)
        bot.register_next_step_handler(message, button_menu)


@bot.message_handler(types=['text'])
def cost_function(message):
    global cny, dop_price
    cny = 14.3
    # bot

    if message.text.strip() == '👟Обувь':
        dop_price = 1000
    elif message.text.strip() == '👕Верхняя/нижняя одежда':
        dop_price = 800
    else:
        bot.send_message(message.chat.id, 'Неверный тип товара', reply_markup=mp2)
        bot.register_next_step_handler(message, cost_function)
        return
    photo1 = open(r"C:\Users\Андрей\Desktop\BOT\1.jpg", 'rb')
    photo2 = open(r"C:\Users\Андрей\Desktop\BOT\2.jpg", 'rb')
    bot.send_photo(message.chat.id, photo1)
    bot.send_photo(message.chat.id, photo2)
    bot.register_next_step_handler(message, get_cost)
    bot.send_message(message.chat.id, 'Введите цену товара в юанях ¥' '\n'
    '*Пожалуйста ознакомьтесь с инструкцией выше' '\n' '\n'
                     f'Курс юаня {cny}')


@bot.message_handler(types=['text'])
def get_cost(message):
    amount = message.text.strip()
    try:
        amount = float(amount)
        if amount <= 0:
            bot.send_message(message.chat.id, 'Неправильно указана стоимость товара' '\n'
                             'Введите ЧИСЛО больше НУЛЯ')
            bot.register_next_step_handler(message, get_cost)
            return
    except ValueError:
        bot.send_message(message.chat.id, 'Неправильно указана стоимость товара' '\n'
                         'Введите ЧИСЛО больше НУЛЯ')
        bot.register_next_step_handler(message, get_cost)

        return
    final_price = amount * cny + dop_price + 1500
    bot.send_message(message.chat.id, f'Итоговая цена: {final_price}₽ ' '\n' '\n' 
    '✈️Доставка до России включена в стоимость.' '\n'
    '🚛 СДЭК до вашего города вы оплачиваете отдельно,' '\n'   
    '(при получении)' '\n'  '\n'    
    'Оформить заказ: @DostavkaDewu', reply_markup=mp3)


@bot.callback_query_handler(func=lambda callback: callback.data)
def callback(callback):
    bot.send_message(callback.message.chat.id, 'Спасибо за использовнаие нашего сервиса!'.format(callback.from_user),
                     reply_markup=mp)
    bot.register_next_step_handler(callback.message, button_menu)


bot.polling(none_stop=True)
