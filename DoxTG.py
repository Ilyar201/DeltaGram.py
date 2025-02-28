# meta developer: DeltaGram
# meta name: DeltaGramDox
# meta desc: Фейковый доксинг с крутящейся анимацией кольца и скрытыми данными

import asyncio
from .. import loader, utils

class DeltaGramDoxMod(loader.Module):
    strings = {"name": "DeltaGramDox"}

    async def deltagramcmd(self, message):
        """Фейковый доксинг с крутящейся псевдо-анимацией круга, скрытыми данными и автоудалением команды"""
        target = utils.get_args_raw(message) or "Цель"

        try:
            await message.delete()
        except:
            pass

        loading_circle = [
            "◜      ◝", 
            " ◜    ◝ ", 
            "  ◜  ◝  ", 
            "   ◜◝   ", 
            "    ●    ", 
            "   ◝◜   ", 
            "  ◝  ◜  ", 
            " ◝    ◜ ", 
            "◝      ◜"
        ]

        stages = [
            "Инициализация системы...",
            "Подключение к базам данных...",
            "Сбор утёкших данных...",
            "Анализ активности в соцсетях...",
            "Отслеживание геолокации...",
            "Поиск родственников...",
            "Получение данных с устройства...",
            "Идентификация других подключённых устройств...",
            "Анализ банковских операций...",
            "Формирование полного досье..."
        ]

        msg = await message.respond(f"DeltaGram - Запуск анализа цели: {target}\n")

        for stage in stages:
            for _ in range(16):  # 16 кадров анимации на каждый этап
                circle_frame = loading_circle[_ % len(loading_circle)]
                await msg.edit(f"DeltaGram - {stage}\n{circle_frame}")
                await asyncio.sleep(0.2)

        final_message = (
            "✅ DeltaGram - Досье на *{target}* сформировано!\n\n"
            "ФИО: ||Петров Сергей Викторович||\n"
            "Дата рождения: ||12 апреля 1995 года||\n"
            "Возраст: ||29 лет||\n"
            "Номер телефона: ||+7 (913) 555-44-33||\n"
            "Запросы в поисковиках: ||Как скрыть IP, Купить биткоин||\n"
            "Адрес прописки: ||г\\. Новосибирск, ул\\. Ленина, д\\. 25, кв\\. 17||\n"
            "Фактический адрес: ||г\\. Москва, ул\\. Лубянка, д\\. 2||\n"
            "Банковские счета: ||Сбербанк, Тинькофф \общий баланс: 6,800,000 ₽\||\n"
            "Соцсети: ||Telegram, VK, Instagram||\n"
            "Учёба: ||НГУ, факультет информационных технологий||\n"
            "Работа: ||ООО «ТехИнвест», должность: системный аналитик||\n"
            "Подключённые устройства: ||iPhone 14 Pro, MacBook Pro M2||\n"
            "Последняя геолокация: ||Шереметьево, терминал D||\n"
            "IP-адрес: ||178\\.54\\.32\\.11||\n"
            "История поездок: ||Яндекс\\.Такси, BlaBlaCar \52 поездки\||\n"
            "Родственники: ||Петрова Анна Викторовна \мать\, Петров Виктор Сергеевич \отец\||\n"
            "Дополнительная информация: ||Активный пользователь даркнета||"
        ).replace(".", "\\.")

        await msg.edit(final_message.format(target=target), parse_mode="MarkdownV2")