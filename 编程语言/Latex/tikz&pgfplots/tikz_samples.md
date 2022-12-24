## tikz 绘图示例

### 官方示例

#### 2 Tutorial: A Picture for Karl’s Students

<div align=center>
<img width="100%" src="programme/Latex/tikz&pgfplots/image/2022-03-04-23-43-51.png"/>
</div>

```latex
\documentclass[border=15pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{intersections}
\usepackage{sansmath}
\renewcommand{\familydefault}{\sfdefault}
\renewcommand{\sfdefault}{phv}
\begin{document}
\begin{tikzpicture}
    [scale=3,line cap=round,
    % Styles
    axes/.style=,
    important line/.style={very thick},
    information text/.style={rounded corners,fill=red!10,inner sep=1ex}]
    \sansmath
    % Colors
    \colorlet{anglecolor}{green!50!black}
    \colorlet{sincolor}{red}
    \colorlet{tancolor}{orange!80!black}
    \colorlet{coscolor}{blue}
    % The graphic
    \draw[help lines,step=0.5cm] (-1.4,-1.4) grid (1.4,1.4);
    \draw (0,0) circle [radius=1cm];
    \begin{scope}[axes]
    \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$} coordinate(x axis);
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$} coordinate(y axis);
    \foreach \x/\xtext in {-1, -.5/-\frac{1}{2}, 1}
    \draw[xshift=\x cm] (0pt,1pt) -- (0pt,-1pt) node[below,fill=white] {$\xtext$};
    \foreach \y/\ytext in {-1, -.5/-\frac{1}{2}, .5/\frac{1}{2}, 1}
    \draw[yshift=\y cm] (1pt,0pt) -- (-1pt,0pt) node[left,fill=white] {$\ytext$};
    \end{scope}
    \filldraw[fill=green!20,draw=anglecolor] (0,0) -- (3mm,0pt)
    arc [start angle=0, end angle=30, radius=3mm];
    \draw (15:2mm) node[anglecolor] {$\alpha$};
    \draw[important line,sincolor]
    (30:1cm) -- node[left=1pt,fill=white] {$\sin \alpha$} (30:1cm |- x axis);
    \draw[important line,coscolor]
    (30:1cm |- x axis) -- node[below=2pt,fill=white] {$\cos \alpha$} (0,0);
    \path [name path=upward line] (1,0) -- (1,1);
    \path [name path=sloped line] (0,0) -- (30:1.5cm);
    \draw [name intersections={of=upward line and sloped line, by=t}]
    [very thick,orange] (1,0) -- node [right=1pt,fill=white]
    {$\displaystyle \tan \alpha \color{black}=
    \frac{{\color{red}\sin \alpha}}{\color{blue}\cos \alpha}$} (t);
    \draw (0,0) -- (t);
    \draw[xshift=1.85cm]
    node[right,text width=6cm,information text]
    {
    The {\color{anglecolor} angle $\alpha$} is $30^\circ$ in the
    example ($\pi/6$ in radians). The {\color{sincolor}sine of
    $\alpha$}, which is the height of the red line, is
    \[
    {\color{sincolor} \sin \alpha} = 1/2.
    \]
    By the Theorem of Pythagoras ...
    };
\end{tikzpicture}
\end{document}

```

#### 3 Tutorial: A Petri-Net for Hagen

<div align=center>
<img width="70%" src="programme/Latex/tikz&pgfplots/image/2022-03-05-00-07-20.png"/>
</div>

```latex
\documentclass[border=15pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,petri,positioning,decorations.pathmorphing,backgrounds,fit}
\usepackage{sansmath}
\renewcommand{\familydefault}{\sfdefault}
\renewcommand{\sfdefault}{phv}
\begin{document}
\begin{tikzpicture}
	[node distance=1.3cm,on grid,>={Stealth[round]},bend angle=45,auto,
	 every place/.style={minimum size=6mm,thick,draw=blue!75,fill=blue!20},
	 every transition/.style={thick,draw=black!75,fill=black!20},
	 red place/.style={place,draw=red!75,fill=red!20},every label/.style={red}]
    \sansmath
    \node[place,tokens=1] (w1) {};
	\node[place] (c1) [below=of w1] {};
	\node[place] (s) [below=of c1,label=above:$s\le 3$] {};
	\node[place] (c2) [below=of s] {};
	\node[place,tokens=1] (w2) [below=of c2] {};
	\node[transition] (e1) [left=of c1] {}
		edge [pre,bend left] (w1)
		edge [post,bend right] (s)
		edge [post] (c1);
	\node[transition] (e2) [left=of c2] {}
		edge [pre,bend right] (w2)
		edge [post,bend left] (s)
		edge [post] (c2);
	\node[transition] (l1) [right=of c1] {}
		edge [pre] (c1)
		edge [pre,bend left] (s)
		edge [post,bend right] node[swap] {2} (w1);
	\node[transition] (l2) [right=of c2] {}
		edge [pre] (c2)
		edge [pre,bend right] (s)
        edge [post,bend left] node {2} (w2);

    \begin{scope}[xshift=6cm]
        \node[place,tokens=1] (w1') {};
        \node[place] (c1') [below=of w1'] {};
        \node[red place] (s1') [below=of c1',       xshift=-5mm] [label=left:$s$] {};
        \node[red place,tokens=3] (s2') [below=of c1',xshift=5mm] [label=right:$\bar s$] {};
        \node[place] (c2') [below=of s1',xshift=5mm] {};
        \node[place,tokens=1] (w2') [below=of c2'] {};
        \node[transition] (e1') [left=of c1'] {}
            edge [pre,bend left] (w1')
            edge [post] (s1')
            edge [pre] (s2')
            edge [post] (c1');
        \node[transition] (e2') [left=of c2'] {}
            edge [pre,bend right] (w2')
            edge [post] (s1')
            edge [pre] (s2')
            edge [post] (c2');
        \node[transition] (l1') [right=of c1'] {}
            edge [pre] (c1')
            edge [pre] (s1')
            edge [post] (s2')
            edge [post,bend right] node[swap] {2} (w1');
        \node[transition] (l2') [right=of c2'] {}
            edge [pre] (c2')
            edge [pre] (s1')
            edge [post] (s2')
            edge [post,bend left] node {2} (w2');
    \end{scope}

    \begin{scope}[on background layer]
        \node (r1) [fill=black!10,rounded corners,fit=(w1)(w2)(e1)(e2)(l1)(l2)] {};
        \node (r2) [fill=black!10,rounded corners,fit=(w1')(w2')(e1')(e2')(l1')(l2')] {};
    \end{scope}
    \draw[shorten >=1mm,->,thick,decorate,
        decoration={snake,amplitude=.4mm,segment length=2mm,
        pre=moveto,pre length=1mm,post length=2mm}]
        (r1) -- (r2) node [above=1mm,midway,text width=3cm,align=center]
        {replacement of the \textcolor{red}{capacity} by \textcolor{red}{two places}};
\end{tikzpicture}  
\end{document}
```
#### 4 Tutorial: Euclid's Amber Version of the Elements

<div align=center>
<img width="40%" src="programme/Latex/tikz&pgfplots/image/2022-03-05-00-13-43.png"/>
</div>

```latex
\documentclass[border=15pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{calc,intersections,through}
\usepackage{sansmath}
\renewcommand{\familydefault}{\sfdefault}
\renewcommand{\sfdefault}{phv}
\begin{document}
\begin{tikzpicture}[thick,help lines/.style={thin,draw=black!50}]
    \sansmath
    \def\A{\textcolor{orange}{$A$}} \def\B{\textcolor{input}{$B$}}
	\def\C{\textcolor{input}{$C$}} \def\D{$D$}
	\def\E{$E$} \def\F{$F$}
	\def\G{$G$} \def\H{$H$}
	\def\K{$K$} \def\L{\textcolor{output}{$L$}}
	\colorlet{input}{blue!80!black} \colorlet{output}{red!70!black}
	\coordinate [label=left:\A] (A) at ($ (0,0) + .1*(rand,rand) $);
	\coordinate [label=right:\B] (B) at ($ (1,0.2) + .1*(rand,rand) $);
	\coordinate [label=above:\C] (C) at ($ (1,2) + .1*(rand,rand) $);
	\draw [input] (B) -- (C);
	\draw [help lines] (A) -- (B);
	\coordinate [label=above:\D] (D) at ($ (A)!.5!(B) ! {sin(60)*2} ! 90:(B) $);
	\draw [help lines] (D) -- ($ (D)!3.75!(A) $) coordinate [label=-135:\E] (E);
	\draw [help lines] (D) -- ($ (D)!3.75!(B) $) coordinate [label=-45:\F] (F);
	\node (H) at (B) [name path=H,help lines,circle through=(C),draw,label=135:\H] {};
	\path [name path=B--F] (B) -- (F);
	\path [name intersections={of=H and B--F,by={[label=right:\G]G}}];
	\node (K) at (D) [name path=K,help lines,circle through=(G),draw,label=135:\K] {};
	\path [name path=A--E] (A) -- (E);
	\path [name intersections={of=K and A--E,by={[label=below:\L]L}}];
	\draw [output] (A) -- (L);
	\foreach \point in {A,B,C,D,G,L}
		\fill [black,opacity=.5] (\point) circle (2pt);
	% \node ...
\end{tikzpicture}
\end{document}
```
#### 5 Tutorial: Diagrams as Simple Graphs

<div align=center>
<image width="100%" src="programme/Latex/tikz&pgfplots/image/2022-03-05-00-36-28.png"/>
</div>

```latex
\documentclass[border=15pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,graphs,shapes.misc}
\usepackage{sansmath}
\renewcommand{\familydefault}{\sfdefault}
\renewcommand{\sfdefault}{phv}
\begin{document}
\begin{tikzpicture}[>={Stealth[round]}, black!50, text=black, thick,
    every new ->/.style = {shorten >=1pt},
     graphs/every graph/.style = {edges=rounded corners},
     skip loop/.style = {to path={-- ++(0,#1) -| (\tikztotarget)}},
     hv path/.style = {to path={-| (\tikztotarget)}},
     vh path/.style = {to path={|- (\tikztotarget)}},
     nonterminal/.style = {
         rectangle, minimum size=6mm, very thick, draw=red!50!black!50, top color=white,
         bottom color=red!50!black!20, font=\itshape, text height=1.5ex,text depth=.25ex},
     terminal/.style = {
         rounded rectangle, minimum size=6mm, very thick, draw=black!50, top color=white,
         bottom color=black!20, font=\ttfamily, text height=1.5ex, text depth=.25ex},
     shape = coordinate
    ]
    \sansmath
    \graph [grow right sep, branch down=7mm, simple] {
		/ -> unsigned integer[nonterminal] -- p1 -> "." [terminal] -- p2 -> digit[terminal] --
		p3 -- p4 -- p5 -> E[terminal] -- q1 ->[vh path]
		{[nodes={yshift=7mm}]
			"+"[terminal], q2, "-"[terminal]
		} -> [hv path]
		q3 -- /unsigned integer [nonterminal] -- p6 -> /;
		p1 ->[skip loop=5mm] p4;
		p3 ->[skip loop=-5mm] p2;
		p5 ->[skip loop=-11mm] p6;
		q1 -- q2 -- q3; % make these edges plain
    };
\end{tikzpicture}
\end{document}
```

#### 6 Tutorial: A Lecture Map for Johannes

```latex

```

#### 40 Three Dimensional Drawing Library (Page 566)

<div align=center>
<image width="100%" src="programme/Latex/tikz&pgfplots/image/2022-03-18-21-58-43.png"/>
</div>

```latex
\documentclass[border=15pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{3d}
\usepackage{sansmath}
\renewcommand{\familydefault}{\sfdefault}
\renewcommand{\sfdefault}{phv}
\begin{document}
\begin{tikzpicture}[x={(10:10mm)}, y={(-45:5mm)}, z={(90:10mm)}]
    \sansmath
    \def\wave{
        \draw[fill,thick,fill opacity=.2]
            (0,0) sin (1,1) cos (2,0) sin (3,-1) cos (4,0)
            sin (5,1) cos (6,0) sin (7,-1) cos (8,0)
            sin (9,1) cos (10,0)sin (11,-1)cos (12,0);
    \foreach \shift in {0,4,8}
    {
        \begin{scope}[xshift=\shift cm,thin]
            \draw (.5,0) -- (0.5,0 |- 45:1cm);
            \draw (1,0) -- (1,1);
            \draw (1.5,0) -- (1.5,0 |- 45:1cm);
            \draw (2.5,0) -- (2.5,0 |- -45:1cm);
            \draw (3,0) -- (3,-1);
            \draw (3.5,0) -- (3.5,0 |- -45:1cm);
        \end{scope}
        }
    }
    \begin{scope}[canvas is xz plane at y=0,fill=blue]
        \wave
        \node at (6,-1.5) [transform shape] {magnetic field};
    \end{scope}
    \begin{scope}[canvas is xy plane at z=0,fill=red]
        \draw[help lines] (0,-2) grid (12,2);
        \wave
        \node at (6,1.5) [transform shape] {electric field};
    \end{scope}
\end{tikzpicture}
\end{document}
```

### 网上示例

#### 用 TikZ 绘制一个相对复杂的流程图

地址：<https://www.latexstudio.net/index/details/index/mid/1250>

<div align=center>
<image width="100%" src="programme/Latex/tikz&pgfplots/image/2022-06-06-22-46-27.png"/>
</div>

```latex

\documentclass[border=15pt]{standalone} 
\usepackage[utf8]{inputenc}
\usepackage{tikz}
\usetikzlibrary{matrix, shapes, arrows, positioning, chains, calc}

\begin{document}

% Define block styles
\tikzset{
    desicion/.style={
            diamond,
            draw, thick,
            text width=4em,
            text badly centered,
            inner sep=0pt
        },
    block/.style={
            rectangle,
            draw, thick,
            text width=9em,
            text centered,
            rounded corners
        },
    cloud/.style={
            draw,
            ellipse,
            minimum height=2em
        },
    descr/.style={
            fill=white,
            inner sep=2.5pt
        },
    connector/.style={
            -latex,
            font=\scriptsize
        },
    rectangle connector/.style={
            connector,
            to path={(\tikztostart) -- ++(#1, 0pt) \tikztonodes |- (\tikztotarget) },
            pos=0.5
        },
    rectangle connector/.default=-2cm,
    straight connector/.style={
            connector,
            to path=--(\tikztotarget) \tikztonodes
        },
    line/.style={>=latex, ->, thick}
}

\begin{tikzpicture}
    \matrix (m) [matrix of nodes, column sep=3cm, row sep=8mm, align=center, nodes={rectangle, draw, anchor=center}]
    {
    |[block]| {Start}       &   & \\
    |[block]| {Assume that $a=c$ the optimilalty cretierin given by }  &  &                                  \\
    |[desicion]| {Locally optimal}          &           &                                 \\
    |[block]| {Assume that $a=d$ the optimilalty cretierin given by}    &                                            & \\
    |[desicion]| {Locally optimal}         &               &                           \\
    |[block]| {Assume that $a=e$ the optimilalty cretierin given by}    &       |[block]| {$A=c^2$ \\ $A=b^2$}           &        |[block]| {Globsl \\  Optimal \\ Configuration}                 \\
    |[desicion]| {Locally optimal}         &    &                       \\
    |[block]| {Assume that $a=f$ the optimilalty cretierin given by}    &   &   \\
    |[desicion]| {Locally optimal}               & &  |[block]| {Stop}  \\
    |[block]| {Assume that $a=k$ the optimilalty cretierin given by}    &    |[desicion]| {Locally optimal}    &     \\
    };
    \foreach \f/\t [evaluate=\f as \t using int(\f+1)] in {3, 4, 5, 6, 7, 8, 9} {
            \draw [line] (m-\f-1) -- node[midway, right]{No} (m-\t-1);
        }
    \node[above,xshift=1.5cm] at (m-10-2) {No};
    \foreach \f/\t [evaluate=\f as \t using int(\f+1)] in {1, 2} {
            \draw [line] (m-\f-1) -- (m-\t-1);
        }
    \path [line, red] (m-10-1) edge (m-10-2);
    \path [line, red] (m-6-3) edge (m-9-3);
    \draw [line, red] (m-10-2) -| (m-9-3);

    \draw [line, red] (m-3-1.east) -- node [midway, above, text=black] {Yes, Pass (a1, c1)} ++ (2.8cm, 0) coordinate [] (a);
    \draw [line, red] (m-3-1.east) -| ([xshift=1.5cm]m-4-1.north);
    \draw [line, red] (m-5-1.east) --node [midway, above, text=black] {Yes, Pass (a2, c2)} ++ (2.8cm, 0) coordinate [] (b);
    \draw [line, red] (m-5-1.east) -| ([xshift=1.5cm]m-6-1.north);
    \draw [line, red] (m-7-1.east) --node [midway, above, text=black] {Yes, Pass (a3, c3)} ++ (2.8cm, 0) coordinate [] (c);
    \draw [line, red] (m-7-1.east) -| ([xshift=1.5cm]m-8-1.north);
    \draw [line, red] (m-9-1.east) --node [midway, above, text=black] {Yes, Pass (a4, c4)} ++ (2.8cm, 0) coordinate [] (d);
    \draw [line, red] (m-9-1.east) -| ([xshift=1.5cm]m-10-1.north);
    \draw [line, red] (m-10-2) -- (m-6-2) node [pos=0.3, right, text=black] {Yes, Pass (a5, c5)};
    \draw [line] (m-6-2) -- node [midway, below, text=black] {Yes, Pass (a6, c6)} node [midway, above, text=black] {Step 6} (m-6-3);

    \node [xshift=4cm] at (m-1-1) {A, b, c, d, k given};
    \node [xshift=-2cm] at (m-3-1) {Step 1 (4)};
    \node [xshift=-2cm] at (m-5-1) {Step 2 (7)};
    \node [xshift=-2cm] at (m-7-1) {Step 3 (9)};
    \node [xshift=-2cm] at (m-9-1) {Step 4 (3)};
    \node [xshift=-2cm,above] at (m-10-2) {Step 5};
    \draw [>=latex, -, red, thick] (a) -- (d);
    \draw [line, red] ($(a)!0.5!(d)$) -- (m-6-2);
\end{tikzpicture}
\end{document}

```

#### 相位延迟板示意图

地址：<https://www.latexstudio.net/index/details/index/mid/2127.html>

<div align=center>
<image width="100%" src="programme/Latex/tikz&pgfplots/image/2022-03-18-00-02-08.png"/>
</div>

```latex
\documentclass[border=2pt]{standalone}

% Drawing
\usepackage{tikz}

% Tikz Library
\usetikzlibrary{3d, shapes.multipart, arrows.meta, angles, quotes, calc}

\usepackage{sansmath}
\renewcommand{\familydefault}{\sfdefault}
\renewcommand{\sfdefault}{phv}

% Styles
\tikzset{every node/.style={align=center}}

% New Commands
%% Polarizer
\newcommand{\polarizer}[1]{%
	\begin{scope}[canvas is xz plane at y=1.2]
		\draw[line join=round, thick, fill=black!40] (#1,-1.2) rectangle (#1+0.2,1.2);
	\end{scope}
	%
	\begin{scope}[canvas is xy plane at z=1.2]
		\draw[line join=round, thick, fill=black!25](#1,-1.2) rectangle (#1+0.2,1.2);
	\end{scope}
	%
	\begin{scope}[canvas is yz plane at x=#1]
		\draw[line join=round, thick, fill=black!10] (-1.2,-1.2) rectangle (1.2,1.2);
		\draw[line join=round, thick, fill=white] (0,0) circle (0.8cm);
		\draw[line join=round, thick] (0,-0.8) -- (0,0.8);
	\end{scope}
}
%% Phase Delay Plate
\newcommand{\pkf}[3]{%
	\begin{scope}[canvas is xz plane at y=1.2]
		\draw[line join=round, thick, fill=black!40] (#1,-1.2) rectangle (#1+0.4,1.2);
	\end{scope}
	%
	\begin{scope}[canvas is xy plane at z=1.2]
		\draw[line join=round, thick, fill=black!25](#1,-1.2) rectangle (#1+0.4,1.2);
	\end{scope}
	%
	\begin{scope}[canvas is yz plane at x=#1]
		\draw[line join=round, thick, fill=black!10] (-1.2,-1.2) rectangle (1.2,1.2);
		\draw[line join=round, thick, fill=white] (0,0) coordinate (B) ellipse (0.8cm and 0.8cm);
		\draw[line join=round, thick] (-{0.8*cos(#2)}, -{0.8*sin(#2)}) -- ({0.8*cos(#2)},{0.8*sin(#2)}) coordinate (C');
		\draw[line join=round, thick] (-{0.8*cos(#3)}, -{0.8*sin(#3)}) coordinate (A') -- ({0.8*cos(#3)},{0.8*sin(#3)}) coordinate (A);
		\draw[line join=round, dashed, thick] (0,-0.8) -- (0,0.8) coordinate (C);
		\pic[line join=round, draw, thick, "$\theta$", angle radius=0.4cm, angle eccentricity=1.6] {angle = C--B--A};
		\MarkRightAngle[size=5pt](A',B,C');
	\end{scope}
}
%% Analyser
\newcommand{\analyser}[2]{%
	\begin{scope}[canvas is xz plane at y=1.2]
		\draw[line join=round, thick, fill=black!40] (#1,-1.2) rectangle (#1+0.2,1.2);
	\end{scope}
	%
	\begin{scope}[canvas is xy plane at z=1.2]
		\draw[line join=round, thick, fill=black!25](#1,-1.2) rectangle (#1+0.2,1.2);
	\end{scope}
	%
	\begin{scope}[canvas is yz plane at x=#1]
		\draw[line join=round, thick, fill=black!10] (-1.2,-1.2) rectangle (1.2,1.2);
		\draw[line join=round, thick, fill=white] (0,0) coordinate (B) ellipse (0.8cm and 0.8cm);
		\draw[line join=round, dashed] (0,0) coordinate (B) ellipse (0.6cm and 0.8cm);
		\draw[line join=round, thick] (-{0.8*cos(#2)}, -{0.8*sin(#2)}) -- ({0.8*cos(#2)},{0.8*sin(#2)}) coordinate (A);
		\draw[line join=round, dashed, thick] (0,-0.8) -- (0,0.8) coordinate (C);
		\MarkRightAngle[size=6pt](A,B,C);
	\end{scope}
}
%% Draw Line in Polar Coordinates from (0,0) to (r,theta)
\newcommand{\cdraw}[2]{\draw[very thick, -stealth, red] (0,0) -- ({#1*cos(#2)}, {#1*sin(#2)});}

% Notation
\usepackage{amsmath}

\begin{document}

%Layers
\pgfdeclarelayer{layer1}
\pgfdeclarelayer{layer2}
\pgfdeclarelayer{layer3}
\pgfdeclarelayer{layer4}
\pgfdeclarelayer{layer5}
\pgfdeclarelayer{layer6}
\pgfdeclarelayer{layer7}
%
\pgfsetlayers{main, layer7, layer6, layer5, layer4, layer3, layer2, layer1}

% Right Angle Mark
\def\MarkRightAngle[size=#1](#2,#3,#4){\draw[thick, line join=round] ($(#3)!#1!(#2)$) -- ($($(#3)!#1!(#2)$)!#1!90:(#2)$) -- ($(#3)!#1!(#4)$)}
	
\begin{tikzpicture}[x={(1cm,0.4cm)}, y={(8mm, -3mm)}, z={(0cm,1cm)}, line cap=round, line join=round]
    \sansmath
%	% Main Axes
%	\draw[->] (0,0,0) -- (12,0,0) node[right] {$x$};
%	\draw[->] (0,0,0) -- (0,2,0) node[below left] {$y$};
%	\draw[->] (0,0,0) -- (0,0,2) node[above] {$z$};
	
	% Big Axis 
	\draw[line cap=round, -latex, very thick] (-0.5,0,0) -- (14.5,0,0);
	
	% Polarizers
	\begin{pgfonlayer}{layer2}
		\polarizer{2}
	\end{pgfonlayer}
	\begin{pgfonlayer}{layer4}
		\pkf{5.5}{40}{130}
	\end{pgfonlayer}
	\begin{pgfonlayer}{layer6}
		\analyser{10.5}{0}
	\end{pgfonlayer}
	
	% Electric Field
	%% Unpolarized
	\begin{pgfonlayer}{layer1}
		\begin{scope}[canvas is yz plane at x=0.5]
			\foreach \i in {0,45,...,315}
			{
				\cdraw{0.8}{\i}
			}		
		\end{scope}
	\end{pgfonlayer}
	%% Polarized Linearly 1
	\begin{pgfonlayer}{layer3}
		\foreach \i in {3,3.5,...,5}
			{
				\begin{scope}[canvas is yz plane at x=\i]
					\cdraw{0.8}{90}
					\cdraw{0.8}{270}
				\end{scope}
			}
	\end{pgfonlayer}
	%% Polarized Elliptically
	\begin{pgfonlayer}{layer5}
		\draw[very thick, red, variable=\t, domain=5.5:10.5, samples=300] plot (\t, {0.6*sin(deg(\t*4+90))}, {0.8*cos(deg(\t*4+90))});
	
		\foreach \i [evaluate={\k = \i*4; \ii = \i;}] in {5.5,5.55,...,10.5}
			{
				\draw[-{Latex[length=1mm]}] (\ii,0,0) -- +(0, {0.6*sin(deg(\k+90))}, {0.8*cos(deg(\k+90))});
			}
	\end{pgfonlayer}
	%% Polarized Linearly 2
	\begin{pgfonlayer}{layer7}
		\begin{scope}[canvas is yz plane at x=13]
			\cdraw{0.6}{0}
			\cdraw{0.6}{180}
			\draw[dashed] (0,-0.8) -- (0,0.8);
			\coordinate (A) at ({0.6*cos(0)},{0.6*sin(0)});
			\coordinate (B) at (0,0);
			\coordinate (C) at (0,0.6); 
			\MarkRightAngle[size=6pt](A,B,C);
		\end{scope}
		
		\foreach \i in {10,10.5,...,13.5}
			{	
				\begin{scope}[canvas is yz plane at x=\i]
					\cdraw{0.6}{0}
					\cdraw{0.6}{180}
				\end{scope}
			}
	\end{pgfonlayer}
	
	% Nodes
	%% Upper
	\begin{scope}[canvas is yz plane at x=1.8]
		\node[rotate=-20] at (0.7,2) {\small{Polarizer}};
	\end{scope}
	%
	\begin{scope}[canvas is yz plane at x=5.5]
		\node[rotate=-20] at (0.7,2) {\small{PDP $\lambda/4$}};
	\end{scope}
	%
	\begin{scope}[canvas is yz plane at x=10.3]
		\node[rotate=-20] at (0.7,2) {\small{Analyser}};
	\end{scope}
	%% Lower
	\begin{pgfonlayer}{layer2}
		\begin{scope}[canvas is xy plane at z=-0.2]
			\draw[latex-] (2,0) to[out=160, in=275] (2,2.8) node[right, yshift=-3pt] {\small{Polarization Plate}\\[-0.5mm]\small{of Polarizer}};
		\end{scope}
	\end{pgfonlayer}
	%
	\begin{pgfonlayer}{layer4}
		\begin{scope}[canvas is xy plane at z=-0.38]
			\draw[latex-] (5.5,0.3) to[out=130, in=275] (6,2.5) node[right, yshift=-3pt] {\small{$\mathrm{T}$ Axis}};
		\end{scope}
		\begin{scope}[canvas is xy plane at z=0.38]
			\draw[latex-] (5.5,0.47) to[out=130, in=275] (6,3) node[right, yshift=-3pt] {\small{$\mathrm{B}$ Axis}};
		\end{scope}
	\end{pgfonlayer}
	%
	\begin{pgfonlayer}{layer6}
		\begin{scope}[canvas is xy plane at z=0]
			\draw[latex-] (10.5,0.5) to[out=180, in=270] (10.5,2.8) node[right, yshift=-3pt] {\small{Polarization Plate}\\[-0.5mm]\small{of Analyser}};
		\end{scope}
	\end{pgfonlayer}	
	%% Intensities of Light
	\node at (0.5,0,1.2) {\small{$I_o$}};
	\node at (3.8,0,1.2) {\small{$I_1$}};	
	\node at (8,0,1.4) {\small{$I_2$}};
	\node at (12,0,0.8) {\small{$I_3$}};
	%% Propagation Direction
	\node at (14,0.5,1) {\small{Propagation}\\[-0.5mm]\small{Direction}};
	
	% Refinements
	\begin{pgfonlayer}{layer1}
		\draw[line cap=round, thick] (2,0,-0.8) -- (2,0,0.8);
	\end{pgfonlayer}
	\begin{pgfonlayer}{layer1}
		\draw[line cap=round, very thick] (1,0,0) -- (1.99,0,0);
	\end{pgfonlayer}
	\begin{pgfonlayer}{layer4}
		\draw[line cap=round, very thick] (4.5,0,0) -- (5.5,0,0);
	\end{pgfonlayer}
	\begin{pgfonlayer}{layer6}
		\draw[line cap=round, very thick] (9.5,0,0) -- (10.49,0,0);
	\end{pgfonlayer}
\end{tikzpicture}
	
\end{document}
```

#### 

地址：<https://www.latexstudio.net/index/details/index/mid/2004.html>

### Latex Stack Exchange

#### 3D 效果箭头

地址：<https://tex.stackexchange.com/questions/267222/3d-arrows-with-tikz>

```latex
\documentclass[tikz]{standalone}
\usepgflibrary{arrows.meta}
\usepackage{tikz-3dplot}
\begin{document}

\makeatletter

\pgfkeys{
  /pgf/arrow keys/.cd,
  pitch/.code={%
    \pgfmathsetmacro\pgfarrowpitch{#1}
    \pgfmathsetmacro\pgfarrowcospitch{abs(cos(\pgfarrowpitch))}
    \pgfmathsetmacro\pgfarrowsinpitch{    sin(\pgfarrowpitch)}
  }
}

\pgfdeclarearrow{
  name = Cone1,
  defaults = {       % inherit from Kite
    length     = +3.6pt +5.4,
    width'     = +0pt +0.5,
    line width = +0pt 1 1,
    pitch      = +0, % lie on screen
  },
  cache = false,     % no need cache
  setup code = {},   % so no need setup
  drawing code = {   % but still need math
    % draw the base
    \pgfmathsetmacro\pgfarrowhalfwidth{.5\pgfarrowwidth}
    \pgfmathsetmacro\pgfarrowhalfwidthsin{\pgfarrowhalfwidth*abs(\pgfarrowsinpitch)}
    \pgfpathellipse{\pgfpointorigin}{\pgfqpoint{\pgfarrowhalfwidthsin pt}{0pt}}{\pgfqpoint{0pt}{\pgfarrowhalfwidth pt}}
    \pgfusepath{fill}
    % test if the cone part visible
    \pgfmathsetmacro\pgfarrowlengthcos{\pgfarrowlength*\pgfarrowcospitch}
    \ifdim\pgfarrowlengthcos pt>\pgfarrowhalfwidthsin pt
      % it is visible, so draw
      \pgfmathsetmacro\pgfarrowlengthtemp{\pgfarrowhalfwidthsin*\pgfarrowhalfwidthsin/\pgfarrowlengthcos}
      \pgfmathsetmacro\pgfarrowwidthtemp{\pgfarrowhalfwidth/\pgfarrowlengthcos*sqrt(\pgfarrowlengthcos*\pgfarrowlengthcos-\pgfarrowhalfwidthsin*\pgfarrowhalfwidthsin)}
      \pgfpathmoveto{\pgfqpoint{\pgfarrowlengthcos pt}{0pt}}
      \pgfpathlineto{\pgfqpoint{\pgfarrowlengthtemp pt}{ \pgfarrowwidthtemp pt}}
      \pgfpathlineto{\pgfqpoint{\pgfarrowlengthtemp pt}{-\pgfarrowwidthtemp pt}}
      \pgfpathclose
      \pgfusepath{fill}
    \else
      % it is invisible, check in pointing your eye
      \ifdim\pgfarrowsinpitch pt>0pt
      \pgfpathcircle{\pgfqpoint{\pgfarrowlengthcos pt}{0pt}}{.5\pgfarrowlinewidth}
      \pgfsetcolor{white}
      \pgfusepath{fill}
      \fi
    \fi
    \pgfpathmoveto{\pgfpointorigin}
  }
}
%\begin{tikzpicture}[line width=5]
%   \draw[-{Cone1          }](0,0,0)--(1,0,0);
%   \draw[-{Cone1          }](0,0,0)--(0,1,0);
%   \draw[-{Cone1[pitch=60]}](0,0,0)--(0,0,1);
%   \path(3,0,0)(0,3,0)(0,0,3);
%\end{tikzpicture}
%\foreach\theta in{0,10,...,350}{
%   \tikz[line width=5]\draw[-{Cone1[width'=0 1,pitch=\theta]}](-2,-.5)(2,.5)(0,0)--({cos(\theta)},0);
%}
%\foreach\theta in{0,10,...,350}{
%   \tikz[line width=5,opacity=.5]\draw[-{Cone1[width'=0 1,pitch=\theta]}](-2,-.5)(2,.5)(0,0)--({cos(\theta)},0);
%}

\def\pgfarrowtangenttosincos#1{
    #1
    \tdplotcrossprod(\pgf@xx,\pgf@yx,\pgf@zx)(\pgf@xy,\pgf@yy,\pgf@zy)
    \pgfmathsetmacro\pgfarrowtangentxxyy{\pgf@x*\pgf@x+\pgf@y*\pgf@y}
    \pgfmathsetmacro\pgfarrowtangentxy{sqrt(\pgfarrowtangentxxyy)}
    \pgfmathsetmacro\pgfarrowtangentz{(\pgftemp@x*\tdplotresx+\pgftemp@y*\tdplotresy+\pgftemp@z*\tdplotresz)/72.27*2.54}
    %\message{^^J^^J(\tdplotresx,\tdplotresy,\tdplotresz)(\pgfarrowtangentxy,\pgfarrowtangentz)}\show\\
    \pgfmathsetmacro\pgfarrowtangentxyz{sqrt(\pgfarrowtangentxxyy+\pgfarrowtangentz*\pgfarrowtangentz)}
    \pgfmathsetmacro\pgfarrowcospitch{\pgfarrowtangentxy/\pgfarrowtangentxyz}
    \pgfmathsetmacro\pgfarrowsinpitch{\pgfarrowtangentz/\pgfarrowtangentxyz}
}
\pgfkeys{
  /pgf/arrow keys/.cd,
  tangent/.code={%
    \tikz@scan@one@point\pgfarrowtangenttosincos#1
  }
}
\pgfdeclarearrow{
  name = Cone2,
  defaults = {             % inherit from Kite
    length     = +3.6pt +5.4,
    width'     = +0pt +0.5,
    line width = +0pt 1 1,
    tangent    = {(1,0,0)} % lie on x-axis
  },
  cache = false,           % no need cache
  setup code = {},         % so no need setup
  drawing code = {         % but still need math
    % draw the base
    \pgfmathsetmacro\pgfarrowhalfwidth{.5\pgfarrowwidth}
    \pgfmathsetmacro\pgfarrowhalfwidthsin{\pgfarrowhalfwidth*abs(\pgfarrowsinpitch)}
    \pgfpathellipse{\pgfpointorigin}{\pgfqpoint{\pgfarrowhalfwidthsin pt}{0pt}}{\pgfqpoint{0pt}{\pgfarrowhalfwidth pt}}
    \pgfusepath{fill}
    % test if the cone part visible
    \pgfmathsetmacro\pgfarrowlengthcos{\pgfarrowlength*\pgfarrowcospitch}
    \ifdim\pgfarrowlengthcos pt>\pgfarrowhalfwidthsin pt
      % it is visible, so draw
      \pgfmathsetmacro\pgfarrowlengthtemp{\pgfarrowhalfwidthsin*\pgfarrowhalfwidthsin/\pgfarrowlengthcos}
      \pgfmathsetmacro\pgfarrowwidthtemp{\pgfarrowhalfwidth/\pgfarrowlengthcos*sqrt(\pgfarrowlengthcos*\pgfarrowlengthcos-\pgfarrowhalfwidthsin*\pgfarrowhalfwidthsin)}
      \pgfpathmoveto{\pgfqpoint{\pgfarrowlengthcos pt}{0pt}}
      \pgfpathlineto{\pgfqpoint{\pgfarrowlengthtemp pt}{ \pgfarrowwidthtemp pt}}
      \pgfpathlineto{\pgfqpoint{\pgfarrowlengthtemp pt}{-\pgfarrowwidthtemp pt}}
      \pgfpathclose
      \pgfusepath{fill}
    \else
      % it is invisible, check in pointing your eye
      \ifdim\pgfarrowsinpitch pt>0pt
      \pgfpathcircle{\pgfqpoint{\pgfarrowlengthcos pt}{0pt}}{.5\pgfarrowlinewidth}
      \pgfsetcolor{white}
      \pgfusepath{fill}
      \fi
    \fi
    \pgfpathmoveto{\pgfpointorigin}
  }
}
\tdplotsetmaincoords{70}{110}
\begin{tikzpicture}[line width=5,tdplot_main_coords]
    \draw[-{Cone2[tangent={(1,0,0)}]}](0,0,0)--(1,0,0)node[cyan]{X};
    \draw[-{Cone2[tangent={(0,1,0)}]}](0,0,0)--(0,1,0)node[cyan]{Y};
    \draw[-{Cone2[tangent={(0,0,1)}]}](0,0,0)--(0,0,1)node[cyan]{Z};
    \path(-2cm,-2cm)(2cm,2cm);
\end{tikzpicture}

\foreach\theta in{0,5,...,355}{
    \tdplotsetrotatedcoords{\theta}{30}{30}
    \tikz[line width=5,line cap=round,tdplot_rotated_coords]{
        \draw[-{Cone2[tangent={(1,0,0)}]}](0,0,0)--(1,0,0)node[cyan]{X};
        \draw[-{Cone2[tangent={(0,1,0)}]}](0,0,0)--(0,1,0)node[cyan]{Y};
        \draw[-{Cone2[tangent={(0,0,1)}]}](0,0,0)--(0,0,1)node[cyan]{Z};
        \path(-2cm,-2cm)(2cm,2cm);
    }
}

\def\pgfpointxyz#1#2#3{%
  \pgfmathparse{#1}%
  \let\pgftemp@x=\pgfmathresult%
  \pgfmathparse{#2}%
  \let\pgftemp@y=\pgfmathresult%
  \pgfmathparse{#3}%
  \let\pgftemp@z=\pgfmathresult%
  \pgf@x=\pgftemp@x\pgf@xx%
  \advance\pgf@x by \pgftemp@y\pgf@yx%
  \advance\pgf@x by \pgftemp@z\pgf@zx%
  \pgf@y=\pgftemp@x\pgf@xy%
  \advance\pgf@y by \pgftemp@y\pgf@yy%
  \advance\pgf@y by \pgftemp@z\pgf@zy%
  % ↑↑↑old definition↑↑↑ ↓↓↓new code↓↓↓
  \global\let\pgfolderpointx\pgfoldpointx
  \global\let\pgfolderpointy\pgfoldpointy
  \global\let\pgfolderpointz\pgfoldpointz
  \global\let\pgfoldpointx\pgftemp@x
  \global\let\pgfoldpointy\pgftemp@y
  \global\let\pgfoldpointz\pgftemp@z
}

\pgfdeclarearrow{
  name = Cone3,
  defaults = {             % inherit from Kite
    length     = +3.6pt +5.4,
    width'     = +0pt +0.5,
    line width = +0pt 1 1,
    tangent    = {(1,0,0)} % lie on x-axis
  },
  cache = false,           % no need cache
  setup code = {},         % so no need setup
  drawing code = {         % but still need math
    % calculate the tangent
    \pgfkeys{pgf/arrow keys/tangent={(\pgfoldpointx-\pgfolderpointx,\pgfoldpointy-\pgfolderpointy,\pgfoldpointz-\pgfolderpointz)}}
    % draw the base
    \pgfmathsetmacro\pgfarrowhalfwidth{.5\pgfarrowwidth}
    \pgfmathsetmacro\pgfarrowhalfwidthsin{\pgfarrowhalfwidth*abs(\pgfarrowsinpitch)}
    \pgfpathellipse{\pgfpointorigin}{\pgfqpoint{\pgfarrowhalfwidthsin pt}{0pt}}{\pgfqpoint{0pt}{\pgfarrowhalfwidth pt}}
    \pgfusepath{fill}
    % test if the cone part visible
    \pgfmathsetmacro\pgfarrowlengthcos{\pgfarrowlength*\pgfarrowcospitch}
    \ifdim\pgfarrowlengthcos pt>\pgfarrowhalfwidthsin pt
      % it is visible, so draw
      \pgfmathsetmacro\pgfarrowlengthtemp{\pgfarrowhalfwidthsin*\pgfarrowhalfwidthsin/\pgfarrowlengthcos}
      \pgfmathsetmacro\pgfarrowwidthtemp{\pgfarrowhalfwidth/\pgfarrowlengthcos*sqrt(\pgfarrowlengthcos*\pgfarrowlengthcos-\pgfarrowhalfwidthsin*\pgfarrowhalfwidthsin)}
      \pgfpathmoveto{\pgfqpoint{\pgfarrowlengthcos pt}{0pt}}
      \pgfpathlineto{\pgfqpoint{\pgfarrowlengthtemp pt}{ \pgfarrowwidthtemp pt}}
      \pgfpathlineto{\pgfqpoint{\pgfarrowlengthtemp pt}{-\pgfarrowwidthtemp pt}}
      \pgfpathclose
      \pgfusepath{fill}
    \else
      % it is invisible, check in pointing your eye
      \ifdim\pgfarrowsinpitch pt>0pt
      \pgfpathcircle{\pgfqpoint{\pgfarrowlengthcos pt}{0pt}}{.5\pgfarrowlinewidth}
      \pgfsetcolor{white}
      \pgfusepath{fill}
      \fi
    \fi
    \pgfpathmoveto{\pgfpointorigin}
  }
}
\tdplotsetmaincoords{70}{110}
\begin{tikzpicture}[line width=5,tdplot_main_coords]
    \draw[-{Cone2[tangent={(1,0,0)}]}](0,0,0)--(1,0,0)node[cyan]{X};
    \draw[-{Cone2[tangent={(0,1,0)}]}](0,0,0)--(0,1,0)node[cyan]{Y};
    \draw[-{Cone2[tangent={(0,0,1)}]}](0,0,0)--(0,0,1)node[cyan]{Z};
    \path(-2cm,-2cm)(2cm,2cm);
\end{tikzpicture}

\foreach\theta in{0,5,...,355}{
    \tdplotsetrotatedcoords{\theta}{2*\theta}{3*\theta}
    \tikz[line width=5,line cap=round,tdplot_rotated_coords]{
        \draw[-Cone3](0,0,0)--(1,0,0)node[cyan]{X};
        \draw[-Cone3](0,0,0)--(0,1,0)node[cyan]{Y};
        \draw[-Cone3](0,0,0)--(0,0,1)node[cyan]{Z};
        \path(-2cm,-2cm)(2cm,2cm);
    }
}

\end{document}
```

<div align=center>
<image width="10%" src="programme/Latex/tikz&pgfplots/image/2022-03-26-12-17-52.png"/>
</div>

```latex
\documentclass[margin=10pt]{standalone}
\usepackage[svgnames]{xcolor}
\usepackage{tikz}
\begin{document}

\begin{tikzpicture}[scale=3]
\def\opaque{0.035}    % rendering opacity 
\def\prop{1.3}        % variable of rendering opacity
\def\R{2} %           % cone slant height
\def\theta{21}        % 2*\theta is the angle of expanded by the tip of the cone
\def\range{100}       % number of interaction for smooth rending effect
\def\ratio{0.4}       % ellipse b/a for cone lower edge 
\def\aratio{0.35}     % a_rod / a_cone  
\def\height{0.8}      % rod height 
\def\fraction{0.375}  % ellipse b/a for rod edge 
\def\angle{12}        % angle extended by rod edge
\def\total{60}        % number of interaction for smooth rending effect
\def\conecolor{red!\range!black!40!red}   % cone color 

\foreach \i in {0,...,\range}
{
    \fill[\conecolor, opacity={\opaque+\prop*\opaque*(\range-2*\i)/\range}] (0, {\R*cos(\theta)}) -- ({\R*sin(\theta)*cos(270+90*\i/\range)},{\ratio*\R*sin(\theta)*sin(270+90*\i/\range)})  arc({270+90*\i/\range}:360: {\R*sin(\theta)}  and {\ratio*\R*sin(\theta)} ) -- cycle;
    \fill[\conecolor, opacity={\opaque+\prop*\opaque*(\range-\i)/\range}] (0, {\R*cos(\theta)}) -- ({\R*sin(\theta)*cos(270-90*\i/\range)},{\ratio*\R*sin(\theta)*sin(270-90*\i/\range)})  arc({270-90*\i/\range}:180: {\R*sin(\theta)}  and {\ratio*\R*sin(\theta)} ) -- cycle;
}
\definecolor{conered}{RGB}{255,114,114}
\definecolor{conegreen}{RGB}{37,146,37}
\definecolor{coneblue}{RGB}{107,107,236}

\fill[conered] (-0.7167,0) arc (180:360: 0.7167 and 0.2867)  arc (0:180: 0.7167 and 0.2867) -- cycle ;

\pgfmathparse{\R*sin(\theta)*\aratio}

\fill[conered] (-0.251, -{sqrt(1-0.251*0.251/(0.7167*0.7167) )*0.2867}) arc ({360-acos(-0.251/0.7167) )}:{360-acos(0.251/0.7167 )}: 0.7167 and 0.2867 ) -- (0.251,-\height) arc (360:180:0.251 and 0.0941) --cycle ;

\foreach \i  in {0,...,\total}
{
    \fill[\conecolor, opacity={2*\opaque+\prop*\opaque*(\total-1*\i)/\total}] ({\pgfmathresult*\i/\total}, {\pgfmathresult*\ratio*sqrt(1-\i/\total*\i/\total) } )  arc ( {acos(\i/\total)}:0: {\R*sin(\theta)*\aratio} and {\R*sin(\theta)*\aratio*\ratio} ) -- ++(0,-\height) arc (360: {360-acos(\i/\total)}: {\R*sin(\theta)*\aratio} and {\R*sin(\theta)*\aratio*\ratio} ) -- cycle;
    \fill[\conecolor, opacity={2*\opaque+\prop*\opaque*(\total-1*\i)/\total}] ({-\R*sin(\theta)*\aratio*\i/\total}, {\R*sin(\theta)*\aratio*\ratio*sqrt(1-\i/\total*\i/\total) } )  arc ( {acos(-\i/\total)}:180: {\R*sin(\theta)*\aratio} and {\R*sin(\theta)*\aratio*\ratio} ) -- ++(0,-\height) arc (180: {360-acos(-\i/\total)}: {\R*sin(\theta)*\aratio} and {\R*sin(\theta)*\aratio*\ratio} ) -- cycle;
}

\draw[thick, conered, yshift=-0.8cm] (-0.251,0.8) -- (-0.251,0) arc (180:360:0.251 and 0.0941) -- (0.251,0.8);
\end{tikzpicture}

\end{document}
```
#### 绘制两条线之间的夹角

地址：<https://tex.stackexchange.com/questions/20826/label-angle-with-tikz?msclkid=b4b4feb5b1a611ecbd1923d402c29d8c>
<div align=center>
<image width="40%" src="programme/Latex/tikz&pgfplots/image/2022-04-01-18-45-20.png"/>
</div>

```latex
\documentclass{minimal}
\usepackage{tikz}
\usetikzlibrary{calc}

\begin{document}

\newcommand{\tikzAngleOfLine}{\tikz@AngleOfLine}
  \def\tikz@AngleOfLine(#1)(#2)#3{%
  \pgfmathanglebetweenpoints{%
    \pgfpointanchor{#1}{center}}{%
    \pgfpointanchor{#2}{center}}
  \pgfmathsetmacro{#3}{\pgfmathresult}%
  }

  \begin{tikzpicture}
    \coordinate (A) at (1,1);
    \coordinate (B) at ($(A)+(25:3)$);
    \coordinate (C) at ($(A)+(100:5)$);
    \draw (A) node[left]{$A$} -- (B) node[right]{$B$}node[midway,below]{$c$} -- (C)node[above]{$C$}node[midway,above]{$a$} -- (A)node[midway,left]{$b$};

    \tikzAngleOfLine(A)(B){\AngleStart}
    \tikzAngleOfLine(A)(C){\AngleEnd}
    \draw[red,<->] (A)+(\AngleStart:2cm) arc (\AngleStart:\AngleEnd:2 cm);
    \node[circle,fill=green] at ($(A)+({(\AngleStart+\AngleEnd)/2}:1 cm)$) {$\alpha$};
\end{tikzpicture}
\end{document} 
```


