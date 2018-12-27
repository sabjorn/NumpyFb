import os
import logging

import numpy as np

class NumpyFb(object):
    """A class for manipulating Linux framebuffer 
    as a memorymapped numpy array"""
    def __init__(self, framebuf="fb0", cursorclear=True):
        self.logger = logging.getLogger("NpFramebuf")

        self.colorOrder = "BRG"

        if cursorclear:
            self.logger.debug("Clearning cursor on TTY1")
            os.system("echo -e '\033[?17;0;0c' > /dev/tty1")
            os.system("echo 0 > /sys/class/graphics/fbcon/cursor_blink")

        # get screen size
        self.logger.debug("Calculating screen size")
        SIZE_DIR = "/sys/class/graphics/{0}/virtual_size".format(framebuf)
        with open(SIZE_DIR, "r") as f:
            read_data = f.read()
        self.xsize, self.ysize = [int(n) for n in (read_data.strip().split(','))]
        self.minsize = min(self.xsize, self.ysize)
        self.logger.debug("Screen size, xsize:{0} ysize:{1}". format(self.xsize, self.ysize))

        self.array = np.memmap("/dev/{0}".format(framebuf), dtype='B', mode='w+', shape=(self.ysize, self.xsize, 4))
        self.clear() # clear

    def __del__(self):
        del self.array

    def clear(self):
        self.array[:,:,:] = 0

    def setBackground(self, r, g, b):
        """Framebuffer is 'BRG'"""
        self.array[:,:,0] = b
        self.array[:,:,1] = g
        self.array[:,:,2] = r

if __name__ == '__main__':
    fb = NumpyFb()

    # set background to blue
    fb.setBackground(0, 0, 255)

    # colour a square white
    fb.array[:int(fb.xsize/4), :int(fb.ysize/4), :] = 255