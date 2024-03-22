from typing import Any, Dict, List
import requests
from pydantic import BaseModel, Field
from zerox.tools.base_tool import AbstractBaseTool
from loguru import logger


class AirtableCredentials(BaseModel):
    api_key: str
    base_id: str
    table_name: str


class AirtableRecord(BaseModel):
    fields: Dict[str, Any]
    id: str = Field(None, alias="id")


class AirtableTool(AbstractBaseTool):
    """
    A tool for interacting with Airtable API.

    This tool provides methods to perform CRUD operations on Airtable records.
    """

    base_url = "https://api.airtable.com/v0"

    def __init__(self, credentials: AirtableCredentials):
        self.credentials = credentials

    def _get_headers(self) -> Dict[str, str]:
        """
        Get the headers for making API requests.

        Returns:
            A dictionary containing the headers.
        """
        return {
            "Authorization": f"Bearer {self.credentials.api_key}",
            "Content-Type": "application/json",
        }

    def get_records(self) -> List[AirtableRecord]:
        """
        Get all records from the specified Airtable table.

        Returns:
            A list of AirtableRecord objects representing the records.
        """
        try:
            url = f"{self.base_url}/{self.credentials.base_id}/{self.credentials.table_name}"
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            records = response.json().get("records", [])
            return [
                AirtableRecord(
                    id=record["id"], fields=record["fields"]
                )
                for record in records
            ]
        except Exception as e:
            logger.error(f"Failed to get records: {e}")
            return []

    def create_record(self, record: AirtableRecord) -> AirtableRecord:
        """
        Create a new record in the specified Airtable table.

        Args:
            record: An AirtableRecord object representing the record to be created.

        Returns:
            An AirtableRecord object representing the created record.
        """
        try:
            logger.info(f"Creating record: {record}")
            url = f"{self.base_url}/{self.credentials.base_id}/{self.credentials.table_name}"
            response = requests.post(
                url,
                headers=self._get_headers(),
                json={"fields": record.fields},
            )
            response.raise_for_status()
            return AirtableRecord(
                **response.json()["fields"], id=response.json()["id"]
            )
        except Exception as e:
            logger.error(f"Failed to create record: {e}")
            return AirtableRecord(fields={})

    def update_record(
        self, record_id: str, fields: Dict[str, Any]
    ) -> AirtableRecord:
        """
        Update an existing record in the specified Airtable table.

        Args:
            record_id: The ID of the record to be updated.
            fields: A dictionary containing the updated field values.

        Returns:
            An AirtableRecord object representing the updated record.
        """
        try:
            url = f"{self.base_url}/{self.credentials.base_id}/{self.credentials.table_name}/{record_id}"
            response = requests.patch(
                url,
                headers=self._get_headers(),
                json={"fields": fields},
            )
            response.raise_for_status()
            return AirtableRecord(
                **response.json()["fields"], id=response.json()["id"]
            )
        except Exception as e:
            logger.error(f"Failed to update record: {e}")
            return AirtableRecord(fields={})

    def delete_record(self, record_id: str) -> bool:
        """
        Delete a record from the specified Airtable table.

        Args:
            record_id: The ID of the record to be deleted.

        Returns:
            True if the record was successfully deleted, False otherwise.
        """
        try:
            url = f"{self.base_url}/{self.credentials.base_id}/{self.credentials.table_name}/{record_id}"
            response = requests.delete(
                url, headers=self._get_headers()
            )
            response.raise_for_status()
            return response.status_code == 200
        except Exception as e:
            logger.error(f"Failed to delete record: {e}")
            return False
