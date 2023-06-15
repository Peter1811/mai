#include <iostream>
#include "figure.h"
#include "point.h"

class Triangle : public Figure { 
public:
    Triangle();

    virtual ~Triangle();

    void Print(std::ostream &os);
    double Area();
    unsigned VertexesNumber();

private:
    Point a; Point b; Point c; 
};