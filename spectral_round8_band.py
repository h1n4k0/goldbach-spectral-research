#!/usr/bin/env python3
"""Finite-height rank-one Gram enclosure; GRH(N) only for Hardy identification.

Requires mpmath's outward interval arithmetic (tested with 1.3.0). This is
not an enclosure of the entire arithmetic cross, model, or full norm.
"""
from math import factorial
import mpmath
from mpmath import iv

N = 32768
Q = N // 4
J = 8
P = 6
T = iv.mpf(1) / 2**24
iv.dps = 40
I = iv.mpc(0, 1)
BERN = [(1,6), (-1,30), (1,42), (-1,30), (5,66), (-691,2730)]
# On the Cauchy disks for both boundary rectangles, Re z>=1/2, |z|<=1.
# |R|<=4*(2P)!/(6^(2P)*(2P-1/2)) J^(1/2-2P).
rem = (4*iv.mpf(factorial(2*P))/6**(2*P)
       * iv.mpf(J)**(iv.mpf(1)/2-2*P)/(2*P-iv.mpf(1)/2))
box = iv.mpc([-1,1], [-1,1])
REM = rem * box
DREM = (32*rem) * box


def check(p, text):
    if p is not True and p != True:
        raise ArithmeticError(text)


def abs2(z):
    return z.real**2 + z.imag**2


def euler_data(z):
    a, da = iv.mpc(1), iv.mpc(0)
    out = []
    for k in range(1, 2*P):
        a, da = a*(z+k-1), da*(z+k-1)+a
        if k % 2:
            up, down = BERN[(k-1)//2]
            fac = iv.mpf(up)/(down*factorial(k+1))
            out.append((k, fac*a, fac*da))
    return out


def hurwitz(z, r, pre):
    a = iv.mpf(r)/N
    f, df = iv.mpc(0), iv.mpc(0)
    for j in range(J):
        l = iv.ln(a+j)
        v = iv.exp(-z*l)
        f += v
        df -= v*l
    x = a+J
    lx = iv.ln(x)
    v = iv.exp(-z*lx)
    ze = z-1
    f += v*x/ze+v/2
    df -= v*x*(lx/ze+1/(ze*ze))+v*lx/2
    for k, c, dc in pre:
        p = v/x**k
        f += c*p
        df += (dc-c*lx)*p
    return f+REM, df+DREM


def fft_in_place(a, roots):
    n = len(a)
    k = 0
    for j in range(1, n):
        bit = n//2
        while k & bit:
            k ^= bit
            bit //= 2
        k ^= bit
        if j < k:
            a[j], a[k] = a[k], a[j]
    h = 2
    while h <= n:
        step = n//h
        for j in range(0,n,h):
            for k in range(h//2):
                x, y = a[j+k], roots[k*step]*a[j+k+h//2]
                a[j+k], a[j+k+h//2] = x+y, x-y
        h *= 2


def centered_fft(a, roots):
    centers = []
    radius = iv.mpf(0)
    for z in a:
        cr, ci = z.real.mid, z.imag.mid
        centers.append(iv.mpc(cr, ci))
        # The l1 rectangle radius bounds the complex disk radius. The exact
        # DFT twiddles have modulus 1, hence sum of radii works for every row.
        radius += abs(z.real-cr).b + abs(z.imag-ci).b
    fft_in_place(centers, roots)
    err = radius * box
    return [z + err for z in centers]


def odd_r3(sigma, roots, powers, k3):
    t = T*iv.mpf([-1,1])
    z = iv.mpc(iv.mpf(1)/2+sigma, t)
    check(z.real.a-iv.mpf(1)/32>iv.mpf(1)/2, "Re z on remainder disk")
    check(z.real.b+t.b+iv.mpf(1)/32<1, "|z| on remainder disk")
    pre = euler_data(z)
    f, df = [], []
    for r in powers:
        a, da = hurwitz(z, r, pre)
        b, db = hurwitz(z, N-r, pre)
        f.append(a-b)
        df.append(da-db)
    f = centered_fft(f, roots)
    df = centered_fft(df, roots)
    val = iv.mpc(0)
    mind = None
    for k in range(Q):
        d = abs2(f[k])
        check(d.a>0, f"zero denominator on band, character {k}")
        mind = d.a if mind is None or d.a < mind else mind
        val += roots[(-k*k3)%Q] * df[k] * iv.mpc(f[k].real, -f[k].imag) / d
    val = val/Q - iv.ln(3)*iv.exp(-z*iv.ln(3))
    return val, mind


def run():
    powers = [1]
    for _ in range(1,Q):
        powers.append(5*powers[-1]%N)
    check(len(set(powers))==Q and 5*powers[-1]%N==1 and
          all(r%4==1 for r in powers), "5 fails to generate 1 mod 4")
    k3 = powers.index(N-3)
    check(k3 != 0, "unexpected trivial residue phase")
    roots = [iv.exp(-I*(2*iv.pi*k/Q)) for k in range(Q)]
    L = 15*iv.ln(2)
    a, b = 1/L, iv.mpf(1)/8
    band = iv.mpf(0)
    for index,sigma in enumerate([a,b]):
        val, mind = odd_r3(sigma, roots, powers, k3)
        den = (1+sigma)**2 + (T*iv.mpf([-1,1]))**2
        band += 2*T*abs2(val)/den
        print("boundary", index, "; R_3 band:", val, "; min lower |DFT|^2:", mind, flush=True)
    d = (6*iv.pi*iv.ln(3)**2
         * sum((iv.exp((-2-2*s)*iv.ln(3))-iv.exp((-2-2*s)*iv.ln(4)))/(2+2*s)
               for s in (a,b)))
    print("d:", d)
    print("Band interval m_T:", d*band)
    print("No claim for |t| > T, the beta cross, or the high-by-high block.")


if __name__ == "__main__":
    run()
