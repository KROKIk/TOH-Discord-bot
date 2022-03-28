# bot.py
import os
import feedparser
import transmissionrpc
from discord.ext import tasks
import discord
from discord.ext.commands import Bot

TOKEN = 'bot token'
mute = False
client = Bot("%", allowed_mentions = discord.AllowedMentions(everyone = True))

@tasks.loop(minutes=1.0, count=None)
async def check():
    rrs = "http://rarbg.to/rssdd.php?categories=41"
    feed = feedparser.parse(rrs, request_headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"})
    tc = transmissionrpc.Client("192.168.1.10", port=9091)
    print(feed)
    out = False
    for post in feed['entries']:
        if "The.Owl.House" in post['title'] and "1080p" in post['title']:
            tc.add_torrent(post['link'], download_dir='/mnt/torrents/Owl House/')
            out = True
        
    c = client.get_channel(954746915684253757)
    if not out:
        pass
    else:
        spam.start()

@client.command()
async def mute(ctx):
    global mute
    mute = True
    await asyncio.sleep(86400)
    mute = False


@client.event
async def on_ready():
    check.start()

@tasks.loop(hours=1.0, count=None)
async def spam():
    global mute
    if not mute:
        c = client.get_channel(954746915684253757)
        await c.send('@toh New Episode is out!')

client.run(TOKEN)

