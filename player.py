import argparse
import logging
import time
import sys

from pymouse import PyMouse
from pykeyboard import PyKeyboard

log = logging.getLogger(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

parser = argparse.ArgumentParser(description='automatically play video for a certain time before reloading page')
parser.add_argument('--debug', '-d', dest='debug',
                    action='store_true',
                    help='Debug mode')
parser.add_argument('-x', dest='x', type=int,
                    help='x of the click position to play video. half of screen width if unset')
parser.add_argument('-y', dest='y', type=int,
                    help='y of the click position to play video. half of screen height if unset')
parser.add_argument('--duration', dest='duration', type=int, default=40,
                    help='playtime before reloading the video')

if __name__ == "__main__":
    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    m = PyMouse()
    k = PyKeyboard()

    x, y = m.screen_size()
    x = args.x or x/2
    y = args.y or y/2

    time.sleep(5)

    while 1:
        m.click(int(x), int(y), 1)
        time.sleep(args.duration)
        k.tap_key(k.function_keys[5])
        time.sleep(8)
