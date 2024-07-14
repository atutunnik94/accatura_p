# main.py
import logging
import subprocess
import os
import time
import select

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='app.log',  # Логи будут записываться в файл app.log
                    filemode='w')

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
                venv_python = 'python'
            #subprocess.run([venv_python, script_path])
            process = subprocess.Popen([venv_python, script_path], stdout=None, stderr=None, text=True)
            processes.append((file_name, process))


    return processes

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    print('*** добро пожаловать ***')
    # run_scripts()
    try:
        processes = run_scripts()
        while True:
            for file_name, process in processes:
                retcode = process.poll()
                if retcode is not None:  # если что-то пошло не так
                    logger.warning(f"скрипт {file_name} завершился с кодом: {retcode}")
                    print(f"скрипт {file_name} завершился с кодом: {retcode}")
                    processes.remove((file_name, process))
                #print(process.communicate())
            time.sleep(5)  # Повторная проверка
    except KeyboardInterrupt:
        logger.warning("завершение работы пользователем")
        print("\nзавершение работы пользователем")
        for file_name, process in processes:
            process.terminate()  # Прерывание процесса
            logger.info(f"Процесс {file_name} был завершен")
    finally:
        # Блок finally будет выполнен в любом случае,
        # даже если произошло исключение (например, KeyboardInterrupt)
        print("конец")