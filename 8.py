import threading
import time


def print_messages(thread, sleep, messages):
    for message in messages:
        time.sleep(sleep)
        print(f"{thread}: {message}")


thread1 = threading.Thread(target=print_messages, args=("Thread 1", 1, ("first_message", "second_message")))
thread2 = threading.Thread(target=print_messages, args=("Thread 2", 2, ("first_message", "second_message")))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

