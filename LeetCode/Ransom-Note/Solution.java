1class Solution {
2    public boolean canConstruct(String ransomNote, String magazine) {
3        int ranInd;
4        int magInd;
5        int[] freqRan = new int[26];
6        int[] freqMag = new int[26];
7
8        for(ranInd = 0; ranInd < ransomNote.length(); ranInd++)
9        {
10            char ch = ransomNote.charAt(ranInd);
11            freqRan[ch - 'a']++;
12        }
13
14        for(magInd= 0; magInd < magazine.length(); magInd++)
15        {
16            char ch = magazine.charAt(magInd);
17            freqMag[ch - 'a']++;
18        }
19
20        int c1;
21        int c2;
22        for(ranInd = 0 ; ranInd < ransomNote.length() ; ranInd++)
23        {
24            char ch = ransomNote.charAt(ranInd);
25            c1 = freqRan[ch-'a'];
26            c2 = freqMag[ch-'a'];
27            if(c2 >= c1){
28                continue;
29            }
30            else{
31                return false;
32            }
33        }
34        return true;
35    }
36}