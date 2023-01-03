from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import csv
import random
import time

api_id = 29716023
api_hash = '60f3c80bd5b27f3f1529fe581dd936b4'
phone = '+237650151436'
SLEEP_TIME = 30
client = TelegramClient(session=phone, api_id=api_id, api_hash=api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

users = []
with open("members.csv", encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",", lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {'username': row[0], 'id': int(row[1]), 'access_hash': int(row[2]), 'name': row[3]}
        users.append(user)

mode = int(input("Enter 1 to send by user ID or 2 to send by username: "))

text = [["Hello {}, sorry for finding my self in your inbox without permition trust you are well"]
    , ["hello {}, how are you"]
    , ["hello {}, can we connect sorry for finding my self in you inbox"]
    , ["hello {}, trust you are well "]]
messages = random.choice(text)
for user in users:
    if mode == 2:
        if user['username'] == "":
            continue
        receiver = client.get_input_entity(user['username'])
    elif mode == 1:
        receiver = InputPeerUser(user['id'], user['access_hash'])
    else:
        print("Invalid Mode. Exiting.")
        client.disconnect()
    message = random.choice(messages)
    try:
        print("Sending Message to:", user['name'])
        client.send_message(receiver, message.format(user['name']))
        print("Waiting {} seconds".format(SLEEP_TIME))
        time.sleep(SLEEP_TIME)
    except PeerFloodError:
        print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        client.disconnect()
    except Exception as e:
        print("Error:", e)
        print("Trying to continue...")
        continue
client.disconnect()
print("Done. Message sent to all users.")
