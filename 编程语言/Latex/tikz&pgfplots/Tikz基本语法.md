# Tikz 基本语法

本内容主要来自 [The TikZ and PGF Packages](https://tikz.dev/)。

## Specifying Coordinates 指定坐标

1. **坐标**是**画布**上绘制图片的位置。TikZ 使用一种特殊的语法来指定坐标。<mark>坐标总是放在圆括号里，默认单位是 cm。</mark>
2. 坐标系包括**笛卡尔坐标系**、**极坐标系**和**球面坐标系**。
3. 在 xyz 坐标系中，默认的 x、y、z 矢量分别指向 (1cm, 0)、(0, 1cm)、(-3.85mm, -3.85mm)。