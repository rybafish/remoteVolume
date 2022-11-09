# Overview

Remote Volume is a small application to control the PC volume with your mobile phone (iPhone, Andriod).

On the mobile the interface looks like this:

![main](/img/00_main_app.png)

In addition to master volume level you can send the following events:
- ```[Previous], [Play/Pause], [Next]``` - media events
- ```[Left arrow], [Space], [Right arrow]``` - key-presses

This allows to get basic control over the media playback on the PC.

Actually no application required on the phone, only on the PC, see details below. 

The only requirement is PC and mobile need to be connected to the same WiFi network.

Step by step instruction below.

# PC side
You need to [download](#download) and unpack the binary wherever you prefer and run it. This should look something like this:
![image](https://user-images.githubusercontent.com/53466066/200941396-b16cbe84-a0ae-4ac2-b02f-6c1e2efa0367.png)

On the first execution windows firewall might ask a permission to open the connection:
![image](https://user-images.githubusercontent.com/53466066/200941938-abd99cef-f3d2-4fc8-b170-1a0167bcd1a2.png)

Note: enable the local addreses and press "Allow access".

Take a note on the port number and the IP address(es), this precious information will be required right away.

# Mobile side

The setup more or less the same for iPhone and Android users. You need to start the browser and open the ip-adress and the port, in this case 192.168.5.6:8000, should look like this:

![safari](/img/01_web.png)

If everything works fine you will be able so see the app running already:

![safari](/img/02_web.png)

Now you can create a home screen icon. Press "Share", scroll down a bit and choose "Add to Home Screen".

![add home](/img/03_add_home.png)

Type any preferred name:

![add home](/img/04_add_home.png)

![thatsit](/img/05_home.png)

That's it, you should see the volume icon on you home screen.

<a name="download" />

# Download
Version [0.1 beta](https://github.com/rybafish/remoteVolume/releases/download/v0.1beta/RemoteVolume_01beta.7z) for Windows 10, 2022-11-07.

# Troubleshooting
The moist common problem is windows firewall. In this case server the console does not show any interraction, just the "Listening..." message. On the mobile side you will see a blank screen.

To make sure you have allowed the connections to the volume application:
- hit the start button
- start typing "firewall"
- select "Firewall & network protection"

![image](https://user-images.githubusercontent.com/53466066/200745924-7feacb4c-a0d3-4112-862d-8d76b108bf6c.png)

Open the "Allow an app through firewall":

![image](https://user-images.githubusercontent.com/53466066/200746060-542d9d9d-675c-46e4-b955-790609ca6ad1.png)

In the list of applications find the "volume" and check the settings.

![image](https://user-images.githubusercontent.com/53466066/200942237-429866b4-df9d-4446-9290-0f45ecbb030b.png)

It should be allowed to communicate through private and public networks.

# Report issues

To report issues or request features create a ticket on the projects [github page](https://github.com/rybafish/remoteVolume/issues).
