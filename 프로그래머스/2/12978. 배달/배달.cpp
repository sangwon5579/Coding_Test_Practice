#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>

using namespace std;

const int INF = INT_MAX / 2;

int nodeCount;
int start = 1;
int dist[51];
int map[51][51];
bool visited[51];

int find_short(){
    int minDist, minIdx;
    
    minDist = INF;
    minIdx = -1;
    
    for(int i = 1; i <= nodeCount; i++){
        if(visited[i] == true){
            continue;
        }
        if(dist[i] < minDist){
            minDist = dist[i];
            minIdx = i;
        }
    }
    return minIdx;
}

void dijkstra(){
    for(int i = 1; i <= nodeCount; i++){
        dist[i] = map[start][i];
    }
    
    dist[start] = 0;
    visited[start] = true;
    
    for(int i = 0; i < nodeCount -1 ; i++){
        int newNode = find_short();
        
        if(newNode == -1){
            break;
        }
        
        visited[newNode] = true;
        
        for(int j = 1; j<=nodeCount; j++){
            if(visited[j] == true){
                continue;
            }
            if(dist[j] > dist[newNode] + map[newNode][j]){
                dist[j] = dist[newNode] + map[newNode][j];
            }
        }
    }
}

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;
    nodeCount = N;
    for(int i = 1; i <= N; i++){
        visited[i] = false;
        
        for(int j = 1; j<= N;j++){
            map[i][j] = INF;
        }
        map[i][i] = 0;
    }

    
    // 도로 정보 저장
    for (int i = 0; i < road.size(); i++) {
        int a = road[i][0];
        int b = road[i][1];
        int cost = road[i][2];

        // 같은 두 마을 사이에 여러 도로가 있을 수 있음
        map[a][b] = min(map[a][b], cost);
        map[b][a] = min(map[b][a], cost);
    }

    dijkstra();

    // K 시간 이하인 마을 개수 계산
    for (int i = 1; i <= N; i++) {
        if (dist[i] <= K) {
            answer++;
        }
    }

    return answer;
}

