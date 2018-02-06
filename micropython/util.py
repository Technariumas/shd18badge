def colorWheel(wheelPos):
	if wheelPos < 85:
		return (255 - wheelPos * 3, 0, wheelPos * 3)
	elif wheelPos < 170:
		wheelPos -= 85;
		return (0, wheelPos * 3, 255 - wheelPos * 3)
	else:
		wheelPos -= 170;
		return (wheelPos * 3, 255 - wheelPos * 3, 0)

def translate(value, leftMin, leftMax, rightMin, rightMax):
	if value > leftMax:
		return rightMax

	if value < leftMin:
		return rightMin

	# Figure out how 'wide' each range is
	leftSpan = leftMax - leftMin
	rightSpan = rightMax - rightMin
	# Convert the left range into a 0-1 range (float)
	valueScaled = float(value - leftMin) / float(leftSpan)
	# Convert the 0-1 range into a value in the right range.
	return rightMin + (valueScaled * rightSpan)
