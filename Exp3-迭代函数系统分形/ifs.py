import numpy as np
import matplotlib.pyplot as plt

def get_fern_params():
    """
    返回巴恩斯利蕨的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    return [
        [0.0, 0.0, 0.0, 0.16, 0.0, 0.0, 0.01],  # 变换1
        [0.85, 0.04, -0.04, 0.85, 0.0, 1.6, 0.85],  # 变换2
        [0.2, -0.26, 0.23, 0.22, 0.0, 1.6, 0.07],  # 变换3
        [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.07]  # 变换4
    ]

def get_tree_params():
    """
    返回概率树的IFS参数
    每个变换包含6个参数(a,b,c,d,e,f)和概率p
    """
    return [
        [0.05, 0.0, 0.0, 0.6, 0.0, 0.0, 0.1],  # 变换1
        [0.05, 0.0, 0.0, -0.5, 0.0, 1.0, 0.1],  # 变换2
        [0.46, -0.15, 0.39, 0.38, 0.0, 0.6, 0.4],  # 变换3
        [0.47, -0.15, 0.17, 0.42, 0.0, 1.1, 0.4]  # 变换4
    ]

def apply_transform(point, params):
    """
    应用单个变换到点
    :param point: 当前点坐标(x,y)
    :param params: 变换参数[a,b,c,d,e,f,p]
    :return: 变换后的新坐标(x',y')
    """
    x, y = point
    a, b, c, d, e, f, _ = params
    x_new = a * x + b * y + e
    y_new = c * x + d * y + f
    return x_new, y_new

def run_ifs(ifs_params, num_points=100000, num_skip=100):
    """
    运行IFS迭代生成点集
    :param ifs_params: IFS参数列表
    :param num_points: 总点数
    :param num_skip: 跳过前n个点
    :return: 生成的点坐标数组
    """
    points = []
    x, y = 0, 0  # 初始点
    probabilities = [param[-1] for param in ifs_params]

    for i in range(num_points + num_skip):
        # 使用 numpy.random.choice 根据概率选择变换索引
        index = np.random.choice(len(ifs_params), p=probabilities)
        params = ifs_params[index]
        x, y = apply_transform((x, y), params)
        if i >= num_skip:  # 跳过前num_skip个点
            points.append((x, y))
    return np.array(points)

def plot_ifs(points, title="IFS Fractal"):
    """
    绘制IFS分形
    :param points: 点坐标数组
    :param title: 图像标题
    """
    x, y = points[:, 0], points[:, 1]
    plt.figure(figsize=(8, 8))
    plt.scatter(x, y, s=0.1, color="green")
    plt.title(title)
    plt.axis("equal")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    # 生成并绘制巴恩斯利蕨
    fern_params = get_fern_params()
    fern_points = run_ifs(fern_params)
    plot_ifs(fern_points, "Barnsley Fern")
    
    # 生成并绘制概率树
    tree_params = get_tree_params()
    tree_points = run_ifs(tree_params)
    plot_ifs(tree_points, "Probability Tree")
