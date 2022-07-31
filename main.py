import discord
import random
from config import TOKEN

randomNumber = ["/randomnumber"]
yesorno = ["/yesorno"]
hello_worlds = ["/start", "/привет", "/hello", "/начать", "/старт"]
info = ["/info"]
client = discord.Client()
@client.event
async def on_ready():
    print("Logged as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    if msg in hello_worlds:
        await message.channel.send(f"Привет, {message.author.mention}, я InsiBot \n Мои доступные команды: \n /profile \n /randomnumber \n /yesorno \n /info")
    if msg == "/profile":
        lgbt = random.randint(1, 100)
        cattle = random.randint(1, 100)
        await message.channel.send(f"{message.author.mention}, ты быдло на {cattle}% и представитель ЛГБТ на {lgbt}%")
    find_yesorno = False
    for item in yesorno:
        if msg.find(item) >= 0:
            find_yesorno = True
            if find_yesorno:
                truefalse = random.randint(1, 2)
                if "?" not in msg:
                    await message.channel.send(f'{message.author.mention}, это не вопрос')
                else:
                    if truefalse == 1:
                        await message.channel.send(f'{message.author.mention}, да, это так')
                    else:
                        await message.channel.send(f'{message.author.mention}, нет, это не так')

    find_randomNumber = False
    for item in randomNumber:
        if msg.find(item) >= 0:
            find_randomNumber = True
            if find_randomNumber:
                split = message.content.split()
                numberOfWords = len(split)
                if numberOfWords == 3:
                    if message.content.split()[1].isnumeric() and message.content.split()[2].isnumeric():
                        firstNumber = msg.split()[1]
                        secondNumber = msg.split()[2]
                        randNumber = random.randint(int(firstNumber), int(secondNumber))
                        await message.channel.send(f'{message.author.mention}, число: {randNumber}')
                    else:
                        await message.channel.send(f'{message.author.mention} это не 2 числа')
                else:
                    await message.channel.send(f'{message.author.mention}, неверный формат')
    find_info = False
    for item in info:
        if msg.find(item) >= 0:
            find_info = True
            if find_info:
                randomInfo = random.randint(1, 100)
                if randomInfo <= 5:
                    await message.channel.send(f'{message.author.mention}, это вообще не правда')
                else:
                    await message.channel.send(f'{message.author.mention}, это правда на {randomInfo}%')
    if msg == "ping":
        await message.channel.send(f'{message.author.mention} Pong')
    if msg == "king":
        await message.channel.send(f'{message.author.mention} Kong')
    if msg == "пинг":
        await message.channel.send(f'{message.author.mention} Понг')
    if msg == "кинг":
        await message.channel.send(f'{message.author.mention} Конг')
client.run(TOKEN)


# example code
# = False
# for item in :
#     if msg.find(item) >= 0:
#         = True
