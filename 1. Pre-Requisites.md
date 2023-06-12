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

# 4. Expand your storage
```python
sudo raspi-config
  > Advanced Options > Expand FileSystem
```
