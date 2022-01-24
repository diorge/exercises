// https://leetcode.com/problems/rotate-image/

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int diag = 0; diag < n / 2; diag++) {
            for (int cell = diag; cell < n - diag - 1; cell++) {
                int a = matrix[diag][cell];
                int b = matrix[cell][n - diag - 1];
                int c = matrix[n - cell - 1][diag];
                int d = matrix[n - diag - 1][n - cell - 1];
                
                matrix[diag][cell] = c;
                matrix[cell][n - diag - 1] = a;
                matrix[n - cell - 1][diag] = d;
                matrix[n - diag - 1][n - cell - 1] = b;
            }
        }
    }
}
