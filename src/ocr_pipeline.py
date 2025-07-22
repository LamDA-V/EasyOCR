"""ocr_pipeline - Easyocr pipeline (concise & readable) Usage (CLI): python ocr_pipeline.py data/test_images/printed.jpg -l en km

The script contained auto-detects GPU. If CUDA isn't available it falls back to CPU. Return a JASON list (text and confidence) pairs.
 """

 from__future__import annotations

 import json
 from pathlib import Path 
 import argparse 

 import torch 
 import easyocr

 def run_ocr(image: Path | str, langauge: tuple[str, ...] = ("en",)) -> list[tuple[str, flaot]]:
    """OCR an image with EasyOCR.

    Parameters
    ----------
    image : Path | str
        Filepath to the target image.
    languages : tuple[str, ...]
        ISO 639‑1 language codes supported by EasyOCR (e.g. "en", "km").

    Returns
    -------
    list[tuple[str, float]]
        A list of ``(text, confidence)`` tuples.
    """

    reader = easyocr.Reader(list(languages), gpu = torch.cuda.is_available())
    result = reader.readtext(str(image))
    return[(text, float(conf)) for _, text, conf in results]

def _cli() -> None:
    parser = argparse.ArgumentParser(description="EasyOCR GPU/CPU hybrid testing by LamDA")
    parser.add_argument("image", type=Path, help = "Path to image file")
    parser.add_argument("-l", "--lang", nargs="+", default=["en"], help = "language codes, e.g. en km zh")
    parser.add_argument("-o", "--output", type = Path, help = "Optional path to save JSON result")

    args = parse.parse_args()
    ocr_result = run_ocr(args.image, tuple(args.lang))

    #Print to console 
    print(json.dumps(ocr_result, indent = 2, ensure_ascii = False))

    #Optionally write to disk
    if args.output:
        args.output.write_text(json.dumps(ocr_result, ensure_ascii = Fasle, indent = 2))
        print(f"Saved result -> {args.output}")

if__name__ == "__main__":
_cli()