1class Solution {
2    public boolean checkPowersOfThree(int n) {
3        while(n != 1){
4            if(n%3>1) return false;
5            n = n/3;
6        }
7        return true;
8    }
9}