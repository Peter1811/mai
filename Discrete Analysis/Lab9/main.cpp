//#include <bitset>
//#include <iostream>
//#include <map>
//#include <vector>
//#include <algorithm>
//
//const int MAXINT = 110004;
//std::vector<std::vector<size_t>> g;
//std::bitset<MAXINT> used;
//std::vector<size_t> mt;
//
//bool dfs(int v)
//{
//    if (used[v])
//        return false;
//    used[v] = true;
//    for (auto to : graph[v]) {
//        if (matching[to] == -1 || dfs(matching[to])){
//            matching[to] = v;
//            return true;
//        }
//    }
//    return false;
//}
//
//int main()
//{
//    size_t n, m, a, b;
//    std::cin >> n >> m;
//    g.resize(n+1);
//    for (int i = 0; i < m; ++i) {
//        std::cin >> a >> b;
//        --a;
//        --b;
//        g[a].push_back(b);
//        g[b].push_back(a);
//    }
//    mt.assign(n, -1UL);
//
//    for (size_t i = 0; i < n; ++i)
//        if (mt[i] == -1UL) {
//            used.reset();
//            dfs(i);
//        }
//
//    std::map<size_t, size_t> ans;
//    for (size_t i = 0; i < n; ++i)
//        if (mt[i] != -1UL)
//            ans[std::min(i, mt[i])] = std::max(i, mt[i]);
//
//    std::cout << ans.size() << std::endl;
//    // for (auto i : ans)
//    std::for_each(ans.begin(), ans.end(), [](const std::pair<size_t, size_t>& i){std::cout << i.first + 1 << ' ' << i.second + 1 << std::endl;});
//    return 0;
//}

//#include <bitset>
//#include <iostream>
//#include <map>
//#include <set>
//#include <vector>
//
//const int MAX = 110004;
//std::map<int, std::set<int>> graph;
//std::vector<int> matching;
//std::bitset<MAX> used;
//
//bool dfs(int v)
//{
//    if (used[v])
//        return false;
//    used[v] = true;
//    for (auto to : graph[v]) {
//        if (matching[to] == -1 || dfs(matching[to])){
//            matching[to] = v;
//            return true;
//        }
//    }
//    return false;
//}
//
//void kun(int n){
//    for(int i = 0; i<n; ++i){
//        if(matching[i] == -1){
//            used.reset();
//            dfs(i);
//        }
//    }
//}
//
//std::map<int, int> get_ans(int n){
//    std::map<int, int> ans;
//    for (int i = 0; i < n; ++i){
//        if (matching[i] != -1){
//            ans[std::min(i, matching[i])+1] = std::max(i, matching[i])+1;
//        }
//    }
//    return ans;
//}
//
//int main()
//{
//    int n, m;
//    std::cin >> n >> m;
//    int first_v, second_v;
//    for(int i = 0; i < m; ++i){
//        std::cin >> first_v >> second_v;
//        --first_v;
//        --second_v;
//        graph[first_v].insert(second_v);
//        graph[second_v].insert(first_v);
//    }
//    matching.assign(n+2, -1);
//    kun(n);
//    std::map<int, int> ans = get_ans(n);
//    std::cout << ans.size() << "\n";
//    for (auto& i : ans){
//        std::cout << i.first << " " << i.second << "\n";
//    }
//}

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