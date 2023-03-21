# 线性代数

参考书籍：

- 《线性代数及其应用》

## 前言

关键词：高维问题、向量空间、矩阵运算、线性空间、线性变换

支持资料：www.pearsonhighered.com/lay

MyMathLab—在线作业和资源：www.mymathlab.com

交互式教科书（Wolfram）：www.wolfram.com/player

学习指导；www.mypearsonstore.com 

## 第 1 章 线性代数中的线性方程组

线性方程组是线性代数的核心。**线性方程组**等价于**向量方程**与**矩阵方程**。

### 1.1 线性方程组

**线性方程**：包含变量 $x_1,x_2,\cdots,x_n$ 的**线性方程**是形如
$$
    a_1x_1 + a_2x_2 + \cdots + a_nx_n = b
$$
的方程，其中 $b$ 与系数 $a_1,a_2,\cdots,a_n$ 是实数或复数，通常是已知数。下标 $n$ 可以是任意正整数。

**线性方程组**：由一个或几个包含相同变量 $x_1,x_2,\cdots,x_n$ 的线性方程组成的。线性方程组的解是一组数 $(s_1,s_2,\cdots,s_n)$，用这组数分别代替 $x_1,x_2,\cdots,x_n$ 时所有方程的两边相等。

**解集与等价性**：方程组所有可能的解的集合成为线性方程组的**解集**。若两个线性方程组有相同的解集，则这两个线性方程组称为**等价的**。

**几何意义**：求包含两个变量的两个线性方程组成的方程组的解，等价于求两条直线的交点。

**线性方程组的解**：有下列三种情况，

1. 无解；
2. 有唯一解；
3. 有无穷多解。

**相容性**：我们称一个线性方程组是**相容的**，若它有一个解或无穷多个解；称它是**不相容的**，若它无解。

##### 矩阵记号

**系数矩阵与增广矩阵**：一个线性方程组包含的主要信息可以用一个称为**矩阵**的紧凑的矩形阵列表示。给出方程组
$$
\begin{array}{r}
    x_1& -2x_2& + x_3 &=&0 \\
    & 2x_2& - 8x_3 &=&8 \\
    5x_1& & - 5x_3 &=&10
\end{array}
$$
把每一个变量的系数写在对齐的一列中，矩阵
$$
\begin{bmatrix}
  1&  -2& 1\\
  0&  2& -8\\
  5&  0& -5
\end{bmatrix}
$$
称为**系数矩阵**，而
$$
\begin{bmatrix}
  1&  -2& 1& 0\\
  0&  2& -8& 8\\
  5&  0& -5& 10
\end{bmatrix}
$$
称为它的**增广矩阵**。方程组的的增广矩阵是把它的系数矩阵添上一列所得，这一列是由方程组右边的常数组成的。

**矩阵的维数**：矩阵包含的行数和列数。上面的增广矩阵有 3 行 4 列，称为 $3\times 4$ 矩阵。若 $m,n$ 是正整数，$m\times n$ 矩阵是一个有 $m$ 行 $n$ 列的数的矩形阵列。

##### 解线性方程组

**解线性方程组**：基本思路是把方程组用一个更容易解的等价方程组（即有相同解集的方程组）代替。

**初等行变换**：

1. **倍加变换**：把某一行换成它本身与另一行的倍数的和；
2. **对换变换**：把两行对换；
3. **倍乘变换**：把某一行的所有元素乘以同一个非零数。

**行等价性**：行变换可施行于任何矩阵，不仅仅是对于线性方程组的增广矩阵。我们称两个矩阵为**行等价的**，若其中一个矩阵可以经一系列初等行变换成为另一个矩阵。<mark>最重要的一点是行变换是可逆的</mark>。

> 若两个线性方程组的增广矩阵是行等价的，则它们具有相同的解集。

##### 存在性与唯一性问题

线性方程组的两个基本问题：

1. 方程组是否相容，即它是否至少有一个解？
2. 若它有解，它是否只有一个解，即解是否唯一？

### 1.2 行化简与阶梯形矩阵

**行化简算法**：（也称**行消去法**），它可用来解任意线性方程组。这种算法可用于任意矩阵，不管它是否为某一方程组的增广矩阵。在以下定义中，矩阵中**非零行**或**非零列**指在矩阵中至少包含一个非零元素的行或列；**非零行的先导元素**是指该行中最左边的非零元素。

> **定义**：具有以下三个性质的矩阵称为**阶梯形**（或**行阶梯形**）
> 1. 每一非零行都在每一零行之上；
> 2. 某一行的先导元素所在的列位于上一行先导元素的右边；
> 3. 某一行的先导元素所在列下方元素都是零。
> 
> 若一个阶梯形矩阵还满足以下性质，则称它为**简化阶梯形**（或**简化行阶梯形**）
> 1. 每一非零行的先导元素是 1；
> 2. 每一先导元素 1 是该元素所在列的唯一非零元素。

**（简化）阶梯形矩阵**：若一个矩阵具有阶梯形（简化阶梯形），则称它为**阶梯形（简化阶梯形）矩阵**。性质 2 说明先导元素构成阶梯形。

任何非零矩阵都可以行化简（即用初等行变换）变为阶梯形矩阵，但用不同的方法可化为不同的阶梯形矩阵。然而，一个矩阵只能化为唯一的简化阶梯形矩阵。

> **定理 1**：（简化阶梯形矩阵的唯一性）每个矩阵行等价于唯一的简化阶梯形矩阵。

大部分矩阵程序用 RREF 作为简化（行）阶梯形的缩写，有些用 REF 作为（行）阶梯形的缩写。

##### 主元位置

当矩阵经行变换化为阶梯形后，经进一步的行变换将矩阵化为简化阶梯形时，先导元素的位置并不改变。因简化阶梯形是唯一的，故当给定矩阵化为任何一个阶梯形时，**先导元素**总是在相同的位置上。这些先导元素对应于简化阶梯形中的先导元素 1。

> **定义**：矩阵中的**主元位置**是 $A$ 中对应于它的阶梯形中先导元素 1 的位置。**主元列**是 $A$ 的含有主元位置的列。

##### 行化简算法

**向前步骤**（由矩阵得到阶梯形），**向后步骤**（由阶梯形得到简化阶梯形）。

##### 线性方程组的解

行化简算法应用于方程组的增广矩阵时，可以得出线性方程组解集的一种显式表示法。

对应于主元列的变量称为**基本变量**；其它变量称为**自由变量**。<mark>只要一个线性方程组是相容的，其解集就可以显式表示，只需把方程的简化形式解出来再用自由变量表示基本变量即可。</mark>简化阶梯形使每个基本变量仅包含在一个方程中。

方程组的**通解**：所有解的显式表示。

##### 解集的参数表示

我们总是约定以自由变量作为参数来表示解集。解方程组就是要求出解集的这种参数表示或确定它无解。

##### 回代

计算机程序通常用回代法解方程组，而不是求它的简化阶梯形。

##### 存在与唯一性问题

> **定理 2** ：（存在与唯一性定理）线性方程组相容的充要条件是增广矩阵的最右列不是主元列，也就是说，增广矩阵的阶梯形没有形如
$$
\begin{bmatrix} 0  & \cdots  & b \end{bmatrix}, b\ne 0
$$
> 的行，若线性方程组相容，则它的解集可能有两种情形：（1）当没有自由变量时，有唯一解；（2）若至少有一个自由变量，则有无穷多解。

应用行化简算法解线性方程组：
1. 写出方程组的增广矩阵；
2. 应用行化简算法把增广矩阵化为阶梯形，确定方程组是否相容，如果没有解则停止，否则进行下一步；
3. 继续行化简算法得到它的简化阶梯形；
4. 写出由第 3 步所得矩阵对应的方程组；
5. 把第 4 步所得的每个非零方程改写为用任意自由变量表示其基本变量的形式。

### 1.3 向量方程

#### $\mathbb{R}^2$ 中的向量

仅含一列的矩阵称为**列向量**，或简称**向量**，包含两个元素的向量如下所示，
$$
\boldsymbol{u}=\begin{bmatrix}
    3 \\
    -1
\end{bmatrix},
\boldsymbol{v}=\begin{bmatrix}
    0.2 \\
    0.3
\end{bmatrix},
\boldsymbol{w}=\begin{bmatrix}
    w_{1} \\
    w_{2} 
\end{bmatrix}
$$
其中，$w_{1}$ 和 $w_{2}$ 是任意实数，所有两个元素的向量的集记为 $\mathbb{R}^2$，$\mathbb{R}$ 表示向量中的元素是实数，而指数 2 表示每个向量包含两个元素。

$\mathbb{R}^2$ 中两个**向量相等**当且仅当其对应元素相等，因为 $\mathbb{R}^2$ 中的向量是实数的**有序对**。

给定 $\mathbb{R}^2$ 中的两个向量 $\boldsymbol{u}$ 和 $\boldsymbol{v}$，它们的**和** $\boldsymbol{u+v}$ 是把 $\boldsymbol{u}$ 和 $\boldsymbol{v}$ 对应元素相加所得的向量。给定向量 $\boldsymbol{u}$ 和实数 $c$，$\boldsymbol{u}$ 与 $c$ 的**标量乘法**（或**数乘**）是把 $\boldsymbol{u}$ 的每个元素乘以 $c$，所得向量记为 $c\boldsymbol{u}$，$c\boldsymbol{u}$ 中的数 $c$ 称为**标量**（或**数**）。

有时为了方便（以及节省篇幅），我们把列向量 $\begin{bmatrix} 3 \\ -1 \end{bmatrix}$ 写成 $(3, -1)$ 的形式。这时，用圆括弧表示向量，并在两个元素之间加上逗号，以便区别向量 $(3, -1)$ 与 $1\times 2$ 行矩阵 $\begin{bmatrix} 3 -1 \end{bmatrix}$，后者使用方括号且两元素之间无逗号。

#### $\mathbb{R}^2$ 的几何表示

考虑平面上的直角坐标系，因为平面上每个点由实数的有序对确定，所以可把几何点 $(a, b)$ 与列向量 $\begin{bmatrix} a \\ b \end{bmatrix}$ 等同，因此，<mark>我们可把 $\mathbb{R}^2$ 看做平面上所有点的集合</mark>。向量 $\begin{bmatrix} 3 \\ -1 \end{bmatrix}$ 的几何表示是一条由原点 $(0, 0)$ 指向点 $(3, -1)$ 的有向线段（用箭头画出）。

> **向量加法的平行四边形法则**
> 
> 若 $\mathbb{R}^2$ 中向量 $\boldsymbol{u}$ 和 $\boldsymbol{v}$ 用平面上的点表示，则 $\boldsymbol{u + v}$ 对应于以 $\boldsymbol{u}$，$\boldsymbol{0}$ 和 $\boldsymbol{v}$ 为三个顶点的平行四边形的第 4 个顶点。

#### $\mathbb{R}^3$ 中的向量

$\mathbb{R}^3$ 中的向量是 $3\times 1$ 列矩阵，有 3 个元素，它们表示三维坐标空间中的点，或起点为原点的箭头。

#### $\mathbb{R}^n$ 中的向量

若 $n$ 是正整数，则 $\mathbb{R}^n$ 表示所有 $n$ 个实数数列（或有序 $n$ 元组）的集合，通常写成 $n\times 1$ 列矩阵的形式，如
$$
\boldsymbol{u}=\begin{bmatrix}
    u_1\\
    u_2\\
    \vdots \\
    u_n
\end{bmatrix}
$$

所有元素都是零的向量称为**零向量**，用 $\boldsymbol{0}$ 表示（$\boldsymbol{0}$ 中元素的个数可由上下文确定）。$\mathbb{R}^n$ 中向量相等以及向量加法与标量乘法运算类似于 $\mathbb{R}^2$ 中的定义。向量运算有下列性质，它们可直接由实数的相应性质证明。

> **$\mathbb{R}^n$ 中向量的代数性质**
> 
> 对 $\mathbb{R}^n$ 中一切向量 $\boldsymbol{u}$，$\boldsymbol{v}$，$\boldsymbol{w}$ 以及标量 $c$ 和 $d$：</br>
> 1. $\boldsymbol{u} + \boldsymbol{v} = \boldsymbol{v} + \boldsymbol{u}$</br>
> 2. $(\boldsymbol{u} + \boldsymbol{v}) + \boldsymbol{w} = \boldsymbol{u} + (\boldsymbol{v} + \boldsymbol{w})$</br>
> 3. $\boldsymbol{u} + \boldsymbol{0} = \boldsymbol{0} + \boldsymbol{u} = \boldsymbol{u}$</br>
> 4. $\boldsymbol{u} + \boldsymbol{-u} = \boldsymbol{-u} + \boldsymbol{u} = \boldsymbol{0}$，其中 $-\boldsymbol{u}$ 表示 $(-1)\boldsymbol{u}$</br>
> 5. $c(\boldsymbol{u} + \boldsymbol{v}) = c\boldsymbol{u} + c\boldsymbol{v}$</br>
> 6. $(c + d)\boldsymbol{u} = c\boldsymbol{u} + d\boldsymbol{u}$</br>
> 7. $c(d\boldsymbol{u})=(c d)\boldsymbol{u}$</br>
> 8. $1\boldsymbol{u}=\boldsymbol{u}$

为了简单起见，我们也使用 “向量减法”，用 $\boldsymbol{u} - \boldsymbol{v}$ 代替 $\boldsymbol{u} + (-1)\boldsymbol{v}$ 。

#### 线性组合

给定 $\mathbb{R}^2$ 中向量 $\boldsymbol{v}_1, \boldsymbol{v}_2, \cdots,\boldsymbol{v}_p$ 和标量 $c_1, c_2, \cdots, c_p$，向量
$$
\boldsymbol{y} = c_1 \boldsymbol{v}_1 + \cdots + c_p \boldsymbol{v}_p
$$
称为向量 $\boldsymbol{v}_1, \boldsymbol{v}_2, \cdots,\boldsymbol{v}_p$ 以 $c_1, c_2, \cdots, c_p$ 为**权**的**线性组合**。线性组合中的权可为任意实数，包括零。

向量方程
$$ 
    x_1\boldsymbol{a}_1 + x_2\boldsymbol{a}_2 + \cdots + x_n\boldsymbol{a}_n = \boldsymbol{b} 
$$
和增广矩阵为
$$ 
\begin{bmatrix} 
    \boldsymbol{a}_1 &   \boldsymbol{a}_2 & \cdots & \boldsymbol{a}_n & \boldsymbol{b} 
\end{bmatrix} 
$$
的线性方程组有相同的解集。特别地，$\boldsymbol{b}$ 可表示为 $\boldsymbol{a}_1,\boldsymbol{a}_2,\cdots, \boldsymbol{a}_n$ 的线性组合当且仅当对应的线性方程组有解。

线性代数的一个主要思想是研究可以表示为某一固定向量集合 $\{\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots, \boldsymbol{v}_p\}$ 的线性组合的所有向量。

> **定义**：若 $\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots, \boldsymbol{v}_p$ 是 $\mathbb{R}^n$ 中的向量，则 $\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots, \boldsymbol{v}_p$ 的所有线性组合所成的集合用记号 $\text{Span}\{\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots, \boldsymbol{v}_p\}$ 表示，称为**由 $\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots, \boldsymbol{v}_p$ 所生成（或张成）的 $\mathbb{R}^n$ 的子集**。也就是说，$\text{Span}\{\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots, \boldsymbol{v}_p\}$ 是所有形如 $$ c_1 \boldsymbol{v}_1 + c_2 \boldsymbol{v}_2 + \cdots + c_p \boldsymbol{v}_p $$ 的向量的集合，其中 $c_1,c_2,\cdots,c_p$ 为标量。

要判断向量 $\boldsymbol{b}$ 是否属于 $\text{Span}\{\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots, \boldsymbol{v}_p\}$，就是判断向量方程
$$
    x_1\boldsymbol{v}_1 + x_2\boldsymbol{v}_2 + \cdots + x_p\boldsymbol{v}_p = \boldsymbol{b}
$$
是否有解，或等价地，判断增广矩阵为 $\left[\boldsymbol{v}_1\ \boldsymbol{v}_2\ \cdots\ \boldsymbol{v}_p\ \boldsymbol{b}\right]$ 的线性方程组是否有解。

注意 $\text{Span}\{\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots,\boldsymbol{v}_p\}$ 包含的 $\boldsymbol{v}_1$ 所有倍数，这是因为 $c\boldsymbol{v}_1=c\boldsymbol{v}_1+0\boldsymbol{v}_2+\cdots+0\boldsymbol{v}_p$。特别地，它一定包含零向量。

##### $\text{Span}\{\boldsymbol{v}\}$ 与 $\text{Span}\{\boldsymbol{u},\boldsymbol{v}\}$ 的几何解释

设 $\boldsymbol{v}$ 是 $\mathbb{R}^3$ 中的向量，那么 $\text{Span}\{\boldsymbol{v}\}$ 就是 $\boldsymbol{v}$ 的所有标量倍数的集合，也就是 $\mathbb{R}^3$ 中通过 $\boldsymbol{v}$ 和 $\boldsymbol{0}$ 的直线上所有点的集合。

若 $\boldsymbol{u}$ 和 $\boldsymbol{v}$ 是 $\mathbb{R}^3$ 中的非零向量，$\boldsymbol{v}$ 不是 $\boldsymbol{u}$ 的倍数，则 $\text{Span}\{\boldsymbol{u},\boldsymbol{v}\}$ 是 $\mathbb{R}^3$ 中包含 $\boldsymbol{u}$，$\boldsymbol{v}$ 和 $\boldsymbol{0}$ 的平面。特别地，$\text{Span}\{\boldsymbol{u},\boldsymbol{v}\}$ 包含 $\mathbb{R}^3$ 中通过 $\boldsymbol{u}$ 与 $\boldsymbol{0}$ 的直线，也包含通过 $\boldsymbol{v}$ 与 $\boldsymbol{0}$ 的直线。

### 1.4 矩阵方程 $A\boldsymbol{x}=\boldsymbol{b}$

<mark>线性代数中的一个基本思想是把向量的线性组合看作矩阵与向量的积</mark>。下列定义允许我们将 1.3 节的某些概念用新的方法表述出来>

> **定义**：若 $A$ 是 $m\times n$ 矩阵，它的各列为 $\boldsymbol{a}_1,\cdots,\boldsymbol{a}_n$，若 $\boldsymbol{x}$ 是 $\mathbb{R}^n$ 中的向量，则 **$A$ 与 $\boldsymbol{x}$ 的积**（记为 $A\boldsymbol{x}$）就是 **$A$ 的各列以 $\boldsymbol{x}$ 中对应元素为权的线性组合**，即
$$
A \boldsymbol{x}=\left[\begin{array}{llll}
\boldsymbol{a}_1 & \boldsymbol{a}_2 & \cdots & \boldsymbol{a}_n
\end{array}\right]\left[\begin{array}{c}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{array}\right]=x_1 \boldsymbol{a}_1+x_2 \boldsymbol{a}_2+\cdots+x_n \boldsymbol{a}_n
$$

注意 $A\boldsymbol{x}$ 仅当 $A$ 的列数等于 $\boldsymbol{x}$ 中的元素个数时才有定义。

形如 $A\boldsymbol{x}=\boldsymbol{b}$ 的方程称为**矩阵方程**。任何线性方程组或向量方程都可以写成等价的形式为 $A\boldsymbol{x}=\boldsymbol{b}$ 的矩阵方程。

> **定理 3**：若 $A$ 是 $m\times n$ 矩阵，它的各列为 $\boldsymbol{a}_1,\cdots,\boldsymbol{a}_n$，而 $\boldsymbol{b}$ 属于 $\mathbb{R}^m$，则矩阵方程
$$
    A\boldsymbol{x}=\boldsymbol{b}
$$
与向量方程
$$
    x_1\boldsymbol{a}_1 + x_2\boldsymbol{a}_2 + \cdots + x_n\boldsymbol{a}_n = \boldsymbol{b}
$$
有相同的解集。它又与增广矩阵为
$$
\begin{bmatrix}
    \boldsymbol{a}_1 &\boldsymbol{a}_2 &\cdots &\boldsymbol{a}_n &\boldsymbol{b}
\end{bmatrix}
$$
的线性方程组有相同的解集。

##### 解的存在性

$A\boldsymbol{x}$ 的定义直接导致下列有用的事实：<mark>方程 $A\boldsymbol{x}=\boldsymbol{b}$ 有解当且仅当 $\boldsymbol{b}$ 是 $A$ 的各列的线性组合</mark>。

> **定理 4**：设 $A$ 是 $m\times n$ 矩阵，则下列命题是逻辑上等价的。也就是，对于某个 $A$，它们都成立或者都不成立。
> 1. 对 $\mathbb{R}^m$ 中每个 $\boldsymbol{b}$，方程 $A\boldsymbol{x}=\boldsymbol{b}$ 有解。
> 2. $\mathbb{R}^m$ 中每个 $\boldsymbol{b}$ 都是 $A$ 的列的一个线性组合。
> 3. $A$ 的各列生成 $\mathbb{R}^m$。
> 4. $A$ 在每一行都有一个主元位置。

##### $A\boldsymbol{x}$ 的计算

计算 $A\boldsymbol{x}$ 的行-向量规则：若乘积 $A\boldsymbol{x}$ 有定义，则 $A\boldsymbol{x}$ 中的第 $i$ 个元素是 $A$ 的第 $i$ 行元素与 $\boldsymbol{x}$ 的相应元素乘积之和。

主对角线上元素为 1，其它位置上元素为 0 的矩阵称为**单位矩阵**，并记为 $I$。对任意 $\mathbb{R}^3$ 中的 $\boldsymbol{x}$，$I\boldsymbol{x}=\boldsymbol{x}$。类似地，有 $n\times n$ 单位矩阵，有时记为 $I_n$，对任意 $\mathbb{R}^n$ 中的 $\boldsymbol{x}$，$I_n\boldsymbol{x}=\boldsymbol{x}$。

##### 矩阵-向量积 $A\boldsymbol{x}$ 的性质

> **定理 5**：若 $A$ 是 $m\times n$ 矩阵，$\boldsymbol{u}$ 和 $\boldsymbol{v}$ 是 $\mathbb{R}^n$ 中向量，$c$ 是标量，则
> 1. $A(\boldsymbol{u}+\boldsymbol{v})=A\boldsymbol{u}+A\boldsymbol{v}$。
> 2. $A(c\boldsymbol{u})=c(A\boldsymbol{u})$。

### 1.5 线性方程组的解集

##### 齐次线性方程组

线性方程组称为**齐次的**，若它可写成 $A\boldsymbol{x}=\boldsymbol{0}$ 的形式，其中 $A$ 是 $m\times n$ 矩阵而 $\boldsymbol{0}$ 是 $\mathbb{R}^m$ 中的零向量。这样的方程组至少有一个解，即 $\boldsymbol{x}=\boldsymbol{0}$（$\mathbb{R}^n$ 中的**零向量**），这个解称为它的**平凡解**。对给定方程 $A\boldsymbol{x}=\boldsymbol{0}$，重要的是它是否有**非平凡解**，即满足 $A\boldsymbol{x}=\boldsymbol{0}$ 的非零向量 $\boldsymbol{x}$。由 1.2 节解的存在与唯一性定理（定理 2）得出以下事实：<mark>齐次方程 $A\boldsymbol{x}=\boldsymbol{0}$ 有非平凡解当且仅当方程至少有一个自由变量</mark>。

齐次方程 $A\boldsymbol{x}=\boldsymbol{0}$ 总可表示为 $\text{Span}\{\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots, \boldsymbol{v}_p\}$，其中 $\boldsymbol{v}_1,\boldsymbol{v}_2,\cdots, \boldsymbol{v}_p$ 是适当的解向量。若唯一解是零向量，则解集就是 $\text{Span}\{\boldsymbol{0}\}$。若方程 $A\boldsymbol{x}=\boldsymbol{0}$ 仅有一个自由变量，则解集是通过原点的一条直线。若有两个或更多个自由变量，那么通过原点的平面就给出 $A\boldsymbol{x}=\boldsymbol{0}$ 的解集的一个很好的图形说明。注意，类似的图可用来解释 $\text{Span}\{\boldsymbol{u},\boldsymbol{v}\}$，即使 $\boldsymbol{u},\boldsymbol{v}$ 并不是 $A\boldsymbol{x}=\boldsymbol{0}$ 的解。

##### 参数向量形式

方程 $10x_1-3x_2-2x_3=0$ 是平面的**隐式**描述。解此方程就是要找这个平面的**显式**描述，就是说，将它作为 $\boldsymbol{u}$ 和 $\boldsymbol{v}$ 所生成的子集。该方程称为平面的参数向量方程，有时也可写为
$$
    \boldsymbol{x} = s\boldsymbol{u} + t\boldsymbol{v}\ (s,t\ \text{为实数})
$$
来强调参数可取任何实数值。方程 $\boldsymbol{x} = t\boldsymbol{v}$（$t$ 为实数）是直线的参数向量方程。当解集用向量显式表示时，则称之为**解的参数向量形式**。


## 第 2 章 矩阵代数

## 第 3 章 行列式

## 第 4 章 向量空间

## 第 5 章 特征值与特征向量

## 第 6 章 正交性和最小二乘法

## 第 7 章 对称矩阵和二次型

## 第 8 章 向量空间的几何学