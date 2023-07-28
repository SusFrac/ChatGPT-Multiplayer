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

# How to make it available outside of your wifi

1 Open the console and type in ipconfig
   
2 Go to your router page by typing the default gateway fron the ipconfig into any browser
   
3  Log in to the admin page (Usualy the password is admin, password or there are instructions on that page)

5 Set up a public port on your ip and with 55555 as the port.

6 In the client put your public ip (You can find it on https://whatismyipaddress.com/ and remember to turn off your vpn if you are using one)

Do not share the client.py publicly only to people who you trust or you can get a domain
