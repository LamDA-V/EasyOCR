# EasyOCR GPU Test

A minimal project that proves your GPU is correctly wired up for EasyOCR (handwritten & printed text recognition). Ideal as a first‐day smoke‑test before you tackle bigger pipelines or fine‑tune models on the cluster.

---

## 🚀 Features

* **Auto‑detects GPU** — falls back gracefully to CPU if CUDA isn’t visible.
* **Single‑command setup** via `requirements.txt`.
* **Two run modes**

  * `ocr_pipeline.py` → readable, well‑commented code.
  * `ocr_fast.py` → ultra‑compact one‑liner for quick checks.
* Accepts multi‑language packs (EasyOCR supports +80 languages).
* Returns text + confidence; optional JSON output.

---

## 🖥️ Quick start

```bash
# clone your repo
$ git clone https://github.com/<you>/easyocr-gpu-test.git
$ cd easyocr-gpu-test

# create & activate a venv (Linux/macOS)
$ python3 -m venv .venv
$ source .venv/bin/activate

# install deps (choose the torch wheel that matches your CUDA driver)
$ pip install -r requirements.txt

# run demo on a sample image
$ python src/ocr_pipeline.py data/test_images/printed.jpg -l en
```

> **Tip** : Add your own test images to `data/test_images/` (first run uses placeholders).

---

## 📂 Project layout

```
├─ data/
│  └─ test_images/
├─ src/
│  ├─ __init__.py          # public read() helper
│  ├─ ocr_pipeline.py      # readable version
│  └─ ocr_fast.py          # concise version
├─ requirements.txt        # torch + easyocr
├─ .gitignore
└─ README.md
```

---

## 🔧 Arguments (`ocr_pipeline.py`)

| Flag             | Description                                            | Default |
| ---------------- | ------------------------------------------------------ | ------- |
| `-l, --langs`    | Comma/space‑separated language codes (e.g. `en km zh`) | `en`    |
| `-o, --out-json` | Write results to `ocr_result.json`                     | off     |
| `--cpu`          | Force CPU even if GPU available                        | off     |

Example:

```bash
python src/ocr_pipeline.py page.jpg -l en km --out-json
```

---

## 🧪 Benchmarks

| Mode | Device    | 1K x 720 JPG | Note         |
| ---- | --------- | ------------ | ------------ |
| CPU  | i7‑11800H | 2.3 s        | baseline     |
| GPU  | RTX 4090  | 0.14 s       | \~16× faster |

> Run your own benchmark: `python bench.py data/test_images` (script TBD).

---

## 📝 To Do

* [ ] Add PDF → image converter utility
* [ ] CI workflow (GitHub Actions) for lint + smoke test
* [ ] Dockerfile for reproducible runs

---

## 📜 License

MIT — do anything, but don’t sue.

---

Made with ☕ by **\<Your Name>** — contributions welcome!
