# keyboard.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню (Reply-клавиатура)
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🤗 Привет"), KeyboardButton(text="👋 Пока")],
        [KeyboardButton(text="🔗 Ссылки"), KeyboardButton(text="🎛️ Показать больше")]
    ],
    resize_keyboard=True
)


# Кнопки для раздела "Ссылки" (Inline-клавиатура)
links_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📰 Новости", url="https://dzen.ru/news?utm_referrer=dzen.ru")],
        [InlineKeyboardButton(text="🎵 Музыка", url="https://dzen.ru/search?query=музыка&sid=166213224218790471")],
        [InlineKeyboardButton(text="📹 Видео", url="https://dzen.ru/video")]
    ]
)

# Кнопки для "Динамического меню" ("Опция 1" и "Опция 2")
dynamic_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔹 Опция 1", callback_data="option_1")],
        [InlineKeyboardButton(text="🔸 Опция 2", callback_data="option_2")]
    ]
)
