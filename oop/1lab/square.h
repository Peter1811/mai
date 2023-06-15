#include "figure.h"
#include "point.h"

class Square : public Figure{
public:
    Square();

    virtual ~Square();

    void Print(std::ostream &os);
    double Area();
    unsigned VertexesNumber();

private:
    Point a; Point b; Point c; Point d;
};
