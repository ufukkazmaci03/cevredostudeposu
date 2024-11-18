import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content.startswith('$merhaba'):
        await message.channel.send("Merhaba ben çevre kirliliği hakkında bilgi veren bir botum. Ne tür bilgi vermemi istersin? ")
    
    if message.content.startswith("Çevre kirliliği ne demek?"):
        await message.chennel.send("Çevre kirliliği, çevrenin doğal olmayan bir şekilde insan eliyle doğallığının bozulmasıdır. Bu ekosistemi bozma eylemleri; kirlenme şeklinde tabir edilmektedir.")
    
    if message.content.startswith("Peki insan eli deymeyen doğal afetler çevre kirliliğine neden olur mu?"):
        await message.chennel.send("Hayır tabiki!! Doğal afetler insan eli deymeyen olaylardır. Bu yüzden çevre kirliliğine neden olmaz.")
    
    if message.content.startswith("Çevre kirliliği nasıl önlenebilir?"):
        await message.channel.send("1.Evimizde ve bahçemizde ozon tabakasına zarar veren kimyasal maddeler kullanmamalıyız. -- 2.Evlerimizde ısı yalıtımı yaptırmalı, güneş enerjisi veya doğalgaz enerjisini tercih etmeliyiz. -- 3.Alışverişlerde gereksiz yere plastik poşet kullanmamaya dikkat etmeli ve elimizdeki plastik poşetleri yeniden kullanmalıyız. Bu şekilde çevrekirliliğini önlenebilir. ")

    if message.content.startswith("Çevre kirliliğinin önüne geçmezsek ne olur?"):
        with open("cevrekirliligi.png", "rb") as f:
            resim = discord.File(f)
        await message.channel.send(file=resim)

    if message.content.startswith("Çevre kirliliği ile alakalı bir video gönderirmisin?"):
        await message.channel.send("https://www.youtube.com/watch?v=hir6AW1RNq4")



client.run("GİZLİ TOKEN")