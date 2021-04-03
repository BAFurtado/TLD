# coding: utf-8

# Originally from
# https://github.com/PPartisan/THE_LONG_DARK

# Simply adapted to LINUX by Bernardo Alves Furtado

import threading
import time

import psutil
from pylab import rcParams
from pynput.keyboard import Key, Controller

import mapping

rcParams['figure.figsize'] = 12, 9.5


def is_tld_running():
    return True
    processes_numbers = psutil.pids()
    for n in processes_numbers:
        if 'tld.x86_64' == psutil.Process(n).name():
            return True


def background(func, args):
    th = threading.Thread(target=func, args=args)
    th.start()


class Interaction:
    def __init__(self):
        self.recording = True
        self.keyboard = Controller()

    def start_recording(self):
        print('Started recording')
        self.recording = True

    def stop_recording(self):
        print('Stopped recording')
        self.recording = False

    def press(self):
        print(f'Pressed the button')
        self.keyboard.press(Key.f8)
        self.keyboard.release(Key.f8)

    def start_interactive_mapping(self, s_path, f_path):
        print(f'Started!')
        if self.recording:
            while is_tld_running():
                self.press()
                coord = mapping.read_coords_from_screenshots(s_path)
                mapping.write_coords_to_file(coord, f_path + "coords.txt", "a")
                mapping.delete_screenshots(s_path)
                time.sleep(30)
