from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



socials_kb = [
    [InlineKeyboardButton(text='Telegram', url='https://t.me/sudoteach')],
    [InlineKeyboardButton(text='YouNube', url='https://youtube.com/@sudoteach')]

]
socials = InlineKeyboardMarkup(inline_keyboard=socials_kb)

sub_kb = [
    [InlineKeyboardButton(text='Подписаться', url='https://t.me/fsoky_community')]

]
sub = InlineKeyboardMarkup(inline_keyboard=sub_kb)