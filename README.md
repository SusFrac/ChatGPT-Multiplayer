# ChatGPT-Multiplayer
This is an API request made in Python that allows you to chat with ChatGPT together.

# Setting up the server:
(These steps will set it up on your Wi-Fi.)

Get an API key from https://platform.openai.com/account/api-keys.

Set the API key as an environment variable.

Open the console and type in ipconfig.

Get the IPv4 address and paste it in the host variable. (host = 'Your IP')

# Setting up the client:
Paste the host variable from the server into client.connect(('Host variable', 55555)) in the client.py file. (client.connect(('Host variable', 55555)))

# Making it available outside of your Wi-Fi:
Open the console and type in ipconfig.

Go to your router page by typing the default gateway from the ipconfig output into any browser.

Log in to the admin page (Usually the password is admin, password, or there are instructions on that page).

Set up a public port on your IP with 55555 as the port.

In the client, put your public IP (You can find it on https://whatismyipaddress.com/ and remember to turn off your VPN if you are using one).

Note: It is not reccomonded not share the client.py publicly;
