#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(), people.end());
    int num = people.size();
    int small = 0;
    int big = num - 1;
    while(small<=big){
        // if(small>big){
        //     break;
        // }
        if(people[small] + people[big] <= limit){
            small++;
            big--;
            answer++;
        }
        else{
            big--;        
            answer++;
        }
        
    }
    return answer;
}


