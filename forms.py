from aiogram.fsm.state import StatesGroup, State


class BaseForm(StatesGroup):
    choosing_the_branch = State()
    process_the_choice = State()


class ImageForm(StatesGroup):
    enter = State()
    describing_an_image = State()
    processing_image_request = State()
    final_image_choice = State()


class DialogForm(StatesGroup):
    writing_a_question = State()
    keeping_the_dialog = State()
    final_message_choice = State()
