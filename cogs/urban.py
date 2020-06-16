import discord
from discord.ext import commands
from scrapers import scrape_word, scrape_wotd, scrape_trending_words, scrape_random_word
from utils.messages import help_message, error_message, define_message, trending_message
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
        embed = help_message()
        await ctx.send(embed=embed)

    @commands.command()
    async def define(self, ctx, word='', result=0):
        if not word:
            # Parse message arguments if word not provided
            args = ctx.message.content.split(' ')[1:]

            # Invalid argument length
            if len(args) == 0:
                return await ctx.send("Define accepts two arguments `!string {word}` and `?int {result}`")

            # Invalid argument order
            if args[0].isnumeric():
                return await ctx.send("Define requires at least one argument `{word}`")

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
            word_definition = scrape_word(word, result)

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

    @commands.command()
    async def trending(self, ctx):
        # Parse args
        args = ctx.message.content.split(' ')[1:]

        # Check if trending data is cached
        trending = self.cache.get("trending-cmd")

        if not trending:
            # Scrape trending words
            trending = scrape_trending_words()

            # Cache trending words
            self.cache["trending-cmd"] = trending

        if len(args) != 0 and args[0].isnumeric():
            num = int(args[0])

            if num > len(trending):
                return await ctx.send(f"Please choose a number between 1 and {len(trending)}")

            word = trending[num-1]["word"]

            await self.define(ctx, word)
        else:
            embed = trending_message(trending)
            await ctx.send(embed=embed)

    @commands.command()
    async def random(self, ctx):
        word_definition = scrape_random_word()

        embed = define_message(word_definition)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Commands(client))
