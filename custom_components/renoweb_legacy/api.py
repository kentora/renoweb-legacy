"""Sample API Client."""
import asyncio
import logging
import socket
import json

import aiohttp
import async_timeout

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}

"""Simple API Client"""


class RenowebLegacyApiClient:
    def __init__(self, host: str, addrid: str, session: aiohttp.ClientSession) -> None:
        self._host = host
        self._addrid = addrid
        self._session = session

    async def async_get_data(self) -> dict:
        """Get data from the API."""
        url = self._host + "/Legacy/JService.asmx/GetAffaldsplanMateriel_mitAffald"
        obj = {"adrid": self._addrid, "common": "false"}
        postres = await self.api_wrapper("post", url, obj, HEADERS)

        jsonres = json.loads(postres["d"])["list"]
        res = {}
        for r in jsonres:
            res[r.get("id")] = r

        return res

    async def api_wrapper(
        self, method: str, url: str, data: dict = {}, headers: dict = {}
    ) -> dict:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(TIMEOUT):
                if method == "get":
                    response = await self._session.get(url, headers=headers)
                    return await response.json()

                elif method == "put":
                    await self._session.put(url, headers=headers, json=data)

                elif method == "patch":
                    await self._session.patch(url, headers=headers, json=data)

                elif method == "post":
                    response = await self._session.post(url, headers=headers, json=data)
                    return await response.json()

        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)
