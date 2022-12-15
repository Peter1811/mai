#include <iostream>
#include <algorithm>
#include <vector>

bool dfs(std::vector<std::vector<int>> &list, int from,
         std::vector<bool> &used, std::vector<int> &matching) {
    if (used[from])
        return false;
    used[from] = true;

    for (int i = 0; i < list[from].size(); ++i) {
        int to = list[from][i];
        if (matching[to] == -1 || dfs(list, matching[to], used, matching)) {
            matching[to] = from;
            matching[from] = to;
            return true;
        }
    }

    return false;
}


int main() {
    int n, m, count = 0;

    std::cin >> n >> m;

    std::vector<std::vector<int>> list(n);
    std::vector<int> matching(n, -1);
    std::vector<bool> used(n);

    for (int k = 0; k < m; ++k) {
        int i, j;
        std::cin >> i >> j;
//        i = 3, j = 4;
        list[i - 1].push_back(j - 1);
        list[j - 1].push_back(i - 1);
    }

    for (int k = 0; k < n; ++k) {
        std::sort(list[k].begin(), list[k].end());
    }

    for (int i = 0; i < n; ++i) {
        if (matching[i] == -1) {
            std::fill(used.begin(), used.end(), false);
            dfs(list, i, used, matching);
        }
    }


    for (int i = 0; i < n; ++i) {
        if (matching[i] > i)
            count++;
    }
    std::cout << count << '\n';

    for (int i = 0; i < n; ++i) {
        if (matching[i] > i)
            std::cout << i + 1 << ' ' << matching[i] + 1 << '\n';
    }

    return 0;
}
