#!/usr/bin/python3

PUNKTE={
    "X": [5, -5],
    "Y": [-0.5, 7.5]
}


def y_gesamt(Y):
    if Y[0] > Y[1]:
        Y_GSM=Y[0]-Y[1]
        GRAPH="Fallender"
    elif Y[0] < Y[1]:
        GRAPH="Steigender"
        Y_GSM=Y[1]-Y[0]
    else:
        GRAPH="Bleibender"
        Y_GSM=0
    return [Y_GSM, GRAPH]


def x_gesamt(X):
    if X[0] > X[1]:
        X_GSM=X[0]-X[1]
    elif X[0] < X[1]:
        X_GSM=X[1]-X[0]
    else:
        X_GSM=0

    return X_GSM


XGMT=x_gesamt(PUNKTE["X"])
YGSMT=y_gesamt(PUNKTE["Y"])
STEIGUNG=YGSMT[0]/XGMT
#print("Steigung: " + str(STEIGUNG))
print(YGSMT[1] + " Graph")

B=PUNKTE["Y"][0]+((0-PUNKTE["X"][0])*STEIGUNG)

print ("f(x) = " + str(STEIGUNG) + "x + " + str(B))
