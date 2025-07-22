"""
Package initializer for *easyocr‑gpu‑test*.

Public helper:
    read(image_path, langs=['en']) → list[(text, confidence)]
        Wrapper around src.ocr_pipeline.run_ocr()

Usage example:
    from easyocr_gpu_test import read
    print(read("data/test_images/printed.jpg", langs=['en', 'km']))
"""

from importlib.metadata import version as _pkg_version
from pathlib import Path
from typing import List, Tuple

# Package semantic version (falls back if metadata missing)
try:
    __version__: str = _pkg_version(__name__)
except Exception:
    __version__ = "0.1.0"

# -- Public API -------------------------------------------------------------

def read(image_path: str | Path,
         langs: list[str] | None = None,
         as_dict: bool = False):
    """Convenience wrapper around run_ocr in ocr_pipeline.

    Args:
        image_path: Path to image file.
        langs: Language codes for EasyOCR; default ['en'].
        as_dict: If True, return list[dict{text,conf}], else list[(text,conf)].

    Returns:
        List of results in chosen format.
    """
    from .ocr_pipeline import run_ocr   # lazy import, keeps __init__ lightweight
    result = run_ocr(Path(image_path), langs or ['en'])
    if as_dict:
        return [{"text": t, "conf": c} for t, c in result]
    return result


__all__: list[str] = ["read", "__version__"]
