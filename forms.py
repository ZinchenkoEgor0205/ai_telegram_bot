from aiogram.fsm.state import StatesGroup, State


class SectionForm(StatesGroup):
    enter = State()
    image_description = State()
    fincal_choice = State()
