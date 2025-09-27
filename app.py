!pip install gradio

import gradio as gr
tasks = []

def add_task(task):
    if task.strip():
        tasks.append(task.strip())
    return "\n".join([f"{i+1}. {t}" for i,t in enumerate(tasks)]) or "No tasks yet!"

def remove_task(index):
    try:
        index = int(index) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
    except:
        pass
    return "\n".join([f"{i+1}. {t}" for i,t in enumerate(tasks)]) or "No tasks yet!"

def reset_tasks():
    tasks.clear()
    return "No tasks yet!"

with gr.Blocks() as demo:
    gr.Markdown("## 📝 To-Do List Web App")

    with gr.Row():
        new_task = gr.Textbox(label="Enter Task")
        add_btn = gr.Button("➕ Add Task")

    with gr.Row():
        remove_index = gr.Textbox(label="Remove Task (Enter Task Number)")
        remove_btn = gr.Button("❌ Remove Task")

    reset_btn = gr.Button("🔄 Reset All")
    task_list = gr.Textbox(label="Your Tasks", value="No tasks yet!", interactive=False)

    add_btn.click(add_task, inputs=new_task, outputs=task_list)
    remove_btn.click(remove_task, inputs=remove_index, outputs=task_list)
    reset_btn.click(reset_tasks, inputs=None, outputs=task_list)

demo.launch(debug=True)
