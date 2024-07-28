# main.py
import subprocess
import os
import time

loads_script = {
    "tg_bot_accatura_v2": [
        "tg_bot_accatura_v2.py",
        "tg_web3app.py",
        "ngrok.py"
    ],

    # Далее можно добавлять любые проекты
    "files": []
}

def run_scripts():
    processes = []
    for folder in loads_script:
        for file_name in loads_script[folder]:
            script_path = os.path.join(os.path.dirname(__file__), folder, file_name)
            venv_python = os.path.join(os.path.dirname(__file__), '.venv', 'Scripts', 'python.exe')
            if not os.path.exists(venv_python):
                venv_python = 'python.exe'
            process = subprocess.Popen([venv_python, script_path], stdout=None, stderr=None, text=True)
            processes.append((file_name, process))


    return processes

if __name__ == '__main__':

    # добавление изначально 15 пустых строк в консоли.
    for i in range(15):
        print(i)
    try:
        processes = run_scripts()
        while True:
            for file_name, process in processes:
                retcode = process.poll()
                if retcode is not None:  # если что-то пошло не так
                    print(f"скрипт {file_name} завершился с кодом: {retcode}")
                    processes.remove((file_name, process))
            time.sleep(5)  # Повторная проверка
    except Exception as e:
        print(f"завершение работы: {e}")
    except KeyboardInterrupt:
        print("\nзавершение работы пользователем")
        for file_name, process in processes:
            process.terminate()  # Прерывание процесса
    finally:
        # Блок finally будет выполнен в любом случае,
        # даже если произошло KeyboardInterrupt)
        print("конец")