#include "square.h"
#include <cmath>

Square::Square() {
    std::cout << "Enter numbers for square: " << std::endl;
    std::cin >> a;
    std::cin >> b;
    std::cin >> c;
    std::cin >> d;
}

void Square::Print(std::ostream &os){
    os << "Square: ";
    os << a << " " << b << " " << c << " " << d << std::endl;
}

double Square::Area(){
    double first = a.dist(b);
    return pow(first, 2);
}

unsigned Square::VertexesNumber() {
    return 4;
}

Square::~Square() {
    std::cout << "Square deleted!" << std::endl;
}