#!/usr/bin/python3
""" print linare function """
import sys
import matplotlib.pyplot as plt

try:
    sys.argv[1:]
except:
    print("missing arguments: \"1x|1y 2x|2y\"")


PUNKTE = {}
PUNKTE["X"] = []
PUNKTE["Y"] = []


for werte in sys.argv[1:][0].split():
    WERT = werte.split("|")
    PUNKTE["X"].append(float(WERT[0]))
    PUNKTE["Y"].append(float(WERT[1]))


def steigung(punkte):
    """ steigung ermitteln """
    m = abs(punkte["Y"][0] - punkte["Y"][1]) / abs(punkte["X"][0] - punkte["X"][1])

    if (punkte["X"][0] < punkte["X"][1] and punkte["Y"][0] < punkte["Y"][1]) or (punkte["X"][0] > punkte["X"][1] and punkte["Y"][0] > punkte["Y"][1]):
        return ["steigenger Graph", M]
    elif punkte["X"][0] == punkte["X"][1] and punkte["Y"] != punkte["Y"]:
        return ["gleichbleibender Graph", 0]
    else:
        return ["fallender Graph", M*-1]

def isint(wert):
    """ prüft ob wert float oder int ist """
    if str(wert).endswith(".0"):
        return int(wert)
    else:
        return float(wert)

M = steigung(PUNKTE)

print("")
print("Graph:")
print(M[0])

B = PUNKTE["Y"][0] + (0-PUNKTE["X"][0])*M[1]

print("")
print("lineare Funktion:")
print("f(x) = " + str(isint(M[1])) + "x + " + str(isint(B)))
print("")

fig, axs = plt.subplots()
axs.plot(PUNKTE["X"], PUNKTE["Y"], 'o-', label="f(x) = " + str(isint(M[1])) + "x + " + str(isint(B)))
axs.axis([-20, 20, -20, 20])

axs.hlines(0, -20, 20)
axs.vlines(0, -20, 20)
axs.grid(True)

axs.legend()
# The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies
# the viewport of the axes.

plt.xlabel("x") # Text for X-Axis
plt.ylabel("y") # Text for Y-Axis
plt.suptitle("Lineare Funktion")
plt.show()
