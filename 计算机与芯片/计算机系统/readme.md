# 计算机系统

- [osdev.org](https://wiki.osdev.org/X86-64_Instruction_Encoding)

## 寄存器

- [CPU Registers x86-64](https://wiki.osdev.org/CPU_Registers_x86-64)
- [X86-64 Instruction Encoding](https://wiki.osdev.org/X86-64_Instruction_Encoding)
- [x86 and amd64 instruction reference](https://www.felixcloutier.com/x86/)

### 寄存器全名

- AH&AL ＝ AX（Accumulator）：累加寄存器
- BH&BL ＝ BX（Base）：基址寄存器
- CH&CL ＝ CX（Count）：计数寄存器
- DH&DL ＝ DX（Data）：数据寄存器
- SP（Stack Pointer）：堆栈指针寄存器
- BP（Base Pointer）：基址指针寄存器
- SI（Source Index）：源变址寄存器
- DI（Destination Index）：目的变址寄存器
- IP（Instruction Pointer）：指令指针寄存器
- CS（Code Segment）代码段寄存器
- DS（Data Segment）：数据段寄存器
- SS（Stack Segment）：堆栈段寄存器
- ES（Extra Segment）：附加段寄存器
- OF（overflow flag）：溢出标志，操作数超出机器能表示的范围表示溢出溢出时为 1。
- SF（sign Flag）：符号标志，记录运算结果的符号，结果负时为 1。
- ZF（zero flag）：零标志，运算结果等于 0 时为 1，否则为 0。
- CF（carry flag）：进位标志，最高有效位产生进位时为 1，否则为 0。
- AF（auxiliary carry flag）：辅助进位标志，运算时，第 3 位向第 4 位产生进位时为 1，否则为 0。
- PF（parity flag）：奇偶标志，运算结果操作数位为 1 的个数为偶数个时为 1，否则为 0。
- DF（direction flag）：方向标志，用于串处理.DF=1 时，每次操作后使 SI 和 DI 减小.DF=0 时则增大。
- IF（interrupt flag）：中断标志，IF=1 时，允许 CPU 响应可屏蔽中断，否则关闭中断。
- TF（trap flag）：陷阱标志，用于调试单步操作。
