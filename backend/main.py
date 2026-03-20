import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from datetime import datetime

API_TOKEN = '8695954271:AAGUGWGkKElRzhV8jYDKrHC_mzLqzO-5o58'

logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot, storage=storage)

@dispatcher.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    from backend.database import GameDatabase
    db = GameDatabase('street_fighter.db')
    db.create_player(message.from_user.id, message.from_user.username or f'Player_{message.from_user.id}')
    await message.answer('🥊 Welcome to Street Fighter Game! 🥊\n\nYour journey as a street fighter begins now!\n\n/game - Start the game\n/profile - View your profile\n/gym - Train at the gym\n/battles - View available battles\n/clan - Clan management')

@dispatcher.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    help_text = '''\n🥊 **STREET FIGHTER GAME - Help**\n\n**Commands:**\n/start - Start the game\n/game - Open mini app\n/profile - View your stats\n/gym - Train your stats\n/battles - Fight other players\n/clan - Manage your clan\n/leaderboard - View top players\n/shop - Buy items\n/help - This help message\n\n**Game Features:**\n- 🎯 Level up and gain experience\n- 💪 Train strength, agility, endurance\n- 🏆 Compete in 1v1 battles\n- 👥 Join or create a clan\n- 🏋️ Own your own gym and earn passive income\n- 💰 Complex economy system\n- ⭐ Earn trophies and reputation\n'''    
    await message.answer(help_text, parse_mode='Markdown')

@dispatcher.message_handler(commands=['profile'])
async def profile_handler(message: types.Message):
    from backend.database import GameDatabase
    db = GameDatabase('street_fighter.db')
    player = db.get_player(message.from_user.id)
    if player:
        profile_text = f'''\n👤 **{player[1]}**\n\n📊 **Stats:**\nLevel: {player[2]} | Experience: {player[3]}\nAge: {player[4]} | Health: {player[5]}\n\n💪 **Attributes:**\nStrength: {player[6]} | Agility: {player[7]} | Endurance: {player[8]}\n\n💰 **Resources:**\nMoney: {player[9]} BYN | Stars: {player[10]}\n\n🏆 **Battle Stats:**\nWins: {player[14]} | Losses: {player[15]}\nReputation: {player[11]}\n\n📍 Location: {player[17]}\n        '''
        await message.answer(profile_text, parse_mode='Markdown')
    else:
        await message.answer('Player not found. Use /start to create a profile.')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dispatcher, skip_updates=True)