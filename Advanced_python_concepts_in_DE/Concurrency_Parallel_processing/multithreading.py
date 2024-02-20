import threading
import time

# Define a function for the thread
def print_numbers():
    """
    A function that prints numbers from 1 to 5 with delays in between.
    """
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Sleep for 1 second

# Create two threads as follows
try:
    threading.Thread(target=print_numbers).start()
    threading.Thread(target=print_numbers).start()
except:
    print("Error: unable to start threads")
