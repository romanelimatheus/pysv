from asyncio import gather
from socket import AF_PACKET, SOCK_RAW, socket
from typing import TYPE_CHECKING

from pysv.sv import generate_sv_from
from pysv.utils import async_usleep

if TYPE_CHECKING:
    from asyncio import AbstractEventLoop
    from pathlib import Path


async def run(loop: "AbstractEventLoop", interface: str, csv_path: "Path") -> None:
    with socket(AF_PACKET, SOCK_RAW, 0xBA88) as nic:
        nic.bind((interface, 0))
        nic.setblocking(False)  # noqa: FBT003

        for header, pdu in generate_sv_from(csv_path):
            await gather(async_usleep(250), loop.sock_sendall(nic, header + pdu))
