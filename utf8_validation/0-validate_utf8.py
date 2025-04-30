def validUTF8(data):
    """
    Checks if a list of integers represents a valid UTF-8 encoding.
    """
    expected_bytes = 0

    for number in data:
        # Convert the number to an 8-bit binary string
        binary = bin(number)[2:].zfill(8)

        if expected_bytes == 0:
            if binary.startswith('0'):
                continue
            elif binary.startswith('110'):
                expected_bytes = 1
            elif binary.startswith('1110'):
                expected_bytes = 2
            elif binary.startswith('11110'):
                expected_bytes = 3
            else:
                return False
        else:
            # We are expecting a continuation byte starting with '10'
            if not binary.startswith('10'):
                return False
            expected_bytes -= 1

    return expected_bytes == 0
