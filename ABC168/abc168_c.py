# 2021/10/13

from math import cos, pi, sqrt

A, B, H, M = map(int, input().split())

T = 60 * H + M
theta_rad = 2 * pi * abs(M * 12 - T % 720) # 720倍

print(sqrt(A**2 + B**2 - 2 * A * B * cos(theta_rad / 720)))