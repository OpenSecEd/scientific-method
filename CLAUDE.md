# DA2215 Theory of Science and Scientific Methods in Cybersecurity

LaTeX teaching material lives in `modules/NN-*/` (topics, not Canvas
modules). The Canvas course content lives in `canvas/`.

## Canvas (`canvas/`)

Rounds are named `vetcyb<YY><h|v>` (Canvas course `^vetcyb26h$`, id 65757,
starts 2026-10-26). Each round is a Canvas course copy of the previous one;
the files here are then re-dated and pushed. Skill: `canvas-course-repo`.

- Layout: `canvas/NN-<module>/<page>.md`, `…/assignments/<assignment>.md`,
  `…/quizzes/<quiz>.json` (`quizzes export -I`). `NN` is the module's
  position in Canvas. An item in several modules lives under the first; its
  `modules:` front matter lists all. `unlisted/` holds items in no module.
- `*.html.md` files have an HTML body (pushed with `--html`): the two
  checklist pages, whose nested styled lists do not survive Markdown.
- Front matter: assignments are identified by `regex: ^<canvas id>$`, pages
  by exact title (rename: push once with the old regex, then change it).
  `rubric:` and null fields are deliberately absent, so a push never sends
  them (the FeedbackFruits rubrics stay as they are).
- Links use canvaslms's course-independent form
  (`$CANVAS_COURSE_REFERENCE$/assignments/<name>`), so the files push to the
  next round unchanged. A link resolves by name: rename the target first.
- `make push` (in `canvas/`) pushes files changed since the last push
  (stamps in `canvas/.pushed.d/<course>/`). `make push COURSE=vetcyb27v`
  targets another round; `make mark-pushed` stamps everything.
- `make pull` exports only items that have no file yet; `make diff-canvas`
  shows how Canvas differs from the files (edits in the web UI) so they can
  be carried over by hand. Never overwrite a file from Canvas.
- File names carry no dates; titles do (`Live seminar 12/11 at 09:15:
  Literature reviews`).

### Per-round checklist

- Seminar times: TimeEdit (`nytid courses config vetcyb26h -r mine` → `ics`)
  against the sign-up sheet (`signupsheet.url`). The sheet wins when the
  author changed it; TimeEdit is fixed by the author.
- Module names carry ISO work weeks, single hyphen: `Ethics (week 49)`,
  `Case study: Passwords (week 46-47)` — the weeks from the previous
  deadline to this module's own deadline.
- Deadlines are 20:00 local the day before the module's seminar.
  Scientificity part 1 prepares the inferences/experiments seminar, not the
  literature one. Items in several modules keep their seminar pairing.
- Also re-date: the instruction's `unlock_at` (two weeks in), the course
  evaluation's `unlock_at` (after the last participation seminar), the
  intro page title, the final seminar title. FeedbackFruits peer-review dates
  are set by the author in FeedbackFruits.

### Gotchas

- Two modules are both named `Pass by participation`; the checklist page's
  `modules:` lists the regex twice. Avoid pushing it unless needed.
- canvaslms cannot clear a date: `due_at: null` and `''` are not sent.
  Clear it in the web UI (or the API with an empty string).
- Course copies leave unresolved `$CANVAS_OBJECT_REFERENCE$/…g<hex>` links
  in Canvas; replace them with symbolic links by name.
