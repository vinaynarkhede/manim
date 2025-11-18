"""
The Index Paradox - Main Composition

This file combines all scenes into the complete 2:40 animation.
Each scene should be tested independently before composing here.

Timeline:
- 0:00-0:15: Cold Open (scene_00)
- 0:15-0:30: Library Scale (scene_01)
- 0:30-0:45: Character Introductions (scene_02)
- 0:45-1:05: Challenge 1 - Single Target (scene_03)
- 1:05-1:35: Challenge 2 - Range Query (scene_04) - TODO
- 1:35-1:55: Challenge 3 - Sorted Data (scene_05) - TODO
- 1:55-2:25: Revelation (scene_06) - TODO
- 2:25-2:40: Closer (scene_07) - TODO

Usage:
    # Render individual scene at low quality for testing
    manim -ql scenes/scene_00_cold_open.py ColdOpenScene

    # Render all scenes in sequence (when ready)
    manim -qm main.py IndexParadox

    # Final 4K render
    manim -qk main.py IndexParadox
"""

from manim import *
from scenes.scene_00_cold_open import ColdOpenScene
from scenes.scene_01_library import LibraryScaleScene
from scenes.scene_02_characters import CharacterIntroScene
from scenes.scene_03_challenge_1 import Challenge1Scene


class IndexParadox(Scene):
    """
    Master composition combining all scenes of The Index Paradox.

    IMPORTANT: Only use this after all individual scenes are tested and working!
    Test each scene independently first using the individual scene files.
    """

    def construct(self):
        # Note: This is a placeholder for future full composition
        # Each scene should be rendered separately during development

        self.add(
            Text(
                "The Index Paradox - Full Composition",
                font_size=48,
                color="#FFFFFF"
            )
        )

        info = VGroup(
            Text("Render individual scenes for testing:", font_size=24),
            Text("manim -ql scenes/scene_00_cold_open.py ColdOpenScene", font_size=18, color="#00D9FF"),
            Text("manim -ql scenes/scene_01_library.py LibraryScaleScene", font_size=18, color="#00D9FF"),
            Text("manim -ql scenes/scene_02_characters.py CharacterIntroScene", font_size=18, color="#00D9FF"),
            Text("manim -ql scenes/scene_03_challenge_1.py Challenge1Scene", font_size=18, color="#00D9FF"),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).move_to(DOWN*0.5)

        self.add(info)
        self.wait(5)


# Individual scene classes can also be imported and rendered directly
# This allows for modular testing and development
