#include <string>
#include <vector>

using namespace std;

// 연결된 송전탑 개수 
int dfs(int now, vector<vector<int>>& graph, vector<bool>& visit) {
    visit[now] = true;

    int count = 1;

    for (int i = 0; i<graph[now].size(); i++) {
        int next = graph[now][i];

        if (!visit[next]) {
            count += dfs(next, graph, visit);
        }
    }

    return count;
}


int solution(int n, vector<vector<int>> wires) {
    int answer = -1;
    // 짝수홀수
    int k = n % 2;
    
    while(true){
        //차이 
        int dif = (n-k)/2;
        int w = wires.size();
         
        // 전선 하나씩 끊기 
        for(int i = 0 ; i < w ; i++){
            vector<vector<int>> graph(n + 1);
            
            // 안 끊은 걸로 그래프 구성 
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

            //개수가 k랑 같으면 리턴 
            if (count == dif || count == n - dif) {
                answer = k;
                return answer;
            }
        }
        k+=2;
    }
}
