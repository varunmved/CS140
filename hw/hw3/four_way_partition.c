#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

bool contains(int mat[4][4], int N, int target, int &row, int &col);
bool contains(int mat[4][4], int M, int N, int target, int l, int u, int r, int d, int &targetRow, int &targetCol);

bool contains(int mat[4][4], int M, int N, int target, int l, int u, int r, int d, int &targetRow, int &targetCol) 
{
  if (l > r || u > d) return false;
  if (target < mat[u][l] || target > mat[d][r]) return false;
  int col = l + (r-l)/2;
  int row = u + (d-u)/2;
  if (mat[row][col] == target) {
    targetRow = row;
    targetCol = col;
    return true;
  } else if (l == r && u == d) {
    return false;
  }
  if (mat[row][col] > target) {
    return contains(mat, M, N, target, col+1, u, r, row, targetRow, targetCol) || 
           contains(mat, M, N, target, l, row+1, col, d, targetRow, targetCol) ||
           contains(mat, M, N, target, l, u, col, row, targetRow, targetCol);
  } else {
    return contains(mat, M, N, target, col+1, u, r, row, targetRow, targetCol) || 
           contains(mat, M, N, target, l, row+1, col, d, targetRow, targetCol) ||
           contains(mat, M, N, target, col+1, row+1, r, d, targetRow, targetCol);
  }
}
 
bool contains(int mat[4][4], int N, int target, int &row, int &col) {
  return contains(mat, N, N, target, 0, 0, N-1, N-1, row, col);
}

int main()
{
   
   int mat[4][4] = { {10, 20, 30, 40},{15, 25, 35, 45}, {27, 29, 37, 48},{32, 33, 39, 50}};
    int N_MAX = 4; 
   int M = 4;
   int N = 4;
   int target = 25;
   int row = 1;
   int col = 1;
    
   bool val = false;
   val = contains(mat[4][4],N,target,&row,&col);
   return val;
}
