import pyautogui
import sys
import time

# move mouse to keep system awake
def move_mouse(old_pos):
    # generate a new mouse position
    new_pos = (old_pos[0], old_pos[1] + 1)
    if not pyautogui.onScreen(new_pos):
        new_pos = (old_pos[0], old_pos[1] - 1)

    # move to new mouse position then back
    pyautogui.moveTo(*new_pos, pyautogui.MINIMUM_DURATION)
    time.sleep(0.1)
    pyautogui.moveTo(*old_pos, pyautogui.MINIMUM_DURATION)

# check if mouse not moved since last update
def check_inactive(pos):
    time.sleep(60)
    return pyautogui.position() == pos

if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    while True:
        pos = pyautogui.position()
        if check_inactive(pos):
            move_mouse(pos)
