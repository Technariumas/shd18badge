#NCP18XH103F03RB resistance at temperatures [-40, 125] in 5 degree increments
resistances=[
195.652,
148.171,
113.347,
87.559,
68.237,
53.650,
42.506,
33.892,
27.219,
22.021,
17.926,
14.674,
12.081,
10.000,
8.315,
6.948,
5.834,
4.917,
4.161,
3.535,
3.014,
2.586,
2.228,
1.925,
1.669,
1.452,
1.268,
1.110,
0.974,
0.858,
0.758,
0.672,
0.596,
0.531]

temperatures=[-40, -35, -30, -25, -20, -15, -10,  -5,   0,   5,  10,  15,  20,
        25,  30,  35,  40,  45,  50,  55,  60,  65,  70,  75,  80,  85,
        90,  95, 100, 105, 110, 115, 120, 125]

lsbs=[644, 575, 507, 442, 380, 325, 276, 232, 195, 164, 137, 115,  97,
        81,  68,  58,  49,  41,  35,  30,  26,  22,  19,  16,  14,  12,
        11,   9,   8,   7,   6,   5,   5,   4]



def interpolate(val, rangeStart, rangeEnd, valStart, valEnd):
    return (rangeEnd - rangeStart) * (val - valStart) / (valEnd - valStart) + rangeStart;



def interpolateTemperature(lsb, i):
    return interpolate(lsb, temperatures[i-1], temperatures[i], lsbs[i-1], lsbs[i]);



# Returns the index of the first point whose lsb value is greater than argument
def searchLsb(lsb):
	for i, l in enumerate(lsbs):
		if lsb > l:
			return i

	return size(lsbs) - 1;


def lsbToTemperature(lsb):
	if lsb <= lsbs[-1]:
		return temperatures[-1];
	
	if lsb >= lsbs[0]:
		return temperatures[0];

	return interpolateTemperature(lsb, searchLsb(lsb))

#print (thermistorLsbToTemperature(91))	