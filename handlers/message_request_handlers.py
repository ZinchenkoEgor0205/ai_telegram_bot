from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router
from aiogram import F
from aiogram.types import User

from utils.keys import OPENAI_KEY
from utils.answer_generator import answer_the_question

from forms import DialogForm, BaseForm

message_request_router = Router()


@message_request_router.message(DialogForm.writing_a_question, F.text.in_({'Поговорить'}))
async def process_message_choice(message: Message, state: FSMContext) -> None:
    await state.set_state(DialogForm.keeping_the_dialog)
    await message.answer('Спросите о чём-нибудь', reply_markup=ReplyKeyboardRemove())


@message_request_router.message(DialogForm.keeping_the_dialog)
async def process_the_question(message: Message, state: FSMContext) -> None:
    await state.set_state(DialogForm.final_message_choice)
    username = message.from_user.username
    answer = await answer_the_question(message.text, OPENAI_KEY, username)
    await message.answer(
        answer,
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='Хватит')
                ]
            ],
            resize_keyboard=True,
        ),
    )


@message_request_router.message(DialogForm.final_message_choice)
async def process_choice(message: Message, state: FSMContext) -> None:
    if message.text == 'Хватит':
        await state.clear()
    else:
        await state.set_state(DialogForm.keeping_the_dialog)
        await process_the_question(message, state)
