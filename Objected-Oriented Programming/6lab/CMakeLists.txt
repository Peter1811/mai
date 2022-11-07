cmake_minimum_required(VERSION 3.16)
project(6lab)

set(CMAKE_CXX_STANDARD 14)


add_executable(6_lab main.cpp
        main.cpp tqueueitem.h tqueue.h triangle.cpp triangle.h point.cpp point.h titerator.h vector.h tallocationblock.cpp tallocationblock.h
        )
