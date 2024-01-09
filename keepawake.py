import pyautogui
import sys
import time
import random

# move mouse to keep system awake
def move_mouse(old_pos):
    for n in range(1, random.randint(2, 20)):
        # define increment to move mouse, and how long to move mouse for
        new_pos_delta = gen_random_delta()
        move_time = float(1) / random.randint(1, 10)
        
        # generate a new mouse position
        new_pos = (old_pos[0] + new_pos_delta[0],
                   old_pos[1] + new_pos_delta[1])

        # regenerate if off-screen
        while not pyautogui.onScreen(new_pos):
            new_pos_delta = gen_random_delta()
            new_pos = (old_pos[0] + new_pos_delta[0],
                       old_pos[1] + new_pos_delta[1])

        # move to new mouse position
        pyautogui.moveTo(*new_pos, move_time, pyautogui.easeOutElastic)

# generate random change in mouse x, y
def gen_random_delta():
    x = random.randint(10, 100) * (-1 if random.random() > 0.5 else 1)
    y = random.randint(10, 100) * (-1 if random.random() > 0.5 else 1)
    return (x, y)
            
# check if mouse not moved since last update
def check_inactive(pos):
    time.sleep(30)
    return pyautogui.position() == pos

if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    while True:
        pos = pyautogui.position()
        if check_inactive(pos):
            move_mouse(pos)
