from dataclasses import dataclass
from pathlib import Path

from app.domain.formats import Format


@dataclass(frozen=True)
class Document:
    path: Path
    format: Format
    size_bytes: int

    @classmethod
    def from_file(cls, path: str | Path) -> "Document":
        # TODO:
        # 1. converter para Path
        # 2. se o arquivo não existir, lançar FileNotFoundError
        # 3. descobrir o formato com Format.from_path
        # 4. pegar o tamanho (dica: path.stat().st_size)
        # 5. retornar Document(...)
        ...

    def size_mb(self) -> float:
        # TODO: bytes → MB (1 MB = 1024 * 1024 bytes)
        ...