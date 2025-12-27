# Telegram Redirect Bot

A simple Telegram bot that automatically redirects users to another bot.

## Features

- Instantly redirects users when they start the bot
- Works with any message sent to the bot
- Provides a clickable button to the target bot
- Logs all redirect actions

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure the Bot

Edit `config.py` or directly modify `redirect_bot.py`:

- `BOT_TOKEN`: Your bot token from [@BotFather](https://t.me/BotFather)
- `TARGET_BOT_USERNAME`: The username of the bot you want to redirect to (without @)

### 3. Get Your Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token provided

### 4. Run the Bot

```bash
python redirect_bot.py
```

## Usage

Once the bot is running:

1. Users start a chat with your bot
2. They receive a message with a button
3. Clicking the button opens the target bot
4. Any message sent to your bot will trigger the redirect

## Configuration Options

### Using config.py

You can import configuration from `config.py`:

```python
from config import BOT_TOKEN, TARGET_BOT_USERNAME
```

### Direct Configuration

Or directly edit the values in `redirect_bot.py`:

```python
BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
TARGET_BOT_USERNAME = "example_bot"
```

## Example

If you want to redirect users to `@YourTargetBot`:

```python
TARGET_BOT_USERNAME = "YourTargetBot"
```

## Notes

- Make sure your bot has the necessary permissions
- The target bot username should not include the @ symbol
- Keep your bot token secure and never share it publicly

## License

MIT License
