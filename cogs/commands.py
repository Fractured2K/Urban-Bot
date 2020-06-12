import discord
from discord.ext import commands
import scrape_word
from utils.messages import error_message, define_message


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        """
        Returns an embed of possible commands and their descriptions.
        :param ctx:
        :return:
        """
        embed = discord.Embed(
            title="Help", description="`!` denotes an argument is required. `?` denotes an arugment is optional. Following `!` or `?` is the expected data type of the argument. i.e `!string {word}` -> Means the argument `word` is `required` and accepts a `string (letters)`", color=0x0b4ee7)
        embed.add_field(name="help", value="This command", inline=False)
        embed.add_field(
            name="define", value="Accepts two arguments `!string {word}` and `?int {result}`. e.g `.define stupendous`", inline=False)
        embed.add_field(
            name="wotd", value="Returns the word of the day and its definition", inline=False)

        await ctx.send(embed=embed)

    @commands.command()
    async def define(self, ctx):
        args = ctx.message.content.split(' ')[1:]

        # Invalid argument length
        if len(args) == 0:
            return await ctx.send("Define accepts two arguments `!string {word}` and `?int {result}`")

        # Invalid argument order
        if args[0].isnumeric():
            return await ctx.send("Define requires at least one argument `{word}`")

        # Word to define
        word = ''
        # Result to return
        result_num = 0

        for arg in args:
            # Check if arg is word or result_num
            if arg.isnumeric():
                result_num = int(arg)
            else:
                word += f" {arg}"

        # Scrape Word
        word = scrape_word(word, result_num)

        if "error" in word:
            embed = error_message(word["error"])
            return await ctx.send(embed=embed)
        else:
            embed = define_message(word)
            return await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Commands(client))
