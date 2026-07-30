# ML: Foundations to Frontier

A self-paced machine learning course, beginner to advanced, built one module at
a time. Start at [index.html](index.html)
(open it in a browser) — that's the dashboard for all 45 modules.

## How this course works

Every module has two files, in `modules/NN-slug/`:

- **`index.html`** — the actual lesson: intuition, diagrams, an interactive demo,
  worked examples, and a self-check quiz. Open it directly in a browser.
- **`notebook.ipynb`** — hands-on Jupyter notebook with runnable code that mirrors
  the lesson, plus exercises.

Some modules also include small supporting artifacts when they improve learning, such
as a runnable `.py` script or a dataset. The HTML lesson and notebook remain the two
primary learner entry points.

Modules are built **incrementally, in order** — see `curriculum.md` for the full
list and current status. Five modules are fully built right now;
the rest exist as short stub pages (title + objectives) until you reach them.
Start with **[Module 00 — Orientation](modules/00-orientation/index.html)**.

Math in each module defaults to intuition-first. Anything requiring full
derivations (calculus, linear algebra, proofs) lives in a collapsible
**"Math Deep Dive"** section — expand it if you want the rigor, skip it if not.

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

The `torch` dependency is only needed starting the Deep Learning phase
(module 28+); the LLM-track extras (commented out in `requirements.txt`) only
matter from module 39 onward — install them when you get there.

## Structure

```
index.html            Dashboard: all modules, phases, progress
curriculum.md          Full module list (source of truth for scope/order)
modules/NN-slug/       One folder per module (index.html + notebook.ipynb)
shared/css, shared/js   Design tokens & behavior shared by every module page
shared/notebook_utils/  Python helpers imported by every notebook
shared/data/            Shared datasets used across modules
templates/              Reference templates used to build each new module
```

## Progress tracking

Each module page has a "mark complete" button, and the dashboard shows overall
progress. This is stored in your browser's `localStorage` — it's per-browser,
with no account or server. If you open the same file from a different browser,
or from a published copy of the page, progress won't carry over.

## License

[MIT](LICENSE)
