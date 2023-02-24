import random

import telebot
import config
bot = telebot.TeleBot(config.pubginfo_t)
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def keyboard_buttons():
    markup = ReplyKeyboardMarkup()
    itembtn1 = KeyboardButton('Зброя🏹')
    itembtn2 = KeyboardButton('Тест📄')
    itembtn3 = KeyboardButton('Обрати зброю🔫')
    itembtn4 = KeyboardButton('Карти🗺')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    return markup

def inlb():
    markup = InlineKeyboardMarkup()
    ib1 = InlineKeyboardButton('Штурмові Гвинтівки', callback_data="AR")
    ib2 = InlineKeyboardButton('Марксмарські Гвинтівки', callback_data="DMR")
    ib3 = InlineKeyboardButton('Снайперські Гвинтівки', callback_data="SR")
    ib4 = InlineKeyboardButton('Пістолети-Кулемети', callback_data="PP")
    ib5 = InlineKeyboardButton('Кулемети', callback_data="P")
    ib6 = InlineKeyboardButton('Пістолети', callback_data="PT")
    ib7 = InlineKeyboardButton('Гранати', callback_data="G")
    ib8 = InlineKeyboardButton('Холодна Зброя', callback_data="C")
    ib9 = InlineKeyboardButton('Дробовик', callback_data="DB")
    ib10 = InlineKeyboardButton('Арбалет', callback_data="ARB")
    markup.add(ib1, ib2, ib3, ib4, ib5, ib6, ib7, ib8, ib9, ib10)
    return markup
def inb2():
    markup = InlineKeyboardMarkup()
    ib21 = InlineKeyboardButton('Розпочати!', callback_data="StartTest")

    markup.add(ib21)
    return markup
def AR():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('AUG A3', callback_data="AUG")
    ar2 = InlineKeyboardButton('G36C', callback_data="G36C")
    ar3 = InlineKeyboardButton('M16A4', callback_data="M16A4")
    ar4 = InlineKeyboardButton('M416', callback_data="M416")
    ar5 = InlineKeyboardButton('QBZ', callback_data="QBZ")
    ar6 = InlineKeyboardButton('SCAR-L', callback_data="SCAR-L")
    ar7 = InlineKeyboardButton('M762', callback_data="M762")
    ar8 = InlineKeyboardButton('AKM', callback_data="AKM")
    ar9 = InlineKeyboardButton('ГРОЗА', callback_data="GROZA")
    ar10 = InlineKeyboardButton('Mk47 Mutant', callback_data="Mk47 Mutant")
    markup.add(ar1, ar2, ar3, ar4, ar5, ar6, ar7, ar8, ar9, ar10)
    return markup
def DMR():
    markup = InlineKeyboardMarkup()
    dmr1 = InlineKeyboardButton('ВСС', callback_data="VSS")
    dmr2 = InlineKeyboardButton('Mini 14', callback_data="MINI14")
    dmr3 = InlineKeyboardButton('QBU', callback_data="QBU")
    dmr4 = InlineKeyboardButton('SKS', callback_data="SKS")
    dmr5 = InlineKeyboardButton('SLR', callback_data="SLR")
    dmr6 = InlineKeyboardButton('Mk14', callback_data="Mk14")
    markup.add(dmr1, dmr2, dmr3, dmr4, dmr5, dmr6)
    return markup
def PP():
    markup = InlineKeyboardMarkup()
    sr1 = InlineKeyboardButton('UZI', callback_data="UZI")
    sr2 = InlineKeyboardButton('Vector', callback_data="VECTOR")
    sr3 = InlineKeyboardButton('UMP45', callback_data="UMP45")
    sr4 = InlineKeyboardButton('Tommy Gun', callback_data="TOMMYGUN")
    markup.add(sr1, sr2, sr3, sr4)
    return markup

def SR():
    markup = InlineKeyboardMarkup()
    sr1 = InlineKeyboardButton('Win94', callback_data="WIN94")
    sr2 = InlineKeyboardButton('Kar98K', callback_data="KAR98K")
    sr3 = InlineKeyboardButton('M24', callback_data="M24")
    sr4 = InlineKeyboardButton('AWM', callback_data="AWM")
    markup.add(sr1, sr2, sr3, sr4)
    return markup

def DB():
    markup = InlineKeyboardMarkup()
    sr1 = InlineKeyboardButton('Обріз', callback_data="OBREZ")
    sr2 = InlineKeyboardButton('S12K', callback_data="S12K")
    sr3 = InlineKeyboardButton('S1897', callback_data="S1897")
    sr4 = InlineKeyboardButton('S686', callback_data="S686")
    markup.add(sr1, sr2, sr3, sr4)
    return markup
def P():
    markup = InlineKeyboardMarkup()
    sr1 = InlineKeyboardButton('M249', callback_data="M249")
    sr2 = InlineKeyboardButton('DP28', callback_data="DP28")

    markup.add(sr1, sr2)
    return markup

def PT():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('R45', callback_data="R45")
    ar2 = InlineKeyboardButton('R1895', callback_data="R1895")
    ar3 = InlineKeyboardButton('P1911', callback_data="P1911")
    ar4 = InlineKeyboardButton('P92', callback_data="P92")
    ar5 = InlineKeyboardButton('P18C', callback_data="P18C")
    ar6 = InlineKeyboardButton('Skorpion', callback_data="Skorpion")
    ar7 = InlineKeyboardButton('Flare Gun', callback_data="FlareGun")

    markup.add(ar1, ar2, ar3, ar4, ar5, ar6, ar7)
    return markup
def G():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('Осколкова граната', callback_data="FRAGGRENADE")
    ar2 = InlineKeyboardButton('Коктейль Молотова', callback_data="MOLOTOV")
    ar3 = InlineKeyboardButton('Світло-шумова граната', callback_data="LIGHT")
    ar4 = InlineKeyboardButton('Димова Граната', callback_data="SMOKE")
    ar5 = InlineKeyboardButton('Яблуко', callback_data="APPLE")
    ar6 = InlineKeyboardButton('Сніжок', callback_data="SNOWBALL")


    markup.add(ar1, ar2, ar3, ar4, ar5, ar6)
    return markup
def C():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('Удар', callback_data="PUNCH")
    ar2 = InlineKeyboardButton('Удар під час стрибку', callback_data="JPUNCH")
    ar3 = InlineKeyboardButton('Лом', callback_data="LOM")
    ar4 = InlineKeyboardButton('Мачете', callback_data="MACHETE")
    ar5 = InlineKeyboardButton('Серп', callback_data="SERP")
    ar6 = InlineKeyboardButton('Сковорідка', callback_data="PAN")


    markup.add(ar1, ar2, ar3, ar4, ar5, ar6)
    return markup

def T1():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('Ближній бій', callback_data="short")
    ar2 = InlineKeyboardButton('Середній бій', callback_data="mid")
    ar3 = InlineKeyboardButton('Дальній бій', callback_data="long")
    markup.add(ar1, ar2, ar3)
    return markup
def T2():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('Рухомі', callback_data="move")
    ar2 = InlineKeyboardButton('Нерухомі', callback_data="nmove")
    markup.add(ar1, ar2)
    return markup
def T22():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('Рухомі', callback_data="move2")
    ar2 = InlineKeyboardButton('Нерухомі', callback_data="nmove2")
    markup.add(ar1, ar2)
    return markup
def T23():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('Рухомі', callback_data="move3")
    ar2 = InlineKeyboardButton('Нерухомі', callback_data="nmove3")
    markup.add(ar1, ar2)
    return markup
def T3():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('Так', callback_data="yes")
    ar2 = InlineKeyboardButton('Ні', callback_data="no")
    markup.add(ar1, ar2)
    return markup
def T32():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('Так', callback_data="yes2")
    ar2 = InlineKeyboardButton('Ні', callback_data="no2")
    markup.add(ar1, ar2)
    return markup

def T33():
    markup = InlineKeyboardMarkup()
    ar1 = InlineKeyboardButton('Так', callback_data="yes3")
    ar2 = InlineKeyboardButton('Ні', callback_data="no3")
    markup.add(ar1, ar2)
    return markup

def M():
    markup = InlineKeyboardMarkup()
    sr1 = InlineKeyboardButton('Ерангель', callback_data="erangel")
    sr2 = InlineKeyboardButton('Мірамар', callback_data="miramar")
    sr3 = InlineKeyboardButton('Санук', callback_data="sanuk")
    sr4 = InlineKeyboardButton('Вікенді', callback_data="vikendy")
    markup.add(sr1, sr2, sr3, sr4)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.text:
        print(message.from_user.last_name, message.from_user.first_name, ": IS STARTING, userID:", message.from_user)
        bot.send_message(message.chat.id, f"Добрий день {message.from_user.first_name}", reply_markup=keyboard_buttons())

@bot.message_handler(content_types=['text'])
def conversation(message):
    if message.text == "Зброя🏹":
        bot.send_message(message.chat.id, "Оберіть Категорію Зброї", reply_markup=inlb())
        print(message.from_user)
    elif message.text == "Тест📄":
        bot.send_message(message.chat.id, "Це тест на 82 питання на тему PUBG MOBILE.", reply_markup=inb2())
        print(message.from_user)
    elif message.text == 'Обрати зброю🔫':
        bot.send_message(message.chat.id, "На які дистанції ви стріляєте?", reply_markup=T1())
        print(message.from_user)
    elif message.text == "Карти🗺":
        bot.send_message(message.chat.id, "Оберіть карту", reply_markup=M())
        print(message.from_user)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "StartTest":
        bot.send_message(call.from_user.id, "Заходьте за посиланням та вказуйте своє ім'я. https://www.classtime.com/code/QQ86W2")
    elif call.data == "AR":
        bot.send_message(call.from_user.id, "Оберіть зброю", reply_markup=AR())
    elif call.data == "AUG":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_auga3-9832c8cc.png", caption=config.AUG, reply_markup=AR())
    elif call.data == "G36C":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_g36c-c0ef5e6c.png", caption=config.G36C, reply_markup=AR())
    elif call.data == "M16A4":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_m16a4-5450fc58.png", caption=config.M16A4, reply_markup=AR())
    elif call.data == "M416":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_hk416-86afd333.png", caption=config.M416, reply_markup=AR())
    elif call.data == "QBZ":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_qbz95-7e61dce8.png", caption=config.QBZ, reply_markup=AR())
    elif call.data == "SCAR-L":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_scar-l-9e7aa996.png", caption=config.SCARL, reply_markup=AR())
    elif call.data == "M762":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_m762-3679bea9.png", caption=config.M762, reply_markup=AR())
    elif call.data == "AKM":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_ak47-cc3a9fbd.png", caption=config.AKM, reply_markup=AR())
    elif call.data == "GROZA":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_groza-d245c1fe.png", caption=config.Groza, reply_markup=AR())
    elif call.data == "Mk47 Mutant":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_mk47mutant-1ddb6889.png", caption=config.Mk47Mutant, reply_markup=AR())

    elif call.data == "DMR":
        bot.send_message(call.from_user.id, "Оберіть Зброю", reply_markup=DMR())

    elif call.data == "VSS":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_vss_01-16ef9c6c.png", caption=config.VSS, reply_markup=DMR())
    elif call.data == "MINI14":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_mini14-6a06fb02.png", caption=config.MINI14, reply_markup=DMR())
    elif call.data == "QBU":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_qbu88-6448cf30.png", caption=config.QBU, reply_markup=DMR())
    elif call.data == "SKS":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_sks-558bd4e3.png", caption=config.SKS, reply_markup=DMR())
    elif call.data == "SLR":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_fnfal-f599f866.png", caption=config.SLR, reply_markup=DMR())
    elif call.data == "Mk14":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_mi_mk14ebr-96307b83.png", caption=config.Mk14, reply_markup=DMR())

    elif call.data == "SR":
        bot.send_message(call.from_user.id, "Оберіть зброю", reply_markup=SR())

    elif call.data == "WIN94":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_winchester1894-a1465f83.png", caption=config.WIN94, reply_markup=SR())
    elif call.data == "KAR98K":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_kar98k-f27d2f57.png", caption=config.KAR98K, reply_markup=SR())
    elif call.data == "M24":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_m24-9b07e66a.png", caption=config.M24, reply_markup=SR())
    elif call.data == "AWM":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_awm-9adbb87b.png", caption=config.AWM, reply_markup=SR())

    elif call.data == "PP":

        bot.send_message(call.from_user.id, "Оберіть зброю", reply_markup=PP())

    elif call.data == "UZI":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_uzi-2116a32b.png", caption=config.UZI, reply_markup=PP())
    elif call.data == "VECTOR":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_vector_01-238242e0.png", caption=config.VECTOR, reply_markup=PP())
    elif call.data == "UMP45":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_ump-c84bbc1d.png", caption=config.UMP45, reply_markup=PP())
    elif call.data == "TOMMYGUN":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_thompson-56227619.png", caption=config.TOMMYGUN, reply_markup=PP())

    elif call.data == "P":
        bot.send_message(call.from_user.id, "Оберіть зброю", reply_markup=P())

    elif call.data == "M249":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_m249-4a796044.png", caption=config.M249, reply_markup=P())
    elif call.data == "DP28":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_dp28-3b0392e8.png", caption=config.DP28, reply_markup=P())

    elif call.data == "PT":
        bot.send_message(call.from_user.id, "Оберіть зброю", reply_markup=PT())

    elif call.data == "R45":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_rhino-7f06bdc4.png", caption=config.R45, reply_markup=PT())
    elif call.data == "R1895":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_nagantm1895-b521774a.png", caption=config.R1895, reply_markup=PT())
    elif call.data == "P1911":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_m1911-cb307f5b.png", caption=config.P1911, reply_markup=PT())
    elif call.data == "P92":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_m9-c6f26db3.png", caption=config.R1895, reply_markup=PT())
    elif call.data == "P18C":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_glock18c-9e007404.png", caption=config.P18C, reply_markup=PT())
    elif call.data == "Skorpion":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_skorpion-d8319f04.png", caption=config.SKORPION, reply_markup=PT())
    elif call.data == "FlareGun":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_flaregun-c9e08e54.png", caption=config.FlareGun, reply_markup=PT())

    elif call.data == "G":
        bot.send_message(call.from_user.id, "Оберіть зброю", reply_markup=G())

    elif call.data == "FRAGGRENADE":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_grenade-786f5934.png", caption=config.FRAGGRENADE, reply_markup=G())
    elif call.data == "MOLOTOV":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_molotov-5f847169.png", caption=config.MOLOTOV, reply_markup=G())
    elif call.data == "SMOKE":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_smokebomb-0b9bb4c2.png", caption=config.SMOKE, reply_markup=G())
    elif call.data == "LIGHT":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_flashbang-4b2781f8.png", caption=config.LIGHT, reply_markup=G())
    elif call.data == "APPLE":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_apple-4203d3d2.png", caption=config.APPLE, reply_markup=G())
    elif call.data == "SNOWBALL":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_snowball-253f7bc4.png", caption=config.SNOWBALL, reply_markup=G())

    elif call.data == "C":
        bot.send_message(call.from_user.id, "Оберіть зброю", reply_markup=C())

    elif call.data == "PUNCH":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/equipment_hands_d_03-2ff389ba.png", caption=config.PUNCH, reply_markup=C())
    elif call.data == "JPUNCH":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/equipment_hands_d_03-2ff389ba.png", caption=config.JPUNCH, reply_markup=C())
    elif call.data == "LOM":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_cowbar-6e20824e.png", caption=config.LOM, reply_markup=C())
    elif call.data == "MACHETE":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_machete-b2abed31.png", caption=config.MACHETE, reply_markup=C())
    elif call.data == "SERP":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_sickle-e18ef7ff.png", caption=config.SERP, reply_markup=C())
    elif call.data == "PAN":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_pan-a6313de2.png", caption=config.PAN, reply_markup=C())

    elif call.data == "DB":
        bot.send_message(call.from_user.id, "Оберіть зброю", reply_markup=DB())

    elif call.data == "OBREZ":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_sawedoff-63336121.png", caption=config.OBREZ, reply_markup=DB())
    elif call.data == "S12K":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_saiga12-52704742.png", caption=config.S12K, reply_markup=DB())
    elif call.data == "S1897":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_winchester-447956bd.png", caption=config.S1897, reply_markup=DB())
    elif call.data == "S686":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_berreta686-c57d22bb.png", caption=config.S686, reply_markup=DB())

    elif call.data == "ARB":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/game/icons/weapon_crossbow-2b6ba954.png", caption=config.ARB, reply_markup=inlb())

    #------------Give Weapon---------------

    elif call.data == "short":

        bot.send_message(call.from_user.id, "По яким об'єктам ви стріляєте?", reply_markup=T2())
    elif call.data == "move":
        bot.send_message(call.from_user.id, "У вас виходить контролювати віддачу?", reply_markup=T3())
    elif call.data == "yes":
        apple = random.uniform(0, 100)
        if apple < 3:
            bot.send_message(call.from_user.id, "Найбільше вам підійде яблуко")
        bot.send_message(call.from_user.id, "Найбільше вам підійде штурмова гвинтівка")
    elif call.data == "no":
        apple = random.uniform(0, 100)
        if apple < 3:
            bot.send_message(call.from_user.id, "Найбільше вам підійде яблуко")
        bot.send_message(call.from_user.id, "Найбільше вам підійде пістолет-кулемет")
    elif call.data == "nmove":
        apple = random.uniform(0, 100)
        if apple < 3:
            bot.send_message(call.from_user.id, "Найбільше вам підійде яблуко")
        bot.send_message(call.from_user.id, "Найбільше вам підійде дробовик")
    elif call.data == "mid":
        bot.send_message(call.from_user.id, "По яким об'єктам ви стріляєте?", reply_markup=T22())
    elif call.data == "move2":
        bot.send_message(call.from_user.id, "У вас виходить контролювати віддачу?", reply_markup=T32())
    elif call.data == "yes2":
        bot.send_message(call.from_user.id, "Найбільше вам підійде штурмова гвинтівка")
    elif call.data == "no2":
        bot.send_message(call.from_user.id, "Найбільше вам підійде марксмарська гвинтівка")
    elif call.data == "nmove2":
        bot.send_message(call.from_user.id, "У вас виходить контролювати віддачу?", reply_markup=T33())
    elif call.data == "yes3":
        bot.send_message(call.from_user.id, "Найбільше вам підійде штурмова гвинтівка")
    elif call.data == "no3":
        bot.send_message(call.from_user.id, "Найбільше вам підійде марксмарська гвинтівка")
    elif call.data == "long":
        bot.send_message(call.from_user.id, "По яким об'єктам ви стріляєте?", reply_markup=T23())
    elif call.data == "move3":
        bot.send_message(call.from_user.id, "Найбільше вам підійде марксмарська гвинтівка")
    elif call.data == "nmove3":
        bot.send_message(call.from_user.id, "Найбільше вам підійде снайперська гвинтівка")
    elif call.data == "erangel":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/thumbs/erangel-ee673d73.jpg", caption=config.erangel, reply_markup=M())
    elif call.data == "miramar":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/thumbs/miramar-b0ea3b5b.jpg", caption=config.miramar, reply_markup=M())
    elif call.data == "sanuk":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/thumbs/savage-95704938.jpg", caption=config.sanuk, reply_markup=M())
    elif call.data == "vikendy":
        bot.send_photo(call.from_user.id, "https://d1nglqw9e0mrau.cloudfront.net/assets/images/thumbs/vikendi-ce67a32e.jpg", caption=config.vikendy, reply_markup=M())


bot.polling(none_stop=True)