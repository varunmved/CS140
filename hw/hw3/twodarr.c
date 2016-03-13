#include <stdio.h>

int contains(int arr[4][4], int key, int low, int high);

int main()
{
    
    int x = 4;
    int y = 4;
    int mat[4][4] = { {10, 20, 30, 40},
                    {15, 25, 35, 45},
                    {27, 29, 37, 48},
                    {32, 33, 39, 50},
                  };
    
    int low = mat[0][0];
    int high = mat[x][y];
    int key = 10; 
    
    int result = -1;
    //printf("%d",5); 
    
    result = contains(mat,key,low,high);
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            int g = mat[i][j];
            printf("%d ", g);
        }
        printf("\n");
    }
    return result;

}
/*
int contains(int arr[4][4], int key, int low, int high)
{
    if(low < 4 && high > -1)
    {
        if(arr[low][high] == key)
        {
            return 1;
        }
        else if(arr[low][high] < key)
        {
            return contains(arr,key,low+1,high);

        }
        else
        {
            return contains(arr,key,low,high+1);
        }
    }

    return 0;
}
*/

int contains(int mat[4][4], int key, int l, int r, int u, int d)
{
    if (l > r || u < d) return false;
    if (target < mat[u][l] || target > mat[d][r]) return false;

    int col = l + (

    return 0;
}





