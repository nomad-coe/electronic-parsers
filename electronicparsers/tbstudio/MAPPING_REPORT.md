<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## TBStudio

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

The `TBStudioParser` class reads a JSON `.tbm` file directly via `json.load` and populates the archive through hand-written `parse_system`, `parse_method`, and `parse_scc` methods. It declares no `TextParser`/`XMLParser`/`FileParser` subclass with `Quantity(...)` definitions, so there are no file-parser quantities to report.
