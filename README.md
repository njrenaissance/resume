JSON Resume conversion

This folder contains a resume formatted to the JSON Resume schema (<https://jsonresume.org>).

Files added/changed:

- `resume.json` — converted to follow the JSON Resume schema. Key notes:
  - Top-level `basics` is present but left blank for your contact info.
  - `work` entries created from your original experience items. `achievements` -> `highlights`.
  - Where possible, dates were converted to ISO-like `YYYY-MM` (`Oct 2020` -> `2020-10`). Current role uses `endDate: "Present"`.
  - Entries with no date information omit `startDate`/`endDate`.

- `jsonresume-schema.json` — a copy of the JSON Resume schema (trimmed) downloaded from the official repo for reference.

Reference:

- Full spec and tooling: <https://jsonresume.org>
- Schema source: <https://raw.githubusercontent.com/jsonresume/resume-schema/master/schema.json>

If you want, I can:

- Fill `basics` with your contact details from the other `resume.json` you showed me earlier.
- Convert `highlights` or `summary` text to shorter bullet-ready lines.
- Validate `resume.json` against the full schema and fix any issues automatically.

Which would you like next?
