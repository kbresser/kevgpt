import os

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if file_path:
        target_dir = os.path.abspath(os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_dir, "r") as f:
            content = f.read()
            MAX_CHARS = 10000
            if len(content) > MAX_CHARS:
                trunc_doc = content[:MAX_CHARS]
                trunc_message = f'[...File "{file_path}" truncated at 10000 characters]'
                return trunc_doc + trunc_message
            else:
                return content
    except Exception as e:
        return f"ERROR: {e}"
