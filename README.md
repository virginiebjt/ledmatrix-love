# ledmatrix-love

A python 3 script to display SMS on a led matrix panel (I'm using 4 daisy chained MAX7219 devices).
You will need to install the following libraries on your RPI :

- luma led matrix (https://luma-led-matrix.readthedocs.io/en/latest/install.html)
- flask (https://pypi.org/project/Flask/)

And of course python 3.

Wiring is the same as indicated in luma's doc: 
VCC : PIN 2 (5V0)
GDN : PIN 6 (GDN)
DIN : PIN 19 (GPIO 10 (MOSI))
CS : PIN 24 (GPIO 8 (SPI CE0)
CLK : PIN 23 GPIO 11 (SPI CLK)


Troubleshooting : ensure that you've enabled the SPI kernel on your RPI (type sudo rpi-config in your terminal and navigate to interface)

I'm using Nexmo to generate a virtal number. More infos: https://www.nexmo.com/blog/2019/05/31/receive-an-sms-with-python-dr
