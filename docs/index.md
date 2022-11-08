Control PC volume with your phone (iPhone, Andriod).

On the mobile the interface is very clean and simple:

![main](/img/00_main_app.png)

In addition to master volume level you can send
- ```[Previous], [Play/Pause], [Next]``` - media events
- ```[Left arrow], [Space], [Right arrow]``` - key-presses

This allows to get simple control over the media playback on the PC.

Actually, no app required on the phone, see details below. 

Of course, the PC and mobile need to be connected to the same WiFi network.

Step by step instruction below.

# PC side
You need to [download](#download) and unpack the binary wherever you uprefer and run it. This should look something like this:
![image](https://user-images.githubusercontent.com/53466066/200641996-e2fa973d-4121-4172-a9d3-52d0f03aa4f2.png)

On the first execution windows firewall might ask a permission to open the connection:
![image](https://user-images.githubusercontent.com/53466066/199925068-c7b1235a-cd6c-4847-a822-a42f49fa6514.png)

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
[01 beta](https://github.com/rybafish/remoteVolume/releases/download/v0.1beta/RemoteVolume_01beta.7z) for Windows 10 (PC), 2022-11-07.
