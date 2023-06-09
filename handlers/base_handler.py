
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import types, Router
from aiogram import F

from utils.image_generator import generate_image
from utils.keys import OPENAI_KEY
from forms import SectionForm

router = Router()

@router.message(SectionForm.image_description)
async def process_description(message: Message, state: FSMContext) -> None:
    image_data = await generate_image(message.text, OPENAI_KEY)
    image = types.input_file.BufferedInputFile(file=image_data, filename='test')
    await state.set_state(SectionForm.enter)
    await message.answer_photo(
        photo=image,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Ещё одну"),
                    KeyboardButton(text='Хватит')
                ]
            ],
            resize_keyboard=True,
        ),
    )


@router.message(SectionForm.enter, F.text.in_({'Ещё одну', 'Картинки'}))
async def process_choice(message: Message, state: FSMContext) -> None:
    await state.set_state(SectionForm.image_description)
    await message.answer('Опишите картинку')


@router.message()
async def command_start(message: Message, state: FSMContext) -> None:
    try:
        await state.set_state(SectionForm.enter)
        await message.answer(
            f"Что вас интересует?",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Картинки"),
                    ]
                ],
                resize_keyboard=True,
            ),
        )
    except TypeError as err:
        print(err)
        await message.answer("Nice try!")
