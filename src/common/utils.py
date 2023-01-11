from typing import Callable, Any


def get_function_docs(func: Callable, delimiter: str = ":param") -> str:
	if func_doc := func.__doc__:
		return func_doc.split(delimiter)[0]
	return "Empty Docs"


def get_function_response_type(func: Callable) -> Any | None:
	return func.__annotations__.get("return")
