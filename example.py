from zerox.tools.notion.notion_tool import (
    NotionCredentials,
    NotionEntry,
    NotionTool,
)


# Assuming the NotionTool class is already defined and includes methods like connect, add_entry, etc.

# First, set up your credentials (replace placeholders with your actual API key and database ID)
credentials = NotionCredentials(
    api_key="your_notion_api_key",
    database_id="your_notion_database_id",
)

# Initialize the NotionTool with your credentials
notion_tool = NotionTool(credentials=credentials)

# Connect to your Notion database to verify credentials
if notion_tool.connect():
    print("Successfully connected to Notion database.")

    # Example: Add a new entry to your Notion database
    new_entry = NotionEntry(
        parent={"database_id": credentials.database_id},
        properties={
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": (
                                "A new entry from our Notion tool"
                            )
                        }
                    }
                ]
            },
            # Add other properties as needed
        },
    )

    if notion_tool.add_entry(new_entry):
        print("New entry successfully added to Notion database.")
    else:
        print("Failed to add new entry.")

    # Example: Query your Notion database (assuming there's a method called query_database)
    # This is a placeholder example; you'd need to implement the query_database method in your class.
    query_result = notion_tool.query_database()
    if query_result:
        print("Database query successful. Data:", query_result)
    else:
        print("Failed to query database.")

    # Example: Update an existing entry in your Notion database
    # This assumes there's an update_entry method in your class.

else:
    print("Failed to connect to Notion database.")
