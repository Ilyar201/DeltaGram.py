# meta developer: DeltaGram 
# meta name: DeltaGramCollector
# meta desc: Имитирует сбор баз данных DeltaGram с постепенным изменением сообщения

import asyncio
from .. import loader, utils

class DeltaGramCollectorMod(loader.Module):
    strings = {"name": "DeltaGramCollector"}

    async def deltagramcmd(self, message):
        max_steps = 140
        delay = 5 / max_steps

        msg = await message.respond("🔊 DeltaGram - Идёт сбор доступных баз данных 1/140")

        for i in range(2, max_steps + 1):
            await asyncio.sleep(delay)
            await msg.edit(f"🔊 DeltaGram - Идёт сбор доступных баз данных {i}/140")

        final_message = (
            "✅ DeltaGram - Сбор баз данных завершён!\n\n"
            "ФИО: ||Василий Васильевич Егор||\n"
            "День рождения: ||07 января 2000 года||\n"
            "Учился: ||В городе Алматы||\n"
            "Родственники: ||Ушвлаоутыджчщчтввтж||\n"
            "Адрес: ||Кунаево 379||\n"
            "Город проживания: ||Балван||\n"
            "Устройство: ||Редми нот 8||\n"
            "Номер телефона: ||+77016792546||"
        )

        await msg.edit(final_message)