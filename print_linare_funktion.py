#!/usr/bin/python3

import matplotlib.pyplot as plt

PUNKTE={
    "X": [1, 5],
    "Y": [9, 3]
}
#PUNKTE={
#    "X": [-1, 3],
#    "Y": [5, -7]
#}


def steigung(PUNKTE):
  M=abs(PUNKTE["Y"][0] - PUNKTE["Y"][1]) / abs(PUNKTE["X"][0] - PUNKTE["X"][1])

  if (PUNKTE["X"][0] < PUNKTE["X"][1] and PUNKTE["Y"][0] < PUNKTE["Y"][1]) or (PUNKTE["X"][0] > PUNKTE["X"][1] and PUNKTE["Y"][0] > PUNKTE["Y"][1]):
    return ["steigenger Graph",M]
  elif PUNKTE["X"][0] == PUNKTE["X"][1] and PUNKTE["Y"] != PUNKTE["Y"]:
    return ["gleichbleibender Graph",0]
  else:
    return ["fallender Graph",M*-1]


fig, axs = plt.subplots()
axs.plot(PUNKTE["X"], PUNKTE["Y"])
axs.hlines(0,-10, 10)
axs.vlines(0,-10, 10)
plt.grid(True)
# The axis() command in the example above takes a list of [xmin, xmax, ymin, ymax] and specifies the viewport of the axes.
axs.axis([-10, 10, -10, 10])


M=steigung(PUNKTE)

print("")
print("Graph:")
print(M[0])

B=PUNKTE["Y"][0] + (0-PUNKTE["X"][0])*M[1]

print("")
print("lineare Funktion:")
print ("f(x) = " + str(M[1]) + "x + " + str(B))
print("")

fig.suptitle("f(x) = " + str(M[1]) + "x + " + str(B))
plt.show()
