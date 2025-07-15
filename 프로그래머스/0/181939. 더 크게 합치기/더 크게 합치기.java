class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int len_a = (int)(Math.log10(a)+1);
        int len_b = (int)(Math.log10(b)+1);
        int len = len_a + len_b;
        int num1 = 0;
        int num2 = 0;
        for(int i = 0; i < len ; i++){
            num1 = a + (b *(int) (Math.pow(10, len_a)));
        }
        for(int j = 0; j < len ; j++){
            num2 = b + (a *(int) (Math.pow(10, len_b)));
        }
        if(num1 > num2){
            answer = num1;
        }
        else{
            answer = num2;
        }
        return answer;
    }
}