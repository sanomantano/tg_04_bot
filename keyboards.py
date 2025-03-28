from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard():
        """Returns the keyboard for the /start command."""
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            InlineKeyboardButton("Получить расписание", callback_data="schedule"),
            InlineKeyboardButton("Информация о школе", callback_data="send_info")
        )
        return keyboard




