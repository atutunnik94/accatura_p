# main.py
import logging
import subprocess
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='app.log',  # Логи будут записываться в файл app.log
                    filemode='w')

loads_script = {
    "tg_bot_accatura_v2": [
        "tg_bot_accatura_v2.py"
    ],
    "files": []
}

def run_scripts():
    for folder in loads_script:
        # print(folder)
        for file_name in loads_script[folder]:
            script_path = os.path.join(os.path.dirname(__file__), folder, file_name)
            venv_python = os.path.join(os.path.dirname(__file__), '.venv', 'Scripts', 'python.exe')
            subprocess.run([venv_python, script_path])

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    print('*** Добро пожаловать***')
    run_scripts()
