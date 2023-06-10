from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram import types, Router
from aiogram import F
from utils.image_generator import generate_image
from utils.keys import OPENAI_KEY
from forms import ImageForm

image_request_router = Router()


@image_request_router.message(ImageForm.describing_an_image, F.text.in_({'Ещё одну', 'Картинки'}))
async def process_image_choice(message: Message, state: FSMContext) -> None:
    await state.set_state(ImageForm.processing_image_request)
    await message.answer(
        'Опишите картинку',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Отмена"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@image_request_router.message(ImageForm.processing_image_request)
async def process_image_request(message: Message, state: FSMContext) -> None:
    if message.text == 'Отмена':
        await state.clear()
    else:
        await state.set_state(ImageForm.final_image_choice)
        await process_image_description(message, state)


@image_request_router.message(ImageForm.final_image_choice)
async def process_image_description(message: Message, state: FSMContext) -> None:
    image_data = await generate_image(message.text, OPENAI_KEY)
    image = types.input_file.BufferedInputFile(file=image_data, filename='test')
    await state.set_state(ImageForm.enter)
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
