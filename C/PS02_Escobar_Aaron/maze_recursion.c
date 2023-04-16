#include <stdbool.h>
#include "maze.h"

bool solveMaze(int i, int j) {
     if (grid[i][j] == END_MARKER){
          return true;
     }
     if (grid[i][j] == VISITED_MARKER){
          return false;
     }
     if (grid[i][j] == WALL_MARKER || 
          (i|j) < 0 || i > DIM_I || j > DIM_J){
          return false;
     }
     grid[i][j] = VISITED_MARKER;
     display();

     if (solveMaze(i-1, j) || 
          solveMaze(i+1, j) || solveMaze(i, j-1) || solveMaze(i, j+1)) {
          
          grid[i][j] = SOLUTION_MARKER;
          display();
          return true;
     }
     else {
          return false;
     }
}
