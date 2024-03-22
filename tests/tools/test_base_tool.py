from zerox.tools.base_tool import AbstractBaseTool


class ConcreteBaseTool(AbstractBaseTool):
    def connect(self):
        pass

    def add(self, item):
        pass

    def close_connection(self):
        pass

    def cache(self, data):
        pass


def test_base_tool_init():
    tool = ConcreteBaseTool(
        verbose=True, base_url="http://localhost", name="TestTool"
    )
    assert tool.verbose is True
    assert tool.base_url == "http://localhost"
    assert tool.name == "TestTool"


def test_base_tool_log_info(caplog):
    tool = ConcreteBaseTool()
    tool.log_info("Test log message")
    assert "Test log message" in caplog.text
