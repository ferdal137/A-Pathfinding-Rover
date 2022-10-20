# A* search algorithm for the autonomous mission of University Rover Challenge

<div align="center"><img src="https://c.tenor.com/byI653FuZcEAAAAC/mars-rover.gif" width="498" height="292" /></div>

## How does it work?
Given n coordinates (x,y) of the location of the targets where the rover needs to be moved to, the algorithm calculates the distance to each of them and moves to the closest one; where the new starting position of the rover is established and the algorithm is repeated until the rover is at the last target

## Libraries:
<ul>
  <li>pathfinding 1.0.1</li>
  <li>pygame 2.1.2</li>
</ul>

## Map
The map actually consists of an array of zeros and ones where each zero is a coordinate the rover cannot pass.
Only one image was overlaid on top of the matrix to show the map in the game window.

## Chance the targets
To change the coordinates of the objectives or add more, you must change the list called <b>objectives</b> at the beginning of the code as well as the list called <b>points</b> in the <b>create_path</b> function.

As well as you can change the coordinate of the initial position in start at the beginning of the code and starts in the create_path function
