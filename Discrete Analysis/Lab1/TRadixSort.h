#include <vector>
#include <string>
#include <cmath>

#ifndef INC_1_TRADIXSORT_H
#define INC_1_TRADIXSORT_H

short int NumberOfDigits = 32;
int StartValue = 0;


class KeyValue {
public:
    KeyValue(int day, int month, int year, std::string key, unsigned long long value) : day(day), month(month), year(year), key(key), value(value) {}
    int day;
    int month;
    int year;
    std::string key;
    unsigned long long value;
};


class TRadixSort {

public:
    static void RadixSort(std::vector <KeyValue*> & data) {
        auto LengthOfVector = (long long) data.size();
        std::vector <int> numbers (NumberOfDigits, StartValue);
        std::vector <KeyValue*> result (LengthOfVector);

        int shift = log2(NumberOfDigits);


        int divisor = NumberOfDigits - 1;
        for (long long j = 0; j < LengthOfVector; ++j) {
            short int index = (data[j]->day) & divisor;
            ++numbers[index];
        }

        for (short int j = 1; j < NumberOfDigits; ++j) {
            numbers[j] = numbers[j] + numbers[j - 1];
        }

        for (long long j = LengthOfVector - 1; j >= 0; --j) {
            short int index = (data[j]->day) & divisor;
            result[numbers[index] - 1] = data[j];
            --numbers[index];
        }

        std::move(result.begin(), result.end(), data.begin());
        std::fill(numbers.begin(), numbers.end(), 0);



        for (long long j = 0; j < LengthOfVector; ++j) {
            short int index = (data[j]->month) & divisor;
            ++numbers[index];
        }

        for (short int j = 1; j < NumberOfDigits; ++j) {
            numbers[j] = numbers[j] + numbers[j - 1];
        }

        for (long long j = LengthOfVector - 1; j >= 0; --j) {
            short int index = (data[j]->month) & divisor;
            result[numbers[index] - 1] = data[j];
            --numbers[index];
        }

        std::move(result.begin(), result.end(), data.begin());
        std::fill(numbers.begin(), numbers.end(), 0);



        int iterations = ceil(ceil(log2(9999))/shift);
        std::cout << iterations << std::endl;

        for (short int i = 0; i < iterations; ++i) {
            for (long long j = 0; j < LengthOfVector; ++j) {
                short int index = (data[j]->year & divisor) >> shift * i;
                ++numbers[index];
            }

            for (short int k = 1; k < NumberOfDigits; ++k) {
                numbers[k] = numbers[k] + numbers[k - 1];
            }

            for (long long k = LengthOfVector - 1; k >= 0; --k) {
                short int index = (data[k]->year & divisor) >> shift * i;
                result[numbers[index] - 1] = data[k];
                --numbers[index];
            }

            std::move(result.begin(), result.end(), data.begin());
            divisor = divisor << shift;
            std::fill(numbers.begin(), numbers.end(), 0);


        }

    }
};

#endif //INC_1_TRADIXSORT_H
