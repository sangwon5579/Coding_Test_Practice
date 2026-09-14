#include <string>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;

    vector<int> all;

    for (int i = 1; i < n; i++) {
        all.push_back(i);
    }

    vector<int> connected = {0};

    while (!all.empty()) {
        int minCost = INT_MAX;
        int selectedIsland = -1;

        for (int i = 0; i < costs.size(); i++) {
            int a = costs[i][0];
            int b = costs[i][1];
            int cost = costs[i][2];

            bool aConnected =
                find(connected.begin(), connected.end(), a)
                != connected.end();

            bool bConnected =
                find(connected.begin(), connected.end(), b)
                != connected.end();

            // a는 연결되어 있고 b는 연결되지 않음
            if (aConnected && !bConnected && cost < minCost) {
                minCost = cost;
                selectedIsland = b;
            }

            // b는 연결되어 있고 a는 연결되지 않음
            if (bConnected && !aConnected && cost < minCost) {
                minCost = cost;
                selectedIsland = a;
            }
        }

        answer += minCost;
        connected.push_back(selectedIsland);

        all.erase(
            remove(all.begin(), all.end(), selectedIsland),
            all.end()
        );
    }

    return answer;
}