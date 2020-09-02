# docker-telegram-bot

Create your telegram bot in a faster and easy way exploiting docker.
Write your bot in python and start the container.

### Important
The `bot` folder contains an example script of an echo bot. What you need to do is **replacing** the `token` with your own one, obtained by the _BotFather_.

### Usage

1. Enter the directory:
```
cd docker-telegram-bot
```
2. Build the image:
```
docker build . -t docker-telegram-bot
```
3. Run the container:
```
docker run docker-telegram-bot
```

Now open the telegram app and search your bot by name. Start the conversation and send some messages. It should reply with the message you sent.
