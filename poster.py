import argparse
import json
import logging
import random
from random import randint
import sys
import time

from pymouse import PyMouse
import pyautogui
import pyperclip

log = logging.getLogger(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

parser = argparse.ArgumentParser(description='automatically play video for a certain time before reloading page, default values were obtained on a 1920x1080 screen with 80% zoom out')
parser.add_argument('--debug', '-d', dest='debug',
                    action='store_true',
                    help='Debug mode')
parser.add_argument('--config', dest='config', default='comments.json',
                    help='config file with the list of comments to post')
parser.add_argument('--comment-x', dest='comment_x', type=int, default=600,
                    help='x of the form position to input the comment')
parser.add_argument('--comment-y', dest='comment_y', type=int, default=1000,
                    help='y of the form position to input the comment')
parser.add_argument('--validate-x', dest='validate_x', type=int, default=1150,
                    help='x of the form position to input the comment')
parser.add_argument('--validate-y', dest='validate_y', type=int, default=1005,
                    help='y of the form position to input the comment')
parser.add_argument('--progress-start-x', dest='progress_start_x', type=int, default=530,
                    help='y of the form position to input the comment')
parser.add_argument('--progress-end-x', dest='progress_end_x', type=int, default=935,
                    help='y of the form position to input the comment')
parser.add_argument('--progress-y', dest='progress_y', type=int, default=975,
                    help='y of the form position to input the comment')
parser.add_argument('--delay', dest='delay', type=int, default=180,
                    help='delay between each comment')


def get_random_comment(conf):
    with open(args.config, 'r') as f:
        comments = json.load(f)
    return random.choice(comments)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    m = PyMouse()

    time.sleep(5)

    while 1:
        m.click(
            int(randint(args.progress_start_x, args.progress_end_x)),
            int(args.progress_y),
            1
        )
        time.sleep(5)
        m.click(int(args.comment_x), int(args.comment_y), 1)
        comment = get_random_comment(args.config)
        log.info("writting random comments %s" % comment)
        pyperclip.copy(comment)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'v')
        #keyboard.press_and_release('ctrl+v')
        # keyboard.write(comment)
        time.sleep(0.5)
        m.click(int(args.validate_x), int(args.validate_y), 1)
        time.sleep(args.delay - 5)
