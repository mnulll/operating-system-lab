import threading
import random
import time


class Person(threading.Thread):
    running = True  # to make person prepare

    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while(self.running):
            print('Person %s is hungry.' % self.index)
            self.prepare()

    def prepare(self):

        fork1, fork2 = self.left_fork, self.right_fork
        while self.running:
            fork1.acquire()  # hold left fork
            locked = fork2.acquire(False)
            if locked:
                break   # get both fork
            fork1.release()  # release fork if dont get left fork
        else:
            return
        self.eat()
        fork2.release()
        fork1.release()  # release both fork after eating

    def eat(self):
        print('Person %s starts eating. ' % self.index)
        time.sleep(1)  # give person time to eat
        print('Person %s finishes eating and leaves to think.' % self.index)


# use semaphore for flag indicator
forks = [threading.Semaphore() for n in range(5)]


person = [Person(i, forks[i % 5], forks[(i+1) % 5])  # declare person and fork index
          for i in range(5)]


for p in person:
    p.start()  # start the process
time.sleep(5)  # delay 5 sec before executing the next line
Person.running = False  # to stop the process
print("Terminating the process")
