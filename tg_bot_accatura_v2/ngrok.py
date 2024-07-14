# ngrok.py
# Данный скрипт предполагает наличие файлов:
#   ngrok.token
#   ngrok.exe

import os
import subprocess

def load_token():
    token_file = os.path.join(os.path.dirname(__file__), '..', 'tg_bot_accatura_v2', 'ngrok.token')
    try:
        with open(token_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'Файл {token_file} не найден.')
        return None
    except Exception as e:
        print(f'Произошла ошибка при чтении файла: {e}')
        return None


if __name__ == '__main__':
    ngrok_path = os.path.join(os.path.dirname(__file__), 'ngrok.exe')
        # ngrok config add-authtoken
    token = load_token()
    first_command = [ngrok_path, "config", "add-authtoken", token]
    subprocess.run(first_command, text=True)
    second_command = [ngrok_path, "tunnel", "--label", "edge=edghts_2jEhsJzYR90vxy60HxeNgSo71I9", "http://localhost:8080"]
    subprocess.run(second_command, text=True)
    print("ngrok: start")
