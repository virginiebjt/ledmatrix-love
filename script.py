import re
import time
import argparse

from time import time, sleep, strftime
from datetime import datetime

from flask import Flask, request, jsonify

#import Luma's library to display the text on the  led matrix
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, LCD_FONT

#define the led matrix configuration - change the cascaded number to the number of matrix you have, and the block orientation if needed
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90)


#initialize the app
app = Flask(__name__)

@app.route('/webhooks/inbound-sms', methods=['GET', 'POST'])


def inbound_sms():
    if request.is_json:
        print(request.get_json())
        
    else:
        data = dict(request.form) or dict(request.args)
        print(data)
        #submit the text to the leds
        sms = request.args.get('text')
        show_message(device, sms, fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
                
            
       

    return ('', 204)

       


app.run(port=3000)








