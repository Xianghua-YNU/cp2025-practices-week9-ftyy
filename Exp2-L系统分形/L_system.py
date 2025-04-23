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

    current = axiom#初始字符串
    # 迭代次数
    for _ in range(iterations):
        # 生成新的字符串
        new_str = []
        for char in current:# 遍历当前字符串的每个字符
            # 如果字符在规则中，则替换为对应的字符串，否则保持不变
            new_str.append(rules.get(char, char))#规则字典中查找字符对应的字符串
        current = ''.join(new_str)#  # 将列表转换为字符串
    # 返回最终生成的字符串
    return current

def draw_l_system(instructions, angle, step, start_pos=(0,0), start_angle=0, savefile=None, tree_mode=False):
    """
    根据L-System指令绘图
    :param instructions: 指令字符串（如"F+F--F+F"）
    :param angle: 每次转向的角度（度）
    :param step: 每步前进的长度
    :param start_pos: 起始坐标 (x, y)
    :param start_angle: 起始角度（0表示向右，90表示向上）
    :param savefile: 若指定则保存为图片文件，否则直接显示
    :param tree_mode: 是否启用树模式，若为True，则不对角度进行额外调整
    """
    x, y = start_pos#   起始坐标
    # 设置当前角度为起始角度
    current_angle = start_angle
    stack = []# 用于存储位置和角度的栈
    ax = plt.gca()# 获取当前坐标轴
    
    for cmd in instructions:#   遍历指令字符串中的每个字符
        if cmd == '+':# 如果是加号，则顺时针转动
            current_angle += angle
        elif cmd == '-':# 如果是减号，则逆时针转动
            current_angle -= angle
        elif cmd == '[':# 如果是左方括号，则保存当前坐标和角度
            stack.append((x, y, current_angle))# 将当前坐标和角度压入栈中
            if tree_mode:  # 仅在树模式下应用转向
                current_angle += angle
        elif cmd == ']':# 如果是右方括号，则恢复之前的坐标和角度
            if stack:#  如果栈不为空，则弹出栈顶元素
                prev_x, prev_y, prev_angle = stack.pop()# 弹出栈顶元素
                x, y = prev_x, prev_y# 恢复坐标
                current_angle = prev_angle# 恢复角度
                if tree_mode:  # 仅在树模式下应用转向
                    current_angle -= angle
        else:  # 处理移动指令（F/0/1等）
            rad = math.radians(current_angle)#  将角度转换为弧度
            nx = x + step * math.cos(rad)  # 计算新的x坐标
            ny = y + step * math.sin(rad)  # 计算新的y坐标
            ax.plot([x, nx], [y, ny], color='black', linewidth=1)# 绘制线段
            x, y = nx, ny# 更新当前坐标
    
    ax.axis('equal')# 设置坐标轴比例相等
    ax.axis('off')# 关闭坐标轴显示
    if savefile:
        plt.savefig(savefile, bbox_inches='tight')# 保存为图片文件
        plt.close()
    else:
        plt.show()

if __name__ == "__main__":
    """
    主程序示例：分别生成并绘制科赫曲线和分形二叉树
    学生可根据下方示例，调整参数体验不同分形效果
    """
    # 1. 科赫曲线
    draw_l_system(
        apply_rules("F", {"F": "F+F--F+F"}, 3),
        angle=60, step=5, savefile="koch.png"
    )

    # 2. 分形树
    draw_l_system(
        apply_rules("0", {"0": "1[0]0", "1": "11"}, 5),
        angle=45, step=5, start_angle=90,
        tree_mode=True, savefile="tree.png"
    )
