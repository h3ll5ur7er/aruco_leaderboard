from threading import Thread
from .framework import HasLogger
from .camera import Camera
from .marker_detection import MarkerDetector
from .gpio_controller import GpioController
from .database import CarRepository, ResultRepository

from time import sleep

class BackgroundWorker(Thread, HasLogger):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
    def run(self, *a, **kw):
        self._running = True
        self._log.info("starting")
        while self._running:
            img = Camera().grab()
            if img is None:
                self._log.error("unable to grab image from capture device")
                self._running = False
            
            markers = MarkerDetector().detect_ordered_markers(img)
            if len(markers)<4:
                GpioController().set_led(0)
            else:
                GpioController().set_led(1)
                
            # record time
            
            pass
        self._log.info("terminated")
        
    def stop(self):
        self._running = False
        self.join()