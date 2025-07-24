class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        for(int idx = 0; idx < code.length(); idx++){
            if(mode == 0){
                if(code.charAt(idx) == '1'){ mode = 1;}
                else{if(idx % 2 == 0){answer += code.charAt(idx);}}
            }
            else{
                if(code.charAt(idx) == '1'){mode = 0;}
                else{if(idx % 2 != 0){answer += code.charAt(idx);}}
            }          
        }
        if(answer.equals("")){
            answer = "EMPTY";
        }
        return answer;
    }
}