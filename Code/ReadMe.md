# wpa_supplicant.conf
This defines your wireless network settings and can be pre-loaded to the SD card so your Raspberry Pi automatically connects to the network on boot. 
The following are rewquired for this to be a valid wpa_supplicant.conf file: 

- Region
- Wireless SSID
- Wireless Network Key/Passphrase

[wpa_supplicant.conf template](https://github.com/EEN421/Sentinel-Integrated-RPI-Soil-Sensor/blob/Main/Code/wpa_supplicant.conf)

# fluent.conf
This is where your log sources are defined and your WorkspaceID and Key are hard-coded.
Instructions for grabbing your [WorkspaceID and Key](https://github.com/EEN421/Sentinel-Integrated-RPI-Soil-Sensor/blob/Main/Sentinel%20Integration/9.%20Grab%20Workspace%20ID%20and%20Key.md), or to [create a new workspace](https://github.com/EEN421/Sentinel-Integrated-RPI-Soil-Sensor/blob/Main/Sentinel%20Integration/8.%20Create%20Log%20Analytics%20Workspace.md) if you don't already have one. 

# main.py
This is your main application/program code that that loads dependencies, defines variables, calls functions, the star of the show.
It handles [taking the soil temperature and moisture readings, pushing them to the OLED screen, and local logging.](https://github.com/EEN421/Sentinel-Integrated-RPI-Soil-Sensor/blob/Main/Code/main.py)

# Start_Fluent.bash
This is essentially a complicated start command for the fluent service that points to the fluent.conf file (-c), specifies the verbose logging (--log) and where to store them (/var/log/td-agent/fluent.log).
A copy can be found here: [Start_Fluent.bash](https://github.com/EEN421/Sentinel-Integrated-RPI-Soil-Sensor/blob/Main/Code/Start_FluentD.bash)
