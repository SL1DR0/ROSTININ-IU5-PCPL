import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

TOKEN = ""


class Survey(StatesGroup):
    name = State()
    age = State()
    hobby = State()


bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def get_main_menu(state: FSMContext):
    data = await state.get_data()
    has_survey = "user_name" in data

    builder = ReplyKeyboardBuilder()

    start_text = "🔄 Изменить анкету" if has_survey else "📝 Начать анкету"

    builder.row(types.KeyboardButton(text=start_text))
    builder.row(types.KeyboardButton(text="❌ Завершить сессию"))

    return builder.as_markup(resize_keyboard=True)


@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(
        "Добро пожаловать! Я бот-анкета.",
        reply_markup=await get_main_menu(state)
    )


@dp.message(F.text.in_({"📝 Начать анкету", "🔄 Изменить анкету"}))
async def start_survey(message: types.Message, state: FSMContext):
    await message.answer(
        "Начинаем заполнение. Как тебя зовут?",
        reply_markup=types.ReplyKeyboardRemove()
    )
    await state.set_state(Survey.name)


@dp.message(F.text == "❌ Завершить сессию")
async def quit_session(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Все данные стерты. Сессия завершена.",
        reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message(Survey.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(user_name=message.text)
    await message.answer(f"Приятно познакомиться, {message.text}! Сколько тебе лет?")
    await state.set_state(Survey.age)


@dp.message(Survey.age)
async def process_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        return await message.answer("Введи возраст цифрами!")

    await state.update_data(user_age=message.text)

    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="IT 💻", callback_data="h_it"))
    builder.row(types.InlineKeyboardButton(text="Спорт ⚽", callback_data="h_sport"))
    builder.row(types.InlineKeyboardButton(text="Дизайн 🎨", callback_data="h_design"))

    await message.answer("Выбери хобби:", reply_markup=builder.as_markup())
    await state.set_state(Survey.hobby)


@dp.callback_query(Survey.hobby)
async def process_hobby(callback: types.CallbackQuery, state: FSMContext):
    hobbies = {"h_it": "IT 💻", "h_sport": "Спорт ⚽", "h_design": "Дизайн 🎨"}
    chosen_hobby = hobbies.get(callback.data)

    await state.update_data(user_hobby=chosen_hobby)

    user_data = await state.get_data()

    summary = (
        f"✅ Анкета успешно заполнена!\n\n"
        f"👤 Имя: {user_data['user_name']}\n"
        f"📅 Возраст: {user_data['user_age']}\n"
        f"🎨 Хобби: {chosen_hobby}"
    )

    await state.set_state(None)

    await callback.message.answer(summary)
    await callback.message.answer(
        "Теперь вы можете изменить анкету или завершить сессию:",
        reply_markup=await get_main_menu(state)
    )
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
