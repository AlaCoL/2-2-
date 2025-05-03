import telebot
import random
import os

bot = telebot.TeleBot("7047947994:AAGqnklImKWS-fAmamMHe_ym3w3WfW_TSx4")
# memes = os.listdir("./jpeg")
# animals_memes = os.listdir("./jpeg")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)

@bot.message_handler(commands=['help']) 
def send_heh(message):
    bot.reply_to(message, "Команды: start or hello-Bot Здаровается, heh-пишешь heh любая цифра пример heh, calc-Калькулятор, mem-мемы, ecology-Экология")  
    #ВАриант2 
    #bot.reply_to(message, "Команды:")   
    #bot.reply_to(message, "start or hello-Bot Здаровается")
    #bot.reply_to(message, "heh-пишешь heh цифра любая пример heh 1")
    #bot.reply_to(message, "calc-Калькулятор")
    #bot.reply_to(message, "mem-мемы")
@bot.message_handler(commands=['ecology','eco'])
def ecology(message):
    bot.reply_to(message,'''Что вы хотите сделать с пластика?
                        "/1:Ремесла и творчество."
                        "/2: Строительство и благоустройство."
                        "/3: В промышленности."
                        "/4: Что не стоит делать."
                        "/1-/4: Выберите что вам надо."
                        "/0 Если вы не нашли что вам надо напишите боте что бы бот понял какая тебу нужна."
                    ''')
    @bot.message_handler(commands=['1']) 
    def eco_1(message):
        bot.reply_to(message, '''Ремесла и творчество.
"1: Вы можите сдать мусор на металлолом."
"2: Поделки и украшения — из бутылок, крышек, пластиковых ложек и др."
"3: Горшки для растений, кормушки, органайзеры."
"4: Мебель из пластиковых бутылок — пуфики, столики и пр."
''')

    @bot.message_handler(commands=['2']) 
    def eco_2(message):
        bot.reply_to(message, '''Строительство и благоустройство.
"1: Пластиковые панели и плиты."
"2: Тротуарная плитка из переработанного пластика."
"3: Заборы и скамейки."
''')
    @bot.message_handler(commands=['3']) 
    def eco_3(message):    
        bot.reply_to(message, '''В промышленности.
"1: Композитные материалы — смешивание с древесиной, стекловолокном."
"2: Автозапчасти, корпуса техники, упаковка."
''')
    @bot.message_handler(commands=['4']) 
    def eco_4(message): 
        bot.reply_to(message, '''Что не стоит делать.
"1: Сжигать пластик в домашних условиях — это опасно для здоровья."
"2: Захоранивать без переработки — он разлагается сотни лет."
''')
    @bot.message_handler(commands=['0']) 
    def eco_0(message):  
        bot.reply_to(message, 'Простите мы ещё не сделали это скоро будет')
@bot.message_handler(commands=['animals'])   
def animals(message):
    global animals_memes
    
    r_animals = random.choice(animals_memes)
    with open(f"animals/{random.choice(animals_memes)}", "rb") as f:
        bot.send_photo(message.chat.id, f)
    animals_memes.remove(r_animals)
    # if animals_memes == []:
    #     animals_memes = os.listdir("./img")
        
@bot.message_handler(commands=['mem'])
def mem(message):
    global memes
    
    r_mem = random.choice(memes)
    with open(f"jpeg/{random.choice(memes)}", "rb") as f:
        bot.send_photo(message.chat.id, f)
    memes.remove(r_mem)
    if memes == []:
        memes = os.listdir("./img")
     
        
        
@bot.message_handler(commands=['calc']) 
def calc(message):
    words = message.text.split()
    if len(words) > 2:
        if words[1] ==  "summa":
            number = int(words[2])
            summa = 0
            if number < 0:
                for i in range(0, number - 1, -1):
                    summa += i
            elif number > 0:
                for i in range(0, number + 1):
                    summa += i
            else:
                summa = 0
            bot.reply_to(message, f'Сумма всех чисел от 0 до {number} составила {summa}!')
        else:
            if len(words) == 4:
                number1 = int(words[1])
                number2 = int(words[3])
                simbol = words[2]
                result = 0
                if simbol == "+":
                    result = number1 + number2
                if simbol == "-":
                    result = number1 - number2
                if simbol == "*":
                    result = number1 * number2
                if simbol == "/":
                    if number2 != 0:
                        result = number1 / number2
                    else:
                        result = "Ошибка"
                        bot.reply_to(message, f'Результат {result}')
            
            
    else:
        bot.reply_to(message, f'Ошибка')
        
bot.polling()               