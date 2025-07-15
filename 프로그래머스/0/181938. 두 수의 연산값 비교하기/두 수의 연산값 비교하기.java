class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int num1 = 0;
        int num2 = 0;
        int len_b = (int)(Math.log10(b) + 1);
        num1 = b + (a * ((int)(Math.pow(10, len_b))));
        num2 = 2 * a * b;
        if (num1 > num2){
            answer = num1;
        }
        else{
            answer = num2;
        }
        return answer;
    }
}