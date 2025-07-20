import java.util.ArrayList;
import java.util.*; 

class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        ArrayList<Integer> answer1_list = new ArrayList<>();
        ArrayList<Integer> answer2_list = new ArrayList<>();
        int answer1 = 0;
        int answer2 = 0;
        for(int i = 0; i < num_list.length; i++){
            if(num_list[i] % 2 == 0){
                answer1_list.add(num_list[i]);
            }
            else{
                answer2_list.add(num_list[i]);
            }
        }
        
        int len1 = (int) ( answer1_list.size() - 1);
        for(int j = 0; j < answer1_list.size(); j++){
            int num1 = 1;
            for(int k = 0; k < j; k++){
                num1 *= 10;
            }
            answer1 += (num1 * answer1_list.get(len1 - j));
        }
        int len2 = (int) ( answer2_list.size() - 1);
        for(int j = 0; j < answer2_list.size(); j++){
            int num2 = 1;
            for(int k = 0; k < j; k++){
                num2 *= 10;
            }
            answer2 += (num2 * answer2_list.get(len2 - j));
        }
        answer = answer1 + answer2;
        return answer;
    }
}