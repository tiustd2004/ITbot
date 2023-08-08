import telebot
from telebot import types
bot = telebot.TeleBot('')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет', parse_mode='html')
    bot.send_message(message.chat.id, 'Введи команду /prog, чтобы я прислал тебе ссылку, где ты можешь выбрать себе язык программирования ;)')
@bot.message_handler(commands = ['prog'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url = "https://skysmart.ru/articles/programming/top-10-samyh-populyarnyh-yazykov-programmirovaniya"))
    bot.send_message (message.chat.id,'Перейдите на сайт',reply_markup=markup)
    bot.send_message(message.chat.id, 'Введи комманду /next, чтобы продолжить')
@bot.message_handler(commands=['next'])
def choise(message):
    bot.send_message(message.chat.id, 'Какой язык программирования тебе понравился? Скинь цифру топа ;)', parse_mode='html')
@bot.message_handler(content_types = ['text'])
def top(message):
    if message.text == '1':
        markup0 = types.InlineKeyboardMarkup()
        markup1 = types.InlineKeyboardMarkup()
        markup0.add(types.InlineKeyboardButton("Скачать", url = "https://www.java.com/ru/"))
        bot.send_message (message.chat.id,'Java',reply_markup=markup0)
        markup1.add(types.InlineKeyboardButton("ReadME", url = "https://metanit.com/java/tutorial/"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup1)
    if message.text == '2':
        markup2 = types.InlineKeyboardMarkup()
        markup3 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Скачать", url = "https://ru.uptodown.com/windows/c-compilers"))
        bot.send_message (message.chat.id,'Язык C',reply_markup=markup2)
        markup3.add(types.InlineKeyboardButton("ReadME", url = "https://learn.microsoft.com/ru-ru/cpp/c-language/c-language-reference?view=msvc-170"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup3)
    if message.text == '3':
        markup4 = types.InlineKeyboardMarkup()
        markup5 = types.InlineKeyboardMarkup()
        markup4.add(types.InlineKeyboardButton("Скачать", url = "https://www.python.org/downloads/"))
        bot.send_message (message.chat.id,'Python',reply_markup=markup4)
        markup5.add(types.InlineKeyboardButton("ReadME", url = "https://docs.python.org/3/"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup5)
    if message.text == '4':
        markup6 = types.InlineKeyboardMarkup()
        markup7 = types.InlineKeyboardMarkup()
        markup6.add(types.InlineKeyboardButton("Скачать", url = "https://learn.microsoft.com/ru-ru/cpp/windows/latest-supported-vc-redist?view=msvc-170"))
        bot.send_message (message.chat.id,'C++',reply_markup=markup6)
        markup7.add(types.InlineKeyboardButton("ReadME", url = "https://learn.microsoft.com/ru-ru/cpp/cpp/?view=msvc-170"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup7)
    if message.text == '5':
        markup8 = types.InlineKeyboardMarkup()
        markup9 = types.InlineKeyboardMarkup()
        markup8.add(types.InlineKeyboardButton("Скачать", url = "https://www.jetbrains.com/ru-ru/go/download/#section=windows"))
        bot.send_message (message.chat.id,'Golang',reply_markup=markup8)
        markup9.add(types.InlineKeyboardButton("ReadME", url = "https://go.dev/doc/"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup9)
    if message.text == '6':
        markup10 = types.InlineKeyboardMarkup()
        markup11 = types.InlineKeyboardMarkup()
        markup10.add(types.InlineKeyboardButton("Скачать", url = "https://visual-c-sharp.ru.malavida.com/windows/"))
        bot.send_message (message.chat.id,'C#',reply_markup=markup10)
        markup11.add(types.InlineKeyboardButton("ReadME", url = "https://learn.microsoft.com/ru-ru/dotnet/csharp/"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup11)
    if message.text == '7':
        markup12 = types.InlineKeyboardMarkup()
        markup13 = types.InlineKeyboardMarkup()
        markup12.add(types.InlineKeyboardButton("Скачать", url = "https://fortran-lang.org/ru/learn/os_setup/install_gfortran/"))
        bot.send_message (message.chat.id,'Fortran',reply_markup=markup12)
        markup13.add(types.InlineKeyboardButton("ReadME", url = "https://www.fortran90.org/"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup13)
    if message.text == '8':
        markup14 = types.InlineKeyboardMarkup()
        markup15 = types.InlineKeyboardMarkup()
        markup14.add(types.InlineKeyboardButton("Скачать", url = "https://support.microsoft.com/ru-ru/topic/%D0%BA%D0%B0%D0%BA-%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B8%D1%82%D1%8C-javascript-%D0%B2-windows-88d27b37-6484-7fc0-17df-872f65168279"))
        bot.send_message (message.chat.id,'JavaScript',reply_markup=markup14)
        markup15.add(types.InlineKeyboardButton("ReadME", url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup15)
    if message.text == '9':
        markup16 = types.InlineKeyboardMarkup()
        markup17 = types.InlineKeyboardMarkup()
        markup16.add(types.InlineKeyboardButton("Скачать", url = "https://www.php.net/downloads.php"))
        bot.send_message (message.chat.id,'PHP',reply_markup=markup16)
        markup17.add(types.InlineKeyboardButton("ReadME", url = "https://www.php.net/docs.php"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup17)
    if message.text == '10':
        markup18 = types.InlineKeyboardMarkup()
        markup19 = types.InlineKeyboardMarkup()
        markup18.add(types.InlineKeyboardButton("Скачать", url = "https://scratch.ru.uptodown.com/windows"))
        bot.send_message (message.chat.id,'Scratch',reply_markup=markup18)
        markup19.add(types.InlineKeyboardButton("ReadME", url = "https://scratch.by/news/project_news/guide_creative_programming/"))
        bot.send_message (message.chat.id,'Документация', reply_markup=markup19)
    



    

bot.polling(non_stop = True)   