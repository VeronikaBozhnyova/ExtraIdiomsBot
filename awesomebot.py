import json
import telebot
from telebot import types


token = '465704493:AAGFQHyBMHes-gLMuqDllCaGQANu0vPYW4A'
bot = telebot.TeleBot(token)


with open(r'C:\Texts\tasks.txt') as json_file1:
    tasks_data = json.load(json_file1)

    for n in tasks_data['tasks']:

        @bot.message_handler(commands=['start'])
        def start(m):
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(letter) for letter in ['A)', 'B)']])
            keyboard.add(*[types.KeyboardButton(letter) for letter in ['C)', 'D)']])
            q1 = bot.send_message(m.chat.id, '1. ' + n['1'], reply_markup=keyboard)
            bot.register_next_step_handler(q1, qstn2)

        with open(r'C:\Texts\correctanswers.txt') as json_file2:
            correct_answers_data = json.load(json_file2)

            for p in correct_answers_data['correctanswers']:

                def qstn2(m):
                    if m.text == p['1']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q2 = bot.send_message(m.chat.id, '2. ' + n['2'])
                        bot.register_next_step_handler(q2, qstn3)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn3(m):
                    if m.text == p['2']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q3 = bot.send_message(m.chat.id, '3. ' + n['3'])
                        bot.register_next_step_handler(q3, qstn4)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn4(m):
                    if m.text == p['3']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q4 = bot.send_message(m.chat.id, '4. ' + n['4'])
                        bot.register_next_step_handler(q4, qstn5)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn5(m):
                    if m.text == p['4']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q5 = bot.send_message(m.chat.id, '5. ' + n['5'])
                        bot.register_next_step_handler(q5, qstn6)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn6(m):
                    if m.text == p['5']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q6 = bot.send_message(m.chat.id, '6. ' + n['6'])
                        bot.register_next_step_handler(q6, qstn7)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)


                def qstn7(m):
                    if m.text == p['6']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q7 = bot.send_message(m.chat.id, '7. ' + n['7'])
                        bot.register_next_step_handler(q7, qstn8)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn8(m):
                    if m.text == p['7']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q8 = bot.send_message(m.chat.id, '8. ' + n['8'])
                        bot.register_next_step_handler(q8, qstn9)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn9(m):
                    if m.text == p['8']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q9 = bot.send_message(m.chat.id, '9. ' + n['9'])
                        bot.register_next_step_handler(q9, qstn10)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn10(m):
                    if m.text == p['9']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q10 = bot.send_message(m.chat.id, '10. ' + n['10'])
                        bot.register_next_step_handler(q10, qstn11)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn11(m):
                    if m.text == p['10']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q11 = bot.send_message(m.chat.id, '11. ' + n['11'])
                        bot.register_next_step_handler(q11, qstn12)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn12(m):
                    if m.text == p['11']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q12 = bot.send_message(m.chat.id, '12. ' + n['12'])
                        bot.register_next_step_handler(q12, qstn13)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn13(m):
                    if m.text == p['12']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q13 = bot.send_message(m.chat.id, '13. ' + n['13'])
                        bot.register_next_step_handler(q13, qstn14)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn14(m):
                    if m.text == p['13']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q14 = bot.send_message(m.chat.id, '14. ' + n['14'])
                        bot.register_next_step_handler(q14, qstn15)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn15(m):
                    if m.text == p['14']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q15 = bot.send_message(m.chat.id, '15. ' + n['15'])
                        bot.register_next_step_handler(q15, qstn16)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn16(m):
                    if m.text == p['15']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q16 = bot.send_message(m.chat.id, '16. ' + n['16'])
                        bot.register_next_step_handler(q16, qstn17)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn17(m):
                    if m.text == p['16']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q17 = bot.send_message(m.chat.id, '17. ' + n['17'])
                        bot.register_next_step_handler(q17, qstn18)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn18(m):
                    if m.text == p['17']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q18 = bot.send_message(m.chat.id, '18. ' + n['18'])
                        bot.register_next_step_handler(q18, qstn19)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn19(m):
                    if m.text == p['18']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q19 = bot.send_message(m.chat.id, '19. ' + n['19'])
                        bot.register_next_step_handler(q19, qstn20)
                    else:
                        bot.send_message(m.chat.id, 'Wrong!')
                        start(m)

                def qstn20(m):
                    if m.text == p['19']:
                        bot.send_message(m.chat.id, 'Correct!')
                        q20 = bot.send_message(m.chat.id, '20. ' + n['20'])
                    bot.register_next_step_handler(q20, final)


                def final(m):
                    if m.text == p['20']:
                        bot.send_message(m.chat.id, 'Congratulations! Now you are a god of idioms!')
                    else:
                        bot.send_message(m.chat.id, 'Ugh! This is so disgraceful.')
                        start(m)


                @bot.message_handler(commands=['help'])
                def help(m):
                    keyboard = types.InlineKeyboardMarkup()
                    url_button = types.InlineKeyboardButton(text="Idioms and phrases",
                                                            url="http://idioms.thefreedictionary.com/")
                    keyboard.add(url_button)
                    bot.send_message(m.chat.id, "Go read the dictionary and then you can get back to practice.",
                                     reply_markup=keyboard)


bot.polling()
