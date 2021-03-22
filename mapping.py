# 1.1 - Screenshots and savefiles manipulation

# In[2]:

import os

import matplotlib.pyplot as plt
import numpy as np
from numpy import linspace
from scipy.interpolate import griddata


def read_coords_from_screenshots(path):
    screenshots = os.listdir(path)
    screenshots = [S for S in screenshots if "screen" in S]
    coords = np.array([[int(x) for x in s[s.find("(") + 1:s.find(")")].split(",")] for s in screenshots])
    return coords


def read_coords_from_file(file_name):
    c = list()
    with open(file_name) as f:
        content = f.readlines()
        for c in content:
            s = c.split(" ")
            c.append([int(s[0]), int(s[2]), int(s[1])])
    return np.array(c)


def writeCoordsToFile(data, fileName, mode="w"):
    with open(fileName, mode) as f:
        for c in data:
            f.write(str(c[0]) + " " + str(c[2]) + " " + str(c[1]) + "\n")


def deleteScreenshots(path):
    for fileName in os.listdir(path):
        if ((".png" in fileName) and ("screen" in fileName)):
            os.remove(path + fileName)


# 1.2 - Plotting
# In[3]:


def contourPlot(data, path, save=True):
    fig = plt.figure()
    xi = linspace(min(data[:, 0]), max(data[:, 0]), 111)
    yi = linspace(min(data[:, 2]), max(data[:, 2]), 111)
    zi = griddata(data[:, 0], data[:, 2], data[:, 1], xi, yi)
    plt.contour(xi, yi, zi, 41, linewidths=0.5, colors='black')
    plt.contourf(xi, yi, zi, 82, )
    plt.colorbar()
    plt.grid(True)
    plt.set_cmap('terrain')
    if save:
        plt.savefig(path + "TM_map_contour.png", dpi=150)


def scatterPlot(data, path, save=True):
    fig = plt.figure()
    plt.scatter(data[:, 0], data[:, 2], c=data[:, 1], linewidth=0, s=40)
    plt.xlim(min(data[:, 0]), max(data[:, 0]))
    plt.ylim(min(data[:, 2]), max(data[:, 2]))
    plt.colorbar()
    plt.grid(True)
    plt.set_cmap('terrain')
    if save:
        plt.savefig(path + "TM_map_path.png", dpi=150)


# 1.3 - User routines
# In[4]:


def createMaps(sPath, fPath):
    fC = read_coords_from_file(fPath + "coords.txt")
    sC = read_coords_from_screenshots(sPath)
    coordinates = np.array([])

    if (len(fC) == 0) and (len(sC) == 0):
        print("No data to work on! Doing nothing...")
    elif len(fC) == 0:
        print("No files, but screenshots, going on...")
        coordinates = sC
        writeCoordsToFile(coordinates, fpath + "coords.txt")
        deleteScreenshots(sPath)
    elif len(sC) == 0:
        print("No screenshots, but files, going on...")
        coordinates = fC
    else:
        print("Screenshots and files! Going on...")
        coordinates = np.concatenate((fC, sC))
        writeCoordsToFile(coordinates, fPath + "coords.txt")
        deleteScreenshots(sPath)

    contourPlot(coordinates, fPath)
    scatterPlot(coordinates, fPath)


def checkFile(fileName):
    fC = read_coords_from_file(fileName)
    coordinates = np.array([])
    if len(fC) == 0:
        print("No data to work on! Doing nothing...")
    else:
        print("No screenshots, but a file, going on...")
        print("Number of points in the file = ", len(coordinates))
        coordinates = fC
    contourPlot(coordinates, " ", save=False)
    scatterPlot(coordinates, " ", save=False)
