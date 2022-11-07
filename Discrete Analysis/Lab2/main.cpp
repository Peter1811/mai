#include <iostream>
#include "TTree.h"

std::string ToLower(std::string& string) {
    for (unsigned i = 0; i < string.length(); ++i) {
        string[i] = std::tolower(string[i]);
    }
    return string;
}

int main() {
    TTree MyTree;
    std::string command;
    std::string str;
    unsigned long long value;
    while (std::cin >> command) {
        if (command == "+") {
            std::cin >> str >> value;
            std::string new_str = ToLower(str);
            MyTree.InsertElement(new_str, value);
        } else if (command == "-") {
            std::cin >> str;
            std::string new_str = ToLower(str);
            MyTree.Remove(new_str);
        } else if (command == "!") {
            std::string key;
            std::cin >> key;
            if (key == "Save") {
                std::string path;
                std::cin >> path;
                MyTree.Write(path);
            } else if (key == "Load") {
                TTree copy;
                std::string path;
                std::cin >> path;
                MyTree.Clear(MyTree.GetRoot());
                MyTree.SetRoot();
                MyTree.Read(path);
            }
	        std::cout << "OK\n";
        } else {
            std::string new_str = ToLower(command);
            MyTree.SearchOfItem(new_str);
            }

        }
    MyTree.Clear(MyTree.GetRoot());
    return 0;
}