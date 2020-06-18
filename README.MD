# **Urban Bot** 🤖

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/fractured2k/bjorn-bot/#contributing-)[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)

Urban bot, is a simple to use and robust dscord bot that allows you to easily use Urban Dictionary through discord!

# Getting Started 👋

-   [Commands](#commands-%EF%B8%8F)
-   [Configure a Development Environment](#dev-)
-   [Deploy Urban Bot](#deploying-bjorn-)

# Commands ✍

Commands that accept arguments are prefixed with a data type and occasionally with a `?`, denoting that argument is optional. e.g `string {word}` Means the argument `word` is `required` and accepts a `string (letters)`. `?int result` Means the argument `result` is optional and expects a `int (whole number)`.

-   📖 **help** - Returns a succinct list of possible commands
-   📙 **define** - Accepts two arguments `string {word}` and `?int {result}`. e.g `.define stupendous 2`. Returning the word and it's definition.
-   📅 **wotd** - Returns the word of the day and its definition.
-   💹 **trending** - Returns a list of today's currently trending words. If a number is passed, the word and definition correlated with the respective number will be returned.
-   🎲 **random** - Returns a random word and definition.

# Configure a Dev Environment 💻

Want to contribute to Urban Bot or add some features of your own? Here's how to get started!

## Prerequisites

-   [Python](https://www.python.org/downloads/) version `3.8` or greater installed.
-   [Pipenv](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv) installed.

## Steps

1. [Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) or [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this Repo.

2. Open your terminal and cd into this repo.

3. Once inside, type `pipenv shell` in your terminal to create an environment to work in.

4. Next, in type `pipenv install --dev` to install all dev and required dependencies.

5. Lastly, open the Urban-bot in your favorite code editor and start coding! _I prefer [Visual Studio Code](https://code.visualstudio.com/)._

# Deploying Urban Bot 🚀
