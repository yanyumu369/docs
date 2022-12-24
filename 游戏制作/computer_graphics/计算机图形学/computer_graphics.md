# 计算机图形学

## Linear Algebra 线性代数

点乘可以表示两个向量之间的相对方向和距离。

$$\vec{a} \cdot \vec{b}= \vec{a}^{T} \vec{b}=\left(\begin{array}{lll}x_{a} & y_{a} & z_{a}\end{array}\right)\left(\begin{aligned}x_{b} \\\ y_{b} \\\ z_{b} \end{aligned}\right)=\left(x_{a} x_{b}+y_{a} y_{b}+z_{a} z_{b}\right)$$

叉乘（cross product）判断一个向量在另一个向量的左侧还是右侧，一个点在三角形内还是外，三角形三条边顺时针或逆时针旋转，点始终在一边。

$$\vec{a} \times \vec{b}=A^{*} b=\left(\begin{array}{ccc}0 & -z_{a} & y_{a} \\\ z_{a} & 0 & -x_{a} \\\ -y_{a} & x_{a} & 0\end{array}\right)\left(\begin{array}{c}x_{b} \\\ y_{b} \\\ z_{b}\end{array}\right)$$

## Transformation 变换

##### Scale Matrix 缩放矩阵

<div align=center>
<img width="50%" src="game\computer_graphics\image\缩放.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

$$ \left[\begin{array}{l} x^{\prime} \\\ y^{\prime} \end{array}\right]=\left[\begin{array}{ll} s & 0 \\\ 0 & s \end{array}\right]\left[\begin{array}{l} x \\\ y \end{array}\right] $$

##### Scale (Non-Uniform) 缩放（不一致）

<div align=center>
<img width="50%" src="game\computer_graphics\image\缩放2.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

$$ \left[\begin{array}{l} x^{\prime} \\\ y^{\prime} \end{array}\right]=\left[\begin{array}{ll} s_x & 0 \\\ 0 & s_y \end{array}\right]\left[\begin{array}{l} x \\\ y \end{array}\right] $$

##### Reflection Matrix 镜像矩阵

<div align=center>
<img width="50%" src="game\computer_graphics\image\镜像.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

$$ \left[\begin{array}{l} x^{\prime} \\\ y^{\prime} \end{array}\right]=\left[\begin{array}{ll} -1 & 0 \\\ 0 & 1 \end{array}\right]\left[\begin{array}{l} x \\\ y \end{array}\right] $$

##### Shear Matrix 切变矩阵

<div align=center>
<img width="50%" src="game\computer_graphics\image\切变.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

$$ \left[\begin{array}{l} x^{\prime} \\\ y^{\prime} \end{array}\right]=\left[\begin{array}{ll} 1 & a \\\ 0 & 1 \end{array}\right]\left[\begin{array}{l} x \\\ y \end{array}\right] $$

##### Rotate Matrix 旋转矩阵

找特殊点，如 (1, 0) 或 (0, 1) 直接代入求解。

<div align=center>
<img width="50%" src="game\computer_graphics\image\旋转.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

$$ \mathbf{R}_{\theta}=\left[\begin{array}{cc} \cos \theta & -\sin \theta \\\ \sin \theta & \cos \theta \end{array}\right] $$

##### Translation 平移

<div align=center>
<img width="50%" src="game\computer_graphics\image\平移.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

$$\left[\begin{array}{l} x^{\prime} \\\ y^{\prime} \end{array}\right]=\left[\begin{array}{ll} a & b \\\ c & d \end{array}\right]\left[\begin{array}{l} x \\\ y \end{array}\right]+\left[\begin{array}{l} t_{x} \\\ t_{y} \end{array}\right]$$

### Homogenous Coordinates 齐次坐标系

增加第三个坐标（w-坐标）
- 2D point = (x, y, 1)<sup>T</sup>
- 2D vector = (x, y, 0)<sup>T</sup> 向量具有平移不变性，所以 w=0，这样经过平移变换后不变。

如果结果的 w 坐标是 1 或 0：
- vector + vector = vector
- point - point = vector
- point + vector = point 
- point + point = 中点（w=2）

在齐次坐标系中，(x, y, w) 是 2D 点 (x/w, y/w, 1), w≠0。

$$ \left(\begin{array}{c} x^{\prime} \\\ y^{\prime} \\\ w^{\prime} \end{array}\right)=\left(\begin{array}{ccc} 1 & 0 & t_{x} \\\ 0 & 1 & t_{y} \\\ 0 & 0 & 1 \end{array}\right) \cdot\left(\begin{array}{l} x \\\ y \\\ 1 \end{array} \right)=\left(\begin{array}{c} x+t_{x} \\\ y+t_{y} \\\ 1 \end{array}\right) $$

##### Scale

$$ \mathbf{S}\left(s_{x}, s_{y}\right)=\left(\begin{array}{ccc} s_{x} & 0 & 0 \\\ 0 & s_{y} & 0 \\\ 0 & 0 & 1 \end{array}\right) $$

##### Rotation

$$ \mathbf{R}(\alpha)=\left(\begin{array}{ccc} \cos \alpha & -\sin \alpha & 0 \\\ \sin \alpha & \cos \alpha & 0 \\\ 0 & 0 & 1 \end{array}\right) $$

##### Translation

$$ \mathbf{T}\left(t_{x}, t_{y}\right)=\left(\begin{array}{ccc} 1 & 0 & t_{x} \\\ 0 & 1 & t_{y} \\\ 0 & 0 & 1 \end{array}\right) $$

##### Inverse Transform 逆变换

<div align=center>
<img width="40%" src="game\computer_graphics\image\逆变换.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

##### Composing Transform 组合变换

矩阵不满足交换律，所以变换的顺序很重要。

##### Decomposing Complex Transforms 分解复杂变换

<div align=center>
<img width="50%" src="game\computer_graphics\image\分解复杂变换.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

## 3D Transformations 3D变换

正交矩阵—矩阵的逆和转置相同。

先进行线性变换再平移。

$$ \left(\begin{array}{l} x^{\prime} \\ y^{\prime} \\ z^{\prime} \\ 1 \end{array}\right)=\left(\begin{array}{lllc} a & b & c & t_{x} \\\ d & e & f & t_{y} \\\ g & h & i & t_{z} \\\ 0 & 0 & 0 & 1 \end{array}\right) \cdot\left(\begin{array}{l} x \\\ y \\\ z \\\ 1 \end{array}\right) $$

##### Scale 缩放

$$ \mathbf{S}\left(s_{x}, s_{y}, s_{z}\right)=\left(\begin{array}{cccc} s_{x} & 0 & 0 & 0 \\\ 0 & s_{y} & 0 & 0 \\\ 0 & 0 & s_{z} & 0 \\\ 0 & 0 & 0 & 1 \end{array}\right) $$

##### Translation 平移

$$ \mathbf{T}\left(t_{x}, t_{y}, t_{z}\right)=\left(\begin{array}{cccc} 1 & 0 & 0 & t_{x} \\\ 0 & 1 & 0 & t_{y} \\\ 0 & 0 & 1 & t_{z} \\\ 0 & 0 & 0 & 1 \end{array}\right) $$

##### Rotation around x-, y-, or z-axis

<div align=center>
<img width="30%" src="game\computer_graphics\image\3D旋转.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

$$ \mathbf{R}_{x}(\alpha)=\left(\begin{array}{cccc} 1 & 0 & 0 & 0 \\\ 0 & \cos \alpha & -\sin \alpha & 0 \\\ 0 & \sin \alpha & \cos \alpha & 0 \\\ 0 & 0 & 0 & 1 \end{array}\right) $$
$$ \mathbf{R}_{x}(\alpha)=\left(\begin{array}{cccc} \cos \alpha & 0 & \sin \alpha & 0 \\\ 0 & 1 & 0 & 0 \\\ -\sin \alpha & 0 & \cos \alpha & 0 \\\ 0 & 0 & 0 & 1 \end{array}\right) $$
$$ \mathbf{R}_{x}(\alpha)=\left(\begin{array}{cccc} \cos \alpha & -\sin \alpha & 0 & 0 \\\ \sin \alpha & \cos \alpha & 0 & 0 \\\ 0 & 0 & 1 & 0 \\\ 0 & 0 & 0 & 1 \end{array}\right) $$

### 3D Rotation 三维旋转

##### 将任意 3D 旋转分解为三种旋转的组合

$$\mathbf{R}_{x y z}(\alpha, \beta, \gamma)=\mathbf{R}_{x}(\alpha) \mathbf{R}_{y}(\beta) \mathbf{R}_{z}(\gamma)$$

- $\alpha.\ \beta,\ \gamma$ 被称为**欧拉角**（Euler angles）。
- 经常用作飞行模拟：roll，pitch，yaw。

<div align=center>
<img width="40%" src="game\computer_graphics\image\3D旋转2.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

##### Rodrigue's Rotation Formula

绕着轴 $\mathbf{n}$ 旋转角度 $\alpha$：

$$ \mathbf{R}(\mathbf{n}, \alpha)=\cos (\alpha) \mathbf{I}+(1-\cos (\alpha)) \mathbf{n n}^{T}+\sin (\alpha)\left(\begin{array}{ccc} 0 & -n_{z} & n_{y} \\\ n_{z} & 0 & -n_{x} \\\ -n_{y} & n_{x} & 0 \end{array}\right) $$

##### Quaternion 四元数

## Viewing transformation 视图变换

三维到二维图片的变换。

### View/Camera transformation 视图/相机变换

model transformation（**模型变换**，摆造型）+ view transformation（**视图变换**，以一个合适的角度放置相机）+ projection transformation（**投影变换**）

##### 定义一个相机

- Position $\vec{e}$（相机的位置）
- Look-at/gaze direction $\hat{g}$ （相机的朝向）
- Up direction $\hat{t}$ （相机可以旋转，这里定义为朝上的向量，假定垂直于 look-at 方向）

如果相机和所有物体一起旋转，那么拍出来的图片是一样的。所以默认定义如下：
- The origin, up at Y, look at -Z。
- 视图变换操作的是相机，所有其它物体绕着相机旋转。

<div align=center>
<img width="70%" src="game\computer_graphics\image\视图变换.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

##### 变换相机

- Translate $\vec{e}$ to origin
- Rotate $\hat{g}$ to -Z 
- Rotate $\hat{t}$ to Y 
- Rotate $\hat{g} \times \hat{t}$ to X

<div align=center>
<img width="40%" src="game\computer_graphics\image\视图变换2.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

变换矩阵用 $M_{view}$ 表示，则 $M_{view}=R_{view}T_{view}$。

- Translate $\vec{e}$ to origin

$$ T_{\text {view }}=\left[\begin{array}{cccc} 1 & 0 & 0 & -x_{e} \\\ 0 & 1 & 0 & -y_{e} \\\ 0 & 0 & 1 & -z_{e} \\\ 0 & 0 & 0 & 1 \end{array}\right] $$

- Rotate $\hat{g}$ to -Z，$\hat{t}$ to Y，$\hat{g} \times \hat{t}$ to X，$R_{view}$ 不好写，所以考虑其逆变换，，即 X to $\hat{g} \times \hat{t}$，Y to $\hat{t}$，-Z to $\hat{g}$，然后再进行转置（正交矩阵的逆矩阵和它的转置矩阵相同）：

$$R_{\text {view }}^{-1}=\left[\begin{array}{cccc} x_{\hat{g} \times \hat{t}} & x_{t} & x_{-g} & 0 \\\ y_{\hat{g} \times \hat{t}} & y_{t} & y_{-g} & 0 \\\ z_{\hat{g} \times \hat{t}} & z_{t} & z_{-g} & 0 \\\ 0 & 0 & 0 & 1 \end{array}\right] \rightarrow R_{\text {view }}=\left[\begin{array}{cccc} x_{\hat{g} \times \hat{t}} & y_{\hat{g} \times \hat{t}} & z_{\hat{g} \times \hat{t}} & 0 \\\ x_{t} & y_{t} & z_{t} & 0 \\\ x_{-g} & y_{-g} & z_{-g} & 0 \\\ 0 & 0 & 0 & 1 \end{array}\right] $$

### Projection transformation 投影变换

计算机图像中的投影：
- 3D to 2D
- Orthographic projection（正交投影）
- Perspective projection（透视投影，近大远小）

<div align=center>
<img width="60%" src="game\computer_graphics\image\投影变换.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

##### 正交投影 vs 透视投影

<div align=center>
<img width="60%" src="game\computer_graphics\image\投影变换2.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

##### 正交投影

理解的一种简单方式：
- 相机位于 origin，looking at -Z，up at Y
- 扔掉 Z 坐标
- 将得到的矩形平移和缩放到 [-1, 1] × [-1, 1] 范围

<div align=center>
<img width="60%" src="game\computer_graphics\image\正交投影.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

- 更一般的，我们想要将立方的 [l, r] × [b, t] × [f, n] （far 小于 near）映射到 canonical（正则、规范、标准）立方体 [-1, 1]<sup>3</sup>

<div align=center>
<img width="60%" src="game\computer_graphics\image\正交投影2.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

变换矩阵：先**平移**中心到原点，再**缩放**（length/width/height to 2，因为是[-1, 1]）

$$ M_{\text {ortho }}=\left[\begin{array}{cccc} \frac{2}{r-l} & 0 & 0 & 0 \\\ 0 & \frac{2}{t-b} & 0 & 0 \\\ 0 & 0 & \frac{2}{n-f} & 0 \\\ 0 & 0 & 0 & 1 \end{array}\right]\left[\begin{array}{cccc} 1 & 0 & 0 & -\frac{r+l}{2} \\\ 0 & 1 & 0 & -\frac{t+b}{2} \\\ 0 & 0 & 1 & -\frac{n+f}{2} \\\ 0 & 0 & 0 & 1 \end{array}\right] $$

##### 透视投影

<div align=center>
<img width="40%" src="game\computer_graphics\image\透视投影.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

怎么做透视投影 $M_{\text {persp }}=M_{\text {ortho }} M_{\text {persp } \rightarrow \text { orths }}$：
- 先把 frustum 挤成长方体，近、远平面的 n，f，中心不变；
- 再进行正交投影。

<div align=center>
<img width="60%" src="game\computer_graphics\image\透视投影2.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

相似三角形：

<div align=center>
<img width="60%" src="game\computer_graphics\image\透视投影3.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

找到变换后的点 (x', y', z') 和原来的点 (x, y, z) 之间的关系:
$$y^{\prime}=\frac{n}{z},\  y \quad x^{\prime}=\frac{n}{z} x$$

在齐次坐标中，都乘以一个 z，点不变，

$$\left(\begin{array}{c} x \\\ y \\\ z \\\ 1 \end{array}\right) \Rightarrow\left(\begin{array}{c} n x / z \\\ n y / z \\\ \text { unknown } \\\ 1 \end{array}\right) ==\left(\begin{array}{c} n x \\\ n y \\\ \text { still unknown } \\\ z \end{array}\right) $$

$$ M_{\text {persp } \rightarrow \text { ortho }}^{(4 \times 4)}\left(\begin{array}{l} x \\\ y \\\ z \\\ 1 \end{array}\right)=\left(\begin{array}{c} n x \\\ n y \\\ \text { unknown } \\\ z \end{array}\right) $$

$$ M_{\text {persp } \rightarrow \text { ortho }}=\left(\begin{array}{cccc} n & 0 & 0 & 0 \\\ 0 & n & 0 & 0 \\\ ? & ? & ? & ? \\\ 0 & 0 & 1 & 0 \end{array}\right) $$

怎么得到第三行？
- 近平面上的所有点不变

$$ M_{\text {persp } \rightarrow \text { ortho }}^{(4 \times 4)}\left(\begin{array}{l} x \\\ y \\\ z \\\ 1 \end{array}\right)=\left(\begin{array}{c} n x \\\ n y \\\ \text { unknown } \\\ z \end{array}\right) \rightarrow \left(\begin{array}{l} x \\\ y \\\ n \\\ 1 \end{array}\right) \Rightarrow\left(\begin{array}{l} x \\\ y \\\ n \\\ 1 \end{array}\right)==\left(\begin{array}{l} n x \\\ n y \\\ n^{2} \\\ n \end{array}\right) $$

所以第三行必须是 (0, 0, A, B) 的形式。

$$ \left(\begin{array}{llll} 0 & 0 & A & B \end{array}\right)\left(\begin{array}{l} x \\\ y \\\ n \\\ 1 \end{array}\right)=n^{2} \rightarrow A n+B=n^{2}$$

- 远平面上所有点的 z' 不变

$$ \left(\begin{array}{c} 0 \\\ 0 \\\ f \\\ 1 \end{array}\right) \Rightarrow\left(\begin{array}{l} 0 \\\ 0 \\\ f \\\ 1 \end{array}\right)==\left(\begin{array}{c} 0 \\\ 0 \\\ f^{2} \\\ f\end{array}\right) \rightarrow A f+B=f^{2} $$

解出 A 和 B：

$$\begin{array}{ll} A n+B=n^{2} \\\ A f+B=f^{2} \end{array} \rightarrow \begin{array}{ll} A=n+f  \\\ B=-n f \end{array} $$

最终得到：

$$ M_{\text {persp } \rightarrow \text { ortho }}=\left(\begin{array}{cccc} n & 0 & 0 & 0 \\\ 0 & n & 0 & 0 \\\ 0 & 0 & n+f & -n f \\\ 0 & 0 & 1 & 0 \end{array}\right) $$

## Rasterization (Triangles) 光栅化（三角形）

垂直 field-of-view (fovY)（可视角度）和 aspect ratio（宽高比）。

<div align=center>
<img width="60%" src="game\computer_graphics\image\光栅化.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>

如何将 fovY 和宽高比转换为 l, r, b, t？

<div align=center>
<img width="60%" src="game\computer_graphics\image\光栅化2.png"/>
<!-- <div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div> -->
</div>
