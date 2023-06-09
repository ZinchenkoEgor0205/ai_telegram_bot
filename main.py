import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers.base_handler import router

from aiogram.fsm.storage.memory import MemoryStorage
from utils.keys import TELEGRAM_TOKEN

async def main() -> None:
    # Dispatcher is a root router
    dp = Dispatcher(storage=MemoryStorage())
    # ... and all other routers should be attached to Dispatcher
    dp.include_router(router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TELEGRAM_TOKEN, parse_mode="HTML")
    # And the run events dispatching
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
