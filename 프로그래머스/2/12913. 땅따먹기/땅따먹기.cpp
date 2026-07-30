#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int> > land)
{
    int answer = 0;

    int row = land.size();
    
    for(int i =1; i<row; i++){
        for(int j = 0; j < 4; j++){
            int maxValue = 0;
            
            for(int k = 0; k<4;k++){
                if(j==k){
                    continue;
                }
                maxValue = max(maxValue, land[i - 1][k]);

            }
            land[i][j] += maxValue;
        }        
    }
    
    for(int n = 0; n<4;n++){
        answer = max(answer, land[row-1][n]);
    }

    
    return answer;
}


