# The Index Paradox

A high-production educational animation comparing **Hash Index vs B-tree Index** through a cinematic library metaphor. Built with Manim (Mathematical Animation Engine).

**Duration:** 2:40 minutes
**Style:** 3Blue1Brown + Kurzgesagt quality
**Status:** Scenes 0-3 implemented, remaining scenes in development

---

## Project Overview

This animation tells the story of two indexing algorithms through the metaphor of two librarians competing in a massive library during a crisis. Instead of dry technical comparisons, we create **characters with personalities**:

- **Hash Index**: Geometric, crystalline, electric blue - aggressive and fast
- **B-tree Index**: Organic, tree-like, warm amber - patient and wise

---

## Project Structure

```
manim/
├── scenes/                    # Scene files (one per scene)
│   ├── scene_00_cold_open.py       # 0:00-0:15 - The Hook
│   ├── scene_01_library.py         # 0:15-0:30 - Scale Problem
│   ├── scene_02_characters.py      # 0:30-0:45 - Character Intros
│   ├── scene_03_challenge_1.py     # 0:45-1:05 - Single Lookup
│   └── ...                         # Future scenes
├── components/                # Reusable visual components
│   ├── colors.py              # Color palette constants
│   ├── hash_character.py      # Hash Index character
│   ├── btree_character.py     # B-tree Index character
│   └── library_shelf.py       # Library shelf component
├── utils/                     # Utility functions
├── config/
│   └── manim.cfg              # Manim configuration
├── design.md                  # Complete visual design specification
├── CLAUDE.md                  # Implementation guide
└── main.py                    # Master composition (future)
```

---

## Installation

### System Dependencies

Manim requires system libraries. Install based on your OS:

**macOS:**
```bash
brew install py3cairo ffmpeg pango pkg-config
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
```

**Windows:**
See [Manim Windows Installation Guide](https://docs.manim.community/en/stable/installation/windows.html)

### Python Dependencies

```bash
# Install Manim and dependencies
pip install -r requirements.txt
```

### Verify Installation

```bash
manim --version
# Should output: Manim Community v0.18.0 (or later)
```

---

## Usage

### Rendering Individual Scenes (Recommended for Development)

Test each scene independently before combining:

```bash
# Quick low-quality test render (480p, fast)
manim -ql scenes/scene_00_cold_open.py ColdOpenScene

# Medium quality review (720p)
manim -qm scenes/scene_00_cold_open.py ColdOpenScene

# High quality (1080p)
manim -qh scenes/scene_00_cold_open.py ColdOpenScene

# 4K final render
manim -qk scenes/scene_00_cold_open.py ColdOpenScene
```

### Available Scenes

| Scene | File | Class | Duration | Status |
|-------|------|-------|----------|--------|
| Cold Open | `scene_00_cold_open.py` | `ColdOpenScene` | 0:00-0:15 | ✅ Implemented |
| Library Scale | `scene_01_library.py` | `LibraryScaleScene` | 0:15-0:30 | ✅ Implemented |
| Character Intros | `scene_02_characters.py` | `CharacterIntroScene` | 0:30-0:45 | ✅ Implemented |
| Challenge 1 | `scene_03_challenge_1.py` | `Challenge1Scene` | 0:45-1:05 | ✅ Implemented |
| Challenge 2 | `scene_04_challenge_2.py` | `Challenge2Scene` | 1:05-1:35 | 📝 TODO |
| Challenge 3 | `scene_05_challenge_3.py` | `Challenge3Scene` | 1:35-1:55 | 📝 TODO |
| Revelation | `scene_06_revelation.py` | `RevelationScene` | 1:55-2:25 | 📝 TODO |
| Closer | `scene_07_closer.py` | `CloserScene` | 2:25-2:40 | 📝 TODO |

### Rendering the Full Animation

```bash
# When all scenes are complete
manim -qh main.py IndexParadox
```

---

## Development Workflow

**Follow the "Test Every Scene Before Moving Forward" principle:**

1. **Read `CLAUDE.md`** for detailed implementation guide for each scene
2. **Implement scene** following the step-by-step breakdown
3. **Test at `-ql` quality** after each step
4. **Only proceed** when current step renders perfectly
5. **Test full scene at `-qm`** before moving to next scene
6. **Document deviations** from design.md if any

### Example Workflow for a New Scene

```bash
# 1. Implement scene in scenes/scene_XX_name.py

# 2. Test at low quality (fast iteration)
manim -ql scenes/scene_XX_name.py SceneName

# 3. Review output in media/videos/scene_XX_name/480p15/

# 4. Iterate until perfect

# 5. Test at medium quality
manim -qm scenes/scene_XX_name.py SceneName

# 6. Mark as complete and move to next scene
```

---

## Color Palette

Defined in `components/colors.py`:

- **BACKGROUND**: `#0A0E1A` - Deep navy
- **HASH_CYAN**: `#00D9FF` - Electric blue (Hash Index)
- **BTREE_AMBER_START**: `#FFB347` - Warm amber (B-tree)
- **BTREE_AMBER_END**: `#FF6B35` - Deep orange (gradient)
- **SUCCESS_GREEN**: `#50C878` - Emerald (success states)
- **DANGER_RED**: `#C41E3A` - Crimson (errors/failures)
- **GOLD**: `#FFD700` - Highlighted elements

---

## Key Design Principles

From `design.md`:

1. **Characters over diagrams**: Hash and B-tree are personalities, not just algorithms
2. **Cinematic quality**: Camera movement, depth of field, particle systems
3. **Emotional engagement**: Story arc with tension and resolution
4. **Educational clarity**: Accurate while being memorable
5. **Production polish**: Micro-animations, breathing elements, sophisticated easing

---

## Technical Notes

### Manim Version

This project uses **Manim Community Edition** (not ManimGL or original Manim). Ensure you install the correct version:

```bash
pip install manim  # Correct - Community Edition
# NOT: pip install manimgl
```

### Font Fallbacks

Some scenes use fallback fonts if specific fonts aren't available:
- "Monument Extended" → "Monospace"
- "Inter" / "SF Pro" → "Sans"
- "Cormorant Garamond" → "Serif"

For production renders, install the actual fonts for best results.

### Performance Tips

- Use `-ql` during development (10x faster than `-qh`)
- Reduce particle counts if rendering is slow
- Use `--disable_caching` if animations seem incorrect
- Render scenes individually, not full 2:40 at once

---

## Resources

- **Manim Documentation**: https://docs.manim.community/
- **Manim Examples**: https://docs.manim.community/en/stable/examples.html
- **This Project's Design Doc**: [design.md](design.md)
- **Implementation Guide**: [CLAUDE.md](CLAUDE.md)

---

## Roadmap

- [x] Setup project structure
- [x] Create color palette and reusable components
- [x] Implement Scene 0: Cold Open
- [x] Implement Scene 1A: Library Scale
- [x] Implement Scene 1B: Character Introductions
- [x] Implement Scene 3: Challenge 1 (Single Lookup)
- [ ] Implement Scene 4: Challenge 2 (Range Query) - **NEXT**
- [ ] Implement Scene 5: Challenge 3 (Sorted Data)
- [ ] Implement Scene 6: Revelation
- [ ] Implement Scene 7: Closer
- [ ] Master composition combining all scenes
- [ ] Sound design and music integration
- [ ] Final 4K render

---

## Contributing

This is a personal educational project, but suggestions and improvements are welcome! See `CLAUDE.md` for detailed implementation guidelines.

---

## License

Educational use. Created to demonstrate database indexing concepts through animation.

---

**The most important principle: VALIDATE BEFORE ADVANCING.**

Test every scene completely before moving to the next one. Quality over speed.
