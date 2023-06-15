#include <iostream>
#include <vector>

int main() {
    bool solution = true;
    int m, n, cost, numberOfRow;
    std::cin >> m >> n;
    cost = n;
    numberOfRow = n + 1;

    std::vector<int> result(m);
    std::vector<std::vector<double> > elements(m, std::vector<double>(n + 2));
//    elements.resize(m);
//    for (int i = 0; i < m; ++i) {
//        elements[i].resize(n + 2);
//    }

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n + 1; ++j) {
            std::cin >> elements[i][j];
        }
        elements[i][numberOfRow] = i + 1;
    }

    for (int column = 0; column < n; ++column) {
        int minRow = -1;
        int minCost = 51;
        for (int row = column; row < m; ++row) {
            if (elements[row][column] != 0.0 && elements[row][cost] < minCost) {
                minRow = row;
                minCost = elements[row][cost];
            }
        }

        if (minRow == -1) {
            solution = false;
            std::cout << "-1" << std::endl;
            break;
        }

        elements[column].swap(elements[minRow]);
        result.push_back(elements[column][numberOfRow]);
        for (int row = column + 1; row < m; ++row) {
            double c = elements[row][column] / elements[column][column];
            for (int i = column; i < n; ++i) {
                elements[row][i] -= elements[column][i] * c;
            }
        }
    }

    std::sort(result.begin(), result.end());
    if (solution) {
        for (int i = 0; i < result.size(); ++i) {
            std::cout << result[i];
            if (i != result.size() - 1)
            std::cout << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}