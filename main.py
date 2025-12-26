import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

TOKEN ="7524454341:AAHpvUEgbGgIM0aVghsixK9gXcosOqqVpB0"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="Привет!"), types.KeyboardButton(text="Как дела?"))
    builder.row(types.KeyboardButton(text="Создать Inline-кнопки"))

    await message.answer(
        "Привет! Я бот с кнопками. Выбери действие на клавиатуре ниже:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )


@dp.message(F.text == "Создать Inline-кнопки")
async def show_inline(message: types.Message):
    inline_builder = InlineKeyboardBuilder()
    inline_builder.row(types.InlineKeyboardButton(
        text="Перейти на сайт",
        url="https://google.com")
    )
    inline_builder.row(types.InlineKeyboardButton(
        text="Нажми меня (Callback)",
        callback_data="button_pressed")
    )

    await message.answer(
        "А вот и Inline-кнопки! Они 'прилипают' к сообщению:",
        reply_markup=inline_builder.as_markup()
    )


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
