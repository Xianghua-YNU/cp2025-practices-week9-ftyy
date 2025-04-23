import numpy as np
import matplotlib.pyplot as plt

def koch_generator(u, level):
    if level <= 0:
        return u
        
    theta = np.pi/3 # 旋转角度
    for _ in range(level):
        points = []
        for i in range(len(u)-1):
            start = u[i]
            end = u[i+1]
            
            # 生成科赫曲线的四个新线段
            p1 = u[i]
            p2 = u[i + 1]
            a = p1 + (p2 - p1) / 3
            b = p1 + (p2 - p1) * 2 / 3
            angle = np.pi / 3
            c = a + (b - a) * np.exp(1j * angle)
            
            points.extend([p1, a,c,b,p2])
        
        u = np.array(points)
    
    return np.array(u)

def minkowski_generator(u, level):
    u = np.array([0, 1]) # 初始水平线段
    
    theta = np.pi/2 # 旋转角度
    for _ in range(level):
        new_u = []
        for i in range(len(u)-1):
            p1 = u[i]
            p2 = u[i + 1]
            v = (p2 - p1) / 4
            
            # 生成Minkowski曲线的八个新线段
            pts = [
                p1,
                p1 + v,
                p1 + v + v * 1j,
                p1 + 2 * v + v * 1j,
                p1 + 2 * v,
                p1 + 2 * v - v * 1j,
                p1 + 3 * v - v * 1j,
                p1 + 3 * v,
                p2,
            ]
            new_u.extend(pts)
        
        u = np.array(new_u)
    
    return u


if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1])
    
    # 创建2x2子图布局
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    
    # 生成不同层级的科赫曲线
    for i in range(4):
        koch_points = koch_generator(init_u, i+1)
        axs[i//2, i%2].plot(koch_points.real, koch_points.imag, 'k-', lw=1)
        axs[i//2, i%2].set_title(f"Koch Curve Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    
    plt.tight_layout()
    plt.show()

    # 生成不同层级的Minkowski香肠
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        minkowski_points = minkowski_generator(init_u, i+1)
        axs[i//2, i%2].plot(minkowski_points.real, minkowski_points.imag, 'k-', lw=1)
        axs[i//2, i%2].set_title(f"Minkowski Sausage Level {i+1}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    
    plt.tight_layout()
    plt.show()
