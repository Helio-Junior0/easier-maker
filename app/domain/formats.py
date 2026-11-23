from enum import Enum
from pathlib import Path


class UnsupportedFormatError(Exception):
    pass


class Format(Enum):
    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"
    HTML = "html"
    MD = "md"

    @classmethod
    def from_path(cls, path: str | Path) -> "Format":
        # TODO:
        # 1. pegar a extensão (dica: Path(path).suffix)
        # 2. tirar o ponto e deixar minúscula
        # 3. devolver o membro do Enum correspondente
        # 4. se não existir, lançar UnsupportedFormatError com mensagem clara
        ...