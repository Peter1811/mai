cmake_minimum_required(VERSION 3.16)
project(3lab)

set(CMAKE_CXX_STANDARD 14)

add_executable(3_lab main.cpp triangle.h triangle.cpp point.h point.cpp tqueueitem.h tqueueitem.cpp tqueue.h tqueue.cpp)