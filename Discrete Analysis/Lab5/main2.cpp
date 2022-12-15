#include <iostream>
#include <map>
const std:: string SENTINEL = "$";
const int DEFAULT_VALUE = -1;
namespace SuffixTree {
    struct TNode {
        TNode* suffix_link;
        int start;
        int *end;
        std::map<char, TNode*> children;
        bool is_leaf;
        TNode (int start, int *end, bool is_leaf) {
            this->start = start;
            this->end = end;
            suffix_link = nullptr;
            this->is_leaf = is_leaf;
        }
        ~TNode() {
            for (std::map<char, TNode*>:: iterator it = children.begin(); it != children.end(); ++it) {
                delete(it->second);
            }
        }
    };
    struct Tree {
        TNode* root;
        TNode* active_node;
        TNode* last_created_node;
        int active_edge;
        int active_length;
        int suffixes_to_add;
        std::string string;
        int global_end;
        Tree (std::string input) {
            root = new TNode (DEFAULT_VALUE, new int(DEFAULT_VALUE), false);
            active_node = root;
            string = input;
            global_end = DEFAULT_VALUE;
            active_edge = DEFAULT_VALUE;
            active_length = 0;
            suffixes_to_add = 0;
        }
        void UkkonenAlgorithm (int text_position) {
            last_created_node = nullptr;
            ++suffixes_to_add;
            ++global_end; //
            while (suffixes_to_add > 0) {
                if (active_length == 0) {
                    active_edge = text_position;
                }
                if (!active_node->children[string[active_edge]]) {
                    active_node->children[string[active_edge]] = new TNode(text_position, &global_end, true);
                    if (last_created_node != nullptr) {
                        last_created_node->suffix_link = active_node;
                        last_created_node = nullptr;
                    }
                }
                else {
                    TNode* next_node = active_node->children[string[active_edge]];
                    int edge_length = *(next_node->end) - next_node->start + 1;
                    if (active_length >= edge_length) {
                        active_edge += edge_length;
                        active_length -= edge_length;
                        active_node = next_node;
                        continue;
                    }
                    if (string[next_node->start + active_length] == string[text_position]) {//If a newly created node waiting for it's suffix link to be set, then set suffix link of that waiting node to current active node
                        if (last_created_node != nullptr) {
                            last_created_node->suffix_link = active_node;
                            last_created_node = nullptr;
                        }
                        ++active_length;
                        break;
                    }
                    TNode* to_add = new TNode(next_node->start, new int(next_node->start + active_length - 1), false);
                    active_node->children[string[active_edge]] = to_add;
                    next_node->start += active_length;
                    std::pair <char, TNode*> first = std:: make_pair(string[text_position], new TNode(text_position, &global_end, true));
                    std::pair <char, TNode*> second = std:: make_pair(string[next_node->start], next_node);
                    to_add->children.insert(first);
                    to_add->children.insert(second);
                    if (last_created_node != nullptr) {
                        last_created_node->suffix_link = to_add;
                    }
                    last_created_node = to_add;
                }
                --suffixes_to_add;
                if (active_node == root && active_length > 0) {
                    ++active_edge;
                    --active_length;
                }
                else if (active_node != root) {
                    active_node = active_node->suffix_link;
                }
            }
        }
        std::string MinimalLineCut() {
            std::string result_string = "";
            int length = (string.size() - 1) / 2;
            TNode* next = root;
            while (result_string.size() < length) {
                std::map<char, TNode*>:: iterator it = next->children.begin();
                if (it->first == '$') {
                    ++it;
                }
                next = it->second;
                for (int i = next->start; i <= *(next->end); ++i) {
                    result_string += string[i];
                    if (result_string.size() == length) {
                        break;
                    }
                }
            }
            return result_string;
        }
        ~Tree() {
            delete root;
        }
    };
}

int main() {
    std::string input;
    std::cin >> input;
    input = input + input + SENTINEL;
    SuffixTree:: Tree* tree = new SuffixTree::Tree(input);
    for (int i = 0; i < input.size(); ++i) {
        tree->UkkonenAlgorithm(i);
    }
    std::string answer = tree->MinimalLineCut();
    std::cout << answer << "\n";
    delete tree;
    return 0;
}