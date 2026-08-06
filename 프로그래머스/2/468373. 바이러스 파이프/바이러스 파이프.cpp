#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

void spread(const vector<vector<int>>& edges, int type, set<int>& infected){
    bool changed = true;
    
    while(changed){
        changed = false;
        
        for(int i = 0; i < edges.size();i++){
            int x = edges[i][0];
            int y = edges[i][1];
            
            if(edges[i][2] != type){
                continue;
            }
            
            if(infected.count(x) && !infected.count(y)){
                infected.insert(y);
                changed = true;
            }
            
            if(infected.count(y) && !infected.count(x)){
                infected.insert(x);
                changed = true;
            }
        }
    }
}

void dfs(const vector<vector<int>>& edges, set<int> infected, int depth, int k, int& answer){
    answer = max(answer, (int)infected.size());

    if (depth == k)
        return;

    for (int type = 1; type <= 3; type++) {
        set<int> next = infected;

        spread(edges, type, next);

        dfs(edges, next, depth + 1, k, answer);
    }
}

int solution(int n, int infection, vector<vector<int>> edges, int k) {
    int answer = 0;
    
   set<int> infected;
    infected.insert(infection);

    dfs(edges, infected, 0, k, answer);

    
    
    
    return answer;
}


