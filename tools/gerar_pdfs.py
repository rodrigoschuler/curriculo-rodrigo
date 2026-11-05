#!/usr/bin/env python3
"""Gera os PDFs (PT e EN) do currículo a partir de curriculo.html, usando Chromium via Playwright.

Pré-requisitos (uma vez):
    pip install playwright
    playwright install chromium

Uso (na raiz do projeto):
    python tools/gerar_site.py     # atualiza o HTML, se você mudou os dados
    python tools/gerar_pdfs.py     # gera curriculo-rodrigo-schuler-pt.pdf e -en.pdf
"""
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PAGE = (ROOT / "curriculo.html").as_uri()

with sync_playwright() as p:
    browser = p.chromium.launch()
    for lang in ("pt", "en"):
        page = browser.new_page()
        page.goto(f"{PAGE}?lang={lang}&theme=light")
        page.emulate_media(media="print")
        out = ROOT / f"curriculo-rodrigo-schuler-{lang}.pdf"
        page.pdf(path=str(out), format="A4", print_background=True, prefer_css_page_size=True)
        print("PDF gerado:", out.name)
    browser.close()
