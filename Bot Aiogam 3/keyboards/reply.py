from aiogram.types import (ReplyKeyboardMarkup,
                            KeyboardButton,
                            KeyboardButtonPollType,
                            ReplyKeyboardRemove
)

# скобки это новая линия кнопок
main_kb = [
    [KeyboardButton(text='Смайлик'),
     KeyboardButton(text='Ссылки')],
    [KeyboardButton(text='Калькулятор'),
     KeyboardButton(text='Спец. кнопки')]
]
main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберете дейсвие из меню',
                           selective = True,
                           one_time_keyboard = True)

special_buttons_kb = [
    [KeyboardButton(text='Send u geo',request_location=True),
     KeyboardButton(text='Send u contact',request_contact=True),
     KeyboardButton(text='Start quiz and voting',request_poll= KeyboardButtonPollType())],
    [KeyboardButton(text='Back')]
]
special_buttons = ReplyKeyboardMarkup(keyboard=special_buttons_kb,
                                      resize_keyboard=True)

rmk = ReplyKeyboardRemove()