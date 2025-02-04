import functools
import inspect


def enforce_types(func: callable) -> callable:
    """
    Decorator to enforce type hints in function arguments.

    Args:
        func: callable
            Function to be decorated.

    Returns:
        Wrapper function that enforces
        type hints in function arguments
        before calling the original function.

    Raises:
        TypeError: If any argument does not match
        the expected type hint.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get function signature
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        # Get function annotations
        annotations = func.__annotations__

        for param, value in bound_args.arguments.items():
            expected_type = annotations.get(param)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(
                    f"Argument '{param}' must be {expected_type}, got {type(value)} instead."
                )

        return func(*args, **kwargs)

    return wrapper
