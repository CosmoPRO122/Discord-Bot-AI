import discord
import random, os
from discord.ext import commands
from model import predict_image

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)
predict_image()

@bot.event
async def on_ready():
    print(f'Bot {bot.user} kullanıma hazır!, Komutlarınızı yazmak için en başa / sembolünü kullanın!')

@bot.command()
async def komut_listesi(ctx):

    with open("cevretxt/{komut_listesi.txt}", "r", encoding="utf-8") as f:
        content = f.read()
    await ctx.send(content)

@bot.command()
async def cevre_kirliligi_nedir(ctx):
    with open("cevretxt/{cevre.txt}", "r", encoding="utf-8") as f:
        content = f.read()
    await ctx.send(content)

@bot.command()
async def cevreyi_kirliligi_ile_alakli_oyun(ctx):
    with open("cevretxt/{temiz.txt}", "r", encoding="utf-8") as f:
        content = f.read()
    await ctx.send(content)

@bot.command()
async def cevre_kirliligi_fotograflari(ctx):
    kirlicevre_foto = random.choice(os.listdir('kirlicevre'))
    with open(f'kirlicevre/{kirlicevre_foto}', 'rb') as cevrefoto:
    #Bu satır, f değişkenindeki verileri bir Discord File nesnesi olarak oluşturur.
        resim = discord.File(cevrefoto)
    await ctx.send(file=resim)

# Dekaratör => FLASK, DISCORD Kullanıldı. Fonksiyon davranışlarını değiştiren komut parçasıdır. 
@bot.command()
async def foto_kontrol(ctx):
    # Eğer kullanının gönderdiği mesajda bir ek listesi varsa:
    if ctx.message.attachments:
        # Listedeki her bir elemanı kontrol edecek bir döngü oluştur.
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./userPhoto/{file_name}")
            await ctx.send(f"Gönderdiğiniz fotoğraf {file_name} ismiyle kayıt edildi.")
            await ctx.send(f"Gönderdiğiniz fotoğrafı  {file_url} linkine tıklayarak gözlemleyebilirsiniz.")
            await ctx.send(predict_image(image_path=f"./userPhoto/{file_name}"))
    
    else:
        await ctx.send("Fotoğraf göndermediğinizi tespit ettik. Lütfen fotoğraf gönderin.")

bot.run("Token")
    