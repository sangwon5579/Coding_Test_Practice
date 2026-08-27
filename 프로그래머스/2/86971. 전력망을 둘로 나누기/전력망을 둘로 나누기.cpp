#include <string>
#include <vector>

using namespace std;

int dfs(int now, vector<vector<int>>& graph, vector<bool>& visited) {
    visited[now] = true;

    int count = 1;

    for (int i = 0; i<graph[now].size(); i++) {
        int next = graph[now][i];

        if (!visited[next]) {
            count += dfs(next, graph, visited);
        }
    }

    return count;
}


int solution(int n, vector<vector<int>> wires) {
    int answer = -1;
    int k = n % 2;
    
    while(true){
        int dif = (n-k)/2;
        int w = wires.size();
         
        for(int i = 0 ; i < w ; i++){
            vector<vector<int>> graph(n + 1);
            for(int j=0; j< w ; j++){
                if(i==j){
                    continue;
                }
                
                int num1 = wires[j][0];
                int num2 = wires[j][1];
                
                graph[num1].push_back(num2);
                graph[num2].push_back(num1);
                
                
            }
            vector<bool> visit(n+1, false);
            
            int count = dfs(1, graph, visit);

            if (count == dif || count == n - dif) {
                return k;
            }
        }
        k+=2;
    }
    return answer;
}
