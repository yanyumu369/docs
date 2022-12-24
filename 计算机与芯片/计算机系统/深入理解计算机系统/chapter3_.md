# 程序的机器级表示

代码示例：

```c 
// main.c
#include <stdio.h>

long mult2(long a, long b){
    long s = a * b;
    return s;
}

void multstore (long x, long y, long *dest){
    long t = mult2(x, y);
    *dest = t;
}

int main() {
    long d;
    multstore(2, 3, &d);
    printf("2 * 3 --> %ld\n", d);
    return 0;
}
```

通过命令行 `gcc -Og -S -masm=att main.c` 生成 ATT 格式的汇编代码：
```nasm
mult2:
        movq    %rdi, %rax
        imulq   %rsi, %rax
        ret
multstore:
        pushq   %rbx
        movq    %rdx, %rbx
        call    mult2
        movq    %rax, (%rbx)
        popq    %rbx
        ret
.LC0:
        .string "2 * 3 --> %ld\n"
main:
        subq    $24, %rsp
        leaq    8(%rsp), %rdx
        movl    $3, %esi
        movl    $2, %edi
        call    multstore
        movq    8(%rsp), %rsi
        movl    $.LC0, %edi
        movl    $0, %eax
        call    printf
        movl    $0, %eax
        addq    $24, %rsp
        ret
```

通过命令行 `gcc -Og -S -masm=intel main.c` 生成 Intel 格式的汇编代码：

```nasm
mult2:
        mov     rax, rdi
        imul    rax, rsi
        ret
multstore:
        push    rbx
        mov     rbx, rdx
        call    mult2
        mov     QWORD PTR [rbx], rax
        pop     rbx
        ret
.LC0:
        .string "2 * 3 --> %ld\n"
main:
        sub     rsp, 24
        lea     rdx, [rsp+8]
        mov     esi, 3
        mov     edi, 2
        call    multstore
        mov     rsi, QWORD PTR [rsp+8]
        mov     edi, OFFSET FLAT:.LC0
        mov     eax, 0
        call    printf
        mov     eax, 0
        add     rsp, 24
        ret
```



