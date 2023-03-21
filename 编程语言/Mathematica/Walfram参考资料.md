# Walfram 参考资料

参考资料：
- [Walfram 语言与系统：参考资料中心](https://reference.wolfram.com/language/index.html.zh?source=footer)
- [经典 Mathematica 函数大全](https://www.cnblogs.com/huangshiyu13/p/6553658.html)

## 常用函数列表

- 在 Wolfram 语言中，斜体表示某个实例对象，首字母大写表示函数。

### 运算符及特殊符号

|函数|定义|
|-----------------|---------------------------------------|
|`Line1;`|执行 `Line1`，不显示结果|
|`Line1,line2`|顺次执行 `Line1` 和 `Line2`，并显示结果|
|`?name`|关于系统变量 `name` 的信息|
|`??name`|关于系统变量 `name` 的全部信息|
|`!commmand`|执行 Dos 命令|
|`n!`|N 的阶乘|
|`!!filename`|显示文件内容|
|`Expr>>filename`|打开文件写|
|`Expr>>>filename`|打开文件从文件末写|
|`()`|结合律|
|`[]`|函数|
|`{}`|一个列表|
|`<*Math Fun*>`|在 C 语言中使用 math 的函数|
|`(*Note*)`|程序的注释|
|`#n`|第 n 个参数|
|`##`|所有参数|
|`rule&`|把 `rule` 作用于后面的式子|
|`%`|前一次的输出|
|`%%`|倒数第二次的输出|
|`%n`|第 n 个输出|

### 系统常数

|函数|定义|
|-----------------|---------------------------|
|`Pi`|`3.1415....` 的无限精度数值|
|`E`|`2.17828...` 的无限精度数值|
|`Catalan`|`0.915966...` 卡塔兰常数|
|`EulerGamma`|`0.5772...` 高斯常数|
|`GoldenRatio`|`1.61803...` 黄金分割数|
|`Degree`|`Pi/180` 角度弧度换算|
|`I`|复数单位|
|`Infinity`|无穷大|
|`-Infinity`|负无穷大|
|`ComplexInfinity`|复无穷大|
|`Indeterminate`|不定式|

### 代数计算

|函数|定义|
|---|---|
|`Expand[expr]`|展开表达式|
|`Factor[expr]`|因式分解|
|`Simplify[expr]`|化简表达式|
|`FullSimplify[expr]`|将特殊函数等也进行化简|
|`PowerExpand[expr]`|展开所有的幂次形式|
|`ComplexExpand[expr]`|按复数实部虚部展开|
|`FunctionExpand[expr]`|化简 `expr` 中的特殊函数|
|`Collect[expr, x]`|合并同次项|
|`Together[expr]`|通分|
|`Apart[expr]`|部分分式展开|
|`Cancel[expr]`|约分|
|`ExpandAll[expr]`|展开表达式|
|`FactorTerms[poly]`|提出共有的数字因子|
|`Coefficient[expr,form]`|多项式 `expr` 中 `form` 的系数|
|`Exponent[expr,form]`|表达式 `expr` 中 `form` 的最高指数|
|`Numerator[expr]`|表达式 `expr` 的分子|
|`Denominator[expr]`|表达式 `expr` 的分母|
|`ExpandNumerator[expr]`|展开 `expr` 的分子部分|
|`ExpandDenominator[expr]`|展开 `expr` 的分母部分|
|`TrigExpand[expr]`|展开表达式中的三角函数|
|`TrigFactor[expr]`|给出表达式中的三角函数因子|
|`TrigFactorList[expr]`|给出表达式中的三角函数因子的表|
|`TrigReduce[expr]`|对表达式中的三角函数化简|
|`TrigToExp[expr]`|三角函数到指数函数的转化|
|`ExpToTrig[expr]`|指数函数到三角函数的转化|
|`RootReduce[expr]`||
|`ToRadicals`||

### 方程求解

|函数|定义|
|---|---|
|${\rm Solve} \left[ expr,vars\right]$|试图求解以 $vars$ 为变量的方程组或不等式组 $expr$|
|${\rm Solve} \left[ expr,vars,dom\right]$|在定义域 $dom$ 上求解，$dom$ 的常用选择为 `Reals`、`Integers` 和 `Complexes`|
|${\rm DSolve} \left[ eqn,u,x\right]$|为函数 $u$ 求解微分方程，$x$ 为独立变量|
|${\rm DSolve} \left[ eqn,u, \left\{ x,x_{\min},x_{max}\right\} \right]$|为位于 $x_{\min}$ 和 $x_{max}$ 之间的 $x$ 求解微分方程|
|${\rm DSolve} \left[ \left\{ eqn_{1},eqn_{2}, \ldots \right\} , \left\{ u_{1},u_{2}, \ldots \right\} , \ldots \right]$|求解微分方程组|
|${\rm DSolve} \left[ eqn,u, \left\{ x_{1},x_{2}, \ldots \right\} \right]$|求解一个偏微分方程|
|${\rm DSolve} \left[ eqn,u, \left\{ x_{1},x_{2}, \ldots \right\} \in \Omega \right]$|在区域 $\Omega$ 上求解偏微分方程 $eqn$|
|${\rm Eliminate} \left[ eqns,vars\right]$|用来消掉一个联立方程组中的变量|
|${\rm SolveAlways} \left[ eqns,vars\right]$|给出使方程 $eqns$ 对变量 $vars$ 的所有值都有意义的参数的值|
|${\rm Reduce} \left[ expr,vars\right]$|通过求解关于 $vars$ 的方程和不等式以及消除量词来约化表达式 $expr$|
|${\rm Reduce} \left[ expr,vars,dom\right]$|在域 $dom$ 上的约化，$dom$ 的选取通常是 `Reals`、`Integers` 和 `Complexes`|
|${\rm LogicalExpand} \left[ expr\right]$|展开方程式、不等式和其他函数的逻辑组合|
|${\rm InverseFunction} \left[ f\right]$|表示函数 $f$ 的反函数，它的定义使得 ${\rm InverseFunction} \left[ f \right] \left[ y\right]$ 给出 $x$ 的值，并且其中 $f\left[ x\right]$ 等于 $y$|
|||

### 系统常数

|函数|定义|
|----|----|
|||

### 系统常数

|函数|定义|
|----|----|
|||

### 系统常数

|函数|定义|
|----|----|
|||

### 系统常数

|函数|定义|
|----|----|
|||

### 系统常数

|函数|定义|
|----|----|
|||
