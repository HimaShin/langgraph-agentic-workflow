def split_into_tasks(query):
    """
    Very basic splitting logic — you can make it smarter later.
    """
    if "," in query:
        tasks = query.split(",")
    elif " and " in query:
        tasks = query.split(" and ")
    else:
        tasks = [query]

    return [task.strip().capitalize() for task in tasks if task.strip()]
