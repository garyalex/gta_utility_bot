#!/usr/bin/env python3

import bot_functions
import argparse
import requests

config = bot_functions.getconfig("config.yml")

# Setup our arguments
parser = argparse.ArgumentParser()
parser.add_argument("--title", "-t",
                    help="Title of message",
                    type=str, required=True)
parser.add_argument("--message", "-m",
                    help="Message to send",
                    type=str, required=True)
parser.add_argument('--group', choices=config["channel_id"].keys())
args = parser.parse_args()

# Setup request and send message
token = config['telegram_api_token']
api_url = f"https://api.telegram.org/bot{token}/sendMessage"
message_text = f"""
<b>{args.title}</b>
{args.message}
"""
payload = {
    "chat_id": config['channel_id'][args.group],
    "text": message_text,
    "parse_mode": "html",
}
r = requests.get(api_url, params=payload)
# print(r.text)
