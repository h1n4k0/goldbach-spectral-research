# 第十一轮：倍平方族上，固定补偿块的例外数进一步缩小

**S、R 仍未证明，也未否证。** 这次推进的是一个稀疏模数族、一个固定窗口的定量例外数，不是全算子上界，也不是所有倍平方模数都成立的逐项估计。

令 $X=8R^2$，$N=2r^2$，$R<r\le2R$，$L=\log X$，并记物理对数窗口 $J=[\log(1/2),\log(9/16)]$。在**全局 Dirichlet GRH** 下，对任意固定 $A>0,\epsilon>0$，
$$
 \#\left\{R<r\le 2R:\ \|\mathbf1_JT_{2r^2,\log}\mathbf1_J\|_{HS}>L^{-A}\right\}
 \ll_{A,\epsilon}X^{1/3+\epsilon}.
$$
[第十轮](ROUND10.md)的同一块均方界直接用 Markov 不等式只能给 $O(X^{199/400}L^{2A})$。这里选定实际例外子集再做圆法：平方差分解使次弧代价按子集大小的平方根增长；主弧和级数尾逐模数控制。随后对移动矩形作夹逼，再积分到整个固定 $J\times J$ 的 Hilbert–Schmidt 范数。全局 GRH 用于主弧的辅助模数，不能只假设被测模数的局部 GRH。

[推导](arithmetic-post-round10-exceptions.md)还给出随阈值变化的形式：对固定 $0<\delta<1/12$，当 $X^{-\delta/4}\le\tau\le1$，例外数为 $O_{\delta,\epsilon}(\tau^{-6}X^{1/3+\delta/2+\epsilon})$。[独立复核](review-post-round10-exceptions.md)记录了各指数、区间处理和假设范围。

这是相对于项目既有 **Beta 补偿块**的改进，不是对“无任何哥德巴赫表示”例外数的新纪录。窗口外的交叉作用、剩下的例外和逐模数全范数都未控制。
