from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Callable, Any
from loguru import logger


class ToolAction:
    def __init__(self, action: Callable, action_params: dict):
        self.action = action
        self.action_params = action_params

    def execute(self) -> Any:
        try:
            return self.action(**self.action_params)
        except Exception as e:
            logger.error(f"Failed to execute action: {e}")
            return None


class Automation:
    def __init__(self, tools: List[ToolAction], max_workers: int = 5):
        self.tools = tools
        self.max_workers = max_workers

    def execute_all_concurrently(self):
        with ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:
            future_to_tool = {
                executor.submit(tool.execute): tool
                for tool in self.tools
            }
            for future in as_completed(future_to_tool):
                future_to_tool[future]
                try:
                    data = future.result()
                    logger.success(
                        "Tool executed successfully with result:"
                        f" {data}"
                    )
                except Exception as exc:
                    logger.error(
                        f"Tool generated an exception: {exc}"
                    )
