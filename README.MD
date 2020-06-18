# **Urban Bot** 🤖

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/fractured2k/bjorn-bot/#contributing-)[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)

Urban bot, is a simple to use and robust dscord bot that allows you to easily define words. Utilizing Web Scraping and Urban Dictionary.

# Getting Started 👋

Below you'll find some help quick links to help get started!

-   [Commands](#commands-✍)
-   [Configure a Development Environment](#configure-a-dev-environment-💻)
-   [Deploy Urban Bot](#deploy-urban-bot-🚀)
-   [Contributing](#contributing-✨)

# Commands ✍

Commands that accept arguments are prefixed with a data type and occasionally with a `?`, denoting that argument is optional. e.g `string {word}` Means the argument `word` is `required` and accepts a `string (letters)`. `?int result` Means the argument `result` is optional and expects a `int (whole number)`.

-   📖 **help** - Returns a succinct list of possible commands
-   📙 **define** - Accepts two arguments `string {word}` and `?int {result}`. e.g `.define stupendous 2`. Returning the word and it's definition.
-   📅 **wotd** - Returns the word of the day and its definition.
-   💹 **trending** - Returns a list of today's currently trending words. If a number is passed, the word and definition correlated with the respective number will be returned.
-   🎲 **random** - Returns a random word and definition.

#### [back to top](#urban-bot-🤖)

# Configure a Dev Environment 💻

Want to tinker around or add some features to Urban Bot? Here's how to get started!

## Prerequisites

-   [Python](https://www.python.org/downloads/) version `3.8` or greater installed.
-   [Pipenv](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv) installed.

## Steps

1. [Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) or [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this Repo.

2. Open your terminal and cd into this repo.

3. Next, type `pipenv shell` in your terminal to create an environment to work in.

4. Once you're environement is created, type `pipenv install --dev` to install all dev and required dependencies.

5. Now that we have a environment and our dependencies are installed, we need to register our application with discord! Let's head over to [Discord's Developer Portal](https://discord.com/developers/applications) and create a bot user. Here's a brief [article on how to create a bot user and copy its respective token](https://www.writebots.com/discord-bot-token/).

6. Now that a bot user is created and we have its token, in our terminal in the root directory of this repo, paste this command `cp sample.env .env`. This will make a copy of `sample.env` containg all the environment variables Urban Bot utilizes. Currently you should only see the env var `TOKEN=`. Go ahead and paste your token in after the equals sign `=`. e.g `TOKEN=TOKE_GOES_HERE` (Note: _Make sure to never push secrets or tokens up to github! If you do, regenerate them and take action to prevent that from happening again!_)

🎉 Done.

We are good to go! Run `py client.py` in your terminal to run the bot locally or open the Urban-bot in your favorite code editor and start messing around! _I prefer [Visual Studio Code](https://code.visualstudio.com/)._ (Note: _You're command for executing python code may differ._)

#### [back to top](#urban-bot-🤖)

# Deploy Urban Bot 🚀

Want to deploy your own verson of Urban Bot? Here's how!

1. [Fork](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) or [Create a Repo](https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line).

2. Head over to [Heroku](https://www.heroku.com/). If you don't have a Heroku account you can [sign up here](https://signup.heroku.com/).

3. [Create a new app](https://dashboard.heroku.com/new-app). The name is all up to you!

4. Under `Deployment Method` choose GitHub and connect the Repo.

5. Scroll down to `Automatic Deploys` and click `Enable Automatic Deploys`

6. Head over to the settings page. Under `Config Vars` go ahead and select `Reveal Config Vars` and let's add a new one. Set the `KEY` to `TOKEN` and set the value to your bots secret token.

#### [back to top](#urban-bot-🤖)
