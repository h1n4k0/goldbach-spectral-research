# 中央 Type II：两块逐模数消去

[Type I 约化与双外侧](WEAK-S-SECTOR-REDUCTIONS.md) · [中央正性的平滑截断判据](spectral-signed-rectangle-smooth-bridge.md) · [研究状态](POST-R-STATUS.md)

两项结果处理 [Vaughan 分解](spectral-vaughan-central-type-i.md)后真实剩下的带符号中央和式。保持 $N^{.49999}\le t\le N^{.50001}$、$N/2<n\le y\le9N/16$，以及原始条件 $uv+dk=N$、$k>t$、$(uv,N)=1$。设 $L=\log N$，原来的 Vaughan 阈值为 $U=V=N^{.2499}$。以下上界针对带真正的 $\mu(u)\mu(d)b_{\rm II}(v)\mu^2(dk)$ 系数的原始和式，不是无符号的格点估计。

1. [左侧条带，无条件](weak-s-type-ii-left-strip.md)。在 $N^{.2499}<u\le N^{.265}$，保留所有合格的 $d,k$，整个条带均为 $O_A(NL^{-A})$，任意固定 $A>0$。证明利用 [Bettin–Chandee 的三线性估计](https://arxiv.org/pdf/1502.00769#page=2)控制精确保留下来的移动端点，再抵消重组后的密度项；不是把旧 Type I 的短除数阈值直接调大。
2. [乘积截断，在全局 Dirichlet GRH 下](weak-s-type-ii-character-average.md)。在 $u>N^{.265}$，保留精确条件 $d\le D$、$dv\le E$，对应和式为 $O_{A,\epsilon}(NL^{-A}+N^{1/2+\epsilon}(D+\sqrt E))$。取 $D=N^{.4975}$、$E=N^{.995}$ 即得到任意固定逆对数精度。这里用特征平均与位移后的 $\mu(u)$ Perron 估计，需要辅助模数上的 GRH，而非仅原模数的局部 GRH。

若假设全局 Dirichlet GRH，将两块从原中央增量中去除后，在所述 $t$ 带内仍须估计 $u>N^{.265}$、$v>N^{.2499}$，且满足 $d>N^{.4975}$ **或** $dv>N^{.995}$ 的真实带符号剩余项。两项都对各自的硬端点 $t,y$ 一致，但没有覆盖整个 $t$ 轴，没有证明所需的中央矩形误差界，也没有证明弱 S。
