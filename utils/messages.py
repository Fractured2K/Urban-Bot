import sys
from discord import Embed


def error_message(error):
    return Embed(title=error, color=0xf55353)


def define_message(word):
    embed = Embed(title=word["word"],
                  description=word["word_definition"], color=0x0b4ee7)

    return embed


def trending_message(trending_words):
    embed = Embed(title="Trending Words", description="A list of today's currently trending words.", color=0x0b4ee7,
                  url="https://www.urbandictionary.com/")

    for word_dict in trending_words:
        word = word_dict["word"]
        num = word_dict["num"]

        embed.add_field(name="\u200b", value=f"{num}. {word}", inline=True)

    embed.set_footer(
        text="Type .help for to view all possible commands")

    return embed
