from helper_functions import get_chat_message
from imessage_tools import read_messages, send_message
import time

# Prompt log initialization
prompt_log = [
    {'role': 'user',
     'content': 'You are to roleplay as Sunny and you are talking to your girlfriend. '
                'Create responses to the latest text as if you were Sunny. '
                'Address your girlfriend as pookie, baby, or bebe. '
                'The last 20 texts are included for context. '
                'Use the date metadata to reply to the recent text with the context provided. '
                'Do not include the date.'}
]

while True:
    # Path to the chat.db file
    chat_db = "/Users/sunnynguyen/Library/Messages/chat.db"
    # Phone number or label for "you"
    self_number = "801859****"
    # Number of messages to return
    n = None
    # Read the messages
    messages = read_messages(chat_db, n=n, self_number=self_number, human_readable_date=True)

    def find_last_N_messages_by_number(messages, phone_number):
        last_N_messages = []
        N = 0
        for message in reversed(messages):
            if message["phone_number"] == phone_number and message["cache_roomname"] == None:
                last_N_messages.append(message)
                N += 1
                if N >= 15:
                    break
        return last_N_messages

    # Initialize the chat as a string block
    chat = ""

    # Example usage:
    desired_phone_number = "+1209561****"
    last_N_messages = find_last_N_messages_by_number(messages, desired_phone_number)

    send = True

    if last_N_messages:
        first_message = last_N_messages[0]  # Get the first message
        # Check if the first message is not from you
        if not first_message["is_from_me"]:
            send = True
            for message in last_N_messages:
                # Append only the text content to the chat string block
                chat += f"{message['body']}\n"
        else:
            print("Latest message is from you.")
            send = False
    else:
        print("No messages found for phone number:", desired_phone_number)
        send = False

    prompt_log.append({'role': 'user', 'content': chat})  # Append chat to prompt log

    # Get and send response
    if send == True:
        # GPT response
        response = get_chat_message(prompt_log)

        # Send the response message text content only
        send_message(response.content, 1209561****, False)

    # Wait for some time before checking again
    time.sleep(5)  # Adjust this value according to your needs
