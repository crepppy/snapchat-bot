# Snapchat Discord Bot
A simple bot made with the [android development bridge](https://developer.android.com/studio/command-line/adb) that automates sending snapchat messages through discord

## Running
For this you will need an android phone connected with ADB or use an emulator capable of being controlled by the ADB tools

ADB is required for this project and will need to be installed first. These tools will automatically be installed if you have the android SDK. Otherwise follow the instructions on [the Google developers website](https://developer.android.com/studio/releases/platform-tools) and add the binary to your path

Then simply install the single dependency of discord.py using
```
pip install -r requirements.txt
```
using whatever your pip binary is called

To run use
```
python snapchat.py
```
The script optionally takes the discord user ID that's snapchat account is loaded with the bot in order to ask for confirmation in order to send messages for example

```
python snapchat.py 139068524105564161
```
