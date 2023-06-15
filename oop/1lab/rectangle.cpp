#include "rectangle.h"

Rectangle::Rectangle() {
    std::cout << "Enter numbers for rectangle: " << std::endl;
    std::cin >> a;
    std::cin >> b;
    std::cin >> c;
    std::cin >> d;
}

void Rectangle::Print(std::ostream &os) {
    os << "Square: ";
    os << a << " " << b << " " << c << " " << d << std::endl;
}

double Rectangle::Area() {
    double first = a.dist(b);
    double second = b.dist(c);
    return first * second;
}

unsigned Rectangle::VertexesNumber() {
    return 4;
}

Rectangle::~Rectangle() {
    std::cout << "Rectangle deleted!" << std::endl;
}