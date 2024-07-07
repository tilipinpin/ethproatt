import tkinter as tk
from tkinter import ttk
import pandas as pd

def load_excel_data(file_path):
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error loading Excel data: {e}")
        return None

def show_selected_thread(event):
    selected_thread = thread_listbox.get(thread_listbox.curselection())
    if not selected_thread:
        return
    row = excel_data[excel_data['Thread'] == selected_thread]
    if not row.empty:
        thread_details_label.config(text=f"Thread: {selected_thread}\nDetails: {row.iloc[0]['Details']}")

def main():
    global excel_data, thread_listbox, thread_details_label
    # 创建主窗口
    root = tk.Tk()
    root.title("螺纹查询软件")

    # 创建Excel数据加载按钮
    def load_excel():
        file_path = file_path_entry.get()
        global excel_data
        excel_data = load_excel_data(file_path)
        if excel_data is not None:
            thread_listbox.delete(0, tk.END)  # 清空列表框
            for thread in excel_data['Thread']:
                thread_listbox.insert(tk.END, thread)
            thread_listbox.pack()

    # 创建文件路径输入框
    file_path_label = tk.Label(root, text="Excel文件路径:")
    file_path_label.pack()
    file_path_entry = tk.Entry(root)
    file_path_entry.pack()

    load_button = tk.Button(root, text="加载Excel数据", command=load_excel)
    load_button.pack()

    # 创建螺纹列表框
    thread_listbox = tk.Listbox(root)
    thread_listbox.pack()
    thread_listbox.bind('<<ListboxSelect>>', show_selected_thread)

    # 创建显示选定螺纹的标签
    thread_details_label = tk.Label(root, text="")
    thread_details_label.pack()

    root.mainloop()

if __name__ == "__main__":
    excel_data = None
    main()


   