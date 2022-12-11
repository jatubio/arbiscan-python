from arbiscan.core.async_client import AsyncClient
from arbiscan.core.base import BaseClient
from arbiscan.core.sync_client import SyncClient


class ArbiScan:
    """Client factory."""

    def __new__(cls, api_key: str, asynchronous=True, debug=False, timeout=None) -> BaseClient:
        """Create a new client.

        Args:
            api_key (str): Your arbiscan.com API key.
            asynchronous (bool, optional): Whether client is async or not. Defaults to True.
            debug (bool, optional): Display generated URLs for debugging. Defaults to False.

        Returns:
            BaseClient: arbiscan client.
        """
        if asynchronous:
            return AsyncClient(api_key=api_key, debug=debug, timeout=timeout)
        return SyncClient(api_key=api_key, debug=debug, timeout=timeout)
