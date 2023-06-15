


from env import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
import keyboard as kb
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

connected_users: list[int] = []


@dp.message_handler(commands=['start'], state='*')
async def send_welcome(message: types.Message, state: FSMContext):
    """
    Бот понимает команду /start, дает доступ к кнопкам (основе)
    """
    await message.reply(
        "Привет, я Алиса! Выбери лекарство, которое тебе нужно!/\nЧтобы вернуться обратно в меню, нажми на кнопку '/start'!\nPowered by yaarrrk or @hshepisa!",
        reply_markup=kb.greet)


@dp.message_handler(commands=(['Голова']))
async def head(message: types.Message):
    """
    Выдаёт ссылки на лекарства
    """
    await message.reply("Выберите из списка лекарств нужное(все помогают от боли в голове)", reply_markup=kb.golova)


@dp.message_handler(commands=(['Шея']))
async def neck(message: types.Message):
    """
    Выдаёт ссылки на лекарства
    """
    await message.reply("Выберите из списка лекарств нужное(все помогают от боли в районе Шеи)", reply_markup=kb.sheya)


@dp.message_handler(commands=(['Боль_в_плечах']))
async def shoulders(message: types.Message):
    """
    Выдаёт ссылки на лекарства
    """
    await message.reply("Выберите из списка лекарств нужное(все помогают от боли в плечах)", reply_markup=kb.plech)


@dp.message_handler(commands=(['боль_в_районе_бидцепсов']))
async def biceps(message: types.Message):
    """
    Выдаёт ссылки на лекарства
    """
    await message.reply(
        "Люди часто ощущают боль в мышцах рук, выше локтя после интенсивных тренировок, непривычных физических нагрузок, ушибов. Но она может появляться и без видимых причин. Боль может быть постоянной или возникать после физических нагрузок, в обеих руках или только в левой либо в правой. Даже если она ощущается слабо, постоянный дискомфорт мешает спать, работать. Согревающие мази, обезболивающие препараты убирают ее на несколько часов. Такая боль может быть вызвана безобидными причинами, которые легко устранить, или сигнализировать о серьезных заболеваниях. Не используйте лекарства, не выяснив, почему болят мышцы рук. Я не смогла найти Лекарства, но могу дать совет: сходите к травматологу, попарьтесь в бане, сходите в спа-центре, или просто полежите/поспитею Удачи)")


@dp.message_handler(commands=(['Боль_в_районе_груди']))
async def breast(message: types.Message):
    """
    Выдаёт ссылки на лекарства
    """
    await message.reply("Выберите из списка лекарств нужное(все помогают от боли в груди)", reply_markup=kb.gryt)


@dp.message_handler(commands=(['Боль_в_животе']))
async def stomach(message: types.Message):
    """
    Выдаёт ссылки на лекарства
    """
    await message.reply("Выберите из списка лекарств нужное(все помогают от боли в животе)", reply_markup=kb.zshivot)


@dp.message_handler(commands=(['Боль_в_районе_бедер']))
async def hip(message: types.Message):
    """
    Выдаёт ссылки на лекарства
    """
    await message.reply(
        'При возникновении болевых ощущений двигательная активность должна быть снижена. Также необходимо уменьшить нагрузку на больной сустав. Не следует медлить с обращением к врачу. Чем быстрее будет назначено лечение, тем больше шансов сохранить функцию сочленения и избежать осложнений. ')


@dp.message_handler(commands=(['Болят_икры']))
async def caviar(message: types.Message):
    """
    Выдаёт ссылки на лекарства
    """
    await message.reply(
        "При травмах мышц в икрах ног массаж сочетают с тепловыми процедурами. Избавиться от боли в икрах помогут также анальгетики. Если диагностирован инфекционный неврит, то назначают курс противовирусных средств и антибиотиков. Сосудорасширяющие лекарства используют при заболевании, которое возникло вследствие ишемии.")


@dp.message_handler(commands=(['Болит_кисть_ноги']))
async def brush_foot(message: types.Message):
    """
    Выдаёт ссылки на лекарства
    """
    await message.reply("Выберите из списка лекарств нужное(все помогают от боли в ногах)", reply_markup=kb.nogi)


@dp.message_handler(commands=(['Геолокация']))
async def geolocation(message: types.message):
    """Переводит в файл keyboard, где находиться кнопка для определения контакта и геолокации"""
    await message.reply('Определи свою геолокацию, или Контакт', reply_markup=kb.markup_requests)


@dp.message_handler(commands=(['Чатик']))
async def chat(message: types.Message, state: FSMContext):
    """Создаёт команду чата, предлагает пообщаться"""
    await message.answer("Привет! Хочешь пообщатся с людьми по поводу своих проблем со здоровьем?\n Напиши своё имя!")

    await state.set_state("q1")


@dp.message_handler(state="q1")
async def process_name(message: types.Message, state: FSMContext):
    """Узнаёт Имя юзера для Функции echo"""
    name = message.text
    await state.update_data({"name": name})
    await state.set_state("q2")
    await message.answer("Сколько тебе лет?")


@dp.message_handler(state="q2")
async def process_age(message: types.Message, state: FSMContext):
    """Узнаем возраст юзера и дает доступ к чату"""
    age = message.text
    if age.isdigit():
        await state.update_data({"age": int(age)})
        await state.set_state("echo")
        await message.answer("Теперь ты в чате! Напиши /leave для выхода!" )
        connected_users.append(message.from_user.id)
        await bot.send_chat_action(message.from_user.id, types.ChatActions.TYPING)
    else:
        data = await state.get_data()
        await message.answer(f"Напиши свой возраст цифрами, {data['name']}")

@dp.message_handler(commands='leave', state='*')
async def leave(message:types.Message, state: FSMContext):
    """Если бы этой функции небыло, то юзер не смог бы выйти мз чата"""
    await message.reply('Ты вышел из чата! Напиши /start для выхода в меню!')
    await state.reset_state(with_data=False)


@dp.message_handler(state="echo")
async def echo(message: types.Message, state: FSMContext):
    """Позволяет общаться  в юзерами в чате"""
    tasks = []
    data = await state.get_data()
    name, age = data['name'], data['age']
    for user_id in connected_users:
        if message.from_user.id == user_id:
            continue
        try:
            await bot.send_message(user_id, f'{name}, {age} : {message.text}')
        except ConnectionError as er:
            print(f'User {user_id} blocked the bot')
            connected_users.remove(user_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
