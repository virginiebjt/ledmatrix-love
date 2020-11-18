import re
import time
import argparse

from time import time, sleep, strftime
from datetime import datetime

from flask import Flask, request, jsonify

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, LCD_FONT, CP437_FONT
from PIL import ImageFont

font = ImageFont.truetype("examples/pixelmix.ttf", 8)

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=5, block_orientation=-90)



app = Flask(__name__)

@app.route('/webhooks/inbound-sms', methods=['GET', 'POST'])


def inbound_sms():
    if request.is_json:
        print(request.get_json())
        
    else:
        data = dict(request.form) or dict(request.args)
        print(data)
        sms = request.args.get('text')
        show_message(device, sms, fill="white", font=proportional(LCD_FONT), scroll_delay=0.05)
                
            
       

    return ('', 204)

       


app.run(port=3000)








