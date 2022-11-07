#include "triangle.h"
#include <cmath>


Triangle::Triangle() {
    std::cout << "Enter numbers for triangle: " << std::endl;
    std::cin >> a;
    std::cin >> b;
    std::cin >> c;
}



void Triangle::Print(std::ostream &os){
    os << "Triangle: ";
    os << a << " " << b << " " << c << std::endl;
}

double Triangle::Area(){
    double first = a.dist(b);
    double second = b.dist(c);
    double third = a.dist(c);
    double p = (first + second + third) / 2.0;
    return sqrt(p * (p - first) * (p - second) * (p - third));
}

unsigned Triangle::VertexesNumber(){
    return 3;
}


Triangle::~Triangle(){
    std::cout << "Triangle deleted!" << std::endl;
}