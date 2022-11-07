#ifndef RECTANGLE_H
#define RECTANGLE_H

#include "figure.h"
#include "point.h"

class Rectangle : public Figure{
public:
    Rectangle();

    virtual ~Rectangle();

    void Print(std::ostream &os);
    double Area();
    unsigned VertexesNumber();

private:
    Point a; Point b; Point c; Point d;
};


#endif //RECTANGLE_H
