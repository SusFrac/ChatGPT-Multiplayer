# ChatGPT-Multiplayer

This is a API request made in python that allows you to chat to chatGPT together

# Setting up the server:

(This will only set it up on your wifi.)

1 Get an api key from https://platform.openai.com/account/api-keys

2 Paste the api key in the openai.api_key varible on the server. (openai.api_key = 'your key')

3 Open the console and type in ipconfig

4 Get the IPv4 address and paste it in the host varible (host = 'Your ip')


# Setting up the client:

Paste the host varible from the server to the client.connect on the client.py  (client.connect(('Host varible', 55555)))
