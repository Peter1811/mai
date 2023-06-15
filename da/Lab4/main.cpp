#include <iostream>
#include <string>
#include <vector>
#include <ios>
#include <algorithm>



std::vector<unsigned > ZFunction(std::string &string) {



    int n = (int) string.length();
    std::vector<unsigned > result (n);
    result[0] = n;
    for (int i = 1, l = 0, r = 0; i < n; ++i) {
        if (i <= r) {
            result[i] = std::min(r - i + 1, (int) result[i - l]);
        }
        while (i + result[i] < n && string[result[i]] == string[i + result[i]]) {
            ++result[i];
        }
        if (i + result[i] - 1 > r) {
            l = i;
            r = i + result[i] - 1;
        }
    }

    return result;
}

int main() {

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    std::string pattern;
    std::string text;

    std::cin >> text >> pattern;
    std::string s = pattern + '#' + text;
    std::vector<unsigned > Z = ZFunction(s);
    for (int i = (int)pattern.length(); i < Z.size(); ++i) {
        if (Z[i] == pattern.length()) {
            std::cout << i - (pattern.length() + 1) << "\n";
        }
    }
    return 0;
}
