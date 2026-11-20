# `mermaidjs-discord`

`mermaidjs-discord` is a discord bot that allows you to render Mermaid.js diagrams in your discord chats.

## Server Installation instructions

Click here to [invite](https://discord.com/api/oauth2/authorize?client_id=935684419837132910&permissions=274877910016&scope=bot) the bot to your server.

Type in `!mermaid-help` for help on how to use this bot.

<br/>

## Running this bot yourself
### Bot Token
---
First, create a Discord app and grab its bot token.

1. Go to the [Developer Portal](https://discord.com/developers/applications) and press **New Application**. Add a name for your bot, something like `your-username-test-bot`, and press **Create**. You land on the app's **General Information** page. New apps get a bot user automatically.

2. Open the **Bot** page from the side menu. Under **Token**, press **Reset Token** and copy the token. Discord shows it only once; reset it again if you lose it.

3. On the same **Bot** page, under **Privileged Gateway Intents**, turn on the **Message Content** intent. The bot reads `!mermaid-` commands from message text, and Discord refuses its connection if the intent is off.

<br/>

### Answer channel
---
The bot answers only in one text channel, set by `ALLOWED_CHANNEL_ID` (the channel's numeric Discord ID). It takes commands from any channel, any server it is in, and direct messages; an answer to a command sent from anywhere else is posted in that channel. The bot refuses to start without this setting.

Diagrams are posted as an image only, always in Mermaid's dark theme on a dark background.

<br/>

### Running with Docker Compose
---
Copy `.env.example` to `.env` and put your token and channel ID in it:
>```
>TOKEN=[the token you copied above]
>ALLOWED_CHANNEL_ID=[the ID of the answer channel]
>```

Then run the following in the project root directory:
>```bash
>docker compose up -d
>```

This pulls `ghcr.io/baleygr-ofnir/mermaidjs-discord:latest`, which CI builds and publishes on every push to `main`. Run `docker compose pull` to fetch a newer image.

<br/>

### Running with Python
---
This assumes you have Python 3.13 and `pip` installed.

Run the following in the project root directory:
>```bash
>pip install -r requirements.txt
>export TOKEN=[the token you copied above]
>export ALLOWED_CHANNEL_ID=[the ID of the answer channel]
>python main.py
>```

<br/>

### Adding your Bot
---
1. Open the **Installation** page from the side menu.

2. Under **Install Link**, select **Discord Provided Link**. A **Default Install Settings** section appears.

3. Under **Guild Install**, add the `bot` scope. A **Permissions** menu appears; select **Administrator**.

4. Copy the URL from the **Install Link** section and open it to add the bot to your personal Discord server, to test that your code is working correctly.