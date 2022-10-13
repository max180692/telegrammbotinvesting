
import settingsbot
import logging
from aiogram import Bot, Dispatcher, executor, md, types
from aiogram.utils.exceptions import MessageIsTooLong
from aiogram.dispatcher.filters import Text
from investing import Investing


investing = Investing()

logging.basicConfig(level=logging.INFO)


bot = Bot(token=settingsbot.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    button_1 = types.KeyboardButton(text="Получить категории")
    keyboard.add(button_1)
    
    await message.answer("Нажми на кнопку Получить категории", reply_markup=keyboard)

@dp.message_handler(Text(equals="Получить категории"))
async def cmd_info_category(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    text_data = investing.get_list_category()
    for category1 in text_data:
        keyboard.add(types.InlineKeyboardButton(text=category1, callback_data=category1))
    #print(keyboard)
    await message.answer("Список категорий", reply_markup=keyboard)

@dp.callback_query_handler()
async def get_subcategory(callback: types.CallbackQuery,):
    keyboard = types.InlineKeyboardMarkup()
    investing.set_subcategory(callback.data)
    if investing.get_action():
        text_data = investing.get_list_subcategory()
        for category2 in text_data:
            keyboard.add(types.InlineKeyboardButton(text=category2, callback_data=category2))
        await callback.message.answer("Список подкатегорий",reply_markup=keyboard)
    else:
        table = investing.set_info_subcategory(callback.data)
        try:
            await callback.message.answer(f'{table}')
        except MessageIsTooLong:
            await callback.message.answer(investing.get_url())



if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)

