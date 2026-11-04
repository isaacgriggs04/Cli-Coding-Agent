from pathlib import Path

def read_file(file_path, workspace_path):
    workspace_path = Path(workspace_path).resolve()
    file_path = Path(file_path)
    if not file_path.is_absolute():
        file_path = (workspace_path / file_path).resolve()
    file_path = file_path.reoslve()
    if ".env" in file_path.parts:
         return "Agents cannot acces .env files"
    if (file_path.is_relative_to(workspace_path)):
        try:
            content = file_path.read_text()
            return content
        except FileNotFoundError:
                return "Error: File not found."
        except PermissionError:
                return "Error: Permission denied."
        except IsADirectoryError:
            return "Error: path is a directory, not a file."
    else:
         return "Error: Access denied. File is outside the workspace"
        