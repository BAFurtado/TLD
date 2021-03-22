# coding: utf-8

# Originally from
# https://github.com/PPartisan/THE_LONG_DARK

# Simply adapted to LINUX by Bernardo Alves Furtado

import os
import time

import psutil
from pylab import rcParams
from pynput.keyboard import Key, Controller, Listener

import mapping

rcParams['figure.figsize'] = 12, 9.5


def is_tld_running():
    processes_numbers = psutil.pids()
    for n in processes_numbers:
        if 'tld.x86_64' == psutil.Process(n).name():
            return True


class Interaction:
    def __init__(self):
        self.recording = False
        self.keyboard = Controller()
        # with Listener(on_press=self.on_press(), on_release=self.on_release()) as listener:
        #     listener.join()

    def press(self):
        self.keyboard.press(Key.f8)
        self.keyboard.release(Key.f8)

    def on_press(self):
        pass

    def on_release(self):
        pass

    def was_pressed(self):
        if self.keyboard.press(Key.esc):
            # Stop listener
            return False
        return True

    def start_interactive_mapping(self, s_path, f_path, time_step=2.5):
        t = time.time()
        print(f'STARTED!')
        while is_tld_running():
            if self.was_pressed():
                if not self.recording:
                    self.recording = True
                else:
                    self.recording = False

            if self.recording:
                if time.time() - t > time_step:
                    self.press()
                    print(f'TRIED TO PRESS BUTTON')
                    t = time.time()
                    coord = mapping.read_coords_from_screenshots(s_path)
                    mapping.write_coords_to_file(coord, f_path + "coords.txt", "a")
                    mapping.delete_screenshots(s_path)
            time.sleep(30)
        mapping.delete_screenshots(s_path)
