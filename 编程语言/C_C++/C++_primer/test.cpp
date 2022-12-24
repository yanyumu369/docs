#include <iostream>
using std::cerr; using std::cin; using std::cout; using std::endl;

int main()
{
    int sum = 0, value;
    while(cin >> value, !cin.eof())
    {
        if (cin.bad())
        {
            throw std::runtime_error("IO stream corrupted");
            continue;
        }
        if (cin.fail())
        {
            cerr << "bad data" << endl;
            cin.clear();
            cin.ignore(200, '\n');
            continue;
        }
        sum += value;
        cout << "Sum is " << sum << endl;
    }
    return 0;
}