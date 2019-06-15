# Practice project from Automate the Boring Stuff by Al Sweigart

#!/usr/bin/env python3
import pyautogui

print("Press Ctrl+C to quit.")

try:
  while True:
    x, y = pyautogui.position()
