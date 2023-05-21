# Update your system:
sudo apt-get update
sudo apt-get upgrade

# If either of the above complete but with errors, try again with:
sudo apt-get update --fix-missing
#or
sudo apt-get upgrade --fix-missing

# Set Localisation Options:
sudo raspi-config
	> Localisation Options > US > Eastern > OK

# Soil Sensor Setup:
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools

# Enable i2c interface (reboot first!):
sudo reboot -n
sudo raspi-config
	> Interfacing Options > I2C > Enable > OK

sudo pip3 install RPI.GPIO
sudo pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-busdevice
sudo apt install git-all
sudo git clone https://github.com/adafruit/Adafruit_CircuitPython_seesaw.git
sudo pip3 install adafruit-circuitpython-seesaw

#To test hardware detection and return hardware addresses:
sudo i2cdetect -y 1
#Soil Sensor should populate on x36


# OLED Screen Install:
#To test hardware detection and return hardware addresses:
sudo i2cdetect -y 1
#Soil Sensor should populate on x3c

sudo pip3 install adafruit-circuitpython-ssd1306
sudo apt-get install python3-pil
sudo pip3 install requests

# Grab and unzip silkscreen font to clean up txt display:
wget http://kottke.org/plus/type/silkscreen/download/silkscreen.zip
unzip silkscreen.zip

# Build your OLEDstats.py file
sudo nano OLEDstats.py

# Run this file when you want to start the display:
sudo python3 OLEDstats.py

# Append the above command to /etc/rc.local to start on boot:
sudo nano /etc/rc.local
	sudo python3 OLEDstats.py





# Install Ruby
sudo aptitude install ruby-dev

# Check/Confirm Ruby Version:
ruby --ver

# Install FluentD Unified Log Aggregator & Plugin
sudo gem install fluentd -v "~> 0.12.0"
sudo fluent-gem install fluent-plugin-td

# Install FluentD Plugn for Azure Log Analytics
sudo fluent-gem install fluent-plugin-azure-loganalytics


