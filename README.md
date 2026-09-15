# Xcode Skills

Xcode Skills is a Codex plugin for Apple platform work. It bundles Xcode's
native MCP server alongside focused skills. After installation, Codex can use
Xcode's tools and the bundled guidance when you ask for help with Xcode
projects, SwiftUI, UIKit modernization, App Intents, document-based apps,
Swift Testing, device verification, security settings, C bounds safety,
accessibility audits, or String Catalog translation.

## Refresh from Xcode

The skills come from Xcode's generated Codex plugin. The current snapshot is
from Xcode 27.0 (27A266a) and contains 15 skills. Run from this repository root:

```bash
python3 scripts/sync-xcode-skills.py
```

The script locates the generated plugin using:

```bash
xcrun agent plugin path --plugin-format codex
```

It copies the full skill set and adapts qualified `xcode-integration:` references
to this plugin's `xcode-skills:` namespace. It also makes the imported files
owner-writable, since Xcode can export read-only files. Review `git diff` after
refreshing; skills absent from a newer export are reported for manual review.

`xcrun agent skills export --output-dir "$PWD/skills" --replace-existing`
exports only 10 skills in this Xcode build, omitting the three accessibility
skills and two translation skills. Use the plugin export above for the full set.

The generated manifest identifies Apple's plugin as `xcode-integration` and
briefly describes its IDE integration. This repository keeps its own
`xcode-skills` identity, version, interface metadata, and native MCP configuration.
The only content adaptation is the qualified skill references described above.

## Built-in Xcode MCP

The plugin includes an MCP server configuration for Xcode's native tools:

```json
{
  "mcpServers": {
    "xcode": {
      "command": "xcrun",
      "args": ["mcpbridge"]
    }
  }
}
```

When the plugin is enabled, Codex launches Xcode's built-in STDIO bridge and
connects to the Xcode instance selected by `xcode-select`. This gives Codex
access to the tools exposed by Xcode while keeping the workflow integrated with
the open project and Xcode session.

The MCP integration requires an Xcode version that provides `mcpbridge`. It
does not install or use `xcodebuildmcp`, Node.js, npm, or another third-party MCP
server.

## What You Can Ask

Use natural language. Codex will select the relevant skill when your request
matches one of these areas:

- Audit Xcode security settings, compiler warnings, analyzer checks, and
  hardening options.
- Review SwiftUI code for modern best practices, performance risks,
  localization, view structure, data flow, list identity, and deprecated APIs.
- Update SwiftUI code for SDK 27 source changes and new APIs.
- Build or migrate document-based SwiftUI apps with the SDK 27 document APIs.
- Review App Intents for correctness and adopt new SDK 27 App Intents APIs.
- Modernize UIKit apps for scene lifecycle, multi-window behavior, orientation,
  safe areas, and screen APIs.
- Modernize XCTest suites or improve existing Swift Testing tests.
- Verify iOS behavior on simulator or device with screenshots, hierarchy
  inspection, and touch interactions.
- Adopt or review Clang `-fbounds-safety` annotations in C code.
- Audit Dynamic Type, color contrast, and VoiceOver accessibility support.
- Translate String Catalogs with language-specific style guides and coordinated batches.

## Example Prompts

```text
Audit this Xcode project for security build settings.
```

```text
Review this SwiftUI view for performance and modern API issues.
```

```text
Modernize this UIKit app so it works correctly with multiple scenes.
```

```text
Review these App Intents and update them for SDK 27.
```

```text
Build a document-based SwiftUI app with autosave and undo support.
```

```text
Migrate these XCTest tests to Swift Testing where appropriate.
```

```text
Check whether this app flow works in the simulator.
```

```text
Help adopt -fbounds-safety in this C module.
```

## Included Skills

- `accessibility-dynamic-type-specialist`
- `accessibility-sufficient-contrast-specialist`
- `accessibility-voiceover-specialist`
- `adopt-c-bounds-safety`
- `app-intents-specialist`
- `app-intents-whats-new-27`
- `audit-xcode-security-settings`
- `building-document-based-swiftui-applications`
- `device-interaction`
- `modernize-tests`
- `swiftui-specialist`
- `swiftui-whats-new-27`
- `translation`
- `translation-coordinator`
- `uikit-app-modernization`

## Notes

The translation skills depend on Xcode's `LocalizationPlanner`,
`StringCatalogRead`, `StringCatalogContext`, and `StringCatalogEdit` MCP tools.
The coordinator prepares catalogs and delegates batches; the translator handles
the supplied string keys. These workflows require the corresponding tools to be
available in the connected Xcode session.

Some skills include detailed reference material. When a task matches one of
those skills, Codex may read the relevant references before answering or editing
code. This is expected and helps keep guidance specific to the requested
Apple-platform workflow.

For simulator or device verification, Codex may need an available simulator,
an existing app build target, or an already running session. The bundled MCP
configuration launches Xcode's own STDIO bridge with `xcrun mcpbridge` and
connects to the Xcode instance selected by `xcode-select`.

## Plugin Details

The plugin manifest is:

```text
.codex-plugin/plugin.json
```

It declares the plugin name as `xcode-skills`, exposes the bundled skills from:

```text
skills/
```

and loads Xcode's native MCP server from:

```text
.mcp.json
```

To validate the local plugin source:

```bash
python3 /Users/Steven/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/Steven/Project/Team/sugarmo/xcode-skills
```
