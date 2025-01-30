class Errors:
    not_found = lambda object, name: f"{object} {name} not found",
    cannot_set = lambda property: f"Cannot set {property} directly",
    already_set = lambda object, name, type: f"{object} {name} already {type}",


class Common:
    Column = "Column"