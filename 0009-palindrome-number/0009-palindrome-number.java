class Solution {
    public boolean isPalindrome(int x) {
        if(x<0 || (x%10==0 && x!=0) ){
            return false;
        }
        // x =121
        int mod = 0 ;
        while(x>mod){
            //x= 121
        mod =(mod*10) +  x%10;  // mod =12
        x /=10;  // x =1
        }

        return x==mod || mod/10==x;
    }
}