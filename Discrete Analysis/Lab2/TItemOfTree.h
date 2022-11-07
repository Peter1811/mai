class TItemOfTree {
private:
	short balance;
	std::string key;
	unsigned long long value;
	TItemOfTree *left, *right, *parent;
public:
	TItemOfTree() {
		balance = value = 0;
		left = right = parent = nullptr;
	}

	TItemOfTree(std::string key, unsigned long long value, TItemOfTree* parent) {
		this->balance = 0;
		this->value = value;
		this->key = key;
		this->value = value;
		this->parent = parent;
		this->left = this->right = nullptr;
	}
	short GetBalance() {
		return balance;
	}	

	void SetBalance(short balance) {
		this->balance = balance;
	}

	std::string GetKey() {
		return key;
	}

	void SetKey(std::string key) {
		this->key = key;
	}

	TItemOfTree* GetLeft() {
		return left;
	}

	void SetLeft(TItemOfTree* left) {
		this->left = left;
	}

	TItemOfTree* GetParent() {
		return parent;
	}

	void SetParent(TItemOfTree* parent) {
		this->parent = parent;
	}

	TItemOfTree* GetRight() {
		return right;
	}

	void SetRight(TItemOfTree* right) {
		this->right = right;
	}

	unsigned long long GetValue() {
		return value;
	}

	void SetValue(unsigned long long value) {
		this->value = value;
	}

	~TItemOfTree() {};
};