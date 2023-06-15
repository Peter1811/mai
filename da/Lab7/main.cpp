#include <iostream>
#include <string>

int main() {

    long long n, m, lower = 1, upper = 0, result = 0;
    std::cin >> n >> m;
    std::string number = std::to_string(n);
    long long length = number.size();

    for (long long i = 0; i < length; ++i) {
        upper = upper * 10 + (long long)number[i] - (long long)'0';
        long long left = lower + (m - lower % m) % m;
        long long right = upper - upper % m;
        if (left <= right) {
            result += (right - left) / m + 1;
        }
        lower *= 10;
    }

    if (!(n % m)) {
        --result;
    }
    std::cout << result << "\n";
    return 0;
}
