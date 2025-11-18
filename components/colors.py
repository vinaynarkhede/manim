"""
Color palette from design.md specifications for The Index Paradox animation.

This module defines all colors used throughout the animation to ensure
consistency and easy modification.
"""

# Core color palette
BACKGROUND = "#0A0E1A"          # Deep navy with texture
HASH_CYAN = "#00D9FF"            # Electric blue/cyan - aggressive, digital
BTREE_AMBER_START = "#FFB347"    # Warm amber - organic, patient
BTREE_AMBER_END = "#FF6B35"      # Deep orange - gradient end
ACCENT_WHITE = "#FFFFFF"         # Pure white (sparingly used)
DANGER_RED = "#C41E3A"           # Deep crimson - errors, failures
SUCCESS_GREEN = "#50C878"        # Emerald - success states
ACCENT_PURPLE = "#9D4EDD"        # For special effects and accents

# Additional utility colors (for components)
GOLD = "#FFD700"                 # For highlighted elements (target book)
GRAY = "#808080"                 # For neutral elements (shelves)
BLACK = "#000000"                # For text on light backgrounds
WHITE = "#FFFFFF"                # Alias for ACCENT_WHITE

# Color themes for scenes
SCENE_CHALLENGE_1_TINT = "#00D9FF"     # Cool, blue-tinted (Hash wins)
SCENE_CHALLENGE_2_TINT = "#FFB347"     # Warm, amber-tinted (B-tree wins)
SCENE_CHALLENGE_3_TINT = "#FFFFFF"     # Neutral, balanced
SCENE_REVELATION_TINT = "#FFFFFF"      # Pure white (clarity)
