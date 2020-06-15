import discord
from discord.ext import commands
from scrapers import define_word, scrape_wotd
from utils.messages import error_message, define_message
from expiringdict import ExpiringDict


class Commands(commands.Cog):
    def __init__(self, client):
        self.client = client
        # 3600 seconds (1 hour)
        self.cache = ExpiringDict(max_len=100, max_age_seconds=3600)

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

        # Store
        word = ''
        result = 0

        # Parse word and result to return
        for arg in args:
            if arg.isnumeric():
                result = int(arg)
            else:
                word += f" {arg}"

        # check if the word is cached
        word_definition = self.cache.get(f"{word}-{result}")

        if not word_definition:
            # scrape Word
            word_definition = define_word(word, result)

            # cache word
            self.cache[f"{word}-{result}"] = word_definition

        if "error" in word_definition:
            embed = error_message(word_definition["error"])
            return await ctx.send(embed=embed)
        else:
            embed = define_message(word_definition)
            return await ctx.send(embed=embed)

    @commands.command()
    async def wotd(self, ctx):
        # Check if wotd is cached
        wotd = self.cache.get('wotd')

        if not wotd:
            # scrape current wotd
            wotd = scrape_wotd()

            # cache wotd
            self.cache["wotd"] = wotd

        # Return wotd
        embed = define_message(wotd)
        return await ctx.send(embed=embed)

    # @commands.command()
    # async def trending(self, ctx):


def setup(client):
    client.add_cog(Commands(client))
