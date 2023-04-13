
from discord.ext import commands
import discord
import datetime
from dotenv import load_dotenv
import os
from utils import *
load_dotenv()

# CHANNEL_ID = 1092797560579690516
BOT_PREFIX = '!'
BOT_TOKEN = os.getenv("BOT_TOKEN")
IS_VALID_CHANNEL = False

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents().all())

@bot.event
async def on_ready():
        print("Hi, please use /!setup/ to use the bot")

eskid = escid = esrid = erfid = wskid = wscid = wsrid = wrfid = 0

year = datetime.date.today().strftime("%Y")

def caseNumber(inCaseType, inRegion='east'):
    caseType = str.lower(inCaseType)
    listOfGlobals = globals()
    id = 0
    match inRegion:
        case 'east':
            match caseType:
                case 'sk':
                    listOfGlobals['eskid'] += 1
                    id = listOfGlobals['eskid']
                    rslt = f"SK {id}/{year}"
                case 'sc' :
                    listOfGlobals['escid'] += 1
                    id = listOfGlobals['escid']
                    rslt = f"SC {id}/{year}"
                case 'sr' :
                    listOfGlobals['esrid'] += 1
                    id = listOfGlobals['esrid']
                    rslt = f"SR {id}/{year}"
                case 'rf' :
                    listOfGlobals['erfid'] += 1
                    id = listOfGlobals['erfid']
                    rslt = f"RF {id}/{year}"
                case _  :
                    rslt = "Nieznany typ sprawy!"
            return rslt
        case 'west':
            match caseType:
                case 'sk':
                    listOfGlobals['wskid'] += 1
                    id = listOfGlobals['wskid']
                    rslt = f"SK {id}/{year}"
                case 'sc' :
                    listOfGlobals['wscid'] += 1
                    id = listOfGlobals['wscid']
                    rslt = f"SC {id}/{year}"
                case 'sr' :
                    listOfGlobals['wsrid'] += 1
                    id = listOfGlobals['wsrid']
                    rslt = f"SR {id}/{year}"
                case 'rf' :
                    listOfGlobals['wrfid'] += 1
                    id = listOfGlobals['wrfid']
                    rslt = f"RF {id}/{year}"
                case _  :
                    rslt = "Nieznany typ sprawy!"
            return rslt

async def checkAllowedChannel(channelId,region):
    match region:
        case "east":
            if channelId == int(await get_east_id()):
                rslt = True
            else:
                rslt =  False
        case "west":
            if channelId == int(await get_west_id()):
                rslt =  True
            else:
                rslt =  False
        case _:
            rslt =  False
    return rslt

async def sygn(ctx, caseType, caseName=" ", region="east"):
    isAllowedChannel = await checkAllowedChannel(ctx.channel.id,region)
    if isAllowedChannel:
        result =  f"{caseNumber(caseType,region)} {caseName}"
        msg = await ctx.send(f"{result}") 
        usr = ctx.message.author
        thread = await msg.create_thread(name=result, auto_archive_duration=10080)
        await thread.add_user(usr)
    else:
        await ctx.send(f"{ctx.message.author.mention}, You are not allowed to use this command here.")

@bot.command()
async def setup(ctx,param=" ", val=0):
    if await is_owner(ctx.message.author.id):
        channel = ctx.channel
        srv = ctx.message.guild
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
            case "east.sk":
                listOfGlobals = globals()
                listOfGlobals["wskid"] = val
                await channel.send(f"Last used SK number was set to {val}.")
            case "east.sc":
                listOfGlobals = globals()
                listOfGlobals["wscid"] = val
                await channel.send(f"Last used SC number was set to {val}.")
            case "east.sr":
                listOfGlobals = globals()
                listOfGlobals["wsrid"] = val
                await channel.send(f"Last used SR number was set to {val}.")
            case "east.rf":
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
async def east(ctx, caseType, caseName=""):
    await ctx.message.delete()
    await sygn(ctx, caseType, caseName, "east")

@bot.command()
async def west(ctx, caseType, caseName=""):
    await ctx.message.delete()
    await sygn(ctx, caseType, caseName, "west")

@bot.command()
async def get_id (ctx):
    print (ctx.message.guild.id)
    print (ctx.message.guild)


bot.run(BOT_TOKEN)

