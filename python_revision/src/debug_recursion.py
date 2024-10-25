from functools import wraps
import sys
import tqdm


def show_recursive_structure(f):
    """Show call entry/exits on stderr

    Wrapper to instrument a function to show the
    call entry and exit from that function. Can
    customize view with instrument flags.
    """

    @wraps(f)
    def wrapper(*args, **kwargs):
        arg_str = ", ".join(str(a) for a in args)
        if (
            show_recursive_structure.TRIM_ARGS is not None
            and len(arg_str) > show_recursive_structure.TRIM_ARGS
        ):
            # Trim the output if more than given lines
            arg_str = arg_str[:show_recursive_structure] + " ..."
        if show_recursive_structure.SHOW_CALL:
            tqdm.tqdm(f'{"   " * wrapper.depth}call to {f.__name__}: {arg_str}\n')
        wrapper.count += 1
        wrapper.depth += 1
        wrapper.max_depth = max(wrapper.depth, wrapper.max_depth)
        result = f(*args, **kwargs)
        wrapper.depth -= 1
        res_str = str(result)
        # if (
        #     show_recursive_structure.TRIM_RET is not None
        #     and len(res_str) > show_recursive_structure
        # ):
        #     res_str = res_str[: show_recursive_structure] + " ..."
        if show_recursive_structure.SHOW_RET:
            sys.stdout.write(
                f'{"   " * wrapper.depth}call to {f.__name__} returns: {res_str}\n'
            )
        return result

    wrapper.count = 0
    wrapper.depth = 0
    wrapper.max_depth = 0
    return wrapper


show_recursive_structure.SHOW_CALL = True
show_recursive_structure.SHOW_RET = True
show_recursive_structure.TRIM_ARGS = 55  # None if no trimming
show_recursive_structure.TRIM_RET = 120  # None if no trimming
