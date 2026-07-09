#include <string>
#include <vector>

using namespace std;


int solution(int n) {
    int answer = 0;
    vector<char> isPrime(n+1 , 1);
    isPrime[0] = 0;
    isPrime[1] = 0;
    for(int i = 2; i*i <= n; i++){
        if(isPrime[i]){
            for(int j = i*i; j <= n; j+=i){
                isPrime[j] = 0;
            }
        }
    }
    
    
    for(int a = 2 ; a <= n; a++){
        if(isPrime[a]){
            answer++;
        }
    }
    return answer;
}
