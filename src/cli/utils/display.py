from rich.console import Console
from rich.table import Table

def display_tasks(tasks) -> None:
    """
    Prints to CMD the tasks as a table, neat and colorful.
    :param tasks: tasks to print, possibly filtered.
    :return:
    """
    console = Console()
    table = Table(title="Task List")

    table.add_column("ID", style="cyan", justify="right")
    table.add_column("Description", style="magenta")
    table.add_column("Status", style="green")
    table.add_column("Created At", style="dim")
    table.add_column("Updated At", style="dim")

    for task in tasks:
        status_color = "green" if task["status"].lower() == "done" else "yellow"
        table.add_row(
            str(task["task_id"]),
            task["description"],
            f"[{status_color}]{task['status']}[/{status_color}]",
            task["created_at"],
            task["updated_at"],
        )

    console.print(table)
