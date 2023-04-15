from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
from utils import *  

load_dotenv()

BOT_PREFIX = '!'
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents().all())

@bot.event
async def on_ready():
        print("Hi, please use /!setup/ to use the bot")

@bot.command()
async def sygn(ctx, caseType, caseName=" "):
    isAllowedChannel = check_channel(ctx.channel.id,ctx.message.guild.id)
    if isAllowedChannel:
        caseNum = get_case_number(ctx,caseType)
        if caseNum != 0:
            result =  f"{caseNum} {caseName}"
            msg = await ctx.send(f"{result}") 
            usr = ctx.message.author
            thread = await msg.create_thread(name=result, auto_archive_duration=10080)
            await thread.add_user(usr)
        else:
            await ctx.send(f"Nieznany typ sprawy [{caseType}]! Wybierz jeden z dostępnych typów: {await get_case_types(ctx.message.guild.id,ctx.channel.id)}")
    else:
        await ctx.send(f"{ctx.message.author.mention}, Ta komenda nie jest obsługiwana na tym kanale.")

@bot.command()
async def setup(ctx,param=" ", val=0):
    if await is_owner(ctx.message.author.id):
        channel = ctx.channel
        match param:
            # case 'channel.east':
                # if val == 0:
                #     await channel.send("Please provide a propper channel_id (use: !setup channel.east <channel_id>)")
                #     for ch in srv.channels:
                #         if str(ch.type) == 'text':
                #             await channel.send(f"name: {ch.name} | ID: {ch.id}")
                # elif param == "channel.east" and val != 0:
                #     isExistingChannel = False
                #     for ch in srv.channels:
                #         if ch.id == val:
                #             isExistingChannel = True
                #     if isExistingChannel:        
                #         listOfGlobals = globals()
                #         listOfGlobals['CHANNEL_EAST'] = val
                #         await channel.send("Done.")
                #     else:
                #         await channel.send("Wrong channel ID.")
            # case 'channel.west':
            #     if val == 0:
            #         await channel.send("Please provide a propper channel_id (use: !setup channel.west <channel_id>)")
            #         for ch in srv.channels:
            #             if str(ch.type) == 'text':
            #                 await channel.send(f"name: {ch.name} | ID: {ch.id}")
            #     elif param == "channel.west" and val != 0:
            #         isExistingChannel = False
            #         for ch in srv.channels:
            #             if ch.id == val:
            #                 isExistingChannel = True
            #         if isExistingChannel:        
            #             configData["ChannelIdWest"] += val
            #             await channel.send("Done.")
            #         else:
            #             await channel.send("Wrong channel ID.")
            case "east.sk":
                listOfGlobals = globals()
                listOfGlobals["eskid"] = val
                await channel.send(f"Last used SK number was set to {val}.")
            case "east.sc":
                listOfGlobals = globals()
                listOfGlobals["escid"] = val
                await channel.send(f"Last used SC number was set to {val}.")
            case "east.sr":
                listOfGlobals = globals()
                listOfGlobals["esrid"] = val
                await channel.send(f"Last used SR number was set to {val}.")
            case "east.rf":
                listOfGlobals = globals()
                listOfGlobals["erfid"] = val
                await channel.send(f"Last used RF number was set to {val}.")
            case "west.sk":
                listOfGlobals = globals()
                listOfGlobals["wskid"] = val
                await channel.send(f"Last used SK number was set to {val}.")
            case "west.sc":
                listOfGlobals = globals()
                listOfGlobals["wscid"] = val
                await channel.send(f"Last used SC number was set to {val}.")
            case "west.sr":
                listOfGlobals = globals()
                listOfGlobals["wsrid"] = val
                await channel.send(f"Last used SR number was set to {val}.")
            case "west.rf":
                listOfGlobals = globals()
                listOfGlobals["wrfid"] = val
                await channel.send(f"Last used RF number was set to {val}.")
            case _:
                await channel.send("Available options:\n" \
                                    # "  channel.east <channel_id> - to set on which channel bot is going to work\n" \
                                    # "  channel.west <channel_id> - to set on which channel bot is going to work\n" \
                                    "  east.sk <lastID>     - to set the last used SK (Sprawy Karne) case number\n" \
                                    "  east.sc <lastID>     - to set the last used SC (Sprawy Cywilne) case number\n" \
                                    "  east.sr <lastID>     - to set the last used SR (Sprawy Rodzinne) case number\n" \
                                    "  east.rf <lastID>     - to set the last used RF (Reprezentowaine Firm) case number\n" \
                                    "  west.sk <lastID>     - to set the last used SK (Sprawy Karne) case number\n" \
                                    "  west.sc <lastID>     - to set the last used SC (Sprawy Cywilne) case number\n" \
                                    "  west.sr <lastID>     - to set the last used SR (Sprawy Rodzinne) case number\n" \
                                    "  west.rf <lastID>     - to set the last used RF (Reprezentowaine Firm) case number\n" \
                                    )
    else:
        await ctx.send(f"ONLY FOR HITMAN")

@bot.command()
async def getserverid (ctx):
    print (ctx.message.guild.id)
    print (ctx.message.guild)

@bot.command()
async def botinfo (ctx):
    await ctx.send(f"Generator sygnatur dla Fitz&Adams / ALO\n"
                   "Dostępne komendy: \n"
                   "!botinfo\n"
                   "!sygn <typ sprawy> <nazwa / opis>"
                   )

bot.run(BOT_TOKEN)