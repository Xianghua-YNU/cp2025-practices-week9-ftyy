import numpy as np
import matplotlib.pyplot as plt

def koch_generator(u, level):
    if level == 0:
        return u
    points = []
    for i in range(len(u) - 1):
        p1 = u[i]
        p2 = u[i + 1]
        a = p1 + (p2 - p1) / 3
        b = p1 + (p2 - p1) * 2 / 3
        angle = np.pi / 3
        c = a + (b - a) * np.exp(1j * angle)
        # 只添加p1, a, c, b（不加p2，避免重复）
        points.extend([p1, a, c, b,p2])
    # 递归
    next_points = koch_generator(np.array(points), level - 1)
    # 递归后补上终点
    return np.concatenate([next_points, [u[-1]]])

def minkowski_generator(u, level):
    if level == 0:
        return u
    points = []
    for i in range(len(u) - 1):
        p1 = u[i]
        p2 = u[i + 1]
        v = (p2 - p1) / 4
        pts = [
            p1,
            p1 + v,
            p1 + v + v * 1j,
            p1 + 2 * v + v * 1j,
            p1 + 2 * v,
            p1 + 2 * v - v * 1j,
            p1 + 3 * v - v * 1j,
            p1 + 3 * v,
            p2
        ]
        points.extend(pts)
    # 递归
    next_points = minkowski_generator(np.array(points), level - 1)
    # 递归后补上终点
    return np.concatenate([next_points, [u[-1]]])

if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1])

    # 绘制不同层级的科赫曲线
    fig, axs = plt.subplots(2, 2, figsize=(6, 6))
    for i in range(4):
        koch_points = koch_generator(init_u, i + 1)
        axs[i//2, i%2].plot(
            np.real(koch_points), np.imag(koch_points), 'k-', lw=1
        )
        axs[i//2, i%2].set_title(f"Koch Curve Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.show()

    # 绘制不同层级的闵可夫斯基香肠曲线
    fig, axs = plt.subplots(2, 2, figsize=(6, 6))
    for i in range(4):
        minkowski_points = minkowski_generator(init_u, i + 1)
        axs[i//2, i%2].plot(
            np.real(minkowski_points), np.imag(minkowski_points), 'k-', lw=1
        )
        axs[i//2, i%2].set_title(f"Minkowski Sausage Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.show()
