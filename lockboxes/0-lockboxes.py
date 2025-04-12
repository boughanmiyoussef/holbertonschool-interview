#!/usr/bin/python3

"""
Module 0-lockboxes
This module provides a function to determine if all lockboxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list where each element is a list of keys contained in that box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    opened_boxes = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        if current_box not in opened_boxes:
            opened_boxes.add(current_box)
            for key in boxes[current_box]:
                if key not in opened_boxes and key < len(boxes):
                    queue.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
