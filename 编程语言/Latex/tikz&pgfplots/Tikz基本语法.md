# Tikz 基本语法

本内容主要来自 [The TikZ and PGF Packages](https://tikz.dev/)。

## Specifying Coordinates 指定坐标

### Coordinate Systems 坐标系

#### Canvas, XYZ, and Polar Coordinate Systems

1. **坐标**是**画布**上绘制图片的位置。TikZ 使用一种特殊的语法来指定坐标。<mark>坐标总是放在圆括号里，默认单位是 cm。</mark>
2. 坐标系包括**笛卡尔坐标系**、**极坐标系**和**球面坐标系**。
3. 在 xyz 坐标系中，默认的 x、y、z 矢量分别指向 (1cm, 0)、(0, 1cm)、(-3.85mm, -3.85mm)。隐式地选择该坐标系只需提供两到三个逗号分隔的因子（而不是单位）。
4. `(1,2cm)` 既不是 canvas 坐标也不是 xyz 坐标。规则如下：
   1. 如果一个坐标是隐式的 (⟨*x*⟩,⟨*y*⟩)，那么会独立地检查它们是否有单位或是否是无量纲的。
   2. 如果两者都有单位，则使用 canvas 坐标系。
   3. 如果两者都缺少单位，则使用 xyz 坐标系。
   4. 如果 ⟨*x*⟩ 有单位，而 ⟨*y*⟩ 没有，则使用两个坐标 (⟨*x*⟩,0cm) 和 (0,⟨*y*⟩) 的和。
   5. 如果 ⟨*y*⟩ 有单位，而 ⟨*x*⟩ 没有，则使用两个坐标 (⟨*x*⟩,0) 和  (0cm,⟨*y*⟩) 的和。
5. `(2+3cm,0)` 与 `(2cm+3cm,0)` 并不相同。如果在 ⟨*x*⟩ 或 ⟨*y*⟩ 内部混合使用有单位的值和无量纲的值，那么所有无量纲值的单位都会被解释为 pt，1pt=0.35146mm。因此，`2+3cm` 等价于 `2pt+3cm`。
6. 在 canvas polar 坐标系中：
   1. 0° 角指向右，90° 角指向上。
   2. 极坐标只是给定半径的圆上的一个点，当你提供 `x radius` 和 `y radius` 时，可以指定椭圆而不是圆。
   3. `radius` 选项与指定相同的 `x radius` 和 `y radius` 选项具有相同的效果。
   4. canvas polar 坐标系的隐式形式如下：指定角度和距离，用冒号分隔，如 `(30:1cm)` 所示，可以通过 `(30:1cm and 2cm)` 指定两种不同的半径。
   5. 对于隐式形式，你也可以使用某些单词，而不是用数字来表示角度。例如，`up` 与 `90` 相同，因此可以写作 `(up:1cm)`。除了 `up`，你还可以使用 `left, right, north, south, west, east, north east, north west, south east, south west`。
7. `xyz polar` 坐标系的工作原理与 `canvas polar` 坐标系类似，但是半径和角度在 xy 坐标系统中进行解释，而不是在画布系统中，因此 0° 角对应 `x` 矢量，90° 角对应 `y` 矢量，并且图形会随着 `x` 矢量和 `y` 矢量定义的不同而发生改变。`xyz polar` 坐标系的隐式形式与 `canvas polar` 坐标系的隐式形式相同，只是不提供单位。
8. `xy polar` 坐标系只是 `xyz polar` 坐标系的一个别名，有些人可能更喜欢这个名字，因为 `xyz polar` 坐标系中不涉及 `z` 坐标。
