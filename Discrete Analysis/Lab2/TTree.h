#include "TItemOfTree.h"
#include <iostream>
#include <fstream>

class TTree {
private:
	TItemOfTree* root;
public:
	TTree() {
		root = nullptr;
	}

	void SetRoot() {
		root = nullptr;
	}

	void SearchOfItem(std::string key) {
		if (!root) {
			std::cout << "NoSuchWord\n";
			return;
		}
		TItemOfTree* result = Search(root, key);
		if (!result) {
			std::cout << "NoSuchWord\n";
		}
		else {
			std::cout << "OK: " << result->GetValue() << "\n";
		}
	}

	void Balance(TItemOfTree* item, bool flag) {
		short balance = item->GetBalance();
		while ((item) && (((flag) && (balance != 0)) || ((!flag) && ((balance == -2) || (!balance) || (balance == 2))))) {
			if ((item) && ((balance >= -1) && (balance <= 1))) {
				TItemOfTree* parent = item->GetParent();
				if (parent) {
					if (((flag) && (parent->GetLeft() == item)) || ((!flag) && (parent->GetRight() == item))) {
						parent->SetBalance(parent->GetBalance() + 1);
					} else if (((!flag) && (parent->GetLeft() == item)) || ((flag) && (parent->GetRight() == item))) {
						parent->SetBalance(parent->GetBalance() - 1);
					}
				}
				item = parent;
				if (item) {
					balance = item->GetBalance();
				}
			} else if (balance == 2) {
				TItemOfTree* left = item->GetLeft();
				short left_balance = left->GetBalance();
				if (left_balance >= 0) {
					if (left_balance == 1) {
						item->SetBalance(0);
						left->SetBalance(0);
						balance = 0;
					} else {
						item->SetBalance(1);
						left->SetBalance(-1);
						balance = -1;
					}

				} else {
					TItemOfTree* right = left->GetRight();
					short right_balance = right->GetBalance();
					balance = 0;
					if (right_balance == -1) {
						item->SetBalance(0);
						left->SetBalance(1);
					} else if (!right_balance) {
						item->SetBalance(0);
						left->SetBalance(0);
					} else {
						item->SetBalance(-1);
						left->SetBalance(0);
					}
					right->SetBalance(0);
					RotateLeft(left);
				}
				RotateRight(item);
				item = item->GetParent();
			} else {
				TItemOfTree* right = item->GetRight();
				short right_balance = right->GetBalance();
				if (right_balance <= 0) {
					if (right_balance == -1) {
						item->SetBalance(0);
						right->SetBalance(0);
						balance = 0;
					} else {
						item->SetBalance(-1);
						right->SetBalance(1);
						balance = 1;
					}
				} else {
					TItemOfTree* left = right->GetLeft();
					short left_balance = left->GetBalance();
					balance = 0;
					if (left_balance == -1) {
						item->SetBalance(1);
						right->SetBalance(0);
					} else if (!left_balance) {
						item->SetBalance(0);
						right->SetBalance(0);
					} else {
						item->SetBalance(0);
						right->SetBalance(-1);
					}
					left->SetBalance(0);
					RotateRight(right);
				}
				RotateLeft(item);
				item = item->GetParent();
			}
		}
		std::cout << "OK\n";
	}


	void Read(std::string path) {
		std::ifstream infile(path, std::ios::binary);
		char first_symbol;
		infile.read((char*)(&first_symbol), sizeof(char));
		if (first_symbol == '#') {
			root = nullptr;
		} else if (first_symbol == '|') {
			std::string key;
			short balance, length;
			unsigned long long value;
			infile.read((char*)(&balance), sizeof(short));
			infile.read((char*)(&value), sizeof(unsigned long long));
			infile.read((char*)(&length), sizeof(short));
			char* buffer = new char[length + 1];
			infile.read(buffer, length);
			buffer[length] = '\0';
			root = new TItemOfTree(std::string(buffer), value, nullptr);
			root->SetBalance(balance);
			delete[] buffer;
			ReadFromFile(root, infile, true);
			ReadFromFile(root, infile, false);
		}
		infile.close();
	}

	void ReadFromFile(TItemOfTree* parent, std::ifstream& infile, bool left) {
		char first_symbol;
		infile.read((char*)(&first_symbol), sizeof(char));
		if (first_symbol == '#') {
			return;
		}
		else if (first_symbol == '|') {
			std::string key;
			short balance, length;
			unsigned long long value;
			infile.read((char*)(&balance), sizeof(short));
			infile.read((char*)(&value), sizeof(unsigned long long));
			infile.read((char*)(&length), sizeof(short));
			char* buffer = new char[length + 1];
			infile.read(buffer, length);
			buffer[length] = '\0';
			TItemOfTree* item = new TItemOfTree(std::string(buffer), value, parent);
			item->SetBalance(balance);
			if (left) {
				parent->SetLeft(item);
			}
			else {
				parent->SetRight(item);
			}
			delete[] buffer;
			ReadFromFile(item, infile, true);
			ReadFromFile(item, infile, false);
		}
	}

	void Write(std::string path) {
		std::ofstream outfile(path, std::ios::binary);
		if (!root) {
			char symbol = '#';
			outfile.write((char*)(&symbol), sizeof(char));
		}
		else {
			WriteToFile(root, outfile);
		}
		outfile.close();
	}

	void WriteToFile(TItemOfTree* item, std::ofstream& outfile) {
		if (!item) {
			char end_symbol = '#';
			outfile.write((char*)(&end_symbol), sizeof(char));
			return;
		} else {
			char begin_symbol = '|';
			std::string key = item->GetKey();
			short balance = item->GetBalance();
			short length = key.length();
			unsigned long long value = item->GetValue();
			outfile.write((char*)(&begin_symbol), sizeof(char));
			outfile.write((char*)(&balance), sizeof(short));
			outfile.write((char*)(&value), sizeof(unsigned long long));
			outfile.write((char*)(&length), sizeof(short));
			outfile.write(key.data(), length);
			WriteToFile(item->GetLeft(), outfile);
			WriteToFile(item->GetRight(), outfile);
		}
	}
	
	void Clear(TItemOfTree* item) {
		if (item == nullptr) {
			return;
		}
		Clear(item->GetLeft());
		Clear(item->GetRight());
		item->SetLeft(nullptr);
		item->SetRight(nullptr);
		item->SetParent(nullptr);
		delete item;
	}	

	TItemOfTree* GetRoot() {
		return root;
	};

	void InsertElement(std::string key, unsigned long long value) {
		if (!root) {
			root = new TItemOfTree(key, value, nullptr);
			std::cout << "OK\n";
		}
		else {
			Insert(root, key, value);
		}
	}

	TItemOfTree* GetMinRight(TItemOfTree* item) {
		while (item->GetLeft()) {
			item = item->GetLeft();
		}
		return item;
	}



	void Remove(std::string key) {
		if (!root) {
			std::cout << "NoSuchWord\n";
			return;
		}
		TItemOfTree* result = Search(root, key);
		if (!result) {
			std::cout << "NoSuchWord\n";
		} else {
			TItemOfTree* parent = result->GetParent();
			if ((!result->GetLeft()) && (!result->GetRight())) {
				if (parent) {
					result->SetParent(nullptr);
					if (parent->GetLeft() == result) {
						parent->SetBalance(parent->GetBalance() - 1);
						parent->SetLeft(nullptr);
					} else {
						parent->SetBalance(parent->GetBalance() + 1);
						parent->SetRight(nullptr);
					}
					Balance(parent, false);
				}
				else {
					root = nullptr;
					std::cout << "OK\n";
				}
				delete result;
			} else if (!result->GetRight()) {
				TItemOfTree* left = result->GetLeft();
				left->SetParent(nullptr);
				result->SetKey(left->GetKey());
				result->SetValue(left->GetValue());
				result->SetBalance(result->GetBalance() - 1);
				result->SetLeft(nullptr);
				delete left;
				Balance(result, false);
			} else {
				TItemOfTree* min = GetMinRight(result->GetRight());
				TItemOfTree* parent_min = min->GetParent();
				TItemOfTree* right_min = min->GetRight();
				result->SetKey(min->GetKey());
				result->SetValue(min->GetValue());
				if (parent_min == result) {
					parent_min->SetRight(right_min);
					parent_min->SetBalance(parent_min->GetBalance() + 1);
				} else {
					parent_min->SetLeft(right_min);
					parent_min->SetBalance(parent_min->GetBalance() - 1);				
				} if (right_min) {
					right_min->SetParent(parent_min);
				}
				min->SetRight(nullptr);
				min->SetParent(nullptr);
				delete min;
				Balance(parent_min, false);
			}
		}
	}

	void RotateLeft(TItemOfTree* item) {
		TItemOfTree* right = item->GetRight();
		TItemOfTree* right_left = right->GetLeft();
		TItemOfTree* parent = item->GetParent();
		if (!parent) {
			root = right;
		}
		right->SetParent(parent);
		if (parent) {
			if (parent->GetLeft() == item) {
				parent->SetLeft(right);
			}
			else {
				parent->SetRight(right);
			}
		}
		if (right_left) {
			right_left->SetParent(item);
		}
		item->SetRight(right_left);
		right->SetLeft(item);
		item->SetParent(right);
	}

	void RotateRight(TItemOfTree* item) {
		TItemOfTree* left = item->GetLeft();
		TItemOfTree* left_right = left->GetRight();
		TItemOfTree* parent = item->GetParent();
		if (!parent) {
			root = left;
		}
		left->SetParent(parent);
		if (parent) {
			if (parent->GetLeft() == item) {
				parent->SetLeft(left);
			} else {
				parent->SetRight(left);
			}
		}
		if (left_right) {
			left_right->SetParent(item);
		}
		item->SetLeft(left_right);
		left->SetRight(item);
		item->SetParent(left);
	}

	TItemOfTree* Search(TItemOfTree* item, std::string key) {
		if (!item) {
			return nullptr;
		}
		std::string key_item = item->GetKey();
		if (key == key_item) {
			return item;
		} else if (key < key_item) {
			return Search(item->GetLeft(), key);
		} else {
			return Search(item->GetRight(), key);
		}
	}
	

	void Insert(TItemOfTree* item, std::string key, unsigned long long value) {
		std::string key_item = item->GetKey();
		if (key_item == key) {
			std::cout << "Exist\n";
			return;
		} else if (key_item > key) {
			TItemOfTree* left = item->GetLeft();
			if (!left) {
				left = new TItemOfTree(key, value, item);
				TItemOfTree* parent = left->GetParent();
				parent->SetLeft(left);
				parent->SetBalance(parent->GetBalance() + 1);
				Balance(parent, true);
				return;
			} else {
				Insert(left, key, value);
			}
		} else {
			TItemOfTree* right = item->GetRight();
			if (!right) {
				right = new TItemOfTree(key, value, item);
				TItemOfTree* parent = right->GetParent();
				parent->SetRight(right);
				parent->SetBalance(parent->GetBalance() - 1);
				Balance(parent, true);
				return;
			} else {
				Insert(right, key, value);
			}
		}
	}

};