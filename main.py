from aiogram import Bot,Dispatcher,types,executor
import instaloader
import sec
import os
from shutil import rmtree
import requests as rq

bot = Bot(sec.api_key)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def welcome(payam: types.Message):
    await payam.reply("Hello, welcome to the Instagram profile downloader bot 😌")
    await payam.answer("Please send the desired Instagram account ID without '@'")

@dp.message_handler()
async def download(payam: types.Message):
    user = payam.text
    await payam.answer("Please wait 🙏")
    
    ig = instaloader.Instaloader()
    ig.login(sec.ig_user, sec.ig_pass)

    ig.download_profile(user, profile_pic_only=True)
    ll = os.listdir(user)

    for i in ll:
        if ".jpg" in i:
            ax = i
    pic = f"{user}/{ax}"

    await bot.send_photo(chat_id=payam.chat.id, photo=open(pic,"rb"))
    await payam.answer("Here you are 🫡")

    rmtree(user)


executor.start_polling(dp)




