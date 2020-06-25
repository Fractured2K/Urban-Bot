import sys
import os
from discord import Embed


def help_message():
    embed = Embed(
        title="Help", description="Commands that accept arguments are prefixed with a data type and occasionally with a `?`, denoting that argument is optional. e.g `string {word}` -> Means the argument `word` is `required` and accepts a `string (letters)`. `?int {result}` -> Means the argument `int` is optional and accepts a `int (whole number)`.", color=0x0b4ee7)
    embed.add_field(name="help", value="This command", inline=False)
    embed.add_field(
        name="define", value="Accepts two arguments `string {word}` and `?int {result}`. e.g `.define stupendous`.", inline=False)
    embed.add_field(
        name="wotd", value="Returns the word of the day and its definition.", inline=False)
    embed.add_field(
        name="trending", value="Returns a list of today's currently trending words. If a number is passed, the word correlated with that number will be defined. e.g `.trending 2`.")
    embed.add_field(
        name="random", value="Returns a random word and definition.")

    return embed


def error_message(error):
    return Embed(title=error, color=0xf55353)


def define_message(definition_block):
    # Word, Description, Word URL, Embed Color
    embed = Embed(title=definition_block["word"],
                  description=definition_block["word_definition"], url=definition_block["url"], color=0x0b4ee7)

    # Embed Thumbnail
    fallback_avatar = "https://cdn.discordapp.com/app-icons/720363121386193009/a686399461394ed4912e78175d962ebc.png"
    embed.set_thumbnail(url=(os.getenv("AVATAR_URL") or fallback_avatar))

    # Add field for each example
    for num, example in enumerate(definition_block["word_examples"]):
        embed.add_field(name=f"Example #{num+1}", value=example, inline=False)

    # Word ratings
    ratings = definition_block["ratings"]
    like_emoji = "<:thumbsup:725685268413415484>"
    dislike_emoji = "<:thumbsdown:725686415240986714>"
    embed.add_field(name="Likes/Dislikes",
                    value=f"{like_emoji} {ratings[0]} {dislike_emoji} {ratings[1]}")

    # Word contributor (Author)
    embed.set_footer(text=definition_block["contributor"])
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
