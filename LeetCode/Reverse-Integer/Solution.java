1class Solution {
2    public int reverse(int x) {
3        int temp = 0;
4        if(x<0){
5            temp = -(x);
6        }
7        else{
8            temp = x;
9        }
10        long rev = 0;
11        while(temp > 0){
12            int rem = temp%10;
13            rev = (rev*10)+rem;
14            if(rev>2147483647){
15                return 0;
16            }
17            temp = temp/10;
18        }
19        int res = (int) rev;
20        if(x<0){
21            return -(res);
22        }
23        return res;
24    }
25}