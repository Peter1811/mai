#include "triangle.h"


double Triangle::Area() { return (abs(a.x_ - b.x_) * abs(a.y_ - b.y_)); }

Triangle::Triangle() : a(), b(), c() {
  cout << "Default Triangle is created" << endl;
}

Triangle::Triangle(const Triangle &other) {
  a = other.a;
  b = other.b;
  c = other.c;
  cout << "Made copy of Triangle" << endl;
}

Triangle::Triangle(vector<Point> v) : a(v[0]), b(v[1]), c(v[2]) {
  cout << "Triangle with vertices " << a << ", " << b << ", " << c << " was created" << endl;
}

istream &operator>>(istream &is, Triangle &obj) {
  cout << "Enter cords" << endl;
  is >> obj.a >> obj.b >> obj.c;
  return is;
}

ostream &operator<<(ostream &os, const Triangle &obj) {
  os << "Triangle: " << obj.a << ", " << obj.b << ", " << obj.c;
  return os;
}

Triangle &Triangle::operator++() { // инкрементируем каждую вершину
  ++this->a;
  ++this->b;
  ++this->c;
  return *this;
}

Triangle operator+(const Triangle &left, const Triangle &right) {
  vector<Point> v{left.a + right.a, left.b + right.b, left.c + right.c};
  return Triangle(v);
}

Triangle &Triangle::operator=(const Triangle &other) {
  if (this == &other) {
    return *this;
  }
  this->a = other.a;
  this->b = other.b;
  this->c = other.c;
  return *this;
}

Triangle::~Triangle() { cout << "Triangle was deleted" << endl; }

size_t Triangle::VertexNumbers() { return 3; }
