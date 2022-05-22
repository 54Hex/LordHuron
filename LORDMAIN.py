import nextcord
from nextcord.ext import commands 
import random 


# /-------------Upcoming plans-------------/
# 1. Host it on a server so that it works most 
# of the time instead of relying on this mac 
# ^ heroku doesnt want me to hook it up with github >:( 

Token = "OTc2ODE5MTY5MDM3MjcxMDcy.GWwSD7.bk8pFVFJjGtl3fIWmBRY4mvT1T9LnFqy6TRMzk"
client = nextcord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event 
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_msg} ({channel})')

    if message.author == client.user:
        return 
    
    if message.channel.name == 'prison-cafeteria':
        if user_msg.lower() == 'sup':
            await message.channel.send(f'quack {username}!')
            return 

        elif user_msg.lower() == 'bye':
            await message.channel.send(f'cya {username}!')
            return 

        elif user_msg.lower() == '!help':
            await message.channel.send("""
            heres a number of things that I can do! 
            0. Introduce myself! (!whoareyou)
            1. I can give you a random number! (!random)
            2. Clear messages (WIP)
            3. Sing lord huron songs (obv hehe) (WIP)
            4. ???
            """)
            return 

        elif user_msg.lower() == '!random':
            randresponse = f'RaNd0M nUMbEr: {random.randrange(1000000)}'
            await message.channel.send(randresponse)
            return

        elif user_msg.lower() == '!whoareyou':
            await message.channel.send('I am huron the duck (:')
            return
        

    if message.channel.name == 'prisoncell':
        if message.content != "":
            await message.channel.send(f'n0')
            await message.delete()
            await message.channel.purge(limit = 1)
            return 



client.run(Token)