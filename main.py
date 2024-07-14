# main.py
import logging
import subprocess
import os
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='app.log',  # Логи будут записываться в файл app.log
                    filemode='w')

loads_script = {
    "tg_bot_accatura_v2": [
        "tg_bot_accatura_v2.py",
        "tg_web3app.py"
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
            print(file_name)
            #subprocess.run([venv_python, script_path])
            process = subprocess.Popen([venv_python, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True)
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
                    processes.remove((file_name, process))
                else:
                    # как то настроить логи
                    stdout, stderr = process.communicate()
                    if stdout:
                        logger.info(f"Output from {file_name}: {stdout}")
                        print(f"{file_name}: {stdout}")
                    if stderr:
                        logger.error(f"Error from {file_name}: {stderr}")
                        print(f"{file_name}: {stderr}")
            time.sleep(5)  # Повторная проверка
    except KeyboardInterrupt:
        logger.warning("завершение работы пользователем")
        print("\nзавершение работы пользователем")
