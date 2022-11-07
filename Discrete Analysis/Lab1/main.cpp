#include <iostream>
#include <vector>
#include <string>
#include <ios>

#include "TRadixSort.h"



int main() {

    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    std::vector <KeyValue*> input;
    std::string key;
    unsigned long long value;

    while (std::cin >> key >> value) {
        auto position1 = (short) key.find('.');
        auto position2 = (short) key.find('.', position1 + 1);
        int day = std::stoi(key.substr(0, position1));
        int month = std::stoi(key.substr(position1 + 1, position2));
        int year = std::stoi(key.substr(position2 + 1));
        KeyValue* element = new KeyValue(day, month, year, key, value);
        input.push_back(element);
    }

    TRadixSort::RadixSort(input);

    for (KeyValue *item: input) {
        std::cout << item->key << "\t" << item->value << "\n";
    }

    for (int k = 0; k < input.size(); ++k) {
        delete input[k];
    }

    return 0;
}