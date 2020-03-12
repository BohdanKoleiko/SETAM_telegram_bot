import telebot
from key_but import *
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)


def start_menu():
    main_menu = 'Головне меню'
    return main_menu

def WhatIsSetam_menu():
    second_menu = 'Меню питання щодо Setam'
    return second_menu

def Bidding_menu():
    bid = "Меню: Взяти участь у торгах"
    return bid

def req_user(message):
    user = 'Пользователь {0} @{1} воспользовался(лась) ботом'.format(message.chat.first_name, message.chat.username)
    return user

@bot.message_handler(regexp='Головне меню')
@bot.message_handler(commands=['start'])
def send_start_keyboard(message):
    # print(req_user(message))
    key_but = types.ReplyKeyboagitrdMarkup(row_width=1, resize_keyboard=True)
    key_but.add(*START_KEYBOARD.values())
    with open('/home/bogdan/My_python_projekt/bot/doc/About bot.txt', 'r') as f:
        txt = f.read()
        bot.send_message(chat_id=message.chat.id, text=txt, reply_markup=key_but)
        f.close()


@bot.message_handler(regexp='Меню питання щодо Setam')
@bot.message_handler(func=lambda msg: msg.text in START_KEYBOARD.values())
def send_menu_answer(msg):
    if (msg.text == START_KEYBOARD.get('WhatIsSetam')) or (msg.text == 'Меню питання щодо Setam'):
        key_but = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        key_but.add(*WhatIsSetam.values())
        key_but.row(start_menu())
        with open('/home/bogdan/My_python_projekt/bot/doc/Choose one option.txt', 'r') as c:
            txt = c.read()
            bot.send_message(chat_id=msg.chat.id, text=txt, reply_markup=key_but)
            c.close()

    if msg.text == START_KEYBOARD.get('OtherServicesSetam'):
        key_but_1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        key_but_1.add(*OtherServicesSetam.values(), start_menu())
        with open('/home/bogdan/My_python_projekt/bot/doc/Choose one option.txt', 'r') as q:
            txt = q.read()
            bot.send_message(chat_id=msg.chat.id, text=txt, reply_markup=key_but_1)
            q.close()


@bot.message_handler(regexp="Меню: Взяти участь у торгах")
@bot.message_handler(func=lambda msg: msg.text in WhatIsSetam.values())
def send_menu_WhatIsSetam(msg):
    if (msg.text == WhatIsSetam.get('Bidding')) or (msg.text == "Меню: Взяти участь у торгах"):
        key_but = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        key_but.add(*Bidding.values())
        key_but.row(WhatIsSetam_menu(), start_menu())
        with open('/home/bogdan/My_python_projekt/bot/doc/Choose one option.txt', 'r') as c:
            txt = c.read()
            bot.send_message(chat_id=msg.chat.id, text=txt, reply_markup=key_but)
            c.close()

    if (msg.text == WhatIsSetam.get('FinanIss')) or (msg.text == 'Меню питання щодо Setam'):
        key_but_2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        key_but_2.add(*FinanIss.values())
        key_but_2.row(WhatIsSetam_menu(), start_menu())
        with open('/home/bogdan/My_python_projekt/bot/doc/Choose one option.txt', 'r') as c:
            txt = c.read()
            bot.send_message(chat_id=msg.chat.id, text=txt, reply_markup=key_but_2)
            c.close()

    if msg.text == WhatIsSetam.get('Familiarization'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Apply for familiarization with the property.txt', 'r') as f:
            txt_familiarization = f.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_familiarization)
            f.close()

    if msg.text == WhatIsSetam.get('VoluntarySale'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Voluntary sale.txt', 'r') as v:
            txt_voluntary = v.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_voluntary)
            v.close()


@bot.message_handler(func=lambda msg: msg.text in Bidding.values())
def send_bidding(msg):
    if msg.text == Bidding.get('Registers'):
        key_but = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        key_but.add(*Registers.values())
        key_but.row(Bidding_menu())
        key_but.row(start_menu())
        with open('/home/bogdan/My_python_projekt/bot/doc/Choose one option.txt', 'r') as c:
            txt = c.read()
            bot.send_message(chat_id=msg.chat.id, text=txt, reply_markup=key_but)
            c.close()

    if msg.text == Bidding.get('ApplyForAuction'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Apply for the Auction.txt', 'r') as a:
            txt = a.read()
            bot.send_message(chat_id=msg.chat.id, text=txt)
            a.close()


@bot.message_handler(func=lambda msg: msg.text in Registers.values())
def send_reg_info(msg):
    if msg.text == Registers.get('RegForIndividuals'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Registration for individuals.txt', 'r') as r:
            txt_individ = r.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_individ)
            r.close()

    if msg.text == Registers.get('RegForLegalEntities'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Registration for legal entities.txt', 'r') as r:
            txt_entities = r.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_entities)
            r.close()

    if msg.text == Registers.get('EdPersonalInfo'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Editing personal information.txt', 'r') as e:
            txt_edit_pers = e.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_edit_pers)
            e.close()

    if msg.text == Registers.get('ProblemsWithReg'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Problems with registration.txt', 'r') as p:
            txt_problem_reg = p.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_problem_reg)
            p.close()


@bot.message_handler(func=lambda msg: msg.text in FinanIss.values())
def send_finans_info(msg):
    if msg.text == FinanIss.get('Individuals'):
        with open('/home/bogdan/My_python_projekt/bot/doc/For individuals.txt', 'r') as f:
            txt_individuals = f.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_individuals)
            f.close()

    if msg.text == FinanIss.get('Entities'):
        with open('/home/bogdan/My_python_projekt/bot/doc/For legal entities.txt', 'r') as f:
            txt_entities = f.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_entities)
            f.close()

    if msg.text == FinanIss.get('Remuneration'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Extra Reward.txt', 'r') as e:
            txt_reward = e.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_reward)
            e.close()

    if msg.text == FinanIss.get('WarrantyСontribution'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Return of the guarantee fee.txt', 'r') as r:
            txt_guarantee_fee = r.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_guarantee_fee)
            r.close()

    if msg.text == FinanIss.get('ReasonsForReturn'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Reasons for the refund of the guarantee fee.txt', 'r') as r:
            txt_refund_guarantee_fee = r.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_refund_guarantee_fee)
            r.close()


@bot.message_handler(func=lambda msg: msg.text in OtherServicesSetam.values())
def send_answer_mariage(msg):
    if msg.text == OtherServicesSetam.get('Marriage'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Marriage for the day.txt', 'r') as m:
            txt = m.read()
            bot.send_message(chat_id=msg.chat.id, text=txt)
            m.close()

    if msg.text == OtherServicesSetam.get('FreeTransfer'):
        with open('/home/bogdan/My_python_projekt/bot/doc/Free transfer.txt', 'r') as f:
            txt_transfer = f.read()
            bot.send_message(chat_id=msg.chat.id, text=txt_transfer)
            f.close()

# print('start bot')
bot.polling()