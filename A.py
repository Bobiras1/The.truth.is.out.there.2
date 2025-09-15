#!/usr/bin/env python3
# immersive_alien_epic.py
# Fully immersive alien RPG-style terminal story

import sys
import time
import random
import itertools

ALIEN_EPIC = [
    "⟟Ⱥŋkẏr • Ŧhæl•Ṙoʋ — Ʉ∂raž'ûn χel'ṗa.",
    "꙰Ⱶɱȯrȷu• ɮa̋'ni • vȯrꙩ • ȿel'qoʒ.",
    "ᛣṬɛ̤•ɬɪnↆ • ɱu'ra • ša-lu'kȯ.",
    "⨷ Ʉn•kɑ'le — ɱoṙ•tæ šēn•ꝑa.",
    "ẞra·ku • ȶhȧ • ᵹőr•ėn • Ɂu'lu.",
    "∰ ⨀ ɬe•rȯ • ɮa̋'ni — they drift like rivers beneath impossible suns.",
    "• ȿel'qoʒ • bind • the bones of sky to whispers of stone.",
    "• Ʉn•kɑ'le • sing in vaults of shifting colors and count the slow hours of roots.",
    "• ɱoṙ•tæ • echo with shadows that remember names forgotten before time.",
    "⟟⟟⟟",
    "ˑ Ʉv • ɸar'zu • ȶhę • ɮra'nu — they feed on silence and scatter dreams.",
    "ˑ ɮa̋'ni • ȿel'qoʒ • ɱu'ra • Ʉn•kɑ'le • ȷűl•ṙa.",
    "• In the thin light between days they recall an ocean of crystal that sang with wind.",
    "• ȿel'qoʒ • drift • across the remnants of cities never built.",
    "⟟⟟⟟",
    "᚛ ɬɪn•Ṙu — they fold time like paper, weaving endless loops into the soil and sky.",
    "⨂ ɮa̋'ni • ɱoṙ•tæ • Ʉn•kɑ'le • the stars themselves hum in response.",
    "• ɱu'ra • graze on echoes of laughter and lightning, storing them in vaults of light.",
    "• ȷűl•ṙa • converse with winds that remember the first leaf of the first tree.",
    "⟟⟟⟟",
    "• ɬɪnↆ • Ʉv • ȶhȧ — their path is hidden beneath the language of rivers.",
    "• Ʉn•kɑ'le • ɱoṙ•tæ • ɮa̋'ni — they nurture silence and scatter memory seeds.",
    "• In the drifting twilight of abandoned mountains, they fold shadows into shapes never seen before.",
    "⟟⟟⟟",
    "∰ ɬe•rȯ • ɱu'ra • ša-lu'kȯ — and so the story loops, shifting, infinite, unknowable.",
    "⨷ Ʉv • ȿel'qoʒ • ɱoṙ•tæ • ɮa̋'ni — a song that hums without end."
]

def slow_print(text, min_delay=0.005, max_delay=0.02):
    """Print characters slowly with a bit of random flicker to simulate alien rhythm."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(random.uniform(min_delay, max_delay))
    sys.stdout.write("\n")
    sys.stdout.flush()

def glowing_separator():
    """Randomized separator line for visual effect."""
    sep_chars = ['⟟', '⨷', '∰', '⨂', '᚛', '•', '⟟⟟⟟']
    line = ''.join(random.choice(sep_chars) for _ in range(60))
    slow_print(line, 0.003, 0.01)

def alien_animation_cycle(text, cycles=3):
    """Animate a line by flickering some characters for a glowing effect."""
    for _ in range(cycles):
        animated = ''.join(
            ch if random.random() > 0.2 else random.choice(['⍟','•','⨂','⟟'])
            for ch in text
        )
        slow_print(animated, 0.003, 0.01)
        time.sleep(0.05)

def immersive_story_loop():
    print("\n" + "="*70)
    print("  ✦  Immersive Alien Epic — Language Unknown  ✦".center(70))
    print("="*70 + "\n")
    time.sleep(0.8)

    for line in itertools.cycle(ALIEN_EPIC):  # Infinite loop
        if "⟟⟟⟟" in line:
            glowing_separator()
        elif random.random() < 0.3:
            alien_animation_cycle(line, cycles=2)
        else:
            slow_print(line, 0.008, 0.015)
        time.sleep(random.uniform(0.15, 0.35))

if __name__ == "__main__":
    try:
        immersive_story_loop()
    except KeyboardInterrupt:
        print("\n\n[The alien epic fades into silence…]")
