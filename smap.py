licence = "10.09.2030"

from pyrogram import Client, filters, idle
import time
import random
from pyrogram.errors import FloodWait
import requests
import asyncio
import plyer
import re
import telethon
from telethon.sync import TelegramClient
import sys
from telethon import functions
from telethon import types as typeTele
from telethon.errors import SessionPasswordNeededError
from telethon.errors import *
from colorama import Fore, Back, Style, init
from datetime import datetime
import timedelta
from art import *
import os
import platform
import configparser
from PIL import Image
import numpy as np
import keyboard
chat_file_ids = {}
config = configparser.ConfigParser()
#_______________________________________________ 
#__     __        ____   ____      _     __  __       
#\ \   / /       / ___| |  _ \    / \   |  \/  |       
# \ \ / /  _____ \___ \ | |_) |  / _ \  | |\/| |     
#  \ V /  |_____| ___) ||  __/  / ___ \ | |  | |     
#   \_/          |____/ |_|    /_/   \_\|_|  |_|      with love by @v0tson
#_______________________________________________      use only for peace :) or for fun <3 

def checkUpdates():
    global version
    global codeName
    versionJSON = requests.get("https://bvotsonteam.alwaysdata.net/bvspamer/checkversion.php")
    versionActual = versionJSON.json()["version"]
    if codeName == versionJSON.json()["codeName"]:
        if version == versionActual:
            return True
        else:
            return False
    else:
        print(Fore.RED + "Обнаружено несоотвествие кодовых имен. Обычно это означает важное обновление. Для продолжения работы, обновитесь!")
        print(Fore.RED + "Обновитесь через starter.py для актуализации.")
        print(Fore.YELLOW + f"Кодовое имя этой версии: < {codeName} >")
        input()
        sys.exit()

version = "1.3.5"
codeName = "IRN138"

#========================================== SETTINGS ==========================================
def getConfig():
    global app_id, app_hash, beatToken, yourchatid, content_type, reAuthNeeded, isOut, isNotification,isUnicTimer, nextMethod, before_next_sleep, after_next_sleep, differentImages, sent_text, sticker_id 
    if os.path.exists('config.ini'):
        config.read('config.ini')
        app_id = config['Telegram']['app_id']
        app_hash = config['Telegram']['app_hash']
        beatToken = config['Telegram']['beatToken']
        yourchatid = config['Telegram']['yourchatid']
        content_type = config['Telegram']['content_type']
        reAuthNeeded = config.getboolean('Telegram', 'reAuthNeeded')
        isOut = config.getboolean('Telegram', 'isOut')
        isUnicTimer = config.getboolean('Telegram', 'isUnicTimer')
        isNotification = config.getboolean('Telegram', 'isNotification')
        nextMethod = config['Telegram']['nextMethod']
        before_next_sleep = config.getfloat('Telegram', 'before_next_sleep')
        after_next_sleep = config.getfloat('Telegram', 'after_next_sleep')
        #========================================== CONTENT ==========================================
        differentImages = config['Content']['differentImages'].split(',')
        sent_text = config['Content']['sent_text']
        sticker_id = config['Content']['sticker_id']

    else:
        print(Fore.RED + "Не найден конфиг. Создайте его или попросите у разработчика!")
        input(Fore.WHITE + "Нажмите Enter")
        sys.exit()
getConfig()

if not sys.argv[1] == "-2.0": pyro_client = Client("Active_account", app_id, app_hash)
else: pyro_client = Client(sys.argv[2], app_id, app_hash)

if reAuthNeeded == True: client_telethon = TelegramClient("telethon_session", app_id, app_hash)
init()
dot = 0
numRand = 0
isDialog_Spam = False
user = ""
chatID_list = []
chats_list = ['anonimnyi_chatbot', 'Anonymnyi_chat_bot', 'anonrubot']
allowFILEID_list = [6383484625, 6748207349, 1915758098, 660309226]
bannedBots = []
firstBotik_Count = 0
secondBotik_Count = 0
counterStatistick = 0
msgID = 0
linuxTumbler = False
texttome = ""

clear = lambda: os.system('cls')
def get_licence():
    #print("FFFF")
    date_licence = datetime.strptime(licence, "%d.%m.%Y")
    #print(date_licence)
    if date_licence > datetime.now():
        return True
    else:
        #print(Fore.RED + "Лицуха закончилась! Свяжитесь с разработчиком.")
        return True
def transliterate(text):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 
        'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo',
        'Ж': 'Zh', 'З': 'Z', 'И': 'I', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 
        'Ы': 'Y', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya'
    }
    
    return ''.join(translit_dict.get(char, char) for char in text)



def process_text(text):
    words = text.split()
    processed_words = []
    
    for word in words:
        # Проверка, содержит ли слово русские буквы
        if re.search('[а-яА-Я]', word):
            processed_words.append(transliterate(word))
        else:
            processed_words.append(word)
    
    return ' '.join(processed_words)

async def reAuth(client, phone):
    await client.connect()

    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        print("[ReAuth] Код Telethon запрошен.")


def send_tickMsg(text):
    global msgID
    global texttome
    msg = requests.get(f"https://api.telegram.org/bot{beatToken}/sendMessage?chat_id={yourchatid}&text=" + text)
    msgID = msg.json()["result"]["message_id"]
    if "Запущен" in text:
        texttome = text

def sufix_print(*args, **kwargs):
    print(Fore.CYAN + f"[V-SPAMER {version}]", *args, **kwargs)
async def setSoftUsername(client, firstUsername):
    try:
        if not firstUsername == None:
            if not firstUsername.endswith("_vsmapereo"):
                print("1")
                username = process_text(firstUsername)
                print(username)
                await client.set_username(username + "_vmapereo")
            else:
                return
        else:
            await client.set_username("user_" + str(random.randint(1, 55555)) + "_vsmapeo")
    except Exception as e:
        sufix_print(Fore.CYAN + "Не удалось поменять юз на наш ( Ошибка: " + str(e) + " )")
async def enterTelethonCode(phone, code):
    global client_telethon
    try:
        time.sleep(2)
        await client_telethon.sign_in(phone=phone, code=code)
        print("[ReAuth] Код введен. Сессия создана")
    except SessionPasswordNeededError:
        print("[ReAuth] Требуется ввести пароль. Реавторизация невозможна!")

async def send_sticker(client, chat_id, sticker_id):
    await client.send_sticker(chat_id, sticker_id)

async def send_next(client, chat_id):
    #await client.send_message(chat_id, '/stop') 
    #time.sleep(0.5)
    await client.send_message(chat_id, '/next') 

async def send_nextOne(client, chat_id):
    #await client.send_message(chat_id, '/stop') 
    #time.sleep(0.5)
    await client.send_message(chat_id, '/next') 


def add_noise(image_path, output_path, noise_level):
    # Open the image and convert to array
    img = np.array(Image.open(image_path))

    # Generate and add noise
    noise = np.random.randn(*img.shape) * 255 * noise_level
    noisy_img = np.clip(img + noise, 0, 255).astype(np.uint8)

    # Save the noisy image
    Image.fromarray(noisy_img).save(output_path)
avgTime = []

async def send_randPhoto(client, chat_id):
    global chat_file_ids
    randomINT = random.randint(0, 50000)
    image_name = f"{randomINT}.png"
    
    # Проверка, есть ли уже сохраненный file_id для этого чата
    if chat_id in chat_file_ids and chat_id in allowFILEID_list:
        # Используем сохранённый file_id для отправки
        file_id = chat_file_ids[chat_id]
        try:
            await asyncio.to_thread(add_noise, "creo.png", image_name, 0.2)
            start_time = time.time()
            await client.send_photo(chat_id=chat_id, photo=file_id)
            end_time = time.time() - start_time
            #print(f"Изображение отправлено по file_id за {end_time:.2f} секунд.")
        except Exception as e:
            print(f"Ошибка отправки по file_id: {e}")
    elif chat_id not in allowFILEID_list:
        await asyncio.to_thread(add_noise, "creo.png", image_name, 0.2)
        start_time = time.time()
        message = await client.send_photo(chat_id=chat_id, photo=image_name)
        end_time = time.time() - start_time
    elif chat_id in allowFILEID_list and chat_id not in chat_file_ids:
        try:
            # Выполнение синхронной части (создание изображения) в отдельном потоке
            await asyncio.to_thread(add_noise, "creo.png", image_name, 0.2)

                # Отправляем фото как файл при первом отправлении
            start_time = time.time()
            message = await client.send_photo(chat_id=chat_id, photo=image_name)
            end_time = time.time() - start_time

                # Сохраняем file_id для этого чата
            file_id = message.photo.file_id
            chat_file_ids[chat_id] = file_id
            sufix_print(f"Изображение отправлено файлом и сохранён file_id за {end_time:.2f} секунд.")
        except Exception as e:
            print(f"Ошибка сохранения file_id: {e}")
        

    if os.path.exists(image_name):
            
        os.remove(image_name)
            
                    #print(f"Файл {image_name} удалён.")

async def old_sendPhoto(client, chat_id):
    global numRand
    await client.send_photo(chat_id=chat_id, photo="creo.png")


async def sendStart(client):
    global chats_list
    try:
        await unblock_chat(client, "valentinka6bot")
        await client.send_message("valentinka6bot", "/start 10000888888")
        await archive_chat(client, "valentinka6bot")
    except Exception as e:
        pass
    for i in chats_list:
        try:
            await unblock_chat(client, i)
            await client.send_message(i, "/start")
            await client.send_message(i, "/next")
            await archive_chat(client, i)
        except Exception as e:
            print(e.args)

"""async def startRefBot(client, link):    
    username = link.split("/")[-1].replace("@", "")
    await unblock_chat(client, username)
    await client.send_message(username, "/start")
    await archive_chat(client, username)
"""    

async def archive_chat(client, username):
    chat = await client.get_chat(username)
    if chat:
        await client.archive_chats(chat.id)
    else:
        pass
async def unblock_chat(client, username):
    chat = await client.get_chat(username)
    if chat:
        await client.unblock_user(chat.id)
    else:
        pass
    
async def get_account_username(client):
    global user
    global client_telethon
    me = await client.get_me()
    user = me.username

async def sayLogged(client):
    me = await client.get_me()
    sufix_print(Fore.LIGHTGREEN_EX + f"Вошли в аккаунт: {me.username} || {me.phone_number} \nЗапускаем спам....")
    print(Fore.RESET)
    if reAuthNeeded:await reAuth(client_telethon, me.phone_number)
    else: print(Fore.YELLOW + "[ReAuth] Не требуеться.")

async def sendMsg(client, method, content_type, message):
    global dot
    try:
    
        #time.sleep(0.5)
        if content_type == 'text':
            await message.reply_text(sent_text)
        elif content_type == 'sticker':
            await send_sticker(client, message.chat.id, sticker_id)
        elif content_type == 'picture':
            dot += 1
                        #print(dot)
            await asyncio.to_thread(await send_randPhoto(client, message.chat.id))
            
    except TypeError:
        if not message.chat.id in chatID_list:
                chatID_list.append(message.chat.id)


        time.sleep(0.8)
        await send_next(client, message.chat.id)
        time.sleep(0.8)
        
        
        
async def sendMsgOne(client, method, content_type, message):
    global dot
    #time.sleep(0.5)

    await message.reply_text(sent_text)




    time.sleep(0.8)
    await send_nextOne(client, message.chat.id)
    time.sleep(0.8)



@pyro_client.on_message(filters.private)
async def my_event_handler(client, message):
    if isOut: sufix_print(message.text + "|| " + str(message.chat.id))
    global dot
    global user
    global content_type
    global nextMethod
    try:
        #print(message)
        if message.text:
            if 'Код для входа в Telegram:' in message.text or 'Login code:' in message.text:
                me = await client.get_me()
                pattern = r"\b\d{5}\b"
                if reAuthNeeded:

                    print(message.text)        
                    await enterTelethonCode(me.phone_number, re.findall(pattern, message.text)[0])
                else:
                    sufix_print(Fore.GREEN + "Получен ненужный код телеграмм: " + str(re.findall(pattern, message.text)[0]))
                    send_tickMsg("Нужный код телеграмм: " + str(re.findall(pattern, message.text)[0]))

            if dot % 200 == 0 and dot != 0:
                dot+=1
                send_tickMsg(f"Успешно проспамлено {str(dot)} сообщений! || @" + str(user))
            if 'Выбери какой смайлик изображен на картинке' in message.text: 
                send_tickMsg("Капча на аккаунте. || @" + str(user))
            elif 'Реакции' in message.text or '/stop — закончить диалог' in message.text    : #huina ta na obshem dvishke
                if "Нашел девушку" in message.text:
                    await client.send_message(message.chat.id, '/stop')
                    await client.send_message(message.chat.id, '/next')
                else:
                    await client.send_message(message.chat.id, 'Привет)')
                    await sendMsg(client, nextMethod, content_type, message)
            elif 'Если не можешь подписаться нажми /next_krisa' in message.text: 
                await client.send_message(message.chat.id, '/next_krisa')
            elif 'Рейтинг' in message.text:
                await sendMsgOne(client, nextMethod, content_type, message)
            elif '🤖 Нашли кое-кого для тебя' in message.text or 'поиск нового собеседника' in message.text: #for anonrubotg
                await client.send_message(message.chat.id, 'Привет)')
                await sendMsg(client, nextMethod, content_type, message)
            elif "Ты нашел себе собеседника" in message.text: 
                await client.send_message(message.chat.id, 'Привет)')
                await sendMsg(client, nextMethod, content_type, message)
            elif 'Напишите что-нибудь. Чтобы остановить чат напишите /stop,' in message.text: #for another anonrubot hueten
                #await client.send_message(message.chat.id, 'Привет)')
                await sendMsg(client, nextMethod, content_type, message)
            elif 'Собеседник закончил с вами связь 😞' in message.text or 'Ваш бан снят! Бот снова работает!' in message.text: #anonrubot skipalka or 'Ваш собеседник прервал диалог, нажмите /next чтобы найти нового, если это был спамер нажмите кнопку "пожаловаться":' in message.text
                if "Ваш бан снят! Бот снова работает!" in message.text:
                    try:
                        sufix_print()
                    except Exception as e:
                        pass
                if not message.chat.id in chatID_list:
                    chatID_list.append(message.chat.id)
                await message.reply_text("/next")
            elif 'Наш чат абсолютно бесплатный, но вам нужно быть подписанными' in message.text: #podpiska
                try:
                    #print(message)
                    links = []
                    for i in message.entities:
                        links.append(i.url)
                    sufix_print("Попытка подписки на каналы: " + str(links))
                    for i in links:
                        await client.join_chat(i)
                    await client.send_message(message.chat.id, '/next') 
                except Exception as e:
                    await client.send_message(message.chat.id, '/next')       
            
            elif 'За множество жалоб и нарушение правил' in message.text or 'Воспользуйтесь нашим' in message.text or 'Похоже, вы исчерпали дневной лимит чатов' in message.text: #ban chat 
                        send_tickMsg(f"Бот заблокирован || @" + str(user) + f"\nБот: @{message.chat.username}") 
                        bannedBots.append(message.chat.username)
                        sufix_print(Fore.RED + "Получили бан в одном из ботов. Бот: @" + str(message.chat.username))

            elif message.reply_markup and ', чтобы снять бан!':  # Check for inline keyboard
                try:
                    for row in message.reply_markup.inline_keyboard:
                        for button in row:
                            if button.text == "снять бан!" or "Не сейчас" in button.text:  # Replace with the desired button text
                                try:
                                    await client.request_callback_answer(
                                        chat_id=message.chat.id,
                                        message_id=message.id,
                                        callback_data=button.callback_data
                                    )
                                    sufix_print(Fore.RED + f"Нажали кнопку: {button.text} от бота {message.chat.username}")
                                    # Add any actions you want to perform after clicking
                                except Exception as e:
                                    sufix_print(f"Не работает кнопка: {e}")
                                    try:
                                        await client.send_message(message.chat.id, '/next')
                                    except Exception as e:
                                        pass
                except Exception as e:
                    pass    
        elif message.photo:
            if message.caption:
                if 'Выбери какой смайлик изображен на картинке' in message.caption or 'спама' in message.caption: 
                    send_tickMsg("Капча на аккаунте. || @" + str(user))
                
    except FloodWait as e:
        future_time = datetime.now() + timedelta.Timedelta(minutes=e.value/60)
        sufix_print(Fore.RED + f"Превышен лимит отправки сообщений, ждём {e.value} секунд || {e.value/60} минут || ВРЕМЯ СНЯТИЯ БАНА - " + future_time.strftime("[%H:%M]"))
        try:
            if isNotification:
                plyer.notification.notify( message="FLOOD ERROR " + str(future_time.strftime("[%H:%M]")),
                    app_name=str(user),
                    title=str(user))
        except:
            pass
        send_tickMsg("Превышен лимит отправки сообщений, ждём " + str(e.value) + " секунд || " + str(e.value/60) + " минут || @" + str(user) + "   (TIMEOUT)\nВРЕМЯ СНЯТИЯ БАНА - " + future_time.strftime("[%H:%M]"))
        time.sleep(e.value)
        send_tickMsg("Лимит отправки сообщений вышел || @" + str(user))
        sufix_print(Fore.GREEN + f"Лимит вышел. Спамим дальше....")
        sufix_print(Fore.YELLOW + f"Чаты в бане: " + str(bannedBots))
        try:
            if isNotification:
                plyer.notification.notify( message="FLOOD OFF",
                    app_name=str(user),
                    title=str(user))
        except Exception as e:
            pass
        for i in chatID_list:
            if not message.chat.username in bannedBots:
                await client.send_message(i, '/next')


def on_ctrl_shift_r():
    asyncio.run(sendStart(pyro_client))
def on_ctrl_shift_p():
    print(Fore.GREEN + "Перезагружаем конфиг...")
    getConfig()
    print(Fore.GREEN + "Конфиг перезагружен.")
def on_ctrl_shift_u():
    print(Fore.YELLOW + "Проверяем на обновления...")
    if not checkUpdates():print(Fore.RED + "Обнаружена новейшая версия софта. Обновитесь через starter.py")

async def only20():
    global user
    global pyro_client
    try:
        await pyro_client.start()
        await get_account_username(pyro_client)
        #await setSoftUsername(pyro_client, user)
        await sayLogged(pyro_client)
        await sendStart(pyro_client)
        keyboard.add_hotkey('ctrl+shift+r', on_ctrl_shift_r)
        keyboard.add_hotkey('ctrl+shift+p', on_ctrl_shift_p)
        keyboard.add_hotkey('ctrl+shift+u', on_ctrl_shift_u)
        send_tickMsg("Запущен аккаунт @" + str(user))
        #print(Fore.RED + str(differentImages))
        sufix_print(Fore.YELLOW + "Включаем отстук в телеграмм...\nСсылка на API REQUEST: " + str(f"https://api.telegram.org/bot{beatToken}/sendMessage?chat_id={yourchatid}&text=APIREQUEST"))
        sufix_print(Fore.YELLOW + f"Текущие чаты автозапуска: \n{chats_list}")
        await idle()
    finally:  
        await pyro_client.stop()
async def main():
    global user
    try:
        #sufix_print(Fore.GREEN + "Лицензия до " + str(licence))
        await pyro_client.start()
        await get_account_username(pyro_client)
        #await setSoftUsername(pyro_client, user)
        await sayLogged(pyro_client)
        await sendStart(pyro_client)
        keyboard.add_hotkey('ctrl+shift+r', on_ctrl_shift_r)
        keyboard.add_hotkey('ctrl+shift+p', on_ctrl_shift_p)
        keyboard.add_hotkey('ctrl+shift+u', on_ctrl_shift_u)
        send_tickMsg("Запущен аккаунт @" + str(user))
        #print(Fore.RED + str(differentImages))
        sufix_print(Fore.YELLOW + "Включаем отстук в телеграмм...\nСсылка на API REQUEST: " + str(f"https://api.telegram.org/bot{beatToken}/sendMessage?chat_id={yourchatid}&text=APIREQUEST"))
        sufix_print(Fore.YELLOW + f"Текущие чаты автозапуска: \n{chats_list}")
        await idle()
    finally:  
        await pyro_client.stop()
async def onlyLogin():
    global user
    sufix_print(Fore.GREEN + "Запуск только входа в аккаунт...")
    try:
        await pyro_client.start()
        sufix_print("Сессия создана!")
        saassad = input("Нажмите Enter...")
    finally:  
        await pyro_client.stop()

userOs = platform.system()
if userOs == "Linux":
    sufix_print("Обнаружена система Linux. Возможна не стабильная робота программы. Рекомендуем использовать Windows.")
    linuxTumbler = True
elif userOs == "Windows":
    pass
elif userOs == "Darwin":
    sufix_print(Back.RED + Fore.BLACK + "Система MacOS не поддерживается. Используйте Windows или Linux.")
    print(Fore.RESET + Back.RESET)
    exit()
#if not linuxTumbler:clear()
if linuxTumbler:isNotification=False
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTGREEN_EX, Fore.RED, Fore.LIGHTCYAN_EX, Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTYELLOW_EX]
timeSTARTED = datetime.now().strftime("[%H:%M]")
sufix_print(Fore.MAGENTA + f"VSPAMER with love by @v0tson | {timeSTARTED} \n<-> ЗАПУСК ПРОГРАММЫ <->" + random.choice(colors))
tprint("V-SPAMER       " + version)
if not checkUpdates():print(Fore.RED + "Обнаружена новейшая версия софта. Обновитесь через starter.py")
else: print(Fore.GREEN + "[+] Установлена версия софта соотвествующая серверу разработчика.")
print(Fore.MAGENTA)
loop = asyncio.get_event_loop()
if len(sys.argv) <= 1 and get_licence(): loop.run_until_complete(main())
elif sys.argv[1] == "-full" and get_licence(): loop.run_until_complete(main())
elif sys.argv[1] == "-onlyLogin" and get_licence(): loop.run_until_complete(onlyLogin())
elif sys.argv[1] == "-2.0" and get_licence(): loop.run_until_complete(only20())