# tg_bot_accatura_v2.py
# Данный скрипт предполагает наличие файлов:
#   accatura_bot.token
#   start.txt

import os
from datetime import datetime
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler, CallbackContext

# Функци для загрузки токена из файла accatura_bot.token
# примерный формат токена: ######:???????????????-????, без добавления "bot" к токену в конце или начале токена.
def load_token():
    token_file = os.path.join(os.path.dirname(__file__), '..', 'tg_bot_accatura_v2', 'accatura_bot.token')
    try:
        with open(token_file, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'Файл {token_file} не найден.')
        return None
    except Exception as e:
        print(f'Произошла ошибка при чтении файла: {e}')
        return None

def run_telegram_bot(token):
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    error_handler = CommandHandler('e', er)
    application.add_handler(error_handler)

    #message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), tg_bot.handle_message)
    #application.add_handler(message_handler)

    application.run_polling()

async def start(update: Update, context: CallbackContext):
    file_text_for_start = os.path.join(os.path.dirname(__file__), '..', 'tg_bot_accatura_v2', 'start.txt')
    # Создание кнопки в сообщении
    keyboard = [
        [InlineKeyboardButton("Запустить", url="https://t.me/accaturaCoinBot/accatura")
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Загрузка приветственного сообщения из файла
    try:
        with open(file_text_for_start, 'r', encoding='utf-8') as file:
            message_text = file.read()
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=(message_text), reply_markup=reply_markup)
    except FileNotFoundError:
        print(f'Файл start.txt не найден.')

async def er(update: Update, context: CallbackContext):
    file_for_error = os.path.join(os.path.dirname(__file__), '..', 'tg_bot_accatura_v2', 'error.txt')
    user_id = update.effective_user.id
    update_id = update.update_id
    message_text = update.message.text
    # key_name = 'tg_bot_update'
    # keys.update_key(key_name, update_id, 'integer')
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_for_error, 'a', encoding='utf-8') as file:
        file.write(f"{current_time}- {user_id} - {message_text}\n")

if __name__ == '__main__':

    # print(f"Переменные окружения: {os.environ}")

    script_name = os.path.basename(__file__)
    print(f"{script_name}: запущен")

    token = load_token()
    print(f"{script_name}: токен: {token}")

    print(f"{script_name}: запуск бота")
    run_telegram_bot(token)