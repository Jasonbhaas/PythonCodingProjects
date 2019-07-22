def getShiftedString(s, leftShifts, rightShifts):
    # Left and right shifts will cancel eachother out
    relative_shifts = leftShifts - rightShifts

    if (relative_shifts == 0):
        return s

    isLeftShift = (relative_shifts > 0)

    # shifting the length of s is the same as 0 shifts
    relative_shifts = abs(relative_shifts) % len(s)

    if not isLeftShift:
        relative_shifts = relative_shifts * -1

    return s[relative_shifts:] + s[:relative_shifts]
