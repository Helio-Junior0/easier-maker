from pathlib import Path

import pytest

from app.domain.document import Document
from app.domain.formats import Format, UnsupportedFormatError

FIXTURES = Path(__file__).parent / "fixtures"

FORMATO_ESPERADO_POR_EXTENSAO = {
    ".pdf": Format.PDF,
    ".docx": Format.DOCX,
    ".txt": Format.TXT,
    ".html": Format.HTML,
    ".md": Format.MD,
}

ARQUIVOS_DE_EXEMPLO = sorted(
    p for p in FIXTURES.iterdir()
    if p.is_file() and p.suffix.lower() in FORMATO_ESPERADO_POR_EXTENSAO
)


# --- Format ---------------------------------------------------------------

def test_from_path_reconhece_pdf_pela_extensao():
    assert Format.from_path("relatorio.pdf") is Format.PDF


def test_from_path_ignora_maiusculas_na_extensao():
    assert Format.from_path("RELATORIO.PDF") is Format.PDF


def test_from_path_lanca_erro_para_extensao_nao_suportada():
    with pytest.raises(UnsupportedFormatError):
        Format.from_path("foto.png")


# --- Document -------------------------------------------------------------

@pytest.mark.parametrize("arquivo", ARQUIVOS_DE_EXEMPLO, ids=lambda p: p.name)
def test_from_file_retorna_formato_correto_e_tamanho_positivo(arquivo: Path):
    documento = Document.from_file(arquivo)

    assert documento.format is FORMATO_ESPERADO_POR_EXTENSAO[arquivo.suffix.lower()]
    assert documento.size_bytes > 0


def test_from_file_lanca_erro_quando_arquivo_nao_existe():
    with pytest.raises(FileNotFoundError):
        Document.from_file("nao_existe.pdf")


@pytest.mark.parametrize(
    ("size_bytes", "esperado_mb"),
    [
        (1024 * 1024, 1.0),
        (2 * 1024 * 1024, 2.0),
        (1024 * 1024 + 512 * 1024, 1.5),
        (0, 0.0),
    ],
)
def test_size_mb_converte_bytes_para_megabytes(size_bytes: int, esperado_mb: float):
    documento = Document(path=Path("qualquer.pdf"), format=Format.PDF, size_bytes=size_bytes)

    assert documento.size_mb() == pytest.approx(esperado_mb)
