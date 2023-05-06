from configparser import ConfigParser
from tkinter.ttk import Progressbar

# from aiohttp_socks import ProxyType

import asyncio

from aiohttp import ClientSession, ClientTimeout

from aiohttp_socks import ProxyType

# from aiohttp import ClientSession, ClientTimeout, DummyCookieJar
class INI:
    def main(self):
        self.Read("config.ini")

    @classmethod
    def Read(self, fileName: str) -> ConfigParser:
        cfg = ConfigParser(interpolation=None)
        cfg.read(fileName, "UTF-8")
        return cfg
    async def FetchAllSources(self,progress:Progressbar):
        '''检测所有源'''
        tasks={}
        async with ClientSession(
            headers={"User-Agent": USER_AGENT},
            cookie_jar=self.cookie_jar,
            timeout=ClientTimeout(total=self.source_timeout),
        ) as session:
            coroutines = (
                self.fetch_source(
                    session=session,
                    source=source,
                    proto=proto,
                    progress=progress,
                    task=tasks[proto],
                )
                for proto, sources in self.sources.items()
                for source in sources
            )
            await asyncio.gather(*coroutines)   

def print1(s: str):
    # print(s)
    return s


def test1()->ConfigParser:
    ini = INI()
    return ini.Read("config.ini")
test1()

# sources = {}
# sources[ProxyType.HTTP] = list(
#     filter(None, cfg["HTTP"]["sources"].split('\n')))
# sources[ProxyType.SOCKS4] = list(
#     filter(None, cfg["SOCKS4"]["sources"].split('\n')))
# sources[ProxyType.SOCKS5] = list(
#     filter(None, cfg["SOCKS4"]["sources"].split('\n')))

# for type, urls in sources.items():
#     for url in urls:
#         print("{}: {}".format(type, url))
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/109.0"





