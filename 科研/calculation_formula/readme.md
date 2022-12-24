## 自旋电子学中的公式计算/推导

### 磁各向异性

各向异性场（anisotropy field）：
$$H_{\rm{an}} = \mu_0 H_{\rm{k}}$$

有效的磁各向异性能量密度（effective magnetic anisotropy energy density）：
$$K_{\rm{u}} = \frac{\mu_0 M_{\rm{S}} H_{\rm{k}}}{2}$$

其中，
$$H_{\rm{k}} = H_{\rm{sat}} + 4 \pi M_{\rm{S}}$$
这里，$H_{\rm{sat}}$ 是难磁化轴饱和场。

##### 参考文献：
1. [Appl. Phys. Lett. 109, 232403 (2016)](https://doi.org/10.1063/1.4971393)

### 畴壁（domain wall，DW） & DM 相互作用（Dzyaloshinskii-Moriya Interaction，DMI）

畴壁形状各向异性场（DW shape anisotropy field）:

$$\mu_0 H_{\rm{DW}} \approx \frac{M_{\rm{S}} t_{\rm{FM}} \ln (2)}{\pi \Delta}$$

DMI 交换常数 $D$ 的大小（magnitude of the DMI exchange constant）：
$$|D| = \mu_0 M_{\rm{S}} \Delta |H_{\rm{DMI}}|$$

其中，$\Delta$ 是畴壁宽度：
$$\Delta = \sqrt{\frac{A}{K_{\rm{u}}}}$$

这里，$A$ 是交换刚度常数（exchange stiffness constant），$K_{\rm{u}}$ 是有效的磁垂直各向异性（PMA）能量密度。

##### 参考文献：
1. [Phys. Rev. B 93, 144409 (2016)](https://doi.org/10.1103/PhysRevB.93.144409)
2. [Europhys. Lett. 100, 57002 (2012)](http://doi.org/10.1209/0295-5075/100/57002)

### SOT 有效场与自旋霍尔角

SOT 有效场与自旋霍尔角的关系：
$$\mu_0 |H_{\rm{SL}}| = \frac{\hbar \theta_{\rm{SH}}}{2 |e| M_{\rm{S}} t_{\rm{FM}}} |j_{\rm{e}}|$$

其中，SOT 效率（SOT efficiency）：
$$\chi = \frac{H_{\rm{SL}}}{|j_{\rm{e}}|} = \frac{\hbar \theta_{\rm{SH}}}{2 |e| \mu_0 M_{\rm{S}} t_{\rm{FM}}}$$

这里，$\hbar$ 是普朗克常数，$\theta_{\rm{SH}}$ 是自旋霍尔角，$|e|$ 是电子电荷大小，$|j_{\rm{e}}|$ 是电流密度大小。

##### 参考文献：
1. [Appl. Phys. Lett. 109, 232403 (2016)](https://doi.org/10.1063/1.4971393)
2. [Nat. Mater. 12, 611–616 (2013)](https://doi.org/10.1038/nmat3675)

### DMI effect on Néel domain wall (DW)

#### DW creep scaling law

DW speed $V$
$$V = V_0 e^{-\alpha H_z^{-\mu}} \tag{eq.1}$$
, where $V_0$ is the characteristic speed, and $\alpha$ is a scaling constant. The creep scaling exponent $\mu$ is 1/4.

The scaling constant $\alpha$ is originally defined as
$$\alpha = \frac{U_{\rm{C}} H_{\rm{crit}}^\mu}{k_{\rm{B}} T}, \tag{eq.2}$$
where $U_{\rm{C}}$ is the energy constant, $H_{\rm{crit}}$ is the critical magnetic field, and $k_{\rm{B}} T$ denotes the thermal fluctuation energy.

$U_{\rm{C}}$ and $H_{\rm{crit}}$ are defined as
$$U_{\rm{C}} \equiv \left(\frac{\mu u_\rm{C}}{2(\mu + 1)\xi}\right)^\mu \frac{\sigma_{\rm{DW}} t_{\rm{f}} u_{\rm{C}}^2}{(1 + \mu) L_{\rm{C}}} \tag{eq.3.1}$$
$${\rm{and}}\ H_{\rm{crit}} \equiv \frac{\sigma_{\rm{DW}} \xi}{M_{\rm{S}} L_{\rm{C}}^2},  \tag{eq.3.2}$$
respectively, where $\xi$ is the correlation length of the disorder potential, $u_\rm{C}$ is the roughness of the DW segment with length $L_{\rm{C}}$, and $L_{\rm{C}}$ is the Larkin length that is the characteristic length of rigid microscopic DW segment. $M_{\rm{S}}$, $t_{\rm{f}}$, $\sigma_{\rm{DW}}$ are the saturation magnetization, the film thickness, and the DW energy density per unit area, respectively.

$L_{\rm{C}}$ is given by
$$L_{\rm{C}} = \left(\frac{\sigma_{\rm{DW}}^2 t_{\rm{f}}^2 \xi^2}{\gamma}\right)^{\frac{1}{3}}, \tag{eq.4}$$
where $\gamma$ is the pinning strength of the disorder. By adopting eq.4 into eq.3.1, $\alpha$ can be written as a function of $\mu$, $\gamma$, $u_{\rm{C}}$, $\xi$, $t_{\rm{f}}$, $k_{\rm{B}} T$, $M_{\rm{S}}$, and $\sigma_{\rm{DW}}$. Because all other parameters except $\sigma_{\rm{DW}}$ do not depend on a magnetic field, the field dependence of $\alpha$ can be solely attributed to the field dependence of $\sigma_{\rm{DW}}$, i.e., 
$$\alpha(H_x) \varpropto \left(\sigma_{\rm{DW}} (H_x) \right)^{\frac{1}{4}} \ {\rm{or}}\  \alpha(H_x) = \alpha(0)\left(\frac{\sigma_{\rm{DW}} (H_x)}{\sigma_{\rm{DW}} (0)} \right)^{\frac{1}{4}}.  \tag{eq.5}$$

#### Derivation process
Let 
$$H_z = H_z^* f(H_x), \tag{eq.1}$$
where $H_z^*$ denotes the value of $H_z$ at $H_x = 0$. The DW speed with $H_x \ne 0$ also follows an identical creep scaling law as given by
$$V = V_0 e^{-\alpha^* H_z^{-\mu}}, \tag{eq.1}$$
except $\alpha$ is replaced by $\alpha^*$, which is defined as
$$\alpha^* \equiv \alpha f^{\mu}(H_x)$$
