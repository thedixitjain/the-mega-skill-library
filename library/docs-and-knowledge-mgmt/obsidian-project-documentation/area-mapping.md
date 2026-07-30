# Area Mapping Reference

Quick reference for file extensions and patterns that indicate project areas.

## File Extension to Area Mapping

| Extension | Area | Description |
| --------- | ---- | ----------- |
| `.ino` | Hardware | Arduino sketch files |
| `.cpp`, `.h` | Hardware* | C/C++ (embedded context) |
| `.pcb` | Hardware | PCB design files |
| `.sch` | Hardware | Schematic files |
| `.js`, `.ts` | Software | JavaScript/TypeScript |
| `.py` | Software | Python |
| `.go` | Software | Go |
| `.rs` | Software | Rust |
| `.java` | Software | Java |
| `.rb` | Software | Ruby |
| `.php` | Software | PHP |
| `.stl` | Woodworking | 3D model (STL) |
| `.obj` | Woodworking | 3D object file |
| `.blend` | Woodworking | Blender file |
| `.f3d` | Woodworking | Fusion 360 file |
| `.skp` | Woodworking | SketchUp file |
| `.pd` | Music Synthesis | Pure Data patch |
| `.maxpat` | Music Synthesis | Max/MSP patch |
| `.syx` | Music Synthesis | SysEx MIDI file |
| `.fxp` | Music Synthesis | VST preset |
| `.amxd` | Music Synthesis | Ableton M4L device |
| `.sh` | Software | Shell |

*Note: `.cpp` and `.h` can be Software or Hardware depending on context. Check for embedded indicators.

## Configuration File Mapping

| File | Area | Description |
| ---- | ---- | ----------- |
| `platformio.ini` | Hardware | PlatformIO configuration |
| `arduino_secrets.h` | Hardware | Arduino secrets |
| `package.json` | Software | Node.js package |
| `requirements.txt` | Software | Python dependencies |
| `Cargo.toml` | Software | Rust package |
| `go.mod` | Software | Go module |
| `pom.xml` | Software | Java Maven |
| `build.gradle` | Software | Java Gradle |
| `cut-list.md` | Woodworking | Woodworking cut list |
| `materials.md` | Woodworking | Materials list |
| `patch-notes.md` | Music Synthesis | Synth patch notes |
| `tuning-table.txt` | Music Synthesis | Musical tuning data |

## Keyword Indicators

### Hardware Keywords

```text
arduino, esp32, esp8266, teensy, stm32
circuit, pcb, schematic, breadboard
sensor, actuator, microcontroller, mcu
i2c, spi, uart, serial, gpio
led, button, motor, servo
voltage, current, resistor, capacitor
```

### Software Keywords

```text
api, rest, graphql, endpoint
backend, frontend, fullstack
server, client, database, db
web, mobile, desktop, app
framework, library, package
npm, pip, cargo, composer
react, vue, angular, flask, django
docker, kubernetes, container
```

### Woodworking Keywords

```text
joinery, dovetail, mortise, tenon
dado, rabbet, tongue, groove
finish, stain, polyurethane, lacquer
wood, lumber, hardwood, plywood, mdf
oak, maple, walnut, cherry, pine
table, saw, router, planer, jointer
shop, workshop, woodshop, bench
clamp, chisel, plane, sandpaper
```

### Music Synthesis Keywords

```text
oscillator, vco, vca, vcf
filter, lowpass, highpass, bandpass
envelope, adsr, attack, decay, sustain, release
lfo, modulation, frequency, amplitude
modular, eurorack, rack, module
patch, voice, polyphony, monophonic
cv, gate, trigger, clock
midi, note, cc, sysex
synthesis, synth, analog, digital
waveform, sine, saw, square, triangle
```

## Detection Priority

When multiple areas match:

1. **Hardware + Software**: Ask user (likely embedded software project)
2. **Woodworking + Hardware**: Ask user (could be CNC or electronics enclosure)
3. **Music Synthesis + Hardware**: Ask user (likely hardware synthesizer build)
4. **Music Synthesis + Software**: Ask user (software synthesizer or plugin)

## Special Cases

### Embedded Software (Hardware + Software)

If both hardware and software indicators present:

- Check for microcontroller keywords (arduino, esp32, etc.) → Hardware
- Check for web/api keywords → Software
- When in doubt, ask user to choose primary area

### 3D Printing Projects

`.stl`, `.gcode` files could be:

- Woodworking (jigs, fixtures, furniture parts)
- Hardware (enclosures, brackets, mechanical parts)
- Music Synthesis (eurorack panels, knobs)

Check context and ask user if needed.

### CAD/Design Projects

`.blend`, `.f3d`, `.skp` files could be:

- Woodworking (furniture design)
- Hardware (enclosure design)
- General 3D modeling

Look for other context clues or ask user.

## Custom Area Support

Users can add custom areas in config.json:

```json
{
  "areas": [
    "Hardware",
    "Software",
    "Woodworking",
    "Music Synthesis",
    "Photography",
    "3D Printing"
  ]
}
```

If user has custom areas, ask them to classify or provide detection rules.

## Canonical Technology Names for Relationship Matching

When populating the `technologies:` frontmatter field or matching cross-project relationships, use these canonical
names for consistency. Matching is case-insensitive; always write the canonical form listed here.

### Hardware

| Canonical Name | Aliases / Indicators |
| -------------- | -------------------- |
| Arduino | arduino, `.ino` |
| ESP32 | esp32, esp-32 |
| ESP8266 | esp8266, esp-8266 |
| Teensy | teensy |
| STM32 | stm32, bluepill |
| Raspberry Pi | raspberry pi, rpi, raspi |
| Raspberry Pi Pico | pico, rp2040 |
| KiCad | kicad, `.kicad_pcb` |
| I2C | i2c, i²c, wire |
| SPI | spi |
| UART | uart, serial |
| MQTT | mqtt |
| BLE | ble, bluetooth le, bluetooth low energy |
| WiFi | wifi, wi-fi, wireless |
| CNC | cnc, gcode, `.gcode` |

### Software

| Canonical Name | Aliases / Indicators |
| -------------- | -------------------- |
| JavaScript | javascript, `.js` |
| TypeScript | typescript, `.ts` |
| Python | python, `.py` |
| Go | golang, `.go` |
| Rust | rust, `.rs`, cargo |
| Java | java, `.java` |
| Ruby | ruby, `.rb` |
| PHP | php, `.php` |
| Shell | bash, sh, zsh, `.sh` |
| React | react, reactjs |
| Vue | vue, vuejs |
| Angular | angular |
| Flask | flask |
| Django | django |
| Express | express, expressjs |
| FastAPI | fastapi |
| Docker | docker, dockerfile, container |
| Kubernetes | kubernetes, k8s, helm |
| PostgreSQL | postgresql, postgres |
| MySQL | mysql |
| MongoDB | mongodb, mongo |
| SQLite | sqlite |
| Redis | redis |
| AWS | aws, amazon web services |
| Claude API | claude api, anthropic, claude code |

### Woodworking

| Canonical Name | Aliases / Indicators |
| -------------- | -------------------- |
| Dovetail joinery | dovetail |
| Mortise and tenon | mortise, tenon |
| CNC routing | cnc router |
| Hand-cut joinery | hand-cut, hand cut |
| Lathe turning | lathe, turned, turning |
| Oak | oak |
| Maple | maple |
| Walnut | walnut |
| Cherry | cherry |
| Pine | pine |
| Plywood | plywood |
| MDF | mdf |
| Oil finish | oil, danish oil, tung oil |
| Polyurethane | polyurethane |
| Fusion 360 | fusion 360, `.f3d` |
| SketchUp | sketchup, `.skp` |

### Music Synthesis

| Canonical Name | Aliases / Indicators |
| -------------- | -------------------- |
| Eurorack | eurorack, euro-rack |
| Pure Data | pure data, pd, `.pd` |
| Max/MSP | max/msp, maxmsp, `.maxpat` |
| Ableton Live | ableton, live, `.als`, `.amxd` |
| MIDI | midi, `.syx`, `.mid` |
| CV/Gate | cv, gate, cv/gate |
| Analog synthesis | analog, analogue |
| FM synthesis | fm, fm synthesis, frequency modulation |
| Granular synthesis | granular |
| Wavetable synthesis | wavetable |
| VCO | vco, oscillator |
| VCF | vcf, filter |
| VCA | vca, amplifier |
| ADSR | adsr, envelope |
| OSC | osc, open sound control |

## Future Enhancements

Potential improvements for area detection:

- Machine learning classification based on file content
- User training: remember classifications for similar projects
- Directory path patterns (~/arduino-projects → Hardware)
- Git repository topics/keywords from GitHub
- README.md badge detection (shields.io)
