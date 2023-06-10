from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import logging
from handlers.base_handlers import command_start

exception_router = Router()


@exception_router.message()
async def handle_exceptions(message: Message, state: FSMContext) -> None:
    try:
        await state.clear()
        await command_start(message=message, state=state)
    except Exception as err:
        logging.log(logging.ERROR, err)
        await message.answer('Что-то пошло не так')
