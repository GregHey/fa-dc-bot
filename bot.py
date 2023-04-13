
from discord.ext import commands
import discord
import datetime
from dotenv import load_dotenv
import os
from utils import *
import yaml
load_dotenv()

BOT_PREFIX = '!'
BOT_TOKEN = os.getenv("BOT_TOKEN")
IS_VALID_CHANNEL = False

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=discord.Intents().all())
if os.path.isfile('./data.yml'):
    with open('data.yml', 'r') as file:
        sygnatures = yaml.safe_load(file)
else:
    sygnatures = {
        1058415477526896782: {'name': 'Fitz&Adams', 
                            1058421816353366016: {'name': 'east', 'ids': {'sk': 100, 'sc': 100, 'sr': 100, 'rf': 100}},
                            1069793385591877672: {'name': 'west', 'ids': {'sk': 10, 'sc': 10, 'sr': 10, 'rf': 10}}
                            },
        1089481656605347901: {'name': 'Hitmans',
                            1093165214725320744: {'name': 'FA', 'ids': {'sk': 0, 'sc': 0, 'sr': 0, 'rf': 0}
                            }
                            },
        1061423234559508531: {'name': 'Gregs',
                            1096051901117771847: {'name': 'fa-bot', 'ids': {'sk': 0, 'sc': 0, 'sr': 0, 'rf': 0}
                            }
                            }
    }

@bot.event
async def on_ready():
        with open('data.yml', 'w') as f:
            yaml.dump(sygnatures, f, default_flow_style=False)
        print("Hi, please use /!setup/ to use the bot")

year = datetime.date.today().strftime("%Y")

def caseNumber(ctx, inCaseType):
    caseType = str.lower(inCaseType)
    global sygnatures
    if caseType in sygnatures[ctx.message.guild.id][ctx.channel.id]['ids'].keys():
        sygnatures[ctx.message.guild.id][ctx.channel.id]['ids'][caseType] += 1
        rslt = f"SK {sygnatures[ctx.message.guild.id][ctx.channel.id]['ids'][caseType]}/{year}"
    else:
        rslt = 0
    with open('data.yml', 'w') as f:
        yaml.dump(sygnatures, f, default_flow_style=False)
    return rslt

async def checkAllowedChannel(channelId,serverId):
    global sygnatures
    if serverId in sygnatures.keys():
        if channelId in sygnatures[serverId].keys():
            rslt = True
        else:
            rslt = False
    return rslt

@bot.command()
async def sygn(ctx, caseType, caseName=" "):
    isAllowedChannel = await checkAllowedChannel(ctx.channel.id,ctx.message.guild.id)
    if isAllowedChannel:
        caseNum = caseNumber(ctx,caseType)
        if caseNum != 0:
            result =  f"{caseNum} {caseName}"
            msg = await ctx.send(f"{result}") 
            usr = ctx.message.author
            thread = await msg.create_thread(name=result, auto_archive_duration=10080)
            await thread.add_user(usr)
        else:
            await ctx.send(f"Nieznany typ sprawy [{caseType}]! Wybierz jeden z dostępnych typów: {list(sygnatures[region].keys())}")
    else:
        await ctx.send(f"{ctx.message.author.mention}, Ta komenda nie jest obsługiwana na tym kanale.")

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
async def get_id (ctx):
    print (ctx.message.guild.id)
    print (ctx.message.guild)

@bot.command()
async def info (ctx):
    print (f"Generator sygnatur dla Fitz&Adams / ALO")

bot.run(BOT_TOKEN)

