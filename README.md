# Rope Intranet Code Jam
Solution to rope intranet puzzle from [google code jam round 1C 2010](https://code.google.com/codejam/contest/619102/dashboard)

##The problem
A company is located in two very tall buildings. The company intranet connecting the buildings consists of many wires, each connecting a window on the first building to a window on the second building.

You are looking at those buildings from the side, so that one of the buildings is to the left and one is to the right. The windows on the left building are seen as points on its right wall, and the windows on the right building are seen as points on its left wall. Wires are straight segments connecting a window on the left building to a window on the right building.

![Problem image][problem]

[problem]: /rope-intranet-diagram.png "Problem Image"

You've noticed that no two wires share an endpoint (in other words, there's at most one wire going out of each window). However, from your viewpoint, some of the wires intersect midway. You've also noticed that exactly two wires meet at each intersection point.

On the above picture, the intersection points are the black circles, while the windows are the white circles.

How many intersection points do you see?

##Solution theory
The script interactively checks for intersections between each rope and a dynamic list of ropes which initially contains only the first rope, then after a rope is checked for intersections with each rope in the dynamic list of ropes, its added to the dynamic list. Thus each rope is checked for intersections with each other rope only once.

##Usage
To use the solution: run the python script from a terminal passing it the name of the input file followed by the desired name of the output file.   

```
User$ python rope-intranet.py C-small-practice.in small-output.out
```
