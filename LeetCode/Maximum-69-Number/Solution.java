1class Solution {
2    public int maximum69Number (int num) {
3        int res = 0;
4        int power = 1;
5        int copy = num;
6        while(copy > 9){
7            power *= 10;
8            copy /= 10;
9        }
10        copy = num;
11        boolean six_found = false;
12        while(power != 0){
13            int digit = copy/power;
14            if(digit == 6 && six_found != true ){
15                res = res*10+9;
16                six_found = true;
17            }
18            else{
19                res = res*10+digit;
20            }
21            copy %= power;
22            power /= 10;
23        }
24        return res;
25
26    }
27}