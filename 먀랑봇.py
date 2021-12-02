import discord, asyncio, datetime, pytz
import random
from discord.utils import get
from discord import message

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("봇의 상태매세지"))


client = discord.Client()


@client.event
async def on_message(message):
    if message.content == "%먀랑아": # 메세지 감지
        ran = random.randint(0,5) #랜덤 갯수
        if ran == 0: #랜덤 뽑기에 0이 걸리면 응답할 메시지
            b = "반갑다냥~"
        if ran == 1: #랜덤 뽑기에 1이 걸리면 응답할 메시지
            b = "안녕하세요냥~"
        if ran == 2: #랜덤 뽑기에 2이 걸리면 응답할 메시지
            b = "인사하기 바쁘다 냥!!"
        if ran == 3: #랜덤 뽑기에 3이 걸리면 응답할 메시지
            b = "참 귀찮게 구는 인간이다냥..."
        if ran == 4: #랜덤 뽑기에 4이 걸리면 응답할 메시지
            b = "냥냥~~"
        if ran == 5: #랜덤 뽑기에 5이 걸리면 응답할 메시지
            b = "친구하자 냥!"
        await message.channel.send ("{} | {} 님!".format(message.author, message.author.mention))
        await message.channel.send(b)

    if message.content == "야": # 메세지 감지
        await message.channel.send ("호~~")

    if message.content == "%특정입력":
        ch = client.get_channel(896411271895875635)
        await ch.send ("{} | {}, User, Hello 테스트".format(message.author, message.author.mention))


    if message.content == "%자기소개": # 메세지 감지
        embed = discord.Embed(title="먀랑봇", description="만능 고양이 봇",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xb8ceff)

        embed.add_field(name="버전", value="알파 0.0.1", inline=False)
        embed.add_field(name="디스코드 공식 서버", value="https://aztra.xyz/invite/WIRh3OZw", inline=False)

        embed.add_field(name="좋아하는 것", value="사람들 응대하기", inline=True)
        embed.add_field(name="싫어하는 것", value="코딩", inline=True)

        embed.set_footer(text="Bot Made by. 먀랑이 #2502")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/899284983892549643/899289023812616192/-001.png")
        await message.channel.send (embed=embed)


# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODk4OTY1MTYyMzY1NzE0NDcy.YWr4jA.sUd1Q_UBSxvH5EBCySmtbwFhqY8')