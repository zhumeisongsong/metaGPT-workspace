from typing import List

def calculate_quadrant(reach: float, engagement: float) -> str:
    """
    Calculate the quadrant of a photo-sharing app based on reach and engagement values.

    Args:
        reach (float): The reach value of the app.
        engagement (float): The engagement value of the app.

    Returns:
        str: The quadrant of the app.
    """
    if reach >= 0.9 and engagement >= 0.9:
        return "quadrant-1"
    elif reach >= 0.9 and engagement < 0.9:
        return "quadrant-2"
    elif reach < 0.9 and engagement >= 0.9:
        return "quadrant-3"
    else:
        return "quadrant-4"

def generate_product_goals(goals: List[str]) -> str:
    """
    Generate a formatted string of product goals.

    Args:
        goals (List[str]): The list of product goals.

    Returns:
        str: The formatted string of product goals.
    """
    formatted_goals = "\n".join([f"- {goal}" for goal in goals])
    return formatted_goals

def generate_user_stories(stories: List[str]) -> str:
    """
    Generate a formatted string of user stories.

    Args:
        stories (List[str]): The list of user stories.

    Returns:
        str: The formatted string of user stories.
    """
    formatted_stories = "\n".join([f"- {story}" for story in stories])
    return formatted_stories

def generate_competitive_analysis(analysis: List[str]) -> str:
    """
    Generate a formatted string of competitive analysis.

    Args:
        analysis (List[str]): The list of competitive analysis.

    Returns:
        str: The formatted string of competitive analysis.
    """
    formatted_analysis = "\n".join([f"- {item}" for item in analysis])
    return formatted_analysis

def generate_task_list(tasks: List[str]) -> str:
    """
    Generate a formatted string of task list.

    Args:
        tasks (List[str]): The list of tasks.

    Returns:
        str: The formatted string of task list.
    """
    formatted_tasks = "\n".join([f"- {task}" for task in tasks])
    return formatted_tasks
