import ast
from typing import Optional, Tuple

def locate_logical_block(source_code: str, target_name: str) -> Optional[Tuple[int, int]]:
    """
    Parses Python source code and returns the 1-indexed (start_line, end_line_inclusive)
    range for a function or class named `target_name`.
    
    This includes any decorators associated with the block.
    """
    try:
        tree = ast.parse(source_code)
    except SyntaxError as e:
        print(f"Syntax error parsing code: {e}")
        return None

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.name == target_name:
                # Find start line (checking if decorators exist)
                start_line = node.lineno
                if node.decorator_list:
                    start_line = min(d.lineno for d in node.decorator_list)
                
                # Find end line (end_lineno is available in Python 3.8+)
                end_line = getattr(node, "end_lineno", start_line)
                return start_line, end_line
                
    return None

def replace_logical_block(file_path: str, target_name: str, replacement_content: str) -> bool:
    """
    Reads the file at `file_path`, locates the logical block matching `target_name`,
    and replaces it atomically with `replacement_content`.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        source_code = f.read()

    bounds = locate_logical_block(source_code, target_name)
    if not bounds:
        print(f"Error: Could not locate logical block '{target_name}' in {file_path}")
        return False

    start_line, end_line = bounds
    lines = source_code.splitlines(keepends=True)

    # 1-indexed to 0-indexed conversion:
    # start_line - 1 gets the index of the start of the block
    # end_line matches the end of the block (inclusive, so slice up to end_line)
    new_lines = lines[:start_line - 1] + [replacement_content.rstrip() + '\n'] + lines[end_line:]

    # Write the modified source back atomically
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"Successfully replaced logical block '{target_name}' (lines {start_line}-{end_line}) in {file_path}.")
    return True
