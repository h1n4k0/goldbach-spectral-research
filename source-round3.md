# 第三轮：中间尺度的零点协方差与可检验的跨尺度目标

**完成两项推导，没有闭合 S 或 R。** 第一，对共同放大的一对平滑窗，精确算出模型基线并证明它等于奇特征族的单零点统计，剩余项是同一 L 函数内的异零点振荡及重零点过量。第二，给全累计核一个定量 dyadic 块判据，说明逐条素数对的平方根量级估计为何不能直接用三角不等式补齐中间带。

## 1. 平滑中间尺度的连续基线

记 $L=\log N$。固定实值 $f,g\in C_c^\infty(0,\infty)$；$f_Y(u)=f(u/Y)$、$g_Y(u)=g(u/Y)$，$Y\ge2$ 可随 $N$ 增长。令 $I=\int f(t)g(t)dt$、$H$ 为第一轮定义的两方向差卷积减和卷积（未放大）；$H(0)=2I$，$\int_0^\infty H(t)dt=0$。设 $\Phi_f(t)=\sqrt t\,f(t)$，Mellin 变换如 [Li–Liu 原文](https://mrc.sdu.edu.cn/__local/6/14/8E/28753731EE31D7635BAF60732C2_0C644604_2CE958.pdf)。连续模型矩阵元为
$$
K(f_Y,g_Y)=Y\sum_{k\ge1}\mathfrak S(kN)H(k/Y)
=\frac Y{2\pi i}\int_{(r)}Y^w\mathcal S_N(w)\widetilde H(w)\,dw ,\qquad r>1 .
$$
从原文 (2.11) 再完整抽出 $\zeta(1+w)$，得
$$
\begin{split}
\mathcal S_N(w)&=\zeta(w)\zeta(1+w)A_N(w),\\
A_N(w)&=2C_2(1-2^{-1-w})
\prod_{p\mid N,\ p>2}\frac{p-1}{p-2}(1-p^{-1-w})
\prod_{p\nmid N,\ p>2}(1+p^{-w}/(p-2))(1-p^{-1-w}).
\end{split}
$$
最后一组局部因子等于 $1+O_\kappa(p^{-2+2\kappa})$，故在 $\Re w\ge-\kappa$（固定 $0<\kappa<1/2$）绝对收敛并一致有界。其在 $0$ 的对数导数逐项为零；由 $C_2$、其余局部因子得到
$$
A_N(0)=1,\qquad A_N'(0)=\sum_{p\mid N}\frac{\log p}{p-1}.
$$
在移线用的新边界上，有限坏素数积 $\ll_\kappa\exp(C_\kappa L^\kappa)$：以 $p=L$ 截开 $\sum_{p\mid N}p^{-1+\kappa}$，小素数用整数和，大素数至多 $L/\log L$ 个。若令 $\kappa=1/\log L\le1/4$，小素数用 Mertens 倒数素数和且 $p^\kappa\le e$，同一上界改善至 $(\log L)^C$。

$\widetilde H(1)=0$ 抵消 $w=1$，$\widetilde H$ 在 $0$ 极点留数 $H(0)$，记常数项 $C_H$。平滑窗使其他竖直方向迅速衰减；可写 $\widetilde H(w)=-w^{-1}\int H'(t)t^{w}dt$ 并再分部积分，因此移到 $-\kappa$ 合法。$w=0$ 的双极点给
$$
\frac{K(f_Y,g_Y)}{Y}
=-I\left(\log Y+\log(2\pi)+\gamma_E+\sum_{p\mid N}\frac{\log p}{p-1}\right)
-\frac{C_H}{2}
+O_{f,g,\kappa}(Y^{-\kappa}e^{C_\kappa L^\kappa}).
$$
取上面的可变 $\kappa$ 时，误差可换成 $O_{f,g}(Y^{-1/\log L}(\log L)^C)$，把 ζ 因子和 Mellin 因子可能的 $\kappa^{-1}$ 吸收到固定幂次中。因而 $Y\ge\exp(C_D\log L\log\log L)$ 已足以得到 $(\log L)^{-D}$ 误差，不必等到幂次 $N^c$。

对角项为 $N^{-1}\sum_{(n,N)=1}\Lambda(n)^2 f(n/(NY))g(n/(NY))$。[普通素数定理的指数误差](https://doi.org/10.1016/j.jmaa.2023.127460) 与分部求和给
$$
\frac{D(f_Y,g_Y)}Y=I\log(NY)+\int f(t)g(t)\log t\,dt
+O_{f,g}(e^{-c\sqrt{\log(NY)}}+L\log(NY)/(NY)).
$$
剔除坏素数幂的误差可用 $\sum_{p\mid N}\log p\le L$ 直接估计。模型的 $-I\log Y$ 与对角的 $+I\log Y$ **严格配对抵消**。

## 2. 与奇特征族单零点项精确匹配

由原文 (2.12) 与 Mellin 卷积，
$$
\widetilde H(w)=\frac{\pi^w\zeta(1-w)}{\zeta(w)}J(w),\qquad
J(w)=\frac1{2\pi i}\int_{(0)}\widetilde\Phi_f(s)\widetilde\Phi_g(w-s)X_1(s)X_1(w-s)\,ds
$$
在 $w=0$ 的邻域解释为解析/亚纯延拓。原来 $\Re w>0$ 可先在 $\Re s=\Re w/2$ 取线，再短距离移线。$J(0)=I$，用 $X_1(s)X_1(-s)=1$；在积分内微分，$X_1'/X_1(-it)=-\Re\psi(3/4+it/2)$（$\psi=\Gamma'/\Gamma$）。前面的 ζ 比值为 $2/w-2(\log2+\gamma_E)+O(w)$，所以 $C_H=2J'(0)-2(\log2+\gamma_E)I$。$J'(0)$ 中由 $\widetilde\Phi_g'(w-s)$ 产生 $\int fg\log t$，正好抵消对角中的同项。于是 $(D+K)/Y$ 的显式基线可简写成
$$
\frac1{2\pi}\int_{\mathbb R}\widetilde\Phi_f(it)\widetilde\Phi_g(-it)
\left[\log\frac N\pi-\sum_{p\mid N}\frac{\log p}{p-1}+\Re\psi(3/4+it/2)\right]dt ,
$$
误差如第 1 节。特别地，$\log N-\sum_{p\mid N}\log p/(p-1)$ 等于模 $N$ 所有特征的平均本原导子对数：对 $p^a\Vert N$，导子 p 指数亏损的第 j 阶尾概率为 $\phi(p^{a-j})/\phi(p^a)$，对 $j\ge1$ 求和恰为 $1/(p-1)$。限于奇特征，只有约化模 $N/p^j\le2$ 时“恰一半奇”失效，误差 $O(L/\phi(N))$。

将 [Weil 公式的 Dirichlet 形式](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.70360) 用于本原诱导奇特征。固定测试函数 $t\mapsto\widetilde\Phi_f(it)\widetilde\Phi_g(-it)$ 的逆 Fourier 支撑由 f、g 的固定支撑比值控制，所以素数侧只出现有界的 $p^r$。若 $p\nmid N$，对奇特征的平均在足够大的 N 时严格为零，因为 $p^r$ 不可能 $\equiv\pm1\pmod N$。若 $p\mid N$，只须处理 p 不整除诱导本原导子的情形；这些特征由 $M=N/p^{v_p(N)}$ 诱导。平均值为
$$
\frac{\phi(M)}{\phi(N)}(\mathbf1_{p^r\equiv1\ (M)}-\mathbf1_{p^r\equiv-1\ (M)}),
$$
故要非零必须 $M\le p^r+1$，总贡献 $O_{f,g}(1/\phi(N))$。若测试函数非偶，可先在闭合于共轭的特征族取平均后用偶部。于是在 GRH(N) 下，$(D+K)/Y$ 等于奇特征族的单零点平均
$$
\mathbb E_{\chi\text{ 奇}}\sum_{\gamma}m_\chi(\gamma)
\widetilde\Phi_f(i\gamma)\widetilde\Phi_g(-i\gamma)
$$
加上述误差与 $O_{f,g}(L/\phi(N))$。这里 γ 取不同纵坐标，$m_\chi$ 为重数，并对每个 χ 使用其本原诱导 L 函数。

另一方面，对平滑素数和直接应用 $-L'/L$ 的 Mellin 移线：
$$
\frac{P_\chi(f_Y)}{\sqrt Y}
=-\sum_\gamma m_\chi(\gamma)\widetilde\Phi_f(i\gamma)e^{i\gamma\log(NY)}
+O_f(L/(NY)^{1/2}).
$$
平凡零点项很小（支撑远离 0）；原始与诱导特征相差的素数侧只在坏素数幂上，固定乘法窗口每个 p 中至多 $O_f(1)$ 个，对数权总计 $O_f(L)$。零点局部计数与 Mellin 衰减给绝对级数 $O_f(L)$，于是把两平滑素数和相乘后的误差为 $O_{f,g}(L^2/(NY)^{1/2})$。将 $D+K$ 从平均乘积扣掉，得到精确识别：
$$
\begin{split}
Y^{-1}\langle T_Nv_{f_Y},v_{g_Y}\rangle
={}&\mathbb E_{\chi\text{ 奇}} \sum_{\gamma\ne\gamma'}
m_\chi(\gamma)m_\chi(\gamma')
\widetilde\Phi_f(i\gamma)\widetilde\Phi_g(-i\gamma')
e^{i(\gamma-\gamma')\log(NY)}\\
&+\mathbb E_{\chi\text{ 奇}}\sum_\gamma m_\chi(\gamma)(m_\chi(\gamma)-1)
\widetilde\Phi_f(i\gamma)\widetilde\Phi_g(-i\gamma)+\text{上述显式误差}.
\end{split}
$$
这个结论只对共同放大的固定平滑窗口作出。固定 N 做任意长的相位平均不能控制随 N 统一的尺度；GRH(N) 本身也不排除重零点或给出异纵坐标项的抵消。原范数有 $\|v_{f_Y}\|^2\asymp_f Y(NY)^{2\alpha}$（对固定非零 f），因此在可用误差的范围内，S 所需的是上述振荡与重数偏差之和乘 $(NY)^{-2\alpha}$ 后达到 $O(\mathfrak S(N)/h(N))$。不能把它简化成“单零点密度正确”。R 的误差更小，这个基线移线误差在不少中间尺度仍不足。

## 3. 可复核的全块 Schur 门槛

对第二轮的累计核，取 $I_i=[2^i,2^{i+1})$、$i\ge0$ 并定义
$$
d_{ij}^2=\frac{\int_{I_i\times I_j}|M_N(x,y)/(xy)|^2\,dx\,dy}{\mathfrak S(N)^2|I_i||I_j|}.
$$
因为 $w_N(x)\asymp (Nx)^{2\alpha}$ 在 x≥1，整块含各接口方向的 HS 范数至多为 $C\mathfrak S(N)2^{-\alpha(i+j)}d_{ij}$。把任一输入向量按 dyadic 分块，对块的 L² 范数作 ℓ² 比较，得到相应非负数值矩阵的算子范数（进而其 Schur 行列和）是原压缩范数除以 $C\mathfrak S(N)$ 的上界。特别地，

* 若 $d_{ij}\le\varepsilon_N(1+|i-j|)^{-1-\nu}$，任意固定 $\nu>0$ 且 $\varepsilon_N\to0$，则该扇区为 $o(\mathfrak S(N))$；
* 若只知 $d_{ij}\le\varepsilon_N$，利用外积 $2^{-\alpha i}2^{-\alpha j}$，须 $\varepsilon_N L\to0$ 才由此法得到目标；
* 若每条别名线在任何长度 ≤X 的沿线窗中的未再加权误差有假想平方根界 $\le\mathfrak S(N)\varepsilon_N\sqrt X$（X≥1），在 x≈X≤y≈Y 的矩形里，各条线最多贡献 $O(\mathfrak S(N)\varepsilon_N\sqrt X\sqrt{XY})$，可用分部积分插入 $\sqrt{uv}$；其沿线总变差至多两倍上确界。约有 $O(Y)$ 条别名线，故逐条三角估计只能给 $d_{ij}\ll\varepsilon_N\sqrt Y$。对最大尺度 U 的前缀，用块 HS 平方求和得上界 $C\mathfrak S(N)\varepsilon_N U^{1/2-\alpha}\sqrt{\min(1+\log U,L)}$。即使 $\varepsilon_N=N^{-1/2}\operatorname{polylog}(N)$，在远尾压缩需要的 $U=N^{C\log\log N}$ 附近也不能闭合。

因此可以把待攻中间带定成一个可直接反验的目标：测算归一累计的 **带符号** 别名总和的 $d_{ij}$，检查是否有可积的尺度间衰减或可控矩阵范数。单独逐条算术相关的一致误差即使达到平方根级，也不足以从上述方法推出所需全算子估计；并非说排除了其他途径。
