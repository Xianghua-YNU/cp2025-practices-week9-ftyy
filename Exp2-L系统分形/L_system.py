"""
项目2: L-System分形生成与绘图模板
请补全下方函数，实现L-System字符串生成与绘图。
"""
import matplotlib.pyplot as plt
import math

def apply_rules(axiom, rules, iterations):
    """
    生成L-System字符串
    :param axiom: 初始字符串（如"F"或"0"）
    :param rules: 规则字典，如{"F": "F+F--F+F"} 或 {"1": "11", "0": "1[0]0"}
    :param iterations: 迭代次数
    :return: 经过多轮迭代后的最终字符串
    """
    # TODO: 实现L-System字符串生成逻辑

    current = axiom
    for _ in range(iterations):
        new_str = []
        for char in current:
            new_str.append(rules.get(char, char))
        current = ''.join(new_str)
    return current

def draw_l_system(instructions, angle, step, start_pos=(0,0), start_angle=0, savefile=None):
    """
    根据L-System指令绘图
    :param instructions: 指令字符串（如"F+F--F+F"）
    :param angle: 每次转向的角度（度）
    :param step: 每步前进的长度
    :param start_pos: 起始坐标 (x, y)
    :param start_angle: 起始角度（0表示向右，90表示向上）
    :param savefile: 若指定则保存为图片文件，否则直接显示
    """
    # TODO: 实现L-System绘图逻辑
    
    x, y = start_pos
    current_angle = start_angle  # 初始角度以度为单位
    stack = []
    ax = plt.gca()
    
    for cmd in instructions:
        if cmd == '+':
            current_angle += angle
        elif cmd == '-':
            current_angle -= angle
        elif cmd == '[':
            stack.append((x, y, current_angle))
            current_angle += angle
        elif cmd == ']':
            if stack:
                x_prev, y_prev, angle_prev = stack.pop()
                x, y = x_prev, y_prev
                current_angle = angle_prev
                current_angle -= angle
        else:
            # 计算移动方向
            rad_angle = math.radians(current_angle)
            dx = step * math.cos(rad_angle)
            dy = step * math.sin(rad_angle)
            nx = x + dx
            ny = y + dy
            # 绘制线段
            ax.plot([x, nx], [y, ny], color='black', linewidth=1)
            x, y = nx, ny

    # 设置坐标轴属性
    ax.axis('equal')
    ax.axis('off')
    
    # 保存或显示图像
    if savefile:
        plt.savefig(savefile, bbox_inches='tight', pad_inches=0)
        plt.close()
    else:
        plt.show()
if __name__ == "__main__":
    """
    主程序示例：分别生成并绘制科赫曲线和分形二叉树
    学生可根据下方示例，调整参数体验不同分形效果
    """
    # 1. 科赫曲线
    axiom = "F"
    rules = {"F": "F+F--F+F"}
    iterations = 3
    angle = 60
    step = 5
    instr = apply_rules(axiom, rules, iterations)
    plt.figure(figsize=(8, 8))
    draw_l_system(instr, angle, step, start_angle=0, savefile="l_system_koch.png")

    # 2. 分形树
    axiom = "0"
    rules = {"1": "11", "0": "1[0]0"}
    iterations = 5
    angle = 45
    step = 5
    instr = apply_rules(axiom, rules, iterations)
    plt.figure(figsize=(8, 8))
    draw_l_system(instr, angle, step, start_pos=(0, -100), start_angle=90, savefile="fractal_tree.png")
