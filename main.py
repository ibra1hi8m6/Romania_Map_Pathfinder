from tkinter import *

from algo import *

window = Tk()
window.title("CS361 Introduction to AI project - Romania Map Pathfinder")
window.geometry("700x500")

def wrapper_DFSL(graph, start, goal):
    return DFSL(start, 50, graph, goal)

algos = {
    "Depth-first Search" : DFS,
    "Limited Depth-first Search" : wrapper_DFSL,
    "Iterative Depth-first Search" : iterativeDFSL,
    "A* Search" : A_star,
}

cities = list(graph.keys())

resultLabel = Label(window, text="")

startDropdownLabel = Label(window, text="Select start city")
selectedStart = StringVar()
selectedStart.set(cities[0])
startDropdown = OptionMenu(window, selectedStart, *cities)

goalDropdownLabel = Label(window, text="Select goal city")
selectedGoal = StringVar()
selectedGoal.set(cities[0])
goalDropdown = OptionMenu(window, selectedGoal, *cities)

algoKeys = list(algos.keys())
algoDropdownLabel = Label(window, text="Select algorithm")
selectedAlgo = StringVar()
selectedAlgo.set(algoKeys[0])
algoDropdown = OptionMenu(window, selectedAlgo, *algoKeys)

def displayResult():
    path = algos[selectedAlgo.get()](graph=graph, start=selectedStart.get(), goal=selectedGoal.get())
    result = ""
    for i in path:
        result += " --> " + i[0]
    resultLabel.config(text=result)

beginBtn = Button(window, text="Begin", command=displayResult)

startDropdownLabel.pack()
startDropdown.pack()
goalDropdownLabel.pack()
goalDropdown.pack()
algoDropdownLabel.pack()
algoDropdown.pack()
beginBtn.pack()
resultLabel.pack()

window.mainloop()