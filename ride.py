import asyncio
import logging
import redis
import random
import sys
from os import getenv

# from typing import Any, Dict

from aiogram import Bot, Dispatcher, Router,F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import(
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

TOKEN = '6884573900:AAGzEytPI8fooM_tFLqCibR58LS5LY5h2TI'

router = Router()


REDIS_CLOUD_HOST = 'redis-10858.c323.us-east-1-2.ec2.cloud.redislabs.com'
REDIS_CLOUD_PORT = 10858
REDIS_CLOUD_PASSWORD = 'HQ11JISBZd9D04F7av96WskGSBqUwX44'

redis_conn = redis.StrictRedis(
    host=REDIS_CLOUD_HOST,
    port=REDIS_CLOUD_PORT,
    password=REDIS_CLOUD_PASSWORD,
    decode_responses=True,
)


class Form(StatesGroup):
    start = State()
    name = State()
    phone = State()
    service = State()
    passenger = State()
    location = State()
    drive = State()
    accept = State()
    check = State()
    cancel = State()
    done = State()
    edit_p = State()
    edit_d = State()

"""
Driver or Passenger
"""
    
@router.message(CommandStart())
async def command_start(message:Message,state:FSMContext) -> None:
    await starter(message,state)


@router.message(Form.start)
async def starter(message:Message,state:FSMContext) -> None:
    id = message.from_user.id
    if redis_conn.exists(id) and redis_conn.hget(id,'driver') == 'no':
        await state.set_state(Form.passenger)
        await message.answer(f'hello, {message.from_user.username}, welcome back',
            reply_markup = ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text = "Book"),
                KeyboardButton(text = "profile"),
            ]
        ],resize_keyboard=True,
    ))
    elif redis_conn.exists(id) and redis_conn.hget(id,'driver') == 'yes':
        await state.set_state(Form.drive)
        await message.answer("hello driver",
            reply_markup = ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text = "Active Order"),
                KeyboardButton(text = "profile"),
            ]
        ],resize_keyboard=True,
    ))
    else:
        await state.set_state(Form.name)
        await message.answer(f'registering {message.from_user.username}')
        await message.answer(f'what is your name?')

#signup
@router.message(Form.name)
async def get_name(message:Message, state:FSMContext) -> None:
    await state.set_state(Form.phone)
    id = message.from_user.id
    redis_conn.hset(id,'fullname',message.text)
    # phone = 
    await message.answer('provide your contact',reply_markup =ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text = "Share Contact",request_contact=True),
            ]
        ],resize_keyboard=True,
        ))

@router.message(Form.phone)
async def get_phone(message:Message, state:FSMContext) -> None:
    await state.set_state(Form.service)
    id = message.from_user.id
    redis_conn.hset(id,'phone',message.contact.phone_number)
    await message.answer('Are you a driver?',
        reply_markup = ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text = "yes"),
                KeyboardButton(text = 'no')
            ]
        ],resize_keyboard=True,
        )
    )

@router.message(Form.service)
async def user_type(message:Message,state:FSMContext) -> None:
    id = message.from_user.id
    redis_conn.hset(id,'driver',message.text)
    await message.answer('you are registerd!')
    await state.set_state(Form.start)
    await starter(message,state)


# show profile
@router.message(Form.passenger, F.text.casefold() == 'profile')
async def profile(message:Message,state:FSMContext) -> None:
    values = redis_conn.hgetall(message.from_user.id)
    await message.answer(f'Name: {values["fullname"]}\nPhone: {values["phone"]}\nDriver: {values["driver"]}',
        reply_markup = ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text = "EDIT"),
            ]
        ],resize_keyboard=True,
        )
    )

@router.message(Form.edit_p, F.text.casefold() == 'edit')
async def profile(message:Message,state:FSMContext) -> None:
    await state.set_state(Form.name)
    await get_name()

#passanger
@router.message(Form.passenger, F.text.casefold() == 'book')
async def book(message:Message,state:FSMContext) -> None:
    await message.answer('Destination?')
    await state.set_state(Form.location)

@router.message(Form.location)
async def location(message:Message,state:FSMContext) -> None:
    await state.set_state(Form.cancel)
    redis_conn.hset('booked',message.from_user.id,message.text)
    await message.answer('waiting for driver...')
    await message.answer('do you want to ...',
    reply_markup=ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text = 'cancel')        
        ]],resize_keyboard=True,
    ))

@router.message(Form.cancel)
async def cancel(message:Message,state:FSMContext) -> None:
    user_id = message.from_user.id
    print(message.from_user.username)
    redis_conn.hdel('booked',user_id)
    await message.answer('Canceled!')
    await starter(message,state)
    await state.set_state(Form.start)


## driver
@router.message(Form.drive, F.text.casefold()=='active order')
async def recive_order(message:Message,state:FSMContext) -> None:
    button_val = redis_conn.hgetall('booked')
    # await state.update_data(user = str(key))
    await message.answer("Locations",
        reply_markup=ReplyKeyboardMarkup(keyboard=[
            [KeyboardButton(text = (txt+","+ str(key))) for key,txt in button_val.items()]
        ],resize_keyboard=True,
    ))
    # print(des)
    await state.update_data(user = button_val)
    await state.set_state(Form.accept)

@router.message(Form.accept)
async def recive_order(message:Message,state:FSMContext) -> None:
    await state.set_state(Form.check)
    text,user_id = message.text.split(',')
    user_id = int(user_id)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.send_message(chat_id=user_id,text = f'your journey is going to take {random.randrange(6)}km, and {random.randrange(3)}hr',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[
                KeyboardButton(text = 'cancel')        
            ]],resize_keyboard = True,
        ))
    await message.answer('Check the status of the user?',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[
                KeyboardButton(text = 'check')        
            ]],resize_keyboard = True,
        ))
    await state.update_data(userid = user_id)

@router.message(Form.check, F.text.casefold() == 'check')
async def recive_order(message:Message,state:FSMContext) -> None:
    user_id = await state.get_data('userid')
    if redis_conn.exists('active') and not redis_conn.hexists('active',user_id):
        await message.answer('The user cancel the trip')
        await state.set_state(Form.start)
        await starter()
    else:
        await state.set_state(Form.done)
        await message.answer('Make it done!',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[
                KeyboardButton(text = 'Done')      
            ]],resize_keyboard = True,
        ))

@router.message(Form.check, F.text.casefold() == 'done')
async def done(message:Message,state:FSMContext) -> None:
    await message.answer('you finish your trip')
    user_id = await state.get_data('userid')
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await bot.send_message(chat_id=user_id,text='Thank you for having ride trip')

#edit for driver
# show profile
@router.message(Form.drive, F.text.casefold() == 'profile')
async def profile(message:Message,state:FSMContext) -> None:
    values = redis_conn.hgetall(message.from_user.id)
    await state.set_state(Form.edit_d)
    await message.answer(f'Name: {values["fullname"]}\nPhone: {values["phone"]}\nDriver: {values["driver"]}',
        reply_markup = ReplyKeyboardMarkup(keyboard=[
            [
                KeyboardButton(text = "EDIT"),
            ]
        ],resize_keyboard=True,
        )
    )

@router.message(Form.edit_d, F.text.casefold() == 'edit')
async def profile(message:Message,state:FSMContext) -> None:
    await message.answer("Editing your profile")
    await state.set_state(Form.name)
    await get_name(message,state)

async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())