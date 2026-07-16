#include<vector>
#include<queue>

using namespace std;

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    int n = maps.size();
    int m = maps[0].size();
    
    queue<pair<int, int>> q;
    q.push({0, 0});
    
    while(true){
        if(q.empty()){
            break;
        }
        int row = q.front().first;
        int col = q.front().second;
        
        q.pop();
        
        int upRow = row - 1;
        int upCol = col;
        int downRow = row + 1;
        int downCol = col;
        int leftRow = row;
        int leftCol = col - 1;
        int rightRow = row;
        int rightCol = col + 1;
        
        if(upRow >= 0){
            if(maps[upRow][upCol] == 1){
                maps[upRow][upCol] = maps[row][col] + 1;
                q.push({upRow, upCol});
            }
        }
        
        if(downRow < n){
            if(maps[downRow][downCol] == 1){
                maps[downRow][downCol] = maps[row][col] + 1;
                q.push({downRow, downCol});
            }
        }
        
        if(leftCol>=0){
            if(maps[leftRow][leftCol] == 1){
                maps[leftRow][leftCol] = maps[row][col] + 1;
                q.push({leftRow, leftCol});
            }
        }
        
        if(rightCol < m){
            if(maps[rightRow][rightCol] == 1){
                maps[rightRow][rightCol] = maps[row][col] + 1;
                q.push({rightRow, rightCol});
            }
        }    
        
    }
    if(maps[n-1][m-1] == 1){
        answer = -1;
    }
    else{
        answer = maps[n-1][m-1];
   }
    
    return answer;
}