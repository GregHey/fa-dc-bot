import datetime
import os
from dotenv import load_dotenv
from supabase import create_client, Client
import yaml

load_dotenv()
URL=os.getenv("VITE_SUPABASE_URL")
KEY=os.getenv("VITE_SUPABASE_KEY")

supabase = Client(URL, KEY)

year = datetime.date.today().strftime("%Y")

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

def check_channel(channelId, serverId):
    global sygnatures
    if serverId in sygnatures.keys():
        if channelId in sygnatures[serverId].keys():
            rslt = True
        else:
            rslt = False
    return rslt


def get_case_number(ctx, inCaseType):
    caseType = str.lower(inCaseType)
    global sygnatures
    if caseType in sygnatures[ctx.message.guild.id][ctx.channel.id]['ids'].keys():
        sygnatures[ctx.message.guild.id][ctx.channel.id]['ids'][caseType] += 1
        rslt = f"{str.upper(caseType)} {sygnatures[ctx.message.guild.id][ctx.channel.id]['ids'][caseType]}/{year}"
    else:
        rslt = 0
    with open('data.yml', 'w') as f:
        yaml.dump(sygnatures, f, default_flow_style=False)
    return rslt

def get_case_types(guildId, channelId):
    return list(sygnatures[guildId][channelId]['ids'].keys())

async def db_test(ctx):
    ind = supabase.table('bot_server_channels').select("server_id").eq('server_id', ctx.message.guild.id).eq('channel_id',12).execute()
    print(list(ind))
    print(f"source server: {ctx.message.guild.id}")
    error, results = supabase.table("bot_server_channels").select("*").execute()
    print(results)
    