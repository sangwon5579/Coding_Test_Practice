#include <string>
#include <vector>

using namespace std;



void dfs(vector<int> numbers, int target,  int num, int sum, int& answer){    
    if(num == numbers.size()){
        
        if(sum == target){
            answer+=1;
        }
        return;
    }
    
    dfs(numbers, target, num +1, sum + numbers[num], answer);
    dfs(numbers, target, num+1, sum - numbers[num], answer);
    
}



int solution(vector<int> numbers, int target) {
    int answer = 0;

    dfs(numbers, target, 0, 0, answer);
    return answer;
}