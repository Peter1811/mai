#include <memory>
#ifndef TITERATOR_H_
#define TITERATOR_H_
template <class node, class T> class Titerator {
public:
  explicit Titerator(std::shared_ptr<node> n) { node_ptr = n; }
  std::shared_ptr<T> operator*() { return node_ptr->GetItem(); }
  std::shared_ptr<T> operator->() { return node_ptr->GetItem(); }
  void operator++() { node_ptr = node_ptr->GetNext(); }
  Titerator operator++(int) {
    Titerator other(*this);
    ++(*this);
    return other;
  }
  bool operator==(Titerator const &i) { return node_ptr == i.node_ptr; };
  bool operator!=(Titerator const &i) { return node_ptr != i.node_ptr; };

private:
  std::shared_ptr<node> node_ptr;
};

#endif // TITERATOR_H_
