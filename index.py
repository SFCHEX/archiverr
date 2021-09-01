from discord import Client
from discord.ext import  commands, tasks
from time import sleep
from random import choice, randint



bot=commands.Bot(command_prefix="~",self_bot=True)

def modify(thing,thing2):
    with open(thing,"a") as f:
        f.write(thing2)
        f.close

def use(thing):
    with open(thing) as f:
        lines = f.readlines()
    return lines

@bot.event
async def on_ready():
    group=bot.get_channel(623242030734376970)
    async for message in group.history(limit=102400,oldest_first=True):
        time =str(message.created_at)

        reaction_names=[]
        for reaction in message.reactions:
            try:
                reaction_names.append(reaction.emoji.name)
            except:
                reaction_names.append(reaction.emoji)

        if len(message.reactions)==0:
            text=f"{message.author} > {time[ :len(time)-7]} | {message.content}\n\n"
        else:

            text=f"{message.author} > {time[ :len(time)-7]} | {message.content}\n\n ^ REACTIONS {reaction_names}\n\n"


        modify("DDD",text)

        

        


    


   



bot.run("mfa.I_FTfuRQyRUkD91ENneYK2DYgJGfDWvCsHjpeu8IU1g-JuwKt_zxCjAUdZm1mraKZA5EQcZFvv346bfGsXmM",bot=False)

