import subprocess
import os
import sys
import shutil
import colorama
import wget
import signal
#daskdsajdkasd
num = 0

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJzdWIiOjU5Mjc2MjksImlzcyI6Imx6dCIsImV4cCI6MCwiaWF0IjoxNzEzODk4NjMwLCJqdGkiOjU1NDc5Miwic2NvcGUiOiJiYXNpYyByZWFkIHBvc3QgY29udmVyc2F0ZSBtYXJrZXQifQ.j4TDljjNmKjFHKVRKYDs4yew9Nfw5DB0fZeh16IkzRTXjc-QH4Kh6t30DbES5KlQnHGqI-rW4NsYuPBN7W3UMdbceWjFT7UFywbhVZMNcwE4krdWgms1l65QHHfVK8-e_p1LqDloBVU27gHLEKELpAzu8yhxgI-Fy2zdUjT_vOc"

def updateScripts():
    print("Удаляем старые версии...")
    if os.path.exists("smap.py"):
        os.remove("smap.py")
    if os.path.exists("starter.py"):
        os.remove("starter.py")
    print("Скачиваем smap.py")
    wget.download("https://bvotsonteam.alwaysdata.net/bvspamer/smap.py")
    print("\nСкачиваем starter.py")
    wget.download("https://bvotsonteam.alwaysdata.net/bvspamer/starter.py")
    print("\nСкачали версию. Пересохраните файлы спамера. -new")

def runLogin_only(num_scripts):
    global num
    # Путь к текущей папке
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Папки, содержащие скрипты
    script_folders = [str(i) for i in range(1, 15)]  # Измените диапазон при необходимости

    # Запуск каждого скрипта в новой терминале
    for folder in script_folders:
        if not num == num_scripts:
            script_path = os.path.join(current_dir, folder, "smap.py")
            
            # Проверка на существование скрипта
            if os.path.exists(script_path):
                subprocess.Popen(['start', 'cmd', '/k', 'python', script_path, '-onlyLogin'], shell=True)
            else:
                print(f"Скрипт {script_path} не найден. Используйте -new для создания скриптов.")

            num += 1

    

def run_scripts_in_new_terminals(num_scripts):
    global num
    # Путь к текущей папке
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Папки, содержащие скрипты
    script_folders = [str(i) for i in range(1, 15)]  # Измените диапазон при необходимости

    # Запуск каждого скрипта в новой терминале
    for folder in script_folders:
        if not num == num_scripts:
            script_path = os.path.join(current_dir, folder, "smap.py")
            
            # Проверка на существование скрипта
            if os.path.exists(script_path):
                subprocess.Popen(['start', 'cmd', '/k', 'python', script_path, '-full'], shell=True)
            else:
                print(f"Скрипт {script_path} не найден. Используйте -new для создания скриптов.")

            num += 1

def create_or_update_scripts(num_scripts):
# Путь к текущей папке

    #get_newAccounts(num_scripts)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Путь к шаблону smap.py
    template_path = os.path.join(current_dir, "smap.py")
    template_path2 = os.path.join(current_dir, "config.ini")
    template_path3 = os.path.join(current_dir, "creo.png")

    # Проверка наличия шаблона
    if not os.path.exists(template_path):
        print(f"Файл шаблона {template_path} не найден.")
        return

    for i in range(1, num_scripts + 1):
        folder_name = str(i)
        folder_path = os.path.join(current_dir, folder_name)

        # Создание папки, если она не существует
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Путь к файлу script.py
        script_path = os.path.join(folder_path, "smap.py")
        script_path2 = os.path.join(folder_path, "config.ini")
        script_path3 = os.path.join(folder_path, "creo.png")

        # Копирование шаблона в файл script.py
        asd = shutil.copyfile(template_path, script_path)
        asd = shutil.copyfile(template_path2, script_path2)
        asd = shutil.copyfile(template_path3, script_path3)
        print("Создан файл.")

def del_activities(num_scripts):
    global num
    # Путь к текущей папке
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Папки, содержащие скрипты
    script_folders = [str(i) for i in range(1, 15)]  # Измените диапазон при необходимости

    # Запуск каждого скрипта в новой терминале
    for folder in script_folders:
        if not num == num_scripts:
            script_path = os.path.join(current_dir, folder, "Active_account.session")
            script_path2 = os.path.join(current_dir, folder, "Active_account.session-journal")
            print(script_path2  )
            # Проверка на существование скрипта
            if os.path.exists(script_path):
                os.remove(script_path)
                try:
                    os.remove(script_path2)
                except Exception as e:
                    pass
            else:
                print(f"Сессия {script_path} не найден. Используйте -new для создания скриптов.")
            

            num += 1

def exitcode():
    print("HUIIII")

if __name__ == "__main__":
    try:
        signal.signal(signal.SIGTERM, exitcode)
        if len(sys.argv) > 1:
            if sys.argv[1] == "-2.0MODE":
                path = sys.argv[2]
                path = path.replace(".session", "")
                os.system(f"python smap.py -2.0 {path}")
        q = input("Выберите действие: \n1. Создание новых скриптов \n2. Открыть скрипты \n3. Soon... \n4. Удалить активные сессии \n5. Запустить только вход \n66. Обновить скрипты \n")
        if q == "1":
            num_scripts = int(input("Введите количество скриптов для создания или обновления: "))
            create_or_update_scripts(num_scripts)
        elif q == "2":
            num_scripts = int(input("Введите максимальное кол-во открытия: "))
            run_scripts_in_new_terminals(num_scripts)
        elif q == "3":
            pass
        elif q == "4":
            num_scripts = int(input("Введите максимальное кол-во удаления: "))
            del_activities(num_scripts)
        elif q == "5":
            num_scripts = int(input("Введите максимальное кол-во открытия: "))
            runLogin_only(num_scripts)
        elif q == "66":
            updateScripts()
    except Exception as e:
        print(e)
        #print("Параметры:\n-new - создание скриптов\n-run - запуск скриптов\n-get - получение аккаунтов\n-del - удалить сессии\n-onlyL - запуск только входа \n-update - обновить спамер")