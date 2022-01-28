import requests


class Scrapper:
    def __init__(self, url: str) -> None:
        self.request = requests.get(url)

    def _getstatuscode(self) -> int:
        return self.request.status_code

    def _getrequest(self) -> str:
        return self.request.text
