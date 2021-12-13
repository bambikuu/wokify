import discord
import os, random, string, requests
from discord.ext import commands
# handler
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command('help')
admins = [499218322261540865]



# API
# API 
#API 
#API 
#API
def genmembers(invite):
    print(f'[+] Sending Members to {invite}')
    posturl = f"https://discord.com/api/v9/invites/" + invite

      



    token = str(random.choice(list(open('discord/tokens.txt'))))
    new_token = token.replace("\n", "")
    headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'de',
            'authorization': new_token,
            'content-length': '0',
            'cookie': '__dcfduid=4a00f9addca4d395b22b67199e2ef4b8; __stripe_mid=4e5a0e6d-5f5f-47ab-a1ec-881aaf62bbd739869f; __sdcfduid=fbb6d08bf3ff11eba23e42010a0a043edc527da86b038911a90acb27a44d9a676443bca690cff7eb1fd888d6c065b7e3',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '''"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"''',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjMyNTAxNzA5ODU5MjA1OTM5MiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI2Njc0NzQ2MjYzMzAyMzA3ODQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAuNDM4OS4xMjgiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODI1OTAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
        }
    proxy = set()
    with open("proxies/proxies.txt", "r") as f:
      file_lines1 = f.readlines()
      for line1 in file_lines1:
          proxy.add(line1.strip())
        
    proxies = {
    'http': 'http://'+line1
    }
    r = requests.post(posturl, headers=headers, proxies=proxies)
    print(r.text)



def genfriends(userid):

    x1, x2 = userid.split("#")
    new_username = x1
    new_usertag = x2

    if new_usertag < '1000':
        print('lower then 1k')
        usertag = new_usertag.replace("0", "")
    else:
        usertag = new_usertag
    posturl = f"https://discord.com/api/v9/users/@me/relationships"

    with open("discord/tokens.txt", "r") as f:
      lines = f.read()
      new_token = lines.split('\n', 1)[0]



    token = new_token.strip()
    headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'de',
            'authorization': token,
            'content-length': '0',
            'cookie': '__dcfduid=4a00f9addca4d395b22b67199e2ef4b8; __stripe_mid=4e5a0e6d-5f5f-47ab-a1ec-881aaf62bbd739869f; __sdcfduid=fbb6d08bf3ff11eba23e42010a0a043edc527da86b038911a90acb27a44d9a676443bca690cff7eb1fd888d6c065b7e3',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '''"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"''',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjMyNTAxNzA5ODU5MjA1OTM5MiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI2Njc0NzQ2MjYzMzAyMzA3ODQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAuNDM4OS4xMjgiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODI1OTAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
        }
    proxy = set()
    with open("proxies/proxies.txt", "r") as f:
      file_lines1 = f.readlines()
      for line1 in file_lines1:
          proxy.add(line1.strip())
        
    proxies = {
    'http': 'http://'+line1
    }
    payload = {"username":f"{new_username}","discriminator":usertag}
    r = requests.post(posturl, headers=headers, json=payload, proxies=proxies)
    print(r.text)
    fn = "discord/tokens.txt"
    f = open(fn)
    output = []
    str=new_token
    for line in f:
        if not line.startswith(str):
          output.append(line)
    f.close()
    f = open(fn, 'w')
    f.writelines(output)
    f.close()
    file7 = open("discord/used.txt", "a")
    file7.write(f'\n{new_token}')
    file7.close()


























# BOT 
# BOT
# BOT

botchannel = 916711850706599976
chatchannel = 916711027872256012
@bot.event
async def on_command_error(ctx, error: Exception):
    if ctx.channel.id == botchannel:
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(color=0xff0000, description=f'{ctx.author.mention} {error}')
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=0xff0000, description='You are missing arguments required to run this command!')
            await ctx.send(embed=embed)
            ctx.command.reset_cooldown(ctx)
        elif 'You do not own this bot.' in str(error):
            embed = discord.Embed(color=0xff0000, description='You do not have permission to run this command!')
            await ctx.send(embed=embed)
        else:
            print(str(error))
    else:
        try:
            await ctx.message.delete()
        except:
            pass


@bot.event
async def on_ready():
  print("Bot Online")
# start






@bot.command()
async def help(ctx):
    if ctx.channel.type != discord.ChannelType.private:
        if ctx.channel.id == botchannel or chatchannel:
            embed=discord.Embed(description=f"!join (server invite)\n!friend (someone#0000)\n!stock", color=0x696969)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/840873001335128095/916741622924984421/Untitled83_20211127003721.png")
            embed.set_author(name=" | Commmands", icon_url="https://cdn.discordapp.com/attachments/840873001335128095/916741622924984421/Untitled83_20211127003721.pngsize=1280")
            embed.set_footer(text="Wokify 2021")
            #Thread(target=main).start()
            #time.sleep(9)
            await ctx.channel.send(embed=embed)


@bot.command()
@commands.cooldown(1, 120, type=commands.BucketType.user)
async def friend(ctx, userid):
    if ctx.channel.type != discord.ChannelType.private:
        if ctx.channel.id == botchannel:
            if '#' in userid:
                embed=discord.Embed(description=f"[Success] Sending Friends to `{userid}`", color=0x696969)
                embed.set_author(name=" | Sending", icon_url="https://cdn.discordapp.com/attachments/840873001335128095/916741622924984421/Untitled83_20211127003721.png")
                await ctx.channel.send(embed=embed)
                for _ in range (2):
                    genfriends(userid)
            if '#' not in userid:
                embed=discord.Embed(description=f"[ERROR] Specify the user name for ex: BambiKu#3311 not the userid", color=0x696969)
                await ctx.channel.send(embed=embed)



@bot.command()
@commands.cooldown(1, 120, type=commands.BucketType.user)
async def join(ctx, invite):
    if ctx.channel.type != discord.ChannelType.private:
        if ctx.channel.id == botchannel:
            if 'https://discord.gg/' in invite:
                print('you have an invite link [1]')
                newinvite = invite.replace("https://discord.gg/", "")
                await ctx.message.delete()
                print(newinvite)    
                
            if 'https://discord.gg/' not in invite:
                newinvite = invite
                print(newinvite)
            embed=discord.Embed(description=f"[Success] Sending Sussy Members to `{newinvite}`", color=0x696969)
            embed.set_author(name=" | Sending", icon_url="https://cdn.discordapp.com/attachments/840873001335128095/916741622924984421/Untitled83_20211127003721.png")
            await ctx.channel.send(embed=embed)

            for _ in range(100000):
                genmembers(newinvite)



getkey_cooldown = []
botchannel = 916711850706599976
@bot.command()
@commands.cooldown(1, 3000, type=commands.BucketType.user)
async def getkey(ctx):
    if ctx.channel.type != discord.ChannelType.private:
      if ctx.channel.id == botchannel:
        embed=discord.Embed(description=f"Generating Your Key! | `Make Sure Your DMS are on`", color=0x696969)
        embed.set_author(name=" | Generating", icon_url="https://cdn.discordapp.com/attachments/840873001335128095/916741622924984421/Untitled83_20211127003721.png")
        #Thread(target=main).start()
        #time.sleep(9)
        await ctx.channel.send(embed=embed)
        letters = string.ascii_letters
        new_genkey = str( ''.join(random.choice(letters) for i in range(10)) )
        await ctx.author.send(f'Your Key is: {new_genkey}')
        await ctx.author.send(f'WARNING: THE  WEBSITE IS NOT DONE YET! ')
        requests.get(f'https://www.maticbot.pl/api/genkey/{new_genkey}')
      else:
        await ctx.channel.send('Wrong channel! use proper channels!')






@bot.command()
async def stock(ctx):
    if ctx.channel.type != discord.ChannelType.private:
      r = requests.get('https://www.maticbot.pl/api/tokens/stock')
      embed=discord.Embed(description=f"Tokens In Stock: undefined", color=0x49a0fc)
      await ctx.channel.send(embed=embed)

@bot.command()
@commands.has_role("Silver")
async def silver(ctx, invite):
  if ctx.channel.type != discord.ChannelType.private:
    if 'https://discord.gg/' in invite:
      #print ('you have an invite link [1]')
      newinvite = invite.replace("https://discord.gg/","")
      await ctx.message.delete()
      print(newinvite)

      if 'https://discord.gg/' not in invite:
        newinvite = invite
        print(newinvite)
        embed=discord.Embed(description=f"[Success] Sending 4 Joins to `{newinvite}`", color=0x696969)
        await ctx.channel.send(embed=embed)

        for _ in range(5):
          genmembers(newinvite)





token = os.environ.get("token")
bot.run("")
