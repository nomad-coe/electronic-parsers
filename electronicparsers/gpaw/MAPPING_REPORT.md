<!-- generated-by: Claude Opus 4.8 | last_updated: 2026-09-09 -->
## GPAW

**Coverage:** Not available — this parser uses custom archive-writing logic and exposes no reportable file-parser quantities.

The GPAW parser reads `.gpw` restart files, which are binary containers rather than text. `GPWParser` subclasses `TarParser` and reads the tar members `info.xml` plus raw numpy arrays via `get_parameter`/`get_array`, driven at runtime by an XML-declared parameter/array map and an `_info_map` dictionary. `GPW2Parser` subclasses `FileParser` and reads the newer ULM format through `ase.io.ulm.Reader`, exposing values through hand-coded `get_parameter`/`get_array` branches. `GPAWParser` is a plain orchestrator (not a `FileParser` subclass) that dispatches to whichever of the two applies and writes the runschema archive in `parse_method`/`parse_system`/`parse_scc`.

None of these classes declare any `Quantity(...)`. All extraction is performed by imperative accessor methods over binary/XML data, so there are no declarative file-parser quantities to report. (The 18 `Quantity(type=...)` definitions in `metainfo/gpaw.py` are metainfo schema quantities and are out of scope for this report.)
