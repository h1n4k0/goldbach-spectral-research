#!/usr/bin/env python3
"""Certified negative Rayleigh quotient at N=30030, conditional operator identification.

All inequality checks use Python integers and Fraction. No internet, external
packages, L-function values, zero lists, or approximate eigensolver are needed.
The fixed probe was selected exploratorily; verifying it is independent of that.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt

N, J, B = 30030, 16, 4
M = N * B
SCALE = 10**19
# Piecewise-linear knot heights f(i/J), including endpoints.
HEIGHT = (
    0, 0, 974, 1000, 846, 763, 686, 624, 601, 563, 548, 537, 523, 492, 466,
    431, 403, 381, 361, 338, 314, 288, 269, 254, 240, 229, 219, 208, 197,
    190, 184, 174, 164, 156, 146, 134, 121, 111, 104, 98, 92, 85, 80, 74,
    68, 61, 56, 51, 46, 41, 38, 33, 29, 25, 21, 18, 15, 12, 9, 7, 5, 4,
    3, 1, 0,
)
assert len(HEIGHT) == B * J + 1 and HEIGHT[0] == HEIGHT[1] == HEIGHT[-1] == 0


def sieve(limit):
    primal = bytearray(b'\x01') * (limit + 1)
    primal[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit) + 1):
        if primal[p]:
            primal[p*p:limit+1:p] = b'\x00' * ((limit - p*p)//p + 1)
    return [p for p in range(2, limit + 1) if primal[p]]


def floor(x):
    return x.numerator // x.denominator


def ceil(x):
    return -floor(-x)


def near_one_log(y, m=16):
    # 1<=y<=2, log y=2 arctanh((y-1)/(y+1)).
    assert 1 <= y <= 2
    t = (y - 1)/(y + 1)
    t2 = t*t
    a, val = t, F(0)
    for j in range(m):
        val += 2*a/(2*j+1)
        a *= t2
    return val, val + 2*a/((2*m+1)*(1-t2))


LOG2 = near_one_log(F(2))


@lru_cache(None)
def log_scaled(y):
    y = F(y)
    assert y >= 1
    k = y.numerator.bit_length() - y.denominator.bit_length()
    t = y / (2**k)
    if t < 1:
        k -= 1
        t *= 2
    assert k >= 0
    l, r = near_one_log(t)
    return floor(SCALE*(l + k*LOG2[0])), ceil(SCALE*(r + k*LOG2[1]))


def ht(i):
    return HEIGHT[i] if 0 <= i <= B*J else 0


def height_times_N(n):
    i, r = divmod(J*n, N)
    return ht(i)*(N-r) + ht(i+1)*r


def atom_bounds(primes):
    # After scaling, interval for Λ(n) f(n/N) has denominator SCALE*N.
    out = {}
    for p in primes:
        if N % p == 0:
            continue
        q = p
        a, b = None, None
        while q < M:
            h = height_times_N(q)
            if h:
                if a is None:
                    a, b = log_scaled(p)
                out[q] = (a*h, b*h)
            q *= p
    return out


def arithmetic_bounds(atom):
    lo = hi = num_diff = num_sum = 0
    for n, (a, b) in atom.items():
        for k in range(1, B+1):
            m = n+k*N
            if m in atom:
                c,d = atom[m]
                lo += 2*a*c
                hi += 2*b*d
                num_diff += 2
        for k in range(1, 2*B+1):
            m = k*N-n
            if m in atom:
                c,d = atom[m]
                lo -= b*d
                hi -= a*c
                num_sum += 1
    den = N**3 * SCALE**2
    return F(lo, den), F(hi, den), num_diff, num_sum


def prism(a, b, c, d):
    # 6 times integral on [0,1] of the two affine interpolants.
    return 2*a*c+a*d+b*c+2*b*d


def model_mass():
    val = 0
    for k in range(1, 2*B+1):
        for i in range(B*J):
            a,b = ht(i),ht(i+1)
            val += 2*prism(a,b,ht(i+k*J),ht(i+k*J+1))
            val -= prism(a,b,ht(k*J-i),ht(k*J-i-1))
    return F(val, 6*J)


def singular_series_bounds(primes):
    # Outward rounding of the twin product at every multiplicative step.
    lo = hi = SCALE
    div = F(2)
    for p in primes:
        if p == 2:
            continue
        d = (p-1)**2
        lo = lo*(d-1)//d
        hi = (hi*(d-1)+d-1)//d
        if N % p == 0:
            div *= F(p-1, p-2)
    # ∏(1-u_p) ≥ 1-Σu_p; Σ_{n>M}(n-1)^(-2) ≤ 1/(M-1).
    return F(lo, SCALE)*div*(1-F(1,M-1)), F(hi, SCALE)*div


def exp_upper(x, m=24):
    assert 0 <= x < m+2
    t = s = F(1)
    for k in range(1, m+1):
        t *= x/k
        s += t
    return s + t*x/(m+1)/(1-x/(m+2))


def weight_upper(x):
    # w_N(x) = 1/[exp(-2 log(Nx)/log N)+exp(-log(Nx)/4)].
    y = F(log_scaled(N*x)[1], SCALE)
    Llo = F(log_scaled(N)[0], SCALE)
    return 1/(1/exp_upper(2*y/Llo) + 1/exp_upper(y/4))


def q_upper(sub=8):
    # w_N increases; integrate |f/2-u f'|^2 exactly, using the right weight.
    q = F(0)
    for i in range(B*J):
        a, b = ht(i), ht(i+1)
        if a == b == 0:
            continue
        slope = J*(b-a)
        for p in range(sub):
            x = F(i*sub + p, J*sub)
            y = x+F(1, J*sub)
            fa = F(a) + slope*(x-F(i,J))
            aa, ab = fa/2 - x*slope, (fa+slope*(y-x))/2 - y*slope
            integral = (y-x)*(aa*aa+aa*ab+ab*ab)/3
            # Round weight upwards before summing, to keep denominators small.
            w_upper = F(ceil(weight_upper(y)*SCALE), SCALE)
            q += w_upper*integral
    # Elementary bound π>3.14.
    return q/F(628,100)


def display(x, *, upper, digs=8):
    scale = 10**digs
    q = ceil(x*scale) if upper else floor(x*scale)
    a, b = divmod(abs(q), scale)
    return ('-' if q < 0 else '') + f'{a}.{b:0{digs}d}'


def interval(a, b):
    return '[' + display(a, upper=False) + ', ' + display(b, upper=True) + ']'


def main():
    primes = sieve(M)
    slo, shi = singular_series_bounds(primes)
    atom = atom_bounds(primes)
    alo, ahi, nd, ns = arithmetic_bounds(atom)
    mass = model_mass()
    mlo,mhi = sorted((slo*mass, shi*mass))
    blo,bhi = alo-mhi, ahi-mlo
    qhi = q_upper()
    if not (qhi > 0 and bhi < -F(27,200)*qhi):
        raise ArithmeticError("Rayleigh enclosure does not clear the asserted bound")
    loglo,loghi = (F(k,SCALE) for k in log_scaled(N))
    if not (slo > 4 and F(43,100)**2 < slo*loglo**3/N
            and shi*loghi**3/N < F(44,100)**2):
        raise ArithmeticError("Singular series or spectral scale enclosure is inconsistent")
    print('N =', N, '; nonzero atoms =', len(atom),
          '; ordered difference / sum terms =', nd, '/', ns)
    print('singular series in', interval(slo,shi))
    print('arithmetic form in', interval(alo,ahi),
          '; exact signed continuous mass multiplier =', mass)
    print('residual numerator in', interval(blo,bhi),
          '; squared Hardy norm <=', display(qhi, upper=True))
    print('certified: lambda_min(T_30030) < -0.135, and 0.43 < delta_30030 < 0.44.')
    print('Only a lower bound for ||T_30030||; GRH(N) is assumed for operator identification.')


if __name__ == '__main__':
    main()
