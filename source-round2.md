# 第二轮：真实算子的累计偏差核与紧尺度等价判据

结论：在 Li–Liu 的 GRH(N) Hardy 实现下，把 $T_N$ 完整等距搬到物理坐标，核正是一次双重累计的有符号素数对偏差。该变换包含半格接口方向。每个固定前缀压缩在 $o(\mathfrak S(N))$ 尺度上与相应加权 Hardy–Littlewood 偏差的弱收敛等价，同时也等价于其 Hilbert–Schmidt 范数在同尺度趋零。这些结论不处理无限物理尺度尾项，因而没有证明 Hypothesis S 或 R。

## 1. 有符号局部测度与精确核

用 $u=n/N$、$v=m/N$，记 $\mu_N$ 为以下局部有限的实对称测度。对于 $k\ge1$，分别在 $v=u+k$ 和转置直线上取正号、在 $v=k-u$ 上取负号，只考虑 $u,v>0$。每条线的贡献是实际原子测度减连续测度 $\mathfrak S(kN)\,du$，实际原子在 $(n/N,m/N)$，权重 $N^{-1}\Lambda(n)\Lambda(m)$，仅含 $(nm,N)=1$ 的格点。注意 $du$ 是按第一个坐标参数化，不是弧长。原文 §7.1–§7.2 的极化如第一轮报告所证：
$$
\langle T_N v_f,v_g\rangle=\int f(u)g(v)\,d\mu_N(u,v)\quad(f,g\in C_c^\infty(0,\infty)\text{ 为实值}).
$$

记 $\alpha=1/\log N,\ \beta=1/8,\ \Delta=\beta-\alpha$ 与
$$
w_N(x)=\frac{(Nx)^{2\alpha}}{1+(Nx)^{-2\Delta}},\quad a_f(x)=(1/2-x\partial_x)f(x).
$$
原文 (2.37) 化为 $\|v_f\|^2=(2\pi)^{-1}\int_0^\infty w_N(x)|a_f(x)|^2dx$。由 Fourier–Laplace 表示，反射、乘权并极化后，$v_f\leftrightarrow\sqrt{w_N/(2\pi)}a_f$ 是到普通 $L^2(dx)$ 的等距变换，实向量配对直接成立，随后复线性延拓。密度也可用下一步的逆公式证明。

对光滑紧支撑的 $a$（支撑远离 0），逆为
$$
f(u)=\sqrt u\int_u^\infty a(x)x^{-3/2}dx .
$$
它在上端至多到达 $a$ 的支撑，在 0 邻域恰为常数乘 $\sqrt u$。乘平滑截断在 $u\to0$ 逼近原测试空间：对固定 $N$，$w_N(u)\asymp(Nu)^{2\beta}$，导数误差支撑在 $u\asymp\varepsilon$，且 $a$ 的加权均方误差趋零。对任一固定 $N$ 及固定反演窗的上界，足够小的下端无实际格点，有限条连续模型线的积分由支配收敛逼近。因此真实算子矩阵元在此稠密坐标类上等于相同测度配对。

两次使用逆公式与 Fubini 得真实算子的核：
$$
\mathcal K_N(x,y)=\frac{2\pi M_N(x,y)}
{x^{3/2}y^{3/2}\sqrt{w_N(x)w_N(y)}},\qquad
M_N(x,y)=\int_{(0,x]\times(0,y]}\sqrt{uv}\,d\mu_N(u,v).
$$
紧支撑坐标上的 Fubini 只涉及有限条线与有界格点。每个远离 0、无穷的平方盒内，此候选核是 $L^2$ 并给出相同压缩；原算子全局是 Hilbert–Schmidt，在重叠的盒上其核唯一。穷尽正半轴即可得到全局核的几乎处处相等与全局 $L^2$，不必先用算术证明尾项可积。这一同构下 $\mathcal K_N$ 包含整个空间，包括第一轮的各补方向。

## 2. 半格交叉项的接口拆分

令 $I_j=(j/2,(j+1)/2)$，$\ell_j=j/2$。在 $I_j\times I_k$ 有精确拆分
$$
M_N(x,y)=M_N(x,\ell_k)+M_N(\ell_j,y)-M_N(\ell_j,\ell_k)+
\int_{(\ell_j,x]\times(\ell_k,y]}\sqrt{uv}\,d\mu_N .
$$
乘上分离乘子后，前三项总秩至多 2，因为它们为一项仅依 $x$ 与一项仅依 $y$ 的和。在两侧都属于原半格内窗闭包时，接口项恰被 $\int_{I_j}a(x)x^{-3/2}dx=0$ 消去；对半格全空间仍须保留。$N>2$ 时，半格边界不会含实际原子（$n/N=j/2$ 则 $(n,N)\ge N/2$）；模型为沿斜线的连续测度，边界也无质量。

最后一项由唯一可能的直线贡献。设 $D(t)$ 是此直线从 $\ell_j$ 到 $t$ 的 $\sqrt{uv}$ 加权有符号偏差前缀。对平移 $v=u+d$，内核是 $D(\min(x,y-d))$；反向平移的 $d$ 为负也适用；对反射 $v=c-u$，内核是 $\mathbf1_{x\ge c-y}(D(x)-D(c-y))$，略去零测集上的端点差别。若整块不含直线或 $j=k$，内核为零。去掉正乘子后，$r=\ell_j+1/2$、$L=1/2$ 时的平方 HS 范数精确为
$$
2\int_{\ell_j}^r(r-t)|D(t)|^2dt\quad\text{（平移）},\qquad
L\int_{\ell_j}^r |D(t)-\overline D|^2dt\quad\text{（反射）},
$$
其中 $\overline D$ 是区间平均值。第一个式子按 $\min(x,y-d)$ 分层，第二个式子是整个平方差分积分的一半。远离 0 的任何固定半格对乘子上下界一致，故可直接把这两个式子转成带权 HS 范数的双边估计。此估计是对去接口的内部核，不是整体，不能假设接口与它不相消。

## 3. 紧尺度控制：低尺度边缘无须新算术假设

对固定 $A>0$，在 $x,y\le A$ 只出现有限条别名线。对固定 $k\le2A$ （差线的 k 更小），$\mathfrak S(kN)\ll_A\mathfrak S(N)$；其下界 $\mathfrak S(N)\gg1$。二元筛给长度为 $Y$ 的任意整数区间中两线性式 $n,\,kN\pm n$ 同时为正素数的上界 $O(Y\mathfrak S(kN)/(\log Y)^2)$，在 $Y\ge N^{3/4}$、两线性式 $\le AN$ 时为统一界。可用 [Matomäki–Merikoski，Lemma 3.2 的上筛权与证明](https://www.utupub.fi/server/api/core/bitstreams/8f46b427-a8ed-4ffd-af2e-0534078bc62c/content) 验证：对素数 p，禁类数 $\nu(p)$ 在 $p\mid kN$ 是 1，其余是 2。取筛级 $D=Y^\theta$ 与筛界 $z=Y^{1/U}$，固定小 $\theta$ 与大 $U$。主项 $\ll Y\prod_{p<z}(1-\nu(p)/p)\ll Y\mathfrak S(kN)/(\log Y)^2$；区间的同余计数余项是 $O(\sum_{d\le D}2^{\omega(d)})=O(D\log D)$。若只有一坐标是 $<z$ 的素数至多 $O(z)$ 个候选，亦可吸收。加 $\Lambda$ 双权后，每个区间的总质量为 $O_A(Y\mathfrak S(N))$；真素数幂总误差粗估 $O_A(\sqrt N(\log N)^3)$，同样可吸收。

设 $0<\varepsilon<1/4$。当 $x\le\varepsilon$ 时，非零的 $M_N(x,y)$ 要 $y\ge3/4$，因为第一条和或差直线距离原点的纵向截距至少为 1。此时 y 方向的分母一致上下有界。由筛上界和乘子 $\sqrt u\le\sqrt x$，对 $N^{-1/4}\le x\le\varepsilon$ 有 $|M_N(x,y)|\ll_A\mathfrak S(N)x^{3/2}$。对 $1/N\le x\le N^{-1/4}$ 用逐点 $\Lambda\le O_A(\log N)$ 给 $|M_N(x,y)|\ll_A(\log N)^2x^{3/2}$。当 $x<1/N$ 无实际原子，模型仍满足 $|M_N(x,y)|\ll_A\mathfrak S(N)x^{3/2}$，且 $w_N(x)\asymp (Nx)^{2\beta}$、$2\beta<1$。三个范围分开积分得到
$$
\big\|\mathbf1_{(0,\varepsilon)}\mathcal K_N\mathbf1_{(0,A)}\big\|_{HS}
\ll_A \mathfrak S(N)\sqrt\varepsilon+N^{-1/8}(\log N)^2 .
$$
这条数论/积分核估计无条件；把核认作原 Hardy 实现仍以 GRH(N) 为前提。它不估计 $y>A$，也通常不能逼近 R 所需误差。

## 4. 紧尺度上的等价结论

固定 $A>0$。沿所考虑的满足 GRH(N) 的偶数序列，以下等价：

1. $\|\mathbf1_{(0,A)}\mathcal K_N\mathbf1_{(0,A)}\|=o(\mathfrak S(N))$。
2. $\|\mathbf1_{(0,A)}\mathcal K_N\mathbf1_{(0,A)}\|_{HS}=o(\mathfrak S(N))$。
3. 在 $(0,A)^2$ 的每一段正/负别名线上，实际素数幂双权测度减 $\mathfrak S(kN)du$，在除以 $\mathfrak S(N)$ 后，对每个固定的连续紧支撑沿线测试函数弱趋零。

$2\Rightarrow1$ 是标准范数关系。$1\Rightarrow3$：以第 2 节的几何定位和不交其他别名线的小盒，用一侧 $f$ 设沿线的光滑测试，另一侧 $g=1$ 覆盖所需像。两者的等距坐标向量支撑均在 $(0,A)$，范数对固定窗一致有界。别名线交点及截断边界可先删小邻域；上筛对长为固定比例 $\rho N$ 的任意滑动区间给归一化质量 $O_A(\rho)$，常数与固定 $\rho$ 无关，只要求 N 足够大。再令 $\rho\downarrow0$，并用一致逼近从光滑推广至连续测试函数。

$3\Rightarrow2$：上筛给每条归一化测度在有限正方形中的总变差 $O_A(1)$，且边缘窄段质量如上可一致做小。因此用连续窗夹逼每个矩形边界，得到 $M_N(x,y)/\mathfrak S(N)\to0$（对几乎处处的固定 $x,y<A$ 已足够），并有一致有界性。正乘子在 $[\varepsilon,A]^2$ 一致有界，由支配收敛得到此区域 HS 为 $o(\mathfrak S(N))$。最后用第 3 节消去低边，再令 $\varepsilon\downarrow0$。

全空间的 S 仍需求随尺度一致的跨块抵消或可控尾项。不能从每个固定 A 的结论交换 $A\to\infty$ 与 $N\to\infty$。给定事先指定的具体 $h(N)$ 或 R 的 $\delta_N$ 还要求相应定量速度，弱趋零本身不提供速度。
