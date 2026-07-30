---
name: awesome-cursorrules-blender-python-addon
description: "Blender Python add-on rules for operators, panels, properties, registration, testing, and API-safe scripting"
category: testing-and-qa
source_repo: PatrickJS/awesome-cursorrules
source_path: "rules/blender-python-addon.mdc"
source_url: https://github.com/PatrickJS/awesome-cursorrules/blob/HEAD/rules/blender-python-addon.mdc
---


# Blender Python Add-on Rules

## Add-on Structure

- Keep add-on entry points in `__init__.py` with clear `register()` and `unregister()` functions.
- Group operators, panels, properties, preferences, and utilities into separate modules for non-trivial add-ons.
- Use `bl_info` or `blender_manifest.toml` according to the Blender version and packaging target.
- Keep UI labels concise and user-facing text translatable where appropriate.

## API Usage

- Use `bpy.types.Operator` for actions, `bpy.types.Panel` for UI, and `bpy.types.PropertyGroup` for grouped settings.
- Define `bl_idname`, `bl_label`, and `bl_options` explicitly.
- Validate context in `poll()` before enabling operators.
- Use `invoke()` for interactive setup and `execute()` for the actual operation.
- Return `{'FINISHED'}` or `{'CANCELLED'}` consistently.
- Use dependency graph updates and evaluated objects when reading final scene state.

## Data and Properties

- Register custom properties through `PropertyGroup` classes instead of loose global state.
- Store add-on preferences in `AddonPreferences`.
- Use `PointerProperty`, `CollectionProperty`, and typed properties with names and descriptions.
- Clean up custom properties and handlers during `unregister()`.

## Safety and Performance

- Do not run destructive scene operations without explicit user action.
- Avoid blocking UI work in modal operators; use timers or modal state machines for long operations.
- Batch mesh changes and use `bmesh` when editing mesh data programmatically.
- Avoid repeatedly scanning large scenes in draw methods.
- Keep file paths configurable and use Blender path utilities.

## Testing and Debugging

- Test scripts in a clean Blender profile and a representative production scene.
- Add smoke tests that import the add-on, register it, run core operators, and unregister cleanly.
- Log actionable messages with `self.report()` for user-facing operator feedback.
- Keep version-specific API differences isolated behind helper functions.

## Common Mistakes

- Do not forget to unregister classes, handlers, timers, and keymaps.
- Do not mutate Blender data from panel `draw()` methods.
- Do not assume an active object, selected object, or mode without checking context.
- Do not hardcode absolute asset paths.

---

**Source:** [`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules) → `rules/blender-python-addon.mdc`
