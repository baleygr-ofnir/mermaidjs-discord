import discord
from discord.ext import commands
import os
import base64
import sys

ALLOWED_CHANNEL_ID = os.environ.get('ALLOWED_CHANNEL_ID', '').strip()
if not ALLOWED_CHANNEL_ID.isdigit():
  sys.exit('ALLOWED_CHANNEL_ID must be set to the ID of the channel the bot writes in')
ALLOWED_CHANNEL_ID = int(ALLOWED_CHANNEL_ID)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=commands.when_mentioned_or(("!mermaid-")), intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
  print('Logged on as', client.user.name)

def allowedChannel():
  return client.get_partial_messageable(ALLOWED_CHANNEL_ID)

# Every answer goes to the allowed channel, also for commands sent from another
# channel, another server or a DM.
async def respond(ctx, content=None, embed=None):
  if ctx.channel.id == ALLOWED_CHANNEL_ID and content is not None:
    await ctx.message.reply(content, embed=embed)
  else:
    await allowedChannel().send(content, embed=embed)

# Diagrams always use Mermaid's dark theme on a dark background, as a PNG.
DARK_IMAGE_OPTIONS = '?theme=dark&bgColor=1b1b1f&type=png'

def diagramUrl(code):
  return 'https://mermaid.ink/img/' + base64.urlsafe_b64encode(code.encode('ascii')).decode('ascii') + DARK_IMAGE_OPTIONS

def helpEmbed():
  embed = discord.Embed(description="Help on using the Mermaid.js Discord Bot.", color=4372867)
  embed.set_author(name="Help")
  embed.add_field(name="Helpful Links", value="[GitHub](https://github.com/Yash-Singh1/mermaidjs-discord) | [Issue Tracker](https://github.com/Yash-Singh1/mermaidjs-discord/issues) | [Mermaid.js Documentation](https://mermaid-js.github.io/)", inline=False)
  embed.add_field(name="Commands", value="__!mermaid-help__: Displays the current message.\n\
__!mermaid-r__ or __!mermaid-render__: Renders the diagram with the code following the command. Allows Mermaid.js diagram syntax.\n\
__!mermaid-invite__: Gets the invite link of the bot.\n\
__!mermaid-support__: Gets a link to a support issue tracker for the bot.\n\
__!mermaid-setStatus__: Sets the current status of the bot. One of `dnd` or `do_not_disturb`, `online`, `idle`, `offline`, or `invisible`.", inline=False)
  embed.add_field(name="Example Diagram", value="""
```markdown
!mermaid-render
graph TD
  A[Christmas] -->|Get money| B(Go shopping)
  B --> C{Let me think}
  C -->|One| D[Laptop]
  C -->|Two| E[iPhone]
  C -->|Three| F[fa:fa-car Car]
```
""")
  embed.set_image(url="https://mermaid.ink/img/pako:eNpVkMtqw0AMRX9FaNVA_ANeFBI7zSbQQrLzeCE8SmZI54E8JgTb_95x00KileCcexEasQuascSLUDRwqpWHPJumMmL75KhvoSjepz0ncMHzfYLt2z5Ab0KM1l9WD3-7SFCNh0VjSMb66_xA1W_-0_MEdXOgmEJsn8npFibYNfbL5PpXYoRz6qM5U3mmoiOBiqTFNToWR1bns8cloDAZdqywzKsmuSpUfs7eEDUl3mmbgmDu-O55jTSkcLz7DsskA_9LtaX8AvdnzT9s-1qQ" + DARK_IMAGE_OPTIONS)
  return embed

@client.event
async def on_guild_join(guild):
  await allowedChannel().send(embed=helpEmbed())

@client.command()
async def help(ctx):
  await respond(ctx, embed=helpEmbed())

@client.command(aliases=['r'])
async def render(ctx, *, arg):
  await respond(ctx, embed=discord.Embed().set_image(url=diagramUrl(arg)))

@client.command()
async def invite(ctx):
  await respond(ctx, embed=discord.Embed(description="The invite link is https://discord.com/api/oauth2/authorize?client_id=935684419837132910&permissions=274877910016&scope=bot", color=4372867))

@client.command()
async def support(ctx):
  await respond(ctx, embed=discord.Embed(description="The link to the issue tracker is https://github.com/Yash-Singh1/mermaidjs-discord/issues", color=4372867))

@client.command()
async def setStatus(ctx,arg='Online'):
  try:
    newStatus = discord.Status[arg]
  except:
    await respond(ctx, "There was an error parsing the status")
  else:
    await client.change_presence(status=newStatus)

client.run(os.environ['TOKEN'])
