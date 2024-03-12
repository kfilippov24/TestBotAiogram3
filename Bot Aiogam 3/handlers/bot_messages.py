from aiogram import Router, F
from aiogram.types import Message


from keyboards import reply, inline, builders, fabrics
from data.subloader import get_json


router = Router()


@router.message(F.text.lower().in_(["хай","хеллоу","привет"]))
async def greetings(message: Message):
    await message.reply("Привеееть!")


@router.message()
async def echo(message: Message) -> None:
    msg = message.text.lower()
    smiles = await get_json("smiles.json")

    if msg == 'ссылки':
        await message.answer('Вот ваши ссылки', reply_markup=inline.socials)
    elif msg =='спец. кнопки':
        await message.answer('Спец. кнопки',reply_markup=reply.special_buttons)
    elif msg =='калькулятор':
        await message.answer('Введите выражение',reply_markup=builders.calc())
    elif msg =='смайлик':
        await message.answer(f'{smiles[0][0]} <b>{smiles[0][1]}</b>',reply_markup=fabrics.paginator())
    else:
        await message.answer('Вы вкрнулись назад',reply_markup=reply.main)

@router.message()
async def echo(message: Message):
    await message.answer(f"I don't understand u!")