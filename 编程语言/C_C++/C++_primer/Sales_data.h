#ifndef SALES_DATA_H
#define SALES_DATA_H

#include "Version_test.h"

#include <string>
#include <iostream>

class Sales_data {
friend Sales_data add(const const Sales_data&, const SAles_data&);
friend std::ostream &print(std::ostream&, const Sales_data&);
friend std::istream &read(std::istream&, Sales_data&)
public:
#if defined(IN_CLASS_INITS) && defined(DEFAULT_FCNS)
    Sales_data() = default;
#else
    Sales_data(): units_sold(0), revenue(0.0) { }
#endif
#ifdef IN_CLASS_INITS
    Sales_data(const std::string &s): bookNo(s) { }
#else
    Sales_data(const std::string &s):
        bookNo(s), units_sold(0), revenue(0.0) { }
#endif
    Sales_data(const std::string &s, unsigned n, double p):
        bookNo(s), units_sold(0), revenue(p*n) { }
    Sales_data(std::istream &);

    std::string isbn() const { return bookNo; }
    Sales_data& combine(const Sales_data&);
    double avg_price() const;

private:
    std::string bookNo;
#ifdef IN_CLASS_INITS
    unsigned units_sold = 0;
    double revenue = 0.0;
#else
    unsigned units_sold;
    double revenue;
#endif
};
#endif