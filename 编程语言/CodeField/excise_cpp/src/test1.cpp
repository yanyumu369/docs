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

void bubblesort1A(int A[], int n) {         //ð�������㷨���汾 1A����0 <= n
    bool sorted = false;                    //���������־�����ȼٶ���δ����
    while (!sorted) {                       //����δȷ����ȫ������֮ǰ�����˽���ɨ�轻��
        sorted = true;                      //�ٶ��Ѿ�����
        for (int i = 1; i < n; i++) {       //����������Լ�鵱ǰ��Χ A[0, n) �ڵĸ�����Ԫ��
            if (A[i - 1] > A[i]) {          //һ�� A[i - 1] �� A[i] ������
                std::swap(A[i - 1], A[i]);       //����֮����
                sorted = false;             //�����������ܱ�֤����Ҫ��������־
            }
        }
        n--;                                //����ĩԪ�ر�Ȼ��λ���ʿ������̴��������е���Ч����
    }
}                                           //���������ͱ�־λ sorted���ɼ�ʱ��ǰ�˳��������������������� n - 1 ��ɨ�轻��
