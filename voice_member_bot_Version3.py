import discord
from discord.ext import commands

TOKEN = "ضع توكن البوت هنا"

# قائمة التوكنات أو معرفات الأعضاء المسموح لهم (يمكنك استخدام قاعدة بيانات)
allowed_members = {
    "user_token_1": 123456789012345678,  # ID العضو
    "user_token_2": 234567890123456789
}

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_voice_state_update(member, before, after):
    # تحقق إذا العضو دخل روم فويس
    if after.channel is not None:
        for token, user_id in allowed_members.items():
            if member.id == user_id:
                # يمكنك هنا إعطاء العضو دور خاص أو رسالة تأكيد
                role = discord.utils.get(member.guild.roles, name="Voice Perm")
                if role and role not in member.roles:
                    await member.add_roles(role)
                    await member.send("تم تثبيتك في الفويس للأبد ✅")
                break

# أمر لإضافة عضو جديد للتثبيت (للمشرف فقط)
@bot.command()
@commands.has_permissions(administrator=True)
async def add_voice_member(ctx, user: discord.Member, token: str):
    allowed_members[token] = user.id
    await ctx.send(f"تمت إضافة {user.mention} إلى قائمة التثبيت بالفويس.")

bot.run(TOKEN)