class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        int len_ms = my_string.length();
        int len_os = overwrite_string.length();
        for(int i = 0; i < s; i++){
            answer += my_string.charAt(i);
        }
        answer += overwrite_string;
        int len = s + len_os;
        if(len_ms > len){
            for(int j = 0; j < (len_ms - len);j++){
                int k = j + len;
                answer += my_string.charAt(k);
            }
        }
        return answer;
    }
}