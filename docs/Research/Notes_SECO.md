## Development Updates
Right click Project -> Project Options -> Options -> Net Identifier Scope, selected "Global (Netlabels and ports global)"

## Design Updates
The difference between MOSFET and BJT, [as explained by Ivan Lara](https://www.quora.com/What-is-the-difference-between-a-MOSFET-and-PNP-or-NPN-transistor), is that BJTs are current-controlled while MOSFETs are voltage-controlled. The circuity to control voltage is easier to design, and I believe it is less strenuous for an MCU to maintain a voltage than a current. For this reason, I will select a voltage-controlled MOSFET, the [IRLB8721PbF HEXFET Power MOSFET](https://www.adafruit.com/product/355), to drive the valve. That will also require an [independent, 12V power supply](https://www.adafruit.com/product/798).

Might want a new temp/humidity sensor, specifically, the [SHT30 Wired (1m) Enclosed Shell seems like the way to go](https://www.adafruit.com/product/5064).

Defining Pinouts
	UART can be any 4 pins on the bus. However, pins 20-25 are the only ones that can be reserved for a special clock feature.
	Due to the physical layout of the pins, GPIO 12-15 is selected as the most suitable for UART transmission. This exposes the CTS/RTS pins, which I don't expect to use, but will include make available.
	Will need one of these connectors, not sure if left- or right-angle: https://www.aliexpress.com/item/1005001999001364.html

	Device class: 
	02h 	Both 	Communications and CDC control 	UART and RS-232 serial adapter, Modem, Wi-Fi adapter, Ethernet adapter. Used together with class 0Ah (CDC-Data) below 
	Leave ID pin floating to designate as slave device	
	

## Links 
1. Adding rst button to pico https://www.raspberrypi.com/news/how-to-add-a-reset-button-to-your-raspberry-pi-pico/

2. The reset button I picked https://www.mouser.com/ProductDetail/Wurth-Elektronik/430152070836?qs=wr8lucFkNMXO5xtOyHnv0g%3D%3D

3. Flow meter for extra sensing https://www.adafruit.com/product/828

4. Recommended MOSFETs for valve https://www.adafruit.com/product/355

5. Activating Pico's UART RTS/CTS https://forums.raspberrypi.com/viewtopic.php?t=319345

6. Pi Zero W UART https://forums.raspberrypi.com/viewtopic.php?t=320865