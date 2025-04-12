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
    n = len(boxes)  # Total number of boxes
    opened_boxes = set()  # Track which boxes have been opened
    queue = [0]  # Start with the first box (box 0), which is unlocked

    while queue:
        current_box = queue.pop(0)  # Get the next box to process
        if current_box not in opened_boxes:
            opened_boxes.add(current_box)  # Mark this box as opened
            # Add valid keys from this box to the queue
            for key in boxes[current_box]:
                if key not in opened_boxes and 0 <= key < n:
                    queue.append(key)
        # Early termination if all boxes are opened
        if len(opened_boxes) == n:
            return True

    # Check if all boxes have been opened
    return len(opened_boxes) == n
