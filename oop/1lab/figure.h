#ifndef FIGURE_H
#define FIGURE_H

#include <iostream>

class Figure {
public:

    virtual unsigned VertexesNumber() = 0;
    virtual void Print(std::ostream &os) = 0;
    virtual double Area() = 0;

    ~Figure() {};

};

#endif //FIGURE_H