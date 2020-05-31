#!/usr/bin/python3
""" print linare function """
import sys
import matplotlib.pyplot as plt

try:
  sys.argv[1:]
except:
  print("missing arguments: \"1x|1y 2x|2y\"")


PUNKTE      = {}
PUNKTE["X"] = []
PUNKTE["Y"] = []


for werte in sys.argv[1:][0].split():
  WERT=werte.split("|")
  PUNKTE["X"].append(float(WERT[0]))
  PUNKTE["Y"].append(float(WERT[1]))


def steigung(PUNKTE):
  M=abs(PUNKTE["Y"][0] - PUNKTE["Y"][1]) / abs(PUNKTE["X"][0] - PUNKTE["X"][1])

  if (PUNKTE["X"][0] < PUNKTE["X"][1] and PUNKTE["Y"][0] < PUNKTE["Y"][1]) or (PUNKTE["X"][0] > PUNKTE["X"][1] and PUNKTE["Y"][0] > PUNKTE["Y"][1]):
    return ["steigenger Graph",M]
  elif PUNKTE["X"][0] == PUNKTE["X"][1] and PUNKTE["Y"] != PUNKTE["Y"]:
    return ["gleichbleibender Graph",0]
  else:
    return ["fallender Graph",M*-1]


def isInt(WERT):
  if str(WERT).endswith(".0"):
    return int(WERT)
  else:
    return float(WERT)

M = steigung(PUNKTE)

print("")
print("Graph:")
print(M[0])

B = PUNKTE["Y"][0] + (0-PUNKTE["X"][0])*M[1]

print("")
print("lineare Funktion:")
print("f(x) = " + str(isInt(M[1])) + "x + " + str(isInt(B)))
print("")

fig, axs = plt.subplots()
axs.plot(PUNKTE["X"], PUNKTE["Y"], 'o-', label="f(x) = " + str(isInt(M[1])) + "x + " + str(isInt(B)))
axs.axis([-20, 20, -20, 20])

axs.hlines(0,-20, 20)
axs.vlines(0,-20, 20)
axs.grid(True)

axs.legend()
# The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.

plt.xlabel("x") # Text for X-Axis
plt.ylabel("y") # Text for Y-Axis
plt.suptitle("Lineare Funktion")
plt.show()
