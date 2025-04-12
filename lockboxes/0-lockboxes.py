#!/usr/bin/python3

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
            # Add all keys from this box to the queue
            for key in boxes[current_box]:
                if key not in opened_boxes and key < len(boxes):
                    queue.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
