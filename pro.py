from inspect import cleandoc
import discord, asyncio, datetime, pytz
from discord import member
from discord import message
import random
import dice
import time
import openpyxl
import os
import sys
import json
import re


client = discord.Client()

@client.event
async def on_ready():
    print("아리아나 그란데")
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("아리아나 그란데 덕질"))
    
    
@client.event
async def on_message(message):

       

    if message.content == "ㅇ랜덤":
               await message.channel.send("1부터 10까지 아무 숫자나 부른다")
              
               await message.channel.send(random.randint(1,10))

    
        
    if message.content.startswith("ㅇ김민균") or message.content.startswith("해냥아 야짤"):
           await message.channel.send("https://i.imgur.com/Ns6xflV.png")


    if message.content.startswith("ㅇ아리") or message.content.startswith("해냥아 야짤"):
           await message.channel.send("http://img.yna.co.kr/etc/inner/KR/2020/10/30/AKR20201030110400005_01_i_P4.jpg")

    if message.content.startswith('ㅇ장서우'):
          msg = await message.channel.send('ㅈㄴ 못생기고 돈 안갚는년')
          await asyncio.sleep(2.3)
          await msg.edit(content = 'ㅋ 미안')
        
    if message.content.startswith('ㅇ양희찬'):
          msg = await message.channel.send('나보다 키 많이 작음')
          await asyncio.sleep(2.3)
          await msg.edit(content = '코딩 엄청 잘 알려주는 천재')

       

    if message.content == "ㅇAri못생":
                   await message.channel.send ("경찰서로 와 Dm왔다.")
                   await message.author.send ("{} | {}, 너 내가 오늘안에 지옥으로 보내준다 ".format(message.author, message.author.mention))

    if message.content.startswith("ㅇ아나"):
         await message.channel.send("https://variancemagazine.com/images/ariana-59903.jpg")
    
    if message.content.startswith("ㅇ그란데"):
        await message.channel.send("https://www.udiscovermusic.com/wp-content/uploads/2019/08/Ariana-Grande-My-Everything-album-cover-820.jpg")

  
    if message.content.startswith ("ㅇ청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0xAAFFFF)
            embed.set_footer(text="Bot Made by. Grande #7578", icon_url="http://img.yna.co.kr/etc/inner/KR/2020/10/30/AKR20201030110400005_01_i_P4.jpg")
            await message.channel.send(embed=embed)
        
    
            

    if message.content == ('ㅇ내정보'):
         user = message.author 
         date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
         await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
         await message.channel.send(f"{message.author.mention}의 이름/아이디/닉네임: {user.name}/{user.id}/{user.display_name}")

    if message.content == "ㅇ도움말": # 메세지 감지
          embed = discord.Embed(title="도움말", description="조용규 따깔봇 도움말",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

          embed.add_field(name="조용규 따깔 기본 도움말", value="ㅇ랜덤 \n ㅇ내정보 \n ㅇ청소", inline=False)
          embed.add_field(name="조용규 따깔 재밌는거", value="ㅇ장서우 \n ㅇ양희찬 \n ㅇ아리 \n ㅇ아나 \nㅇ그란데 \n ㅇAri못생 \n ㅇ김민균  ", inline=False)
          await message.channel.send (embed=embed)
        

    if message.content.startswith("ㅇ디오"):
        await message.channel.send("https://spnimage.edaily.co.kr/images/Photo/files/NP/S/2019/05/PS19053000047.jpg")
    
    

client.run('ODU2MTc1MDI1MzMyODEzODI0.YM9NIQ.r6XWEJGmq91xqUckNEJ4_Lk3kDI')