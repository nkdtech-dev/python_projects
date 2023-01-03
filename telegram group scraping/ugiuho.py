from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

telegram_api_id = 28348074
telegram_app_hash = "ec034321b8e78b79e94efdab078de0af"
phone = "+237654930195"

client = TelegramClient(session=phone, api_hash=telegram_app_hash, api_id=telegram_api_id)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('enter the code: '))

chats = []
last_date = None
chunk_size = 200
groups = []
result = client(GetDialogsRequest(offset_date=last_date,
                                  offset_id=0,
                                  offset_peer=InputPeerEmpty(),
                                  limit=chunk_size,
                                  hash=0
                                  ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print("choose group to get contacts from: ")
i = 0
for group in groups:
    print(f"{i}-{group.title}")
    i += 1
group_index = input("enter chossen group number: ")
target_group = groups[int(group_index)]

print("fetching contacts from group:")
all_members = []
all_members = client.get_participants(target_group, aggressive=True)

print("saving file............")
with open("members.csv", "w", encoding='UTF-a') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
    for user in all_members:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + " " + last_name).strip()
        writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
print("members scrapd succesfully")
