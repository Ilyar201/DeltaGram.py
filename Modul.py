# meta developer: DeltaGram
# meta name: DeltaGramCollector
# meta desc: Имитирует сбор баз данных DeltaGram с постепенным изменением сообщения

import asyncio
from .. import loader, utils

class DeltaGramCollectorMod(loader.Module):
    """Имитирует процесс сбора данных через DeltaGram"""
    strings = {"name": "DeltaGramCollector"}

    async def deltagramcmd(self, message):
        """Запускает процесс сбора данных DeltaGram"""
        max_steps = 140
        delay = 0.2  # Задержка в секундах между обновлениями (можно изменить)

        msg = await message.respond("DeltaGram - Идёт сбор доступных баз данных 1/140")

        for i in range(2, max_steps + 1):
            await asyncio.sleep(delay)
            await msg.edit(f"DeltaGram - Идёт сбор доступных баз данных {i}/140")

        await msg.edit("✅ DeltaGram - Сбор баз данных завершён!")