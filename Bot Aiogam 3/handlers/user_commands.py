import random

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums.dice_emoji import DiceEmoji

from keyboards import reply
from filters.is_admin import IsAdmin
from filters.id_admin import id_admin_bot
from filters.is_digit_or_float import CheckForDigit

router = Router()


@router.message(Command('start'), IsAdmin(id_admin_bot))
async def start(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAEKbLBlGIjkgbUNgsPY41foi67itS-2BQACDAEAAiI3jgR7D1jAYFgdrjAE')
    await message.answer(f'Hello, <b>{message.from_user.first_name}</b>',reply_markup=reply.main)

                

@router.message(F.text.lower().in_(["хай","хеллоу","привет"]))
async def greetings(message: Message):
    await message.reply("Привеееть!")

# Получение id/имени с помощью message.from_user.id
@router.message(F.text.lower() == '/my_id')
async def cmd_my_id(message: Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')
    await message.reply(f'Ваше имя: {message.from_user.first_name}')

   

@router.message(Command(commands=['rn','random-number'])) # rn 1-100
async def get_random_number(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split("-")]
    rnum = random.randint(a, b)
    await message.reply(f'Random number: {rnum}')


@router.message(F.text.lower() == '/play')
async def play_games(message: Message):
    x= await message.answer_dice(DiceEmoji.DICE)
    print(x.dice.value)

@router.message(F.text.lower() == '/play_bs')
async def play_games(message: Message):
    asw= await message.answer_dice(DiceEmoji.BASKETBALL)
    print(asw.dice.value)


@router.message(F.text.lower() == '/play_foot')
async def play_games(message: Message):
    foot= await message.answer_dice(DiceEmoji.FOOTBALL)
    print(foot.dice.value)


@router.message(Command('pay'), CheckForDigit())
async def pay_the_order(message: Message, command: CommandObject) -> None:
    await message.answer('Вы успешно оплатили товар!')

