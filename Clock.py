import time
import threading
class Clock:

    def __init__(self, interval):
        self.interval = interval
        self.workers = []
        self.status = 0

    def add_worker(self, w):
        self.workers.append(w)

    def tick(self):
        #print("Tick!")
        for w in self.workers:
            w.work()

    def tock(self):
        #print("Tock!")
        for w in self.workers:
            w.collect()

    def run(self):
        while (self.status == 1):
            self.tick()
            time.sleep(1)
            self.tock()
            time.sleep(1)

    def start(self):
        self.status = 1
        threading._start_new_thread(self.run, ())

    def stop(self):
        self.status = 0