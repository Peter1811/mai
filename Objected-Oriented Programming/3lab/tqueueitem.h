#ifndef LAB_3_QUEUE_ITEM_H
#define LAB_3_QUEUE_ITEM_H

#include "Triangle.h"
#include <memory>

class TQueue_item {
public:
    TQueue_item(const shared_ptr<Triangle> &triangle);
    TQueue_item(const shared_ptr<TQueue_item> &other);
    shared_ptr<TQueue_item> SetNext(shared_ptr <TQueue_item> &next_);
    shared_ptr<TQueue_item> GetNext();
    shared_ptr<Triangle> GetTriangle();
    friend ostream &operator<<(ostream &os, const TQueue_item &obj);
    virtual ~TQueue_item();

private:
    shared_ptr <Triangle> triangle;
    shared_ptr <TQueue_item> next;
};


#endif //LAB_3_QUEUE_ITEM_H