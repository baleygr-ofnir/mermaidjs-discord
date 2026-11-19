# `mermaidjs-discord`

`mermaidjs-discord` is a discord bot that allows you to render Mermaid.js diagrams in your discord chats.

## Server Installation instructions

Click here to [invite](https://discord.com/api/oauth2/authorize?client_id=935684419837132910&permissions=274877910016&scope=bot) the bot to your server.

Type in `!mermaid-help` for help on how to use this bot.

<br/>

## Running this bot yourself
### Bot Token
---
First, grab a bot token from Discord.

Go to [this url](https://discordapp.com/developers/applications/me) and create a new application.<br/>
Add a name for your local bot, something like: `your-username-test-bot`. 

After you've made an application, you should be redirected to a page with all of the app's details on it. 
Scroll to the bottom of this page and press "create a bot user". You will then have a "click to reveal" link that shows you your bot's **token**.

On the same page, under **Privileged Gateway Intents**, enable **Message Content Intent**. The bot reads `!mermaid-` commands from message text and cannot connect without it.

Make sure you make that bot private in that page. 

<br/>

### Running with Docker Compose
---
Copy `.env.example` to `.env` and put your token in it:
>```
>TOKEN=[the token you copied above]
>```

Then run the following in the project root directory:
>```bash
>docker compose up -d --build
>```

User themes are stored in a SQLite database on the `themes` volume, so they survive restarts and rebuilds.

<br/>

### Running with Python
---
This assumes you have Python 3.13 and `pip` installed.

Run the following in the project root directory:
>```bash
>pip install -r requirements.txt
>export TOKEN=[the token you copied above]
>python main.py
>```

Themes are stored in `themes.db` in the current directory; set `THEME_DB_PATH` to store them elsewhere.

<br/>

### Adding your Bot
---
1. On the side tab go to `OAuth2>URL Generator`.

2. Under scopes, select bot.

3. Under permissions, select admin.

4. Use the generated URL to add it to your personal discord server to test out that your code is working correctly.