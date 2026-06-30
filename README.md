# Xcode Skills

Xcode Skills is a Codex plugin for Apple platform work. After installation,
Codex can use the bundled skills when you ask for help with Xcode projects,
SwiftUI, UIKit modernization, Swift Testing, simulator verification, security
settings, or C bounds-safety adoption.

These skills were exported from Xcode with:

```bash
xcrun agent skills export
```

## What You Can Ask

Use natural language. Codex will select the relevant skill when your request
matches one of these areas:

- Audit Xcode security settings, compiler warnings, analyzer checks, and
  hardening options.
- Review SwiftUI code for modern best practices, performance risks,
  localization, view structure, data flow, list identity, and deprecated APIs.
- Update SwiftUI code for SDK 27 source changes and new APIs.
- Modernize UIKit apps for scene lifecycle, multi-window behavior, orientation,
  safe areas, and screen APIs.
- Modernize XCTest suites or improve existing Swift Testing tests.
- Verify iOS behavior on simulator or device with screenshots, hierarchy
  inspection, and touch interactions.
- Adopt or review Clang `-fbounds-safety` annotations in C code.

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
Migrate these XCTest tests to Swift Testing where appropriate.
```

```text
Check whether this app flow works in the simulator.
```

```text
Help adopt -fbounds-safety in this C module.
```

## Included Skills

- `audit-xcode-security-settings`
- `c-bounds-safety`
- `device-interaction`
- `modernize-tests`
- `swiftui-specialist`
- `swiftui-whats-new-27`
- `uikit-app-modernization`

## Notes

Some skills include detailed reference material. When a task matches one of
those skills, Codex may read the relevant references before answering or editing
code. This is expected and helps keep guidance specific to the requested
Apple-platform workflow.

For simulator or device verification, Codex may need an available simulator,
an existing app build target, or an already running session. For Xcode builds,
prefer the configured Xcode build tooling in your Codex environment.

## Plugin Details

The plugin manifest is:

```text
.codex-plugin/plugin.json
```

It declares the plugin name as `xcode-skills` and exposes the bundled skills
from:

```text
skills/
```

To validate the local plugin source:

```bash
python3 /Users/Steven/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py /Users/Steven/Project/Team/sugarmo/xcode-skills
```
