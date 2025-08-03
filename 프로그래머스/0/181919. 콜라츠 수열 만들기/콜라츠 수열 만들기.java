import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        List<Integer> answer = new ArrayList<>();
        answer.add(n);
        while(true){
            if(n == 1){
                break;
            }else if(n%2==0){
                n = n/2;
                answer.add(n);
            }else{
                n = 3 * n + 1;
                answer.add(n);
            }
        }
        return answer.stream().mapToInt(Integer :: intValue).toArray();
    }
}