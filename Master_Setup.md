# 1. Update your system:
```python
sudo apt-get update
sudo apt-get upgrade
```

# 2. (Optional) If either of the above complete but with errors, try again with:
```python 
sudo apt-get update --fix-missing
sudo apt-get upgrade --fix-missing
```

# 3. Set Localisation Options:
```python
sudo raspi-config
	> Localisation Options > TimeZone > US > Eastern > OK
```

# 4. Soil Sensor Setup:
```python
sudo apt-get install python3-pip
sudo pip3 install --upgrade setuptools
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools
```

# 5. Enable i2c interface (reboot first!):
```python
sudo reboot -n
sudo raspi-config
	> Interfacing Options > I2C > Enable > OK
```
```python
sudo pip3 install RPI.GPIO
sudo pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-busdevice
sudo apt install git-all
sudo git clone https://github.com/adafruit/Adafruit_CircuitPython_seesaw.git
sudo pip3 install adafruit-circuitpython-seesaw
```

# 6. To test hardware detection and return hardware addresses:
```python
sudo i2cdetect -y 1
#Soil Sensor should populate on x36
```

# 7. OLED Screen Install:
```python
#To test hardware detection and return hardware addresses:
sudo i2cdetect -y 1
#Soil Sensor should populate on x3c

sudo pip3 install adafruit-circuitpython-ssd1306
sudo apt-get install python3-pil
sudo pip3 install requests
```

# 8. Grab and unzip silkscreen font to clean up txt display:
```python
wget http://kottke.org/plus/type/silkscreen/download/silkscreen.zip
unzip silkscreen.zip
```

# 9. Build your OLEDstats.py file
```python
sudo nano OLEDstats.py
```

# 10. Run this file when you want to start the display:
```python
sudo python3 OLEDstats.py
```

# 11. Append the above command to /etc/rc.local to start on boot:
```python
sudo nano /etc/rc.local
	sudo python3 OLEDstats.py
```


# Install Ruby
sudo aptitude install ruby-dev

# Check/Confirm Ruby Version:
ruby --ver

# Install FluentD Unified Log Aggregator & Plugin
sudo gem install fluentd -v "~> 0.12.0"
sudo fluent-gem install fluent-plugin-td

# Install FluentD Plugn for Azure Log Analytics
sudo fluent-gem install fluent-plugin-azure-loganalytics


