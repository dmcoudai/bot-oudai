import discord
from discord.ext import commands

TOKEN = "MTM3MzcyMTk1MTQxMDk4Mjk2Mg.G2CFOH.1t0NN8XKchA_g7_U8sxXNp_Lc4MClZwUzNHq4c"

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

allowed_members = set()

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def add_voice_member(ctx, user: discord.Member):
    allowed_members.add(user.id)
    await ctx.send(f"تم تثبيت العضو {user.mention} في الفويس للأبد.")

@bot.event
async def on_voice_state_update(member, before, after):
    if after.channel and member.id in allowed_members:
        role = discord.utils.get(member.guild.roles, name="Voice Perm")
        if role and role not in member.roles:
            await member.add_roles(role)
            await member.send("تم تثبيتك في الفويس للأبد ✅")

bot.run(TOKEN)