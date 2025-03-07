**Girlfriend Texter**

![gfTexter](https://github.com/user-attachments/assets/815857b7-5b0a-49c0-b593-d2325e1059c8)

#Sunny Chatbot - iMessage Auto-Responder

##Overview##

This script is an automated chatbot designed to roleplay as "Sunny" in iMessage conversations. It continuously monitors messages from a specific contact and generates AI-driven responses in a personalized style. The chatbot ensures that it only responds to messages it receives and avoids replying to its own messages.

##Features

Reads iMessage conversations from chat.db.

Filters the last 15 messages from a specific contact.

Generates responses using AI (get_chat_message function).

Sends replies automatically via iMessage.

Avoids sending duplicate responses.

Runs in a loop with a 5-second delay to check for new messages.

##Requirements

Python 3.x

imessage_tools library

helper_functions module (for AI-generated responses)

Access to chat.db (iMessage database on macOS)

##Installation

Clone the repository or copy the script.

Ensure you have the required dependencies installed.

##Modify the script:

Update chat_db with your macOS iMessage database path.

Set self_number to your own phone number.

Set desired_phone_number to the contact you want to auto-respond to.

##Run the script:

python chatbot.py

##Usage

The chatbot will run in the background, continuously checking for new messages.

It will only respond if the latest message is from the designated contact.

Messages are generated based on the last 15 messages for contextual accuracy.

##Customization

Modify the initial prompt in prompt_log to adjust the chatbot's personality.

Change the affectionate terms used in responses (e.g., "pookie," "baby").

Adjust the response logic if needed (e.g., reply frequency, message filtering).

##Disclaimer

This script interacts with the iMessage database, which requires appropriate permissions on macOS.

Use responsibly and ensure compliance with Apple's policies and personal privacy considerations.

##License

This project is for personal use only. Modify and distribute at your own discretion.
