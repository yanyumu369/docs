## Labview

### PID (Proportion Integration Differentiation) 比例，积分，微分控制

<div align=center>
<img width="60%" src="programme\Labview\image\Pid-feedback-nct-int-correct.png"/>
</div>

“标准型”的 PID 为：
$$
\mathrm{MV}(\mathrm{t})=K_{p}\left(e(t)+\frac{1}{T_{i}} \int_{0}^{t} e(\tau) d \tau+T_{d} \frac{d}{d t} e(t)\right)
$$
其中，$T_{i}$ 为积分时间，$T_{d}$ 为微分时间。

在理想的平行式 PID 中，其方程如下：
$$
\mathrm{MV}(\mathrm{t})=K_{p} e(t)+K_{i} \int_{0}^{t} e(\tau) d \tau+K_{d} \frac{d}{d t} e(t)
$$
其中的增益和标准型PID系数的关系是：
$$
K_{i}=\frac{K_{p}}{T_{i}}
K_{d}=K_{p} T_{d}
$$

<div align=center>
<img width="100%" src="programme\Labview\image\PID_Compensation_Animated.gif"/>
</div>



**参考资料**：<br>
- [PID 控制器](https://zh.wikipedia.org/zh-cn/PID%E6%8E%A7%E5%88%B6%E5%99%A8)
- PID 控制算法原理（抛弃公式，从本质上真正理解 PID 控制）
- [PID 算法原理 一图看懂 PID 的三个参数](https://blog.csdn.net/qq_41673920/article/details/84860697)