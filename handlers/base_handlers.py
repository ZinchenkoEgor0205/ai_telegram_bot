from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from forms import ImageForm, BaseForm, DialogForm
from handlers.message_request_handlers import process_message_choice
from handlers.image_request_handlers import image_request_router, process_image_choice

base_router = Router()


@base_router.message(F.text.in_({'старт', 'start', 'Хватит', 'Отмена'}))
async def command_start(message: Message, state: FSMContext) -> None:
    try:
        await state.set_state(BaseForm.choosing_the_branch)
        await message.answer(
            f"Что вас интересует?",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text="Картинки"),
                        KeyboardButton(text="Поговорить"),
                    ]
                ],
                resize_keyboard=True,
            ),
        )
    except TypeError as err:
        print(err)
        await message.answer("Nice try!")


@base_router.message(BaseForm.choosing_the_branch)
async def command_start(message: Message, state: FSMContext) -> None:
    if message.text == 'Картинки':
        await state.set_state(ImageForm.describing_an_image)
        await process_image_choice(message, state)
    if message.text == 'Поговорить':
        await state.set_state(DialogForm.writing_a_question)
        await process_message_choice(message, state)


@image_request_router.message(BaseForm.choosing_the_branch)
async def command_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        f"Нажмите 'старт' для начала",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="старт"),
                ]
            ],
            resize_keyboard=True,
        ),
    )
