# 1 神经形态器件的机制和材料

神经形态器件可以大致分为**九大类**：

<div align=center>
<img width="80%" src="scientific_research\papers_reading\neuromorphic_computing\image\九类神经形态器件.png"/>
</div>

> J. Zhu, T. Zhang, Y. Yang, R. Huang, [A comprehensive review on emerging artificial neuromorphic devices](https://doi.org/10.1063/1.5118217). Appl. Phys. Rev. 7,  (2020).

## 1.1 基于阴离子迁移（anion migration）的系统

**阴离子迁移**是在神经形态器件中观察到的最常见的机制之一，特别是对于**氧化物基忆阻器**。<mark>阴离子迁移机制的基本思想是利用外部刺激，如电场或温度梯度，来驱动阴离子在材料内部移动，并最终导致材料特性的可测量的变化，如电阻</mark>。典型的阴离子是**氧**、**硫**和**硒化物离子**。在一些特殊情况下，也会使用**有机阴离子**。根据外部刺激过程中和刺激后的材料结构，可以将基于阴离子迁移的器件分为两种类型：即**细丝型**和**非细丝型**。

### 1.1.1 细丝型

基于阴离子迁移的细丝器件有一个简单的**金属/绝缘体/金属**（M/I/M）三明治结构。<mark>当对阳极施加适当的电压时，绝缘层的电导率会发生显著变化</mark>。即使在电压脉冲被移除后，这样的电阻变化也能持续。因此，自 20 世纪 60 年代以来，这种器件一直被用作存储器，被称为**电阻式随机存取存储器（简称阻变存储器，resistive random access memory，ReRAM）**。因此，**绝缘层也被称为电阻开关层**。RRAMs 具有低于 **1 ns** 的**快速写入时间**，超过 **10<sup>12</sup>** 个周期的**高耐久性**，在 85­°C 下超过 **10** 年的**良好保持**，并且**可扩展性**小于 **10 nm**。在这些单元中，<mark>两个金属电极之间形成了一条导电细丝，它由一个氧空位浓度增加的区域组成</mark>。<mark>由于其记忆效应和与忆阻器方程的对应关系，细丝型 ReRAM 也是在 2008 年发现的第一种类型的忆阻器</mark>，并从那时起作为一种典型器件应用于神经形态计算。在细丝型器件中观察到两种典型的开关特性，**双极性开关（bipolar switching）**和**单极性开关（unipolar switching）**。对于双极性开关，用于诱导 **SET** 和 **RESET** 操作的电压脉冲是不同极性的，而对于单极性开关，可以用相同极性的电压脉冲进行 SET 和 RESET 操作。这揭示了用于这两种不同类型的开关的不同动力学，分别是**价态变化机制（valence change mechanism, VCM）**和**热化学机制（thermochemical mechanism, TCM）**，其 RESET 过程可能非常不同。

<div align=center>
<img width="100%" src="scientific_research\papers_reading\neuromorphic_computing\image\基于阴离子迁移的忆阻器.png"/>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 基于阴离子迁移的忆阻器。</div>
</div>

> J. Q. Wu, J. B. Cao, W. Q. Han, A. Janotti, H. C. Kim. [Functional metal oxide nanostructures [M]](https://doi.org/10.1007/978-1-4419-9931-3). *Springer Science & Business Media*, 2011.

上图显示了基于阴离子迁移的细丝型器件的工作，可以描述如下：<mark>（1）一个 FORMING（或 SET）过程，将器件从其原始状态初始化到低电阻状态（low resistance state, LRS）和（2）一个 RESET 过程，将器件从 LRS 切换到高电阻状态（high resistance state, HRS）</mark>。之后，该器件在出现故障之前**可以在 HRS 和 LRS 之间进行切换**，这通常是在超过 **10<sup>9</sup>** 个开关周期之后。

<div align=center>
<img width="50%" src="scientific_research\papers_reading\neuromorphic_computing\image\电子传导机制.png"/><br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 导电机制：（1） 肖特基势垒隧穿，（2）Fowler-Nordheim 隧穿，（3）直接隧穿，（4）Poole-Frenkel 发射，（5）欧姆传导，（6）空间电荷限制传导，（7）离子传导，（8）最近邻跳跃，（9）Mott 变程跳跃和（10）陷阱辅助隧穿。</div>
</div>

工作过程中的**电子传导机制**可能非常复杂。根据 Lim 和 Ismail 的研究，在 MIM 结构中通常存在九种传导机制，其中有三种是**电极限制的**：（1）**肖特基发射**（Schottky emission）；（2）**福勒-诺德海姆隧穿**（Fowler-Nordheim tunneling, F-N）；和（3）**直接隧穿**（direct tunneling）；而其他六种是**体限制的**：（1）**蒲尔-弗朗克发射**（Poole-Frenkel emission, P-F）：；（2）**欧姆传导**（Ohmic conduction）；（3）**空间电荷限制传导**（space-charge-limited conduction, SCLC）；（4）**离子传导**（ionic conduction）；（5）**跳跃传导**（hopping conduction）；和（6）**陷阱辅助隧穿**（trap-assisted tunneling, TAT）。基于阴离子迁移的神经形态器件中使用的真正机制可以是这些详细机制的组合。根据下表，<mark>不同的机制对施加的电场或局部温度具有完全不同的电流依赖性</mark>。因此，通过在 **ln(I) vs ln(V) 图**上绘制 **I-V 特性**，可以大致弄清在工作过程中哪种或哪几种传导机制占主导地位。

<div align=center>
<img width="100%" src="scientific_research\papers_reading\neuromorphic_computing\image\电子传导机制2.png"/>
</div>

> E. W. Lim, R. Ismail, [Conduction Mechanism of Valence Change Resistive Switching Memory: A Survey](https://doi.org/10.3390/electronics4030586). *Electronics* **4**, 586 (2015).

通过上述方法，研究了**不同材料系统中 HRS 和 LRS 的传导机制**。典型的机制和相关的材料系统如下所示：

1. <mark>当热激活的电子越过能量势垒注入到氧化物的导带时，就会发生肖特基发射。这是氧化物中最常见的传导机制之一，特别是在相对较高的温度下</mark>。在肖特基主导的过程中，$\ln (J) \propto E^{1/2}$。
2. <mark>Fowler-Nordheim（F-N）隧穿发生在较高的电场下，并且经常在相对较厚的氧化层中观察到。电子会从阴极隧穿进入绝缘层的导带，然后在外加电场的作用下漂移到阳极</mark>。由 F-N 隧穿主导的器件如下：$\ln \left(J / E^{2}\right) \propto E^{-1}$。
3. <mark>直接隧穿也发生在较高的电场下，在这个过程中，电子直接隧穿穿过绝缘层，从阴极传输到阳极</mark>。**等效氧化层厚度**（equivalent oxide thickness, EOT，或即 $t_{\mathrm{ox}, \mathrm{eq}}$）在决定直接隧穿电流的强度方面起着主导作用。在 EOT 相对较小的器件中，直接隧穿电流将起到漏电流的作用，它降低了 HRS 电阻和器件的开/关比。
4. <mark>当被捕获的电子被激发到氧化物的导带时，就会发生 Poole-Frenkel 发射。电场降低了电子的库仑势垒，随后增加了电子从陷阱中被热激发出来的概率</mark>。具有 P-F 发射机制的器件在 $\ln (I/E)$ 和 $(E^{1/2}/T)$ 之间呈现线性关系。
5. <mark>在许多材料系统中，导电细丝形成后，欧姆传导是常见的 LRS 传导方式</mark>。它也可以是低电压范围内 HRS 的传导机制，因为只要施加外部电场，就会因热激发而产生少量的移动电子，并产生漏电流。
6. **空间电荷限制传导**由三部分组成：**欧姆区**（$I \propto V$），**Child 平方律区**（$I \propto V^2$），以及**高电场区的陡然增加**。<mark>在低场区，传导机制由氧化层中热产生的自由电子主导。当电场超过设定电压的平方律时，电极注入的电子密度逐渐超过平衡浓度并主导传导</mark>。（$I \propto V^2$）区域被称为陷阱未填满的 SCLC **区域**，而陡坡区域通常指的是**陷阱填满的 SCLC 区域**。因此，如果电极触点是高载流子注入的，SCLC 传导的概率通常更高。**只要在低场下观察到欧姆传导**，然后**在高场下观察到电流密度的幂律依赖性**（$I \propto V^2$），就可以很容易地确定这一机制。
7. 当施加电场时，也可以诱导**离子传导**。在器件结构中可以观察到**漂移-扩散**过程。<mark>如果氧化还原过程发生在电极/绝缘体界面，电子和空穴可以交换阳离子和阴离子携带的正/负电荷，这导致了恒定电流。在大多数模型中，没有考虑离子传导引起的电流，因为采用的是惰性电极，并且假设在电极/绝缘体界面没有发生氧化还原过程</mark>。
8. <mark>跳跃传导是指电子通过隧穿效应从一个陷阱位置跳到其他陷阱位置</mark>。基本上，有两种主要的跳跃传导机制，即**最近邻跳跃**（nearest neighbor hopping, NNH）和**莫特变程跳跃**（Mott variable range hopping, VRH）。NNH 也被称为**固程跳跃**（fixed range hopping, FRH），它通常在各种氧化物基器件中观察到。Mott VRH 描述了具有局域电荷载流子态的强无序系统中的电子跳跃行为，并被认为是**半导体导电细丝**中的主要传导机制。<mark>与 NNH 相比，VRH 使电子能够跳入更远、更低的能量陷阱中。NNH 通常在较高的工作温度下发生，而 VRH 在较低的工作温度下占主导地位</mark>。
9. <mark>陷阱辅助隧穿是指由电介质中的缺陷辅助的隧穿。在陷阱的辅助下，电子通过两步过程从阴极隧穿到阳极，在此过程中，电子首先从阴极被捕获到陷阱中，然后发射到阳极</mark>。

> 只要是穿过氧化物和半导体的电流都被称为漏电流。

所有上述机制都可以共存，在特定阶段，其中一种机制将占据主导地位。从 $\ln (I)$ vs $\ln (V)$ 图中可以看到，在不同的电压范围内，两种甚至三种不同的机制在 HRS 或 LRS 中占主导地位，这是很常见的。

基于**细丝阴离子迁移**的器件的 **FORMING 过程**已被证实是**由应力诱导的缺陷引起的时间依赖的介电击穿**（time-dependent dielectric break-down, TDDB），这导致单元电阻从 HRS 下降到 LRS。<mark>在高电场（>10 MV/cm）下，氧原子从绝缘层晶格中被击出，并向阳极漂移。同时，氧空位（可以看作是一种缺陷）产生并在阴极附近积累。局域的氧空位形成亚氧相导电细丝，它连接着阳极和阴极，并最终导致从 HRS 到 LRS 的电阻转变。FORMING 过程是必要的，可以在绝缘层中引入足够的氧离子和氧空位，以确保电阻性开关过程可以发生，尤其是对于通过原子层沉积（atom layer deposition, ALD）制造的器件（拥有几乎完美的晶体结构，并且没有太多的缺陷）</mark>。**高分辨率透射电子显微镜**（high-resolution transmission electron microscopy, HR-TEM）、**选区衍射**（selective area diffraction, SAED）图案、和 **X 射线衍射**（x-ray diffraction, XRD）观察都证实了 **FORMING 过程**和形成的**导电细丝**，如 TiO<sub>2</sub> 层中的有序 Ti<sub>4</sub>O<sub>7</sub> Magnéli相导电细丝，和 WO<sub>3</sub> 层的 WO<sub>x</sub> 导电细丝。

显然，<mark>在实际应用中，不希望有一个大的 FORMING 电压</mark>。因此，人们为实现所谓的 “**forming-free**” 器件已经做出了巨大的努力。结果表明，<mark>对于基于阴离子迁移的细丝器件，FORMING 电压与氧化膜的厚度呈线性关系</mark>。因此，**较薄的氧化膜**，例如 ∼3 nm，可以有效降低甚至消除 FORMING 电压。人们还发现，**控制沉积过程中的退火环境**也有助于降低 FORMING 电压，这是因为**在沉积的材料薄膜中引入了氧空位**。**结构优化**，如**双层结构**也被引入。

通过**导电原子力显微镜**（conductive atomic force microscopy, C-AFM）在各种基于阴离子迁移的器件中观察到了局域的 CF 路径，证实了细丝导电机制。**原位静电力显微镜**（electro-static force microscopy, EFM）也被用于揭示导电细丝在 SET 过程中的 FORMING 动力学。通常，沉积的 **RRAM 氧化物薄膜**是**无定形的**或**多晶的**，**导电细丝优先沿着晶界生成**，如 C-AFM 所示。除了上述方法，**扫描隧道显微镜**（scanning tunneling microscopy, STM）、**原位和非原位 TEM** 和 **X 射线光谱**也被报道用来研究 TiO<sub>x</sub>、TaO<sub>x</sub>、HfO<sub>x</sub>、SrRuO<sub>3</sub> 和氧化石墨烯等忆阻材料系统内的**氧离子动力学**。

<mark>从 LRS 到 HRS 的转换可以通过导电细丝的断裂得到强有力的解释</mark>。然而，基于不同的机制，RESET 过程中的电阻开关行为可能会有很大的不同。<mark>对于基于价变机制的器件，需要在阳极上施加负电压脉冲，这将产生与 SET 过程相反的离子迁移过程，中和氧空位，并将亚化学计量区域转换到化学计量区域。通常情况下，导电细丝不能被完全氧化。因此，氧化层的电阻不能恢复到其初始状态</mark>。

<mark>与 FORMING 过程类似，断裂的细丝可以通过阳极上的正电压脉冲进行重整，但要比 FORMING 电压低得多，这是因为 RESET 过程后的导电细丝没有完全溶解</mark>。实际上，剩余的**缺陷富集区域**通常被称为“**虚拟电极**”，有助于导电细丝的形成。在过去的几十年里，**动态 RESET 过程的物理模型**也被开发出来。

<mark>对于基于热化学机制的器件，细丝断裂是焦耳热的结果，它与电压极性没有关系，仅基于电流强度</mark>。因此，可以获得**单极电阻开关**。**热化学电阻开关机制**首次在 **NiO 基器件**中发现。 NiO 基器件中的 SET 过程与 VCM 器件非常相似，因为氧离子和氧空位会发生迁移，并逐渐形成导电细丝。<mark>与价变机制相反，基于热化学机制的器件的 RESET 过程主要依靠 RESET 电流产生的焦耳热，因为较高的温度会增加离子迁移率，从而加速氧空位的扩散，一旦温度足够高，最终会导致导电细丝的断裂。导电细丝发生溶解，并在中间部分断裂，这是由于器件结构造成的热耗散困难，中间部分的温度最高</mark>。这样的断裂过程与基于价变机制的器件完全不同，<mark>在价变机制中，细丝会在最薄的部分断裂，那里的电场最高</mark>。由于 RESET 脉冲产生的焦耳热与 RESET 电压的极性没有直接联系，只依赖于 RESET 电流的大小，所以 **RESET 电压可以具有与 SET 电压相同的极性，这导致了单极行为**。NiO、CuO<sub>x</sub> 和 ZnO 已被证明是表现出显著的基于 TCM 的电阻开关行为的材料。

**TCM** 在电阻开关过程中起着重要的作用，并经常与其他机制，如**价变机制**和**电化学金属化机制**共存。**然而，由于难以精确控制器件的 RESET 温度，以及产生的焦耳热，在 TCM 器件中经常观察到较大的差异**。因此，TCM 器件不是目前研究和应用的兴趣所在。

各种材料，如**金属氧化物**（metal oxides）、**2D 过渡金属二卤化物**（transition metal dichalcogenides, TMDC）材料、**钙钛矿**（perovskite）材料、和**有机材料**（organic materials），已被用作基于忆阻器的人工突触的构建块。

**二元氧化物类**，包括 HfO<sub>2</sub>、ZnO、NiO、TiO<sub>2</sub>、WO<sub>3</sub> 和 TaO<sub>x</sub>，由于其**一般的 CMOS 兼容性**、**多态开关**和**简单的化学成分**而特别令人感兴趣。PdO 和 GaO<sub>x</sub> 薄膜也被用作电阻开关层。也有工作研究了 TaOx 基器件中的氧百分比依赖性。此外，已经报道了 Pt/HfO<sub>x</sub>/TiO<sub>x</sub>/HfO<sub>x</sub>/TiO<sub>x</sub>/TiN 叠层结构，与单层结构相比，它具有更高的开/关电流比和更好的稳定性。WO<sub>3</sub> 是另一种最近在神经形态计算方面备受关注的材料。据报道，WO<sub>3-x</sub> 基器件对电压脉冲刺激的响应可以**生动地模拟生物系统中从短期记忆到长期记忆的转变**，证明它是一种很有前景的神经形态计算的候选材料。也有工作报道了在柔性衬底上制备 WO<sub>3</sub> 的研究。

### 1.1.2 非细丝型

<mark>细丝形成和断裂的随机性给细丝型器件尺寸的进一步缩小带来了许多困难</mark>。因此，近年来非细丝型的器件更受欢迎，特别是**基于界面反应的器件**，因为它们已经被证实了**良好的器件间的均匀性**。近年来，它们已经得到了很多关注。

#### 1. 界面反应

<div align=center>
<img width="100%" src="scientific_research\papers_reading\neuromorphic_computing\image\界面反应.png"/><br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> TiN/PCMO/Pt 结器件到 HRS 的原位 TEM 电阻开关。</div>
</div>


> K. Baek, S. Park, J. Park, Y. M. Kim, H. Hwang, S. H. Oh, [In situ TEM observation on the interface-type resistive switching by electrochemical redox reactions at a TiN/PCMO interface](https://doi.org/10.1039/C6NR06293H). *Nanoscale* **9**, 582 (2017).g

一种类型的非细丝器件是基于**界面氧化还原反应**。这种反应涉及**两个材料层之间的氧空位交换**。一个典型的例子是**基于电极/氧化物界面上发生的氧化还原过程的忆阻器件**，这会造成**界面层的不同厚度**，从而导致**不同的电阻状态**。<mark>由于这种氧化还原过程均匀地发生在界面上，它避免了随机的细丝形成过程，并确保了良好的器件-器件和周期-周期的均匀性</mark>。<mark>对于 Pr<sub>0.7</sub>Ca<sub>0.3</sub>MnO<sub>3</sub>(PCMO)/TiN 基器件，在高电阻状态下，在 PCMO/TiN 界面上会形成一个 TiO<sub>x</sub>N<sub>y</sub> 氧化层，该氧化层起到电子屏障的作用，限制流经该器件的电流。当向阳极施加正电压时，TiO<sub>x</sub>N<sub>y</sub> 层内部氧原子会被还原，其厚度减少，电导率提高，进入低电阻状态，并在 TiO<sub>x</sub>N<sub>y</sub> 层中产生可移动的氧离子。然后这些氧离子会在局部电场的驱动下从 TiO<sub>x</sub>N<sub>y</sub> 层漂移到 PCMO 层，并氧化 PCMO</mark>。如果向阳极施加负电压，一个相反的氧化还原过程就会发生，从而增加 TiO<sub>x</sub>N<sub>y</sub> 层的厚度，并将器件从低电阻状态转变为高电阻状态。

用于**非细丝型 VCM 器件**的典型材料系统是 Ti/Pr<sub>0.7</sub>Ca<sub>0.3</sub>MnO<sub>3</sub>(PCMO)、ZrO<sub>2</sub>:Y (YSZ)/PCMO 和 InGaZnO (IGZO)/α-IGZO、TiN/TiO<sub>x</sub>、Al/a-TiO<sub>2</sub> 和 Ti/TiO<sub>2</sub>。

<mark>通过使用基于界面反应的 VCM 器件，可以极大地改善器件的均匀性，这是因为可以成功地避免导电细丝的随机形成和断裂过程</mark>。此外，这种基于非细丝型 VCM 的人工突触在整体上也显示出更多的权重状态。然而，<mark>它们在对称性和线性度方面仍然存在局限性，这对于人工神经网络的在线训练是不利的</mark>。

## 1.2 基于金属离子迁移（metal ion migration）的系统

用于神经形态器件的另一种主要工作机制是**金属离子迁移机制**。在基于这种机制的器件中，<mark>电阻变化是通过金属离子的迁移和电极之间金属导电细丝的形成来实现的</mark>。通常情况下，基于金属离子迁移的器件也具有**两端的金属/电解质/金属**结构。与基于阴离子迁移的器件相反，在这些类型的器件中，<mark>通常采用活性金属作为阳极材料或掺杂到电解质材料中，以确保金属离子在电场控制下迁移，而阴极材料仍然可以是惰性金属、导电氮化物和氧化物</mark>。<mark>因为电化学反应，特别是在电极和电解质中金属原子和离子的氧化还原反应，是器件工作的关键</mark>。基于金属离子迁移的器件通常被命名为“**电化学金属化（electrochemical metallization, ECM）单元**”。考虑到**金属细丝在低电阻状态下桥接阳极和阴极**，这种类型的器件也被称为**导电桥随机存取存储器**（conductive bridge random access memory, CBRAM）。此外，一种特殊类型的 ECM 器件被称为“**原子开关**”，最初是由于在器件结构的纳米间隙中形成了原子细丝。

目前，ECM 器件因其**超低的工作电压**、**大的开/关电流比**、和**大规模集成的潜力**而被广泛研究，成为神经形态计算的一个有前景的候选器件。

<mark>一般来说，ECM 器件的工作还需要一个 FORMING 过程，以将金属离子纳入电解质层，一个 SET 过程，以确保金属离子迁移和导电细丝的形成，从而导致从高电阻状态切换到低电阻状态，以及一个 RESET 过程，以溶解细丝并将器件从 LRS 切换到 HRS</mark>。有时可以用特殊的结构设计或用特定的材料系统来避免 FORMING 过程。

在<mark> FORMING 过程和 forming-free 器件的 SET 过程中，阳极材料会发生氧化，将活性金属原子变成离子，这些离子可以在电解质内迁移</mark>。在阳极上的这种电化学反应已经被测量出来，并通过**密度泛函理论（density functional theory, DFT）**计算与各种计算方法进行了研究。以 Ag(111)/TiO<sub>2</sub> **金红石和锐钛矿界面**为例（Ag 和 TiO<sub>2</sub> 分别是 ECM 单元中阳极和电解质的典型材料），**DFT 计算表明，由于在相对较低的温度下的热力学限制，离子跨越 Ag/TiO<sub>2</sub> 界面的迁移可能很困难**。然而，一旦界面上的电场足够大，例如由 FORMING 电压引入的电场，Ag 离子和原子可以扩散穿过界面势垒，融入 TiO<sub>2</sub> 中，并将价电子转移到宿主晶体中而被电离，形成 Ti<sup>3+</sup> 态。**融入后，Ag 原子可以稳定在间隙位置或 Ti 的替代位置上**，尽管前者根据热力学定律更有利，并能实现离子迁移。

应该指出的是，<mark>氧化过程可以在阳极/电解质的任何地方发生</mark>。最近的研究表明，利用石墨烯的抗渗性，结构缺陷石墨烯（离散缺陷石墨烯）可以很好地控制阳离子注入电解质层的路径，从而控制细丝的尺寸和质量。

<div align=center>
<img width="100%" src="scientific_research\papers_reading\neuromorphic_computing\image\金属离子迁移.png"/><br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 在 SiN$_\rm{x}$ 膜上制备的 SiO<sub>2</sub> 基平面器件的 TEM 图像。</div>
</div>

> Y. C. Yang, P. Gao, S. Gaba, T. Chang, X. Q. Pan, W. Lu, [Observation of conducting filament growth in nanoscale resistive memories](https://doi.org/10.1038/ncomms1737). *Nat. Commun.* **3**, 732 (2012).<br>

<mark>在典型的 ECM 单元中，在引入阳离子之后，向阳极施加正电压，会持续氧化阳极表面，提供足够的阳离子以形成导电细丝，而阴极/电解质界面上可能同时发生反应以保持电荷中性。积累在阴极表面的阳离子将被还原成金属离子，并变大。在局部电场的控制下，阳离子会迁移并逐渐形成导电细丝，导致电流突然增加，从而完成从高电阻状态到低电阻状态的 SET 过程</mark>。【1】

与第 1 节中介绍的传导机制相同，ECM 单元中的基本传导机制主要涉及欧姆传导和空间电荷限制传导（SCLC）。

<div align=center>
<img width="100%" src="scientific_research\papers_reading\neuromorphic_computing\image\金属离子迁移3.png"/><br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> Ag 细丝 ECM 单元的电阻性开关特性。</div>
</div>

> H. F. Ling, M. D. Yi, M. Nagai, L. H. Xie, L. Y. Wang, B. Hu, W. Huang, [Controllable Organic Resistive Switching Achieved by One-Step Integration of Cone-Shaped Contact](https://doi.org/10.1002/adma.201701333). *Adv. Mater.* **29**, 1701333 (2017).

上图显示了一个典型的电阻开关特性。<mark>在 ECM 单元中通常会观察到突然的 SET 和 RESET 过程，因为金属丝电导和电子跳跃电导之间的差异可能是很大。通过将线性图转为对数图，可以通过拟合曲线的斜率得到高电阻状态（HRS）和低电阻状态（LRS）的传导机制</mark>。【2】

**HRS 拟合结果表明，电荷输运行为与陷阱控制的空间电荷限制传导（SCLC）模型一致**。SCLC 模型包括三个不同的导电区域：

（1）**低电压区域**，I-V 曲线的斜率约为 **1**（I/V），对应于欧姆传导机制；<br>
（2）**过渡区域**，斜率增加到 **2**，这遵循 child 平方定律，对应于陷阱未填满的 SCLC 模型；<br>
（3）**以电流急剧增加为标志的区域**，该区域的斜率约为 **9**，表明从陷阱未填满的 SCLC 过渡到陷阱填满的 SCLC。

LRS 表现出欧姆传导行为，斜率约为 1。结果表明，**高度透明的 RRAM 的传导行为是由 SCLC 和局部细丝路径的形成所控制的**。

<mark>ECM 单元内的导电细丝通常可以完全溶解，这导致了较大的开/关比</mark>。在 ECM 单元中可以实现大于 **$10^6$ 的高开/关电流比**。同时，LRS 主要取决于所形成的细丝的导电性，而 **ECM 单元的 HRS 则强烈地依赖于超薄尺度的氧化物厚度**。因此，<mark>通过设计电解质层的氧化物厚度，可以调整合适的开/关比</mark>。

由于与 VCM 器件相比，**ECM 单元开关所需的电场相对较低**（$\sim$ 1 MV/cm），在纳米尺度上，工作电压可以非常低。**超低的工作电压**（&lt;100 mV）已被许多研究组报道。实现低于 **0.7 V**，甚至 **0.5 V** 的工作电压是很常见的，这对**超低功率应用**来说是很好的。然而，<mark>超低工作电压的一个主要问题是变化幅度大，往往可以达到 50% 以上</mark>。根据最近的一项工作报道，一个具有超低工作电压的器件的 V<sub>set</sub> 分布在 40 mV 到 90 mV 的范围内，V<sub>reset</sub> 分布在 -10 mV 到 -60 mV 的范围内。如此宽的分布范围可能难以实现稳定的工作。

**能耗**也是神经形态器件的一个重要判断因素，因为人们希望能耗可以与人脑相当。由于 ECM 单元的工作电压极低，其能耗可以非常低。每个尖峰的亚皮焦能耗已被普遍报道，**最先进的功耗可以低至 100 aJ $\sim$ 1 fJ/spike**。

电阻开关行为可分为**易失性阈值开关**（threshold switching, TS）和**非易失性存储开关**（memory switching, MS）。<mark>在 MS 模式下，在去除电压刺激后，LRS 和 HRS 都能在 85℃ 下维持 104 秒以上，即在室温下 10 年，显示出良好的保留特性。然而，在 TS 模式下，一旦施加的电压下降，并且低于临界值，LRS 将会下降到 HRS。MS 器件可用于非易失性数据存储，而 TS 器件可作为选择器与存储单元串联，以抑制交叉阵列中的串扰效应</mark>。

上文强调的**宽 SET 电压分布**是低工作电压 ECM 单元的主要挑战，这与**导电细丝的随机形成**密切相关。<mark>由于随机软击穿，导电路径在开关材料中随机形成、断裂和分布，从而破坏了器件的可重复性</mark>。已有报道称，有一些方法可以改善这个问题，如**杂质掺杂**、**界面工程**、**S 型负差分电阻集成**、和**纳米粒子的掺入**。**湿度**是另一个对氧化物基电阻开关系统的开关特性具有重要意义的因素。ECM 单元中的 H<sub>2</sub>O 可以确保在一个相对较低的电压下的 FORMING 过程，并提高 ECM 单元的电流。

如前所述，导电细丝的随机分布可能会导致 ECM 单元的巨大变化。处理这种问题的一个有效方法是**在 ECM 单元内插入一个界面层**。<mark>超薄的 AlN 或 Al<sub>2</sub>O<sub>3</sub> （通常为 $\sim$2 nm）经常被用作界面层，它可以降低 SET/RESET 电压，并通过降低 HRS 来增加 ON/OFF 比</mark>。此外，有效的电阻开关区域受到界面层的限制，因为在 RESET 过程后，在界面层中可以找到残留的细丝，它限制了接下来可以形成细丝的位置。因此，具有界面层的器件拥有尖锐的 V<sub>set</sub> 和 V<sub>reset</sub> 分布，导致稳定的电阻特性。然而，这些优点的权衡是 **FORMING 电压的略微增加**。

## 1.3 基于相变机制（phase change mechanism）的系统

在所有的神经形态器件中，**相变存储**是最成熟的类型，也是已经**商业化的少数类型之一**。发明于 1960s 的**相变材料**得到了深入的研究，既可作为**数字多功能光盘**（DVD）的**光学介质**，也可作为**非易失性存储器**的候选材料，这些材料表现出**良好的稳定性**以及**高密度和超大规模集成的潜力**。用于相变存储器制造的材料系统也引起了极大的关注。近年来，人们对具有**更快结晶速度**的材料进行了研究，取得了丰硕的成果。同时，为了提高相变存储器的性能，还引入了新的器件结构。

在本节中，将讨论**相变存储器基本的工作原理和性能**。还讨论了**材料系统**和**器件结构的优化**，为今后的研究和制造提供了指导。

<div align=center>
<img width="50%" src="scientific_research\papers_reading\neuromorphic_computing\image\相变存储器1.png"/><br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 相变存储器。</div>
</div>

> H. S. P. Wong, S. Raoux, S. B. Kim, J. L. Liang, J. P. Reifenberg, B. Rajendran, M. Asheghi, K. E. Goodson, [Phase change memory](https://doi.org/10.1109/JPROC.2010.2070050). *Proc. IEEE* **98**, 2201 (2010).

上图（左）显示了一种常见的 PCM 单元。PCM 利用了相变材料的**结晶相（低电阻率）**和**非晶相（高电阻率）**之间的大的**电阻率差异**。PCM 的 **SET** 和 **RESET** 状态分别是指**低电阻**和**高电阻**状态。<mark>制备态的相变材料处于结晶的、低电阻状态，因为（BEOL）金属互连层的加工温度足以使相变材料结晶</mark>。<mark>为了使 PCM 单元重置为非晶相，通过在短时间内施加大电流脉冲，首先熔化编程区域，然后快速淬火。这样做会在 PCM 单元中留下一个非晶态、高电阻材料区域。这个非晶区域与 PCM 所有结晶区域相串联，并有效地决定了 PCM 单元在顶部电极触点（top electrode contact, TEC）和底部电极接触（bottom electrode contact, BEC）之间的电阻</mark>。<mark>为了将 PCM 单元 SET 为结晶相，施加一个中等电流脉冲，使编程区域在结晶温度和熔化温度之间的温度下退火，时间长到足以使其结晶</mark>。为了**读取编程区的状态**，通过传递**足够小的电流**来测量单元的电阻，以免干扰电流状态。

<div align=center>
<img width="40%" src="scientific_research\papers_reading\neuromorphic_computing\image\相变存储器2.png"/><br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 相变存储器 SET 和 RESET 过程的 I-V 特性曲线。</div>
</div>

> H. S. P. Wong, S. Raoux, S. B. Kim, J. L. Liang, J. P. Reifenberg, B. Rajendran, M. Asheghi, K. E. Goodson, [Phase change memory](https://doi.org/10.1109/JPROC.2010.2070050). *Proc. IEEE* **98**, 2201 (2010).

上图显示了 **SET 和 RESET 状态的电流-电压（I-V）曲线**。对于低于**阈值开关电压（$V_{th}$）**的电压，SET 和 RESET 状态有较大的电阻比。RESET 状态处于低于 $V_{th}$（**亚阈值区域**）的高电阻状态，并在 $V_{th}$ 处显示出**电子阈值开关行为**，即一个**负微分电阻**。如果电压脉冲很快被移除，这是**可逆的**。但是，如果施加电压的时间超过了结晶时间，就会导致存储器打开，并且单元在施加电压大于 $V_{th}$ 时达到低电阻状态。

SET 过程关键上依赖于上述的**电子阈值开关**效应。<mark>当穿过非晶区域的电场达到阈值时，非晶区域的电阻就会进入低电阻状态，其电阻率与结晶状态相当</mark>。**这种电子阈值切换现象是 PCM 进行成功 SET 编程的关键**，其物理机制尚待充分探索。<mark>当 PCM 处于 RESET 状态时，PCM 单元的电阻过高，无法传导足够的电流来提供焦耳热以使 PCM 单元结晶。电子阈值开关效应将相变材料的电阻降低到动态电阻，并实现了 SET 编程</mark>。

**由于单元需要达到熔化温度，RESET 编程消耗的功率最大**。RESET 电流也由各种材料特性决定，如**电阻率**和**热导率**以及**器件结构**。<mark>一般来说，PCM 的运行速度受到 SET 编程时间的限制，因为它需要一定的时间来使非晶区域完全结晶</mark>。

与基于阴离子和阳离子迁移的器件类似，PCM 单元也具有**高电阻状态**和**低电阻状态**。<mark>PCM 器件的 SET 和 RESET 过程是基于相变材料的结晶化和非晶化。开关过程的直流特性如上图所示，较低的电压将相变材料从 HRS 设置为 LRS，较高的电压将相变材料从 LRS 重置为 HRS。TEM 观察进一步证实，LRS 对应于材料的结晶化，而 HRS 的结果是由于非晶区域的存在</mark>。

通过施加一个**低而宽的电压脉冲**，可以实现 SET 过程。根据相变材料的**成核速率**，可以将 SET 过程分为**成核主导**（nucleation dominated）和**生长主导**（growth dominated）。成核主导的例子是 **Ge<sub>2</sub>Sb<sub>2</sub>Te<sub>5</sub>（GST）**，而 **AgInSbTe（AIST）**是典型的生长主导的相变材料。<mark>在成核主导的 PCM 器件中，首先是发生在非晶区域的孵化，然后是晶体生长。纳米晶体的生长是逐渐进行的，直到非晶区域最终转变成多晶材料。在此过程中，PCM 器件逐渐从 HRS 切换到 LRS。而对于以生长为主的材料，结晶总是发生在非晶/晶体界面。非晶材料逐渐转变为结晶状态，并最终在 SET 过程结束时形成单晶</mark>。对于这两种类型的材料，**典型的结晶温度约为 500 K 到 700 K**。需要一个**高于阈值电压的电压脉冲**来将非晶区域温度升高到结晶温度以上，并使**孵化**和**结晶**过程发生，而电压不能太高（~900K），以免熔化相变材料。进一步的研究表明，**阈值开关电压是结晶时间的函数，因此 PCM 器件可用于逻辑操作**。

<mark>在 RESET 过程中，施加一个高而短的电压脉冲，熔化部分相变材料。这种熔化的材料将很快冷却，形成一个非晶区域。这种非晶区域的电子密度较小，从而导致了从 LRS 到 HRS 的电阻转变</mark>。

由于相变材料长期以来一直用于光盘，在 GST 的调控中，**光学和电子控制机制的结合**也很普遍。在**光子微环谐振器**的应用中采用相变材料已经成为集成光子电路的一种做法。

其中，两个主要问题，即**开关速度**和**能耗**，已经变得越来越紧迫，并可能限制 PCM 器件的潜在应用。因此，人们开始寻找能够克服这些问题的**新材料**和**异质结构**。

<div align=center>
<img width="50%" src="scientific_research\papers_reading\neuromorphic_computing\image\相变材料.png"/> <br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 相变材料。</div>
</div>

<mark>尽管相变器件表现出稳定的性能，但它仍然存在较大的 RESET 电流、显著的热耗散和热串扰以及由此产生的高能耗</mark>。因此，长期以来一直在进行**结构和材料的优化**，以提高相变器件的性能。还提出了多种设计规则来指导基于相变材料的器件的设计。

尽管存在这些挑战，PCM 仍然因其**高度成熟**、**出色的稳定性**、**较低的工作功率**、和**良好的可扩展性**而成为神经形态计算的一个有希望的候选者。**基于 GST（Ge<sub>2</sub>Sb<sub>2</sub>Te<sub>5</sub>） 和 AIST（Ag-In-Sb-Te）的 PCM 单元**在神经形态计算中的集成已得到了广泛证明。**大规模的集成**也已成为现实，这表明了基于相变的器件的广阔前景。

## 1.4 基于铁电机制（ferroelectric mechanism）的系统

<mark>铁电材料是近一个世纪前发现的，最初用于铁电 RAM（FeRAMs），它有一层厚的铁电材料，被两个金属电极夹住。施加在电极上的电压可以控制铁电材料的开关，导致材料电导率的变化，这可以通过外部探测信号来测量。然而，由于铁电材料的厚度通常太大（>100 nm），因此无论在何种情况下，铁电材料的电导率都相对较低</mark>。由于材料生长技术的限制，在 20 世纪末，人们认为 FeRAM 的规模不能进一步缩小。这导致基于铁电材料的器件的发展被搁置了大约 30 年。直到最近几年，**当铁电材料可以被制成几纳米的层时**，才再次对开发先进的铁电器件产生了浓厚的兴趣，这导致了广泛的应用，如**数字信息存储**、**热释电能量转换**和**神经形态计算**。最近，有研究表明，<mark>铁电体可以具有负电容</mark>，这可以提高传统电子产品的能效，超过其基本极限，从而显示出巨大的潜在应用前景。

### 1.4.1 铁电隧道结（ferroelectric tunnel junction, FTJ）

<div align=center>
<img width="70%" src="scientific_research\papers_reading\neuromorphic_computing\image\铁电隧道结2.png"/> <br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div>
</div>

> E. Y. Tsymbal, H. Kohlstedt, [Tunneling across a ferroelectric](https://doi.org/10.1126/science.1126230). Science 313, 181 (2006).

<mark>一个 FTJ 是由两个电极组成的，由一个超薄的铁电隧道势垒隔开，该势垒足够薄以允许电子隧穿通过，同时足够厚以保持其铁电性质。据报道，符合这些要求的合适厚度 ~3-4 nm。铁电隧道势垒中自发极化的反转改变了 FTJ 上的内部电场分布，结合由不同金属组成的两个电极的不同电荷屏蔽特性，从而改变了隧穿电流</mark>。这种效应被称为**隧道电阻效应**。**隧道电阻率**（tunneling electroresistance ratio, TER）被定义为

$$ \mathrm{TER} = \frac{R_{P+}-R_{P-}}{R_{P-}} \times 100\\% $$

<mark>具体来说，在铁电体的表面，通常存在着极化电荷，并根据其符号排斥或吸引电子。这发生在电极的一个短距离内，超过这个距离，电子密度保持其正常值：界面附近的电子屏蔽了极化电荷。在 Thomas-Fermi 理论中，屏蔽长度是费米能级电子态密度的一个函数。对于导电金属，Thomas-Fermi 屏蔽长度可以短于十分之一纳米。而对于半导体来说，它可以达到几十纳米，并且屏蔽是不完美的。然而，正如 Stengel 等人所强调的那样，实际的有效屏蔽长度与 Thomas-Fermi 所定义的不同，并且强烈地依赖于铁电/电极界面系统的微观特性</mark>。

<div align=center>
<img width="100%" src="scientific_research\papers_reading\neuromorphic_computing\image\铁电隧道结3.png"/> <br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> 铁电隧道结。</div>
</div>

<mark>这种不完全的屏蔽会在铁电/电极界面处产生额外的静电势（当极化指向界面时 $&lt;0$，当极化远离界面时 $&gt;0$）。一个夹在两个不同触点之间的超薄铁电层，左边的屏蔽比右边的更有效。在电极的介电常数上的屏蔽长度越大，电极/铁电界面处的额外静电势就越大。为了简单起见，假设初始电子势垒是矩形的，极化电荷效应将引起电子势剖面的不对称调制。电子势剖面的不对称性导致了当极化指向左边（$\varPhi_+$）时，比极化指向右边（$\varPhi_-$）时的平均势垒高度（$\varPhi $）更高。由于隧道输运与势垒高度的平方根成指数关系，结电阻将强烈依赖于极化方向。因此，两个铁电/触点界面之间的不对称性对于调节铁电势垒的电流输运至关重要</mark>。然而，使用不同的触点材料并不是强制性的，因为不对称性可能来自于**界面由于界面端的不同**，**在其中一个界面的超薄介电层**，或**钉扎的界面偶极子**。

**由扫描探针显微镜尖端诱导的铁电畴翻转**在铁电器件研究中是很常见的。在以往的研究中用**扫描探针显微镜**，特别是**压电响应力显微镜**（piezoresponse force microscope, PFM）系统地展示了丰富的**图案动力学**，如**铁电层内的间歇性、准周期性和混沌**，由**针尖诱导的极化翻转和屏蔽电荷动力学之间的相互作用**触发。扫描探针显微镜针尖诱导的单个畴翻转的一般物理图像，包括圆**柱形畴的形成**，是由**电场分布**和**畴壁运动动力学**决定的。实验证明了<mark>电阻的变化依赖于隧道层中特定极化方向的比例</mark>。<mark>结合扫描探针成像、电输运和原子尺度的分子动力学，电导变化可以通过成核主导的畴反转来建模</mark>。基于该物理模型，可以进行仿真来演示铁电纳米器件阵列的突触行为，并可用于设计**尖峰神经网络任务**，如**模式识别**。

使用**扫描探针显微镜**，可以实现**非易失性的多级数据存储**，并**可以测量其与内禀的薄膜特性的相关性**。这已经成为一种常见的做法，而且应该是**采用 SPM 测量**，如**压电响应力显微镜**和**导电原子力显微镜**，**对铁电薄膜内部的极化状态进行编程和表征**的一种有希望的方法。

在 FTJ 单元中也观察到了不同工作机制的共存。FTJ 的记忆状态可以通过光照进行调制，伴随着迟滞的光伏效应。据报道，在具有 3 nm 铁电 Sm<sub>0.1</sub>Bi<sub>0.9</sub>FeO<sub>3</sub> 隧道层和 Nb-doped SrTiO<sub>3</sub> 单晶半导体底电极的器件中，实现了组合的电和光效应，这可归因于在半导体/铁电界面上，在高度和宽度上，由偏压和光诱导的隧道势垒的调制。

自 FTJ 发明以来，同于 FTJ 的材料一直是一个热门话题。<mark>到目前为止，大多数研究都集中在具有钙钛矿铁电隧道势垒的 FTJ 上</mark>。从 FeRAM 发展而来的 **Pb(Zr,Ti)O<sub>3</sub>** 最初被用作 FTJ 的隧道势垒材料，以实现**非易失性开关**特性。为了**提高稳定性和开/关电流比**，**BaTiO<sub>3</sub>**, 和 **(Ba,Sr)TiO<sub>3</sub>** 后来经常被用作隧道势垒，是目前 FTJ 中最常用的隧道势垒材料。

<mark>然而，将 FTJ 用于神经形态计算的一个主要问题是集成能力。上述材料与 CMOS 技术不兼容</mark>。因此，基于 **Hf<sub>0.5</sub>Zr<sub>0.5</sub>O<sub>2</sub>** 的 FTJ 最近引起了人们的广泛关注。铁电 **Hf<sub>0.5</sub>Zr<sub>0.5</sub>O<sub>2</sub>** 薄层中的**本征双势阱能量景观**早就被预测，最近又被测量出来，展示了在基于 CMOS 的集成电路中集成 FTJ 的巨大潜力。与 **Hf<sub>0.5</sub>Zr<sub>0.5</sub>O<sub>2</sub>** 相关的材料，如 **HfO<sub>2</sub>** 近年来也得到了深入研究，作为未来集成的有希望的候选材料。此外，在 **PbZr<sub>x</sub>Ti<sub>1-x</sub>O<sub>3</sub>/SrRuO<sub>3</sub>** 铁电异质结的顶部实现了**金属-绝缘体转变**（metal-insulator transition, MIT）**VO<sub>2</sub>** 高质量薄膜的生长，这揭示了**利用铁电材料实现增强的 MIT 性能**的潜力。

<mark>高温外延薄膜的生长的需求对这种无机结的技术应用提出了挑战，如果能够保持较大的隧道电阻（tunneling electroresistance, TER）和良好的开关耐久性，则更易于加工的有机铁电材料可以作为替代</mark>。最近的一项研究报道了**具有旋涂铁电 p（VDF-TrFE）共聚物隧道势垒**的有机 FTJs。

<mark>铁电/电极界面对 FTJs 的性能有着巨大的影响，因为它决定了铁电起源的微观界面效应，从而极大地影响了隧道电阻。由于量子力学隧穿概率对结中存在的缺陷的高度敏感性，还需要一个高质量的外延隧道势垒</mark>。这一要求将底电极材料的选择限制为外延的 (La,Sr)MnO<sub>3</sub>，Nb:SrTiO<sub>3</sub>，SrRuO<sub>3</sub> 和铟锡氧化物（indium tin oxide, ITO）。与顶电极相比，底电极对 TER 的影响更强，有研究报道 **TER 的极性和大小取决于底电极的电导率**。在具有 Nb-doped STO 半导体底电极的 FTJs 上，在室温下测量到了高达 107% 的 TER，这归因于在衬底的空间电荷区域上形成了一个额外的势垒。这种屏蔽诱导的空间电荷层可以拓宽 HRS 的隧道势垒，从而降低漏电流，进而提高 TER。相反，顶电极材料不受 FTJ 制造工艺的限制。过渡金属，如 Cu，Co；惰性金属，如 Au，Pt；复合氧化物，如 (La,Sr)MnO<sub>3</sub>；和二维材料，如石墨烯已被用作 FTJ 的顶电极。在 (La,Sr)MnO<sub>3</sub>/BaTiO<sub>3</sub>/Cu FTJ 中发现的**巨电极效应**突出了顶电极对 TER 比率的重要影响。最近还报道了对具有 TiN、Si、SiGe 和 Ge 与 HfO<sub>2</sub> 隧道势垒的研究，探索了 CMOS 兼容集成的可行性。

<mark>与基于阴/阳离子迁移的器件或相变器件不同，FTJ 中的开关机制能够无损地读取电阻状态，从而确保了高耐久性和良好的保留性。此外，铁电隧道势垒不一定具有单个铁电畴。相反，两种极化状态可以在两个电极之间共存。这种多畴构型允许两种极端状态之间的中间电阻状态，即两中极化状态的多个铁电畴。中间状态是由两种极化状态之间的尺寸比决定的</mark>。同时，采用了结构优化，以确保更好的多态特性。通过局域地控制铁电-电极界面处的成核能量分布，例如**在电极和 **PbZr<sub>x</sub>Ti<sub>1-x</sub>O<sub>3</sub>/SrRuO<sub>3</sub>** 铁电层之间插入一个非开关的 ZnO**，可以在铁电器件中创建**多个寻址状态**，这对于突触应用是必要的。

<mark>虽然 FTJ 可以实现连续可调的电阻行为和增强的计算能力和能源效率，但 FTJs 的开/关电流比比其他候选材料低几十倍</mark>。因此，结构优化已被考虑用来**提高开/关比**。据报道，在混合 MoS<sub>2</sub>/BaTiO<sub>3</sub>/SrRuO<sub>3</sub> 铁电隧道结（FTJs）中通过**极化诱导的对于 MoS<sub>2</sub> 电子特性的调制**产生了巨大的隧道电阻效应，**开/关电流比高达 10<sup>4</sup>**，与同类型的具有金属电极的 FTJs 相比，增加了 50 倍。该效应源于 MoS<sub>2</sub> 电极对铁电开关的响应而造成的的多数载流子的可逆的积累-消耗，这改变了MoS<sub>2</sub>/BaTiO<sub>3</sub> 界面处的势垒，并能通过 BaTiO<sub>3</sub> 中稳定的有序畴结构实现电阻状态的连续可调性。

### 1.4.2 畴壁运动（domain wall motion）

另一种铁电神经形态器件是基于铁电畴壁的运动。铁电畴壁是指分隔铁电材料中连续的极化、磁化和应变的畴的拓扑壁，它有希望产生新的电子特性，并且在纳米尺度上具有内在的局部性，可以根据需要进行图案化，而不改变材料体积或元素组成。对标准和非标准铁电材料中的域壁传导过程的SPM研究已经在实验和理论上得到证明。关于通过铁电的传输的SPM研究显示，氧化物中的域和拓扑缺陷都可以作为单独的元素被利用，用于功能性的纳米级器件。





## 1.5 基于磁性机制（magnetic mechanism）的系统

### 1.5.1 磁性隧道结（magnetic tunneling junction）

### 1.5.2 自旋轨道矩（spin-orbit torque）

### 1.5.3 磁性转变（magnetic transition）

## 1.6 基于金属-绝缘体转变（metal-insulator transition）的系统

## 1.7 基于光调谐机制（photo-tunable mechanism）的系统

### 1.7.1 俘获（trapping）

### 1.7.2 相变材料辅助（phase change materials assisted）

### 1.7.3 纯光学装置（pure optical setup）

## 1.8 基于电解质门控机制（electrolyte-gated mechanism）的系统

### 1.8.1 静电控制（electrostatic control）

### 1.8.2 电双层（electric double layers）

### 1.8.3 电化学掺杂（electrochemical doping）

### 1.8.4 离子插层（ion intercalation）

## 1.9 基于电子机制（electronic mechanism）的系统

### 1.9.1 俘获和脱离（trapping and detrapping）

### 1.9.2 量子点（quantum dots）

### 1.9.3 场效应电子输运（field-effect electron transport）






