from mcp.server.fastmcp import FastMCP
import requests
from typing import List, Dict, Optional, Any

mcp = FastMCP("Todos MCP", port=8001)

# Base URL for the FastAPI server
BASE_URL = "http://localhost:8000"

@mcp.tool()
def get_todos() -> List[Dict[str, Any]]:
    """Get all todos from the API"""
    try:
        response = requests.get(f"{BASE_URL}/todos/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Failed to fetch todos: {str(e)}"}]

@mcp.tool()
def get_todo(todo_id: int) -> Dict[str, Any]:
    """Get a specific todo by ID"""
    try:
        response = requests.get(f"{BASE_URL}/todos/{todo_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch todo {todo_id}: {str(e)}"}

@mcp.tool()
def create_todo(title: str, description: Optional[str] = None, completed: bool = False) -> Dict[str, Any]:
    """Create a new todo"""
    todo_data = {
        "title": title,
        "description": description,
        "completed": completed
    }
    try:
        response = requests.post(f"{BASE_URL}/todos/", json=todo_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to create todo: {str(e)}"}

@mcp.tool()
def update_todo(todo_id: int, title: Optional[str] = None, description: Optional[str] = None, completed: Optional[bool] = None) -> Dict[str, Any]:
    """Update an existing todo"""
    update_data = {}
    if title is not None:
        update_data["title"] = title
    if description is not None:
        update_data["description"] = description
    if completed is not None:
        update_data["completed"] = completed
    
    try:
        response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=update_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to update todo {todo_id}: {str(e)}"}

@mcp.tool()
def delete_todo(todo_id: int) -> Dict[str, Any]:
    """Delete a todo by ID"""
    try:
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to delete todo {todo_id}: {str(e)}"}

if __name__ == "__main__":
    mcp.run(transport="streamable-http")