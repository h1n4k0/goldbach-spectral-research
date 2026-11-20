#!/usr/bin/env python3
"""Bounded two-node Gauss go/no-go at N=32768, H=1/16.

Returns a validated quadrature SUM and the (loose) proven error from a
Bernstein ellipse. It does not bound the full cross or operator norm.
"""
from time import perf_counter
from mpmath import iv
import spectral_round8_band as r8

N, Q, I = r8.N, r8.Q, r8.I
H = iv.mpf(1)/16


def odd_r3_at(sigma, t, roots, powers, k3):
    z = iv.mpc(iv.mpf(1)/2+sigma, t)
    r8.check(z.real.a-iv.mpf(1)/32>iv.mpf(1)/2, "Re z on remainder disk")
    r8.check(z.real.b+abs(t).b+iv.mpf(1)/32<1, "|z| on remainder disk")
    pre = r8.euler_data(z)
    f, df = [], []
    for r in powers:
        a, da = r8.hurwitz(z, r, pre)
        b, db = r8.hurwitz(z, N-r, pre)
        f.append(a-b)
        df.append(da-db)
    f = r8.centered_fft(f, roots)
    df = r8.centered_fft(df, roots)
    val = iv.mpc(0)
    mind = None
    for k in range(Q):
        d = r8.abs2(f[k])
        r8.check(d.a>0, f"zero denominator at Gauss node, character {k}")
        mind = d.a if mind is None or d.a < mind else mind
        val += roots[(-k*k3)%Q]*df[k]*iv.mpc(f[k].real, -f[k].imag)/d
    val = val/Q - iv.ln(3)*iv.exp(-z*iv.ln(3))
    return val, mind


def run():
    start = perf_counter()
    powers = [1]
    for _ in range(1,Q):
        powers.append(5*powers[-1]%N)
    r8.check(len(set(powers))==Q and 5*powers[-1]%N==1 and
          all(r%4==1 for r in powers), "5 fails to generate 1 mod 4")
    k3 = powers.index(N-3)
    r8.check(k3!=0, "nontrivial phase needed for log N cancellation")
    roots = [iv.exp(-I*(2*iv.pi*k/Q)) for k in range(Q)]
    L = 15*iv.ln(2)
    a, b = 1/L, iv.mpf(1)/8
    x = H/iv.sqrt(3)
    d = (6*iv.pi*iv.ln(3)**2*
         sum((iv.exp((-2-2*s)*iv.ln(3))-iv.exp((-2-2*s)*iv.ln(4)))/(2+2*s)
               for s in (a,b)))
    r8.check(a.a/2>iv.mpf(3)/64, "ellipse leaves the certified strip")
    v = (22*L**2*iv.ln(4*N*(4+iv.mpf(5)/64)) + iv.ln(3))**2
    c = 32*H*d*v
    eps = iv.mpf(1)/10000
    m = next(m for m in range(1,80) if (c/2**(2*m)).b < eps.a)
    print("ellipse prefactor C:", c)
    print("E_2 <= ", (c/2**4).b)
    print("first m whose envelope C*2^(-2m) < 1e-4:", m,
          "(total distinct boundary evaluations =", 2*((m+1)//2),")", flush=True)
    val = iv.mpf(0)
    for index,sigma in enumerate((a,b)):
        prior = perf_counter()
        r3, mind = odd_r3_at(sigma,x,roots,powers,k3)
        dt = perf_counter()-prior
        val += 2*H*d*r8.abs2(r3)/((1+sigma)**2+x*x)
        print("line",index,"time seconds",format(dt,'.3f'),
              "R_3 at positive node",r3,"min lower |DFT|²",mind,flush=True)
    print("two-point Gauss SUM (not integral):",val)
    print("total elapsed seconds:",format(perf_counter()-start,'.3f'))
    print("No useful numerical integral bound from the two-point rule under this envelope.")


if __name__=="__main__":
    run()
