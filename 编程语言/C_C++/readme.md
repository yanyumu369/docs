# C/C++

## 资料

1. [The GNU C Library](https://www.gnu.org/software/libc/) (glibc)
2. [C++ 标准草案来源](https://github.com/cplusplus/draft)（C++ Standard Draft Sources）</br>
   这些是用于生成 C++ 标准草案的来源。这些来源不应被视为 ISO 出版物，由其生成的文件也不应被视为 ISO 出版物，除非被 C++ 工作组（ISO/IEC JTC1/SC22/WG21）正式采用。
3. [cppreference.com 英文版](https://en.cppreference.com/w/)：C 和 C++ 的官方文档，全面而且权威！
4. [cppreference.com 中文版](https://zh.cppreference.com/w/%E9%A6%96%E9%A1%B5)
5. [cplusplus.com](https://cplusplus.com/)
6. [C++ 标准库参考](https://docs.microsoft.com/zh-cn/cpp/standard-library/cpp-standard-library-reference?view=msvc-170)

## 编译 & 汇编 & 反汇编

1. [C++ Insights](https://cppinsights.io/)：主要用于看*代码编译展开后的*具体情况，是个学习 C++ 模板时不错的辅助工具
2. [Compiler Explorer](https://godbolt.org/)：将 C 或者 C++ 语言代码转换成汇编语言。
3. [Defuse](https://defuse.ca/online-x86-assembler.htm#disassembly)：在线汇编文本转机器码，机器码转汇编文本，Intel 语法。
4. [ODA](https://onlinedisassembler.com/odaweb/)：在线汇编文本转机器码，机器码转汇编文本，Intel 语法。

## 在线编辑器

1. [C++ 在线编辑器](https://www.dooccn.com/cpp/)
2. [Json.cn](https://www.json.cn/runcode/run_cpp920/)
3. [OnlineGDB](https://www.onlinegdb.com/online_c++_compiler)：按空格卡顿。

## 代码 CPU、内存、I/O 开销

1. [Compare C++ Builds](https://build-bench.com/b/7xE2wEmi1nF5JQ-0UatixktDVJ0)：可以测试、比较不同 C++ 代码的编译开销（CPU、内存、I/O）
2. [Quick C++ Benchmark](https://quick-bench.com/q/6NbF_RyMhnbl5CF-y_G1AxE6it8)：可以快速对一些 C++ 代码片段进行 benchmark 并可视化显示出来。支持多个版本的 clang 和 gcc。背后用的应该是 [google benchmark](https://github.com/google/benchmark) 这个开源库，你也可以在自己的机器上安装这个库。
