#!/usr/bin/env python3

"""
Simple GUI compliment generator for that special someone.
"""

import simpleguitk
import random


compliments = ['beautiful', 'sexy', 'smart',
               'hard working', 'ambitious',
               'resourceful', 'intelligent',
               'kind', 'brilliant', 'humble',
               'compassionate', 'strong']


girlfriend_name = input("Enter name: ")

message = random.choice(compliments)


# Handler for mouse click
def click():
    global message
    message = random.choice(compliments)

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(girlfriend_name + ',', [30, 50], 48, "Red")
    canvas.draw_text("you are very", [30, 100], 30, "Red")
    canvas.draw_text(message, [30, 150], 48, "Green")

# Create a frame and assign callbacks to event handlers
frame = simpleguitk.create_frame("Logan's Encouragement App!", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
