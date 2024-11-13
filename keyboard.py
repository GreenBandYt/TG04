# keyboard.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню (Reply-клавиатура)
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("🤗 Привет"),
    KeyboardButton("👋 Пока"),
    KeyboardButton("🔗 Ссылки"),
    KeyboardButton("🎛️ Динамическое меню")
)

# Кнопки для раздела "Ссылки" (Inline-клавиатура)
links_menu = InlineKeyboardMarkup(row_width=1)
links_menu.add(
    InlineKeyboardButton("📰 Новости", url="https://news.ycombinator.com/"),
    InlineKeyboardButton("🎵 Музыка", url="https://spotify.com/"),
    InlineKeyboardButton("📹 Видео", url="https://youtube.com/")
)

# Кнопки для "Динамического меню" ("Опция 1" и "Опция 2")
dynamic_menu = InlineKeyboardMarkup(row_width=1)
dynamic_menu.add(
    InlineKeyboardButton("🔹 Опция 1", callback_data="option_1"),
    InlineKeyboardButton("🔸 Опция 2", callback_data="option_2")
)
