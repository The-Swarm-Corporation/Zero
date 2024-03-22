from unittest.mock import patch

from zerox.tools.notion import (
    APIHeaderModel,
    NotionCredentials,
    NotionEntry,
    NotionQuery,
    NotionTool,
    NotionUpdate,
)


# Mocking the requests module
@patch("requests.get")
@patch("requests.post")
@patch("requests.patch")
def test_notion_tool(mock_patch, mock_post, mock_get):
    # Mocking the API responses
    mock_get.return_value.status_code = 200
    mock_post.return_value.status_code = 200
    mock_patch.return_value.status_code = 200

    # Initializing the NotionTool
    credentials = NotionCredentials(
        api_key="test_key",
        database_id="test_id",
        notion_url="test_url",
    )
    headers = APIHeaderModel()
    notion_tool = NotionTool(credentials=credentials, headers=headers)

    # Testing the connect method
    assert notion_tool.connect() is True

    # Testing the add method
    item = NotionEntry(parent={}, properties={})
    assert notion_tool.add(item) is True

    # Testing the query method
    query = NotionQuery(filter={}, sorts=[])
    assert isinstance(notion_tool.query(query), dict)

    # Testing the update method
    update = NotionUpdate(properties={}, page_id="test_page_id")
    assert notion_tool.update(update) is True

    # Testing the connect method with a failed connection
    mock_get.return_value.status_code = 404
    assert notion_tool.connect() is False

    # Testing the add method with a failed addition
    mock_post.return_value.status_code = 404
    assert notion_tool.add(item) is False

    # Testing the query method with a failed query
    assert notion_tool.query(query) is None

    # Testing the update method with a failed update
    mock_patch.return_value.status_code = 404
    assert notion_tool.update(update) is False
