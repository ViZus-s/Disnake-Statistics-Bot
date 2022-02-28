# imports
import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands
from main import glcolor
from parsers.gitthub import parsing_git
from parsers.pypi import parsing_pypi

class slashs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(
        name="stats",
        description="Wanna check statistic? Use this command!",
        guild_ids=[808030843078836254])
    async def stats(self, inter: ApplicationCommandInteraction, option: str = commands.Param(choices=['pypi', 'github'])):
        if option == 'github':
            Member = inter.author
            get_data = parsing_git()
            
            stars = get_data["stars"]
            forks = get_data["forks"]
            issues = get_data["issues"]
            pull = get_data["pull requests"]
            lastcom = get_data["last commit"]
            
            embed1 = disnake.Embed(title="GitHub Statistics [TEST]",
                            description=f":star: **stars**: `{stars}`\n\n:cd: **forks**: `{forks}`\n\n:bangbang: **issues**: `{issues}`\n\n:satellite: **pull requests**: `{pull}`\n\n:hourglass: **last commit**: `{lastcom}`",
                            color=glcolor)
            
            embed1.set_author(name=inter.author.name, icon_url=Member.avatar.url)
            await inter.send(embed=embed1)
            
        elif option == 'pypi':
            Member = inter.author
            get_data = parsing_pypi()
            embed2 = disnake.Embed(
                title="PyPi Disnake Statistics",
                description=f":bulb: **Latest Version**: {get_data[0]}\n\n:bar_chart: **Version Status**: {get_data[1][3:]}",
                color=glcolor)
            embed2.set_author(name=inter.author.name, icon_url=Member.avatar.url)
            await inter.send(embed=embed2)

    @commands.slash_command(
        name="help",
        description="Shows bot commands",
        guild_ids=[808030843078836254])
    async def help(self, inter: ApplicationCommandInteraction):

        embed2 = disnake.Embed(
        title=":book: | Help",
        description="`/stats` - shows any statistics[github/pypi]\n`/info` - shows bot info",
        color=glcolor)
        await inter.send(embed=embed2, ephemeral=True)

    @commands.slash_command(
        name="info",
        description="Shows the bot info",
        guild_ids=[808030843078836254])
    async def info(self, inter: ApplicationCommandInteraction):
        Member = inter.author

        embed = disnake.Embed(
            title="Bot information",
            description=f"<:disnake:922937443039186975> **Disnake version**: `{disnake.__version__}`\n:gear: **Bot version**: `???`\n:timer: **Ping**: `{round(self.bot.latency * 1000)} ms`",
            color=glcolor)
            
        embed.set_author(name=inter.author.name, icon_url=Member.avatar.url)
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(slashs(bot))