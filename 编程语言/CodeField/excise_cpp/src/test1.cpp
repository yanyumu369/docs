#include <iostream>
#include <vector>
#include <algorithm> 

void bubblesort1A(int [], int);

int main() {
    int n = 6;
    int A[] = {10, 5, 6, 8, 56, 25};
    bubblesort1A(A, n);
    for (int i = 0; i < n; ++i){
        std::cout << A[i] << " ";
    }
    std::cout << std::endl; 
}

void bubblesort1A(int A[], int n) {         //冒泡排序算法（版本 1A）：0 <= n
    bool sorted = false;                    //整体排序标志，首先假定尚未排序
    while (!sorted) {                       //在尚未确认已全局排序之前，逐趟进行扫描交换
        sorted = true;                      //假定已经排序
        for (int i = 1; i < n; i++) {       //自左向右逐对检查当前范围 A[0, n) 内的各相邻元素
            if (A[i - 1] > A[i]) {          //一旦 A[i - 1] 与 A[i] 逆序，则
                std::swap(A[i - 1], A[i]);       //交换之，并
                sorted = false;             //因整体排序不能保证，需要清除排序标志
            }
        }
        n--;                                //至此末元素必然就位，故可以缩短待排序序列的有效长度
    }
}                                           //借助布尔型标志位 sorted，可及时提前退出，而不致总是蛮力地做 n - 1 趟扫描交换
