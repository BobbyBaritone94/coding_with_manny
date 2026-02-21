import time

def greeting():
    name = input("whats your name?")
    greeting = f"Hello {name}!"
    print(greeting)

    return 5


def counter():
    continue_looping = True
    for x in range(5):
        time.sleep(1)
        print(x)

    print("RELEASE THE HOUNDS")

    time.sleep(1)
    num_times_looped = 0
    while continue_looping:
        num_times_looped = num_times_looped + 1
        print(f"BARK! {num_times_looped}")
        # print(num_times_looped)
        
counter()