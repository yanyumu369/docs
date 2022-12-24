## 插件 HyperSnips for Math 提供的代码补全

[配置 Latex 公式自动补全](https://www.cnblogs.com/1024th/p/15332686.html)

### Fraction Match 分数匹配

| 代码   | 补全后代码     | 代码     | 补全后代码       |
| ------ | -------------- | -------- | ---------------- |
| `//`   | `\frac{}{}`    | `1/`     | `\frac{1}{}`     |
| `a_1/` | `\frac{a_1}{}` | `a+b^2/` | `a+\frac{b^2}{}` |

### Hat Operation 帽子操作

$$

### 功能

#### 函数名和希腊字母自动加 `\`

在函数名（如 `sin`, `cos`, `ln` 等）和希腊字母（如 `alpha` 等）前面自动加入 `\`。

| 代码    | 补全后代码    |
| ------- | ------------- |
| `oint`  | `\oint`       |
| `eps`   | `\varepsilon` |
| `delta` | `\delta`      |
| `sin`   | `\sin`        |
| `pi`    | `\pi`         |

`oint|iiint|iint|int`

`sin|cos|arccot|cot|csc|ln|log|exp|perp|arcsin|arccos|arctan|arccot|arccsc|arcsec|ell|nabla|notin|not`

`mu|alpha|sigma|rho|beta|gamma|delta|pi|zeta|eta|varepsilon|theta|iota|kappa|vartheta|lambda|nu|pi|rho`
`|tau|upsilon|varphi|phi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega`

#### 极限

在 `\lim`、`\sum` 等巨运算符后面再加个 `\limits`、`\nolimits`、`\displaylimits` 会产生如下效果：

1. `\limits` (原始命令) 把运算范围放到巨运算符的**上面**和**下面**，这是显示样式中的默认位置。
2. `\nolimits` (原始命令) Place limits of a large operator as subscript and superscript expressions. This is the default position in text style.
3. `\displaylimits` (原始命令) Restore default placement for limits.

简言之会强制把运算范围放到巨运算符的**上面**和**下面**（在行内公式中默认是想上下标一样放在右上角和右下角）。

| 代码  | 补全后代码            |
| ----- | --------------------- |
| `lim` | `\lim_{n \to \infty}` |
| `sum` | `\sum_{}`             |

`sum|min|max|argmin|argmax|sup|inf`

#### 特殊的集合

| 代码 | 补全后代码   |
| ---- | ------------ |
| `RR` | `\mathbb{R}` |

$\mathbb{R}\mathbf{er} \because \equiv $
