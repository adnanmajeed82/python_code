import tkinter as tk

def generate_code_response(prompt):
    # Replace this with your logic for generating code using Gemini's built-in capabilities
    # For example, you could use Gemini's text generation or code completion features
    # Here's a basic example using text generation:
    generated_code = f"print('Hello, world! This is generated code based on your prompt: {prompt}')"
    return generated_code

def generate_code():
    prompt = prompt_entry.get()
    response = generate_code_response(prompt)
    code_text.delete(1.0, tk.END)  # Clear the text box
    code_text.insert(tk.END, response)  # Insert the generated code

root = tk.Tk()
root.title("Gemini Bard Code Generator")
root.geometry("400x300")

# Text input for user prompt
prompt_label = tk.Label(root, text="Enter your prompt:")
prompt_label.pack()
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack()

# Text output for generated code
code_label = tk.Label(root, text="Generated Code:")
code_label.pack()
code_text = tk.Text(root, width=50, height=10)
code_text.pack()

# Button to trigger code generation
generate_button = tk.Button(root, text="Generate Code", command=generate_code)
generate_button.pack()

root.mainloop()
