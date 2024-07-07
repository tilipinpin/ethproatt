import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("螺钉信息查询软件")

# 创建标签
label = tk.Label(root, text="请输入螺钉信息:")
label.pack()

# 创建输入框
entry = tk.Entry(root)
entry.pack()

# 创建查询按钮
def query_info():
    screw_info = entry.get()
    # 在这里添加查询螺钉信息的代码
    # 你可以将查询结果显示在另一个标签或弹出窗口中
    result_label.config(text=f"查询结果: {screw_info}")

query_button = tk.Button(root, text="查询", command=query_info)
query_button.pack()

# 创建显示结果的标签
result_label = tk.Label(root, text="")
result_label.pack()

# 启动主循环
root.mainloop()
