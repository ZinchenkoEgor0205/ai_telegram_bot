import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers.image_request_handlers import image_request_router
from handlers.message_request_handlers import message_request_router
from handlers.base_handlers import base_router
from aiogram.fsm.storage.memory import MemoryStorage
from utils.keys import TELEGRAM_TOKEN


async def main() -> None:
    dp = Dispatcher(storage=MemoryStorage())
    base_router.include_routers(message_request_router, image_request_router)
    dp.include_router(base_router)
    bot = Bot(TELEGRAM_TOKEN, parse_mode="HTML")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
