# Context Detection Rules

This document provides detailed rules for detecting project context from the working environment.

## Project Name Detection

### Priority 1: Explicit User Statement

Look for phrases like:

- "I'm working on [name]"
- "This is my [name] project"
- "Building a [name]"
- "Let's document my [name] project"

Extract the project name directly from these statements.

### Priority 2: Git Repository Name

If the current directory is a git repository:

```bash
# Check if git repo
git rev-parse --is-inside-work-tree 2>/dev/null

# Get repository name
basename $(git rev-parse --show-toplevel)
```

**Transform to Title Case:**

- `my-arduino-project` → "My Arduino Project"
- `temperature_sensor` → "Temperature Sensor"
- `synthesizer-build` → "Synthesizer Build"

**Also check README.md first heading:**

```bash
head -10 README.md | grep "^# " | sed 's/^# //'
```

**Or package.json name/description:**

```bash
cat package.json | grep -E '"name"|"description"'
```

### Priority 3: Directory Name

Use the current directory name or parent directory if current is generic:

```bash
# Get current directory name
basename $(pwd)

# If current is generic (src, build, lib, etc.), use parent
CURRENT=$(basename $(pwd))
if [[ "$CURRENT" =~ ^(src|build|lib|dist|bin|test|tests)$ ]]; then
  basename $(dirname $(pwd))
else
  echo "$CURRENT"
fi
```

### Priority 4: Ask User

If none of the above provide a clear name, or if multiple candidates exist, ask:

"What would you like to name this project in your Obsidian vault?"

## Area Classification

### Hardware

**File Extensions:**

- `.ino` - Arduino sketches
- `.cpp`, `.h` - C++ (embedded context)
- `.pcb` - PCB design files
- `.sch` - Schematic files

**Configuration Files:**

- `platformio.ini` - PlatformIO projects
- `arduino_secrets.h` - Arduino projects
- `Makefile` (with avr-gcc, arm-none-eabi)

**Keywords in files/directories:**

- arduino, esp32, esp8266, teensy
- circuit, pcb, schematic, breadboard
- sensor, actuator, microcontroller
- i2c, spi, uart, serial

**Detection command:**

```bash
find . -maxdepth 2 \( -name "*.ino" -o -name "platformio.ini" -o -name "*.pcb" \) 2>/dev/null
```

### Software

**File Extensions:**

- `.js`, `.ts` - JavaScript/TypeScript
- `.py` - Python
- `.go` - Go
- `.rs` - Rust
- `.java` - Java
- `.rb` - Ruby
- `.php` - PHP

**Configuration Files:**

- `package.json` - Node.js projects
- `requirements.txt`, `setup.py` - Python projects
- `Cargo.toml` - Rust projects
- `go.mod` - Go projects
- `pom.xml`, `build.gradle` - Java projects

**Keywords:**

- api, backend, frontend, database
- server, client, web, mobile
- framework, library, npm, pip

**Detection command:**

```bash
find . -maxdepth 2 \( -name "package.json" -o -name "requirements.txt" -o -name "Cargo.toml" -o -name "*.py" -o -name "*.js" \) 2>/dev/null
```

### Woodworking

**File Extensions:**

- `.stl` - 3D model files
- `.obj` - 3D object files
- `.blend` - Blender files
- `.f3d` - Fusion 360 files
- `.skp` - SketchUp files

**Documentation Files:**

- `cut-list.md`, `cut-list.txt`
- `materials.md`, `materials.txt`
- `dimensions.md`

**Keywords:**

- joinery, dovetail, mortise, tenon
- finish, stain, polyurethane
- wood, lumber, hardwood, plywood
- table, saw, router, planer
- shop, workshop, woodshop

**Detection command:**

```bash
find . -maxdepth 2 \( -name "*.stl" -o -name "*.blend" -o -name "*.f3d" -o -name "cut-list.md" \) 2>/dev/null
```

### Music Synthesis

**File Extensions:**

- `.pd` - Pure Data patches
- `.maxpat` - Max/MSP patches
- `.syx` - SysEx MIDI files
- `.fxp` - VST preset files
- `.amxd` - Ableton Max for Live devices

**Documentation Files:**

- `patch-notes.md`
- `tuning-table.txt`
- `modulation-matrix.md`

**Keywords:**

- oscillator, vco, vca, vcf
- filter, envelope, lfo, modulation
- modular, eurorack, synthesizer
- patch, voice, cv, gate
- midi, synthesis, synth

**Detection command:**

```bash
find . -maxdepth 2 \( -name "*.pd" -o -name "*.maxpat" -o -name "*.syx" -o -name "patch-notes.md" \) 2>/dev/null
```

## Area Detection Algorithm

1. Run all detection commands in parallel
2. Count matches for each area
3. If one area has significantly more matches (3+), classify as that area
4. If Hardware AND Software both match, ask user (could be embedded software)
5. If no clear winner or no matches, ask user to choose

Example:

```bash
HW=$(find . -maxdepth 2 \( -name "*.ino" -o -name "platformio.ini" \) 2>/dev/null | wc -l)
SW=$(find . -maxdepth 2 \( -name "package.json" -o -name "*.py" -o -name "*.js" \) 2>/dev/null | wc -l)
WW=$(find . -maxdepth 2 \( -name "*.stl" -o -name "*.blend" \) 2>/dev/null | wc -l)
MS=$(find . -maxdepth 2 \( -name "*.pd" -o -name "*.maxpat" \) 2>/dev/null | wc -l)

if [ $HW -gt 0 ] && [ $HW -gt $SW ] && [ $HW -gt $WW ] && [ $HW -gt $MS ]; then
  AREA="Hardware"
elif [ $SW -gt 0 ] && [ $SW -gt $HW ] && [ $SW -gt $WW ] && [ $SW -gt $MS ]; then
  AREA="Software"
elif [ $WW -gt 0 ] && [ $WW -gt $HW ] && [ $WW -gt $SW ] && [ $WW -gt $MS ]; then
  AREA="Woodworking"
elif [ $MS -gt 0 ] && [ $MS -gt $HW ] && [ $MS -gt $SW ] && [ $MS -gt $WW ]; then
  AREA="Music Synthesis"
else
  # Ask user
  echo "Could not determine project area. Please choose: Hardware, Software, Woodworking, or Music Synthesis"
fi
```

## Description Extraction

### From README.md

```bash
# Get first paragraph after title
sed -n '/^# /,/^$/p' README.md | tail -n +2 | head -n 3
```

### From package.json

```bash
cat package.json | grep '"description"' | sed 's/.*: "\(.*\)".*/\1/'
```

### From Conversation

Look for user statements about:

- "I'm building..."
- "This project is for..."
- "The goal is to..."
- "I'm trying to..."

Extract the sentence as the description.

### Default

If no description found, leave blank in template for user to fill in.

## Date Formatting

Always use ISO 8601 format: YYYY-MM-DD

```bash
date +%Y-%m-%d
# Example: 2025-12-23
```

## Path Handling

### Working Directory Detection

```bash
pwd
# Example: /Users/alister/projects/my-arduino-project
```

### Vault Path

Always use the configured vault path from config.json. Convert to absolute path if needed:

```bash
# If path starts with ~, expand it
VAULT_PATH="${VAULT_PATH/#\~/$HOME}"

# Ensure it exists
if [ ! -d "$VAULT_PATH" ]; then
  echo "Error: Vault path does not exist: $VAULT_PATH"
fi
```

### File Paths

Use forward slashes for cross-platform compatibility. Use absolute paths when writing to vault:

```bash
# Good
/Users/alister/Documents/ObsidianVault/Projects/My Project.md

# Also good (will expand)
~/Documents/ObsidianVault/Projects/My Project.md

# Bad (relative paths from unknown location)
Projects/My Project.md
```

## Edge Cases

### Multi-Area Projects

If project spans multiple areas (e.g., Hardware + Software for embedded project):

- Ask user which area to classify under
- Suggest creating separate notes if truly distinct
- Default to primary area if obvious (hardware with software support → Hardware)

### Ambiguous Directory Names

If directory name is generic (test, demo, project1):

- Check parent directory
- Check git repo name
- Check README
- Ask user as last resort

### No Git Repository

Totally fine! Use directory name and continue normally.

### Nested Projects

If in a subdirectory of a larger project:

- Check if parent has .git
- Ask user if this is a sub-project or independent project
- Offer to create sub-project note or main project note
