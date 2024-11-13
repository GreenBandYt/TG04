import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from config import TOKEN
from keyboard import main_menu, links_menu, dynamic_menu

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()


# Обработчик команды /start
@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("👋 Добро пожаловать! Выберите действие:", reply_markup=main_menu)


# Обработчик кнопки "Привет"
@router.message(lambda message: message.text == "🤗 Привет")
async def greet_user(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}! 😊")


# Обработчик кнопки "Пока"
@router.message(lambda message: message.text == "👋 Пока")
async def goodbye_user(message: Message):
    await message.answer(f"До свидания, {message.from_user.first_name}! 👋")


# Обработчик кнопки "Ссылки"
@router.message(lambda message: message.text == "🔗 Ссылки")
async def show_links(message: Message):
    await message.answer("🔗 Выберите ссылку:", reply_markup=links_menu)


# Обработчик кнопки "Динамическое меню"
@router.message(lambda message: message.text == "🎛️ Динамическое меню")
async def dynamic_menu_handler(message: Message):
    await message.answer("🎛️ Выберите опцию:", reply_markup=dynamic_menu)


# Обработчик инлайн-кнопки "Опция 1"
@router.callback_query(lambda callback: callback.data == "option_1")
async def option_1_handler(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали 🔹 Опцию 1 ✅")
    await callback.answer()


# Обработчик инлайн-кнопки "Опция 2"
@router.callback_query(lambda callback: callback.data == "option_2")
async def option_2_handler(callback: CallbackQuery):
    await callback.message.answer("Вы выбрали 🔸 Опцию 2 ✅")
    await callback.answer()


# Основная функция
async def main():
    print("🤖 Бот запущен...")
    dp.include_router(router)  # Подключаем маршрутизатор
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
