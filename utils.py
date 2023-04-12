
# from discord.ext import commands
# import discord
# import datetime
import os
import json
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

# async def checkAllowedChannel(channelId,region):
#     match region:
#         case "east":
#             global CHANNEL_EAST
#             if channelId == CHANNEL_EAST:
#                 rslt = True
#             else:
#                 rslt =  False
#         case "west":
#             global CHANNEL_WEST
#             if channelId == CHANNEL_WEST:
#                 rslt =  True
#             else:
#                 rslt =  False
#         case _:
#             rslt =  False
#     return rslt

async def is_owner(userId):
    if userId == int(os.getenv("OWNER_ID")):
        return True
    else:
        return False

async def get_token():
    TOKEN = os.getenv("BOT_TOKEN")
    return TOKEN

async def setup_server(ctx):
    return True

async def get_east_id():
    EAST_CH = os.getenv("CHANNEL_EAST")
    return EAST_CH

async def get_west_id():
    WEST_CH = os.getenv("CHANNEL_WEST")
    return WEST_CH