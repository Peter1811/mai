#pragma once
#ifndef TRISNGLE_H
#define TRIANGLE_H


#include <vector>
#include "point.h"

using namespace std;

class Triangle {
public:
    Triangle();

    Triangle(vector<Point>);

    Triangle(const Triangle& other);

    virtual ~Triangle();

    friend istream &operator>>(istream &is, Triangle &obj); // перегруженный оператор >>

    friend ostream &operator<<(ostream &os, const Triangle &obj);

    Triangle &operator++();

    friend Triangle operator+(const Triangle &left, const Triangle &right);

    Triangle &operator=(const Triangle &right);

    size_t VertexNumbers();

    double Area();

private:
    Point a, b, c; 
};


#endif
