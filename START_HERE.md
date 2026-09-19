# Run and edit your CV website

## View it

Open `dist/index.html` in your browser for French, or `dist/en/index.html` for English.

To serve it locally, run this from the extracted project folder:

```sh
python3 -m http.server 8000 --directory dist
```

Then open http://localhost:8000 in your browser.

## Edit it

- Change `content.json` to update the French and English text.
- Change `generate.py` to update the shared page structure.
- Run `python3 generate.py` to regenerate both pages.
- Change `dist/assets/style.css` for the design.
- Change `dist/assets/script.js` for the interactions.
- Replace the two PDF files in `dist/assets/` to update the downloadable CVs.

No package installation or JavaScript framework is required. Upload the contents of `dist/` to a static website host. This archive contains the complete website source and assets, without deployment identity or Git history.
