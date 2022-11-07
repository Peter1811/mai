#include "triangle.h"
#include "square.h"
#include "rectangle.h"

int main(){

    Triangle f;
    f.Print(std::cout);
    std::cout << f.Area() << std::endl;

    Square f2;
    f2.Print(std::cout);
    std::cout << f2.Area() << std::endl;

    Rectangle f3;
    f3.Print(std::cout);
    std::cout << f3.Area() << std::endl;


    return 0;

}