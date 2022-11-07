#ifndef RECTANGLE_H
#define RECTANGLE_H

#include "point.h"
#include <vector>

using namespace std;

class Triangle {
public:
  Triangle();

  Triangle(vector<Point>);

  Triangle(const Triangle &other);

  virtual ~Triangle();

  friend istream &operator>>(istream &is,
                             Triangle &obj); // перегруженный оператор >>

  friend ostream &operator<<(ostream &os, const Triangle &obj);

  Triangle &operator++();

  friend Triangle operator+(const Triangle &left, const Triangle &right);

  Triangle &operator=(const Triangle &right);

  size_t VertexNumbers();

  double Area();

private:
  Point a, b, c; // a - левая нижняя вершина, b - левая верхняя, с - правая
                    // верхняя, d - правая нижняя
};

#endif
