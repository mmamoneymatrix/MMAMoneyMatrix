import os
import json

base_path = "/home/ubuntu/MMAMoneyMatrix"
styles_path = os.path.join(base_path, "styles")
fighters_path = os.path.join(base_path, "data", "fighters")

styles_map = {
    "Karate": ["Shotokan", "Kyokushin", "GojuRyu"],
    "Judo": ["Kodokan", "CombatJudo", "OlympicJudo"],
    "MuayThai": ["DutchStyle", "TraditionalMuayThai", "K1Hybrid"],
    "JiuJitsu": ["BJJ_Gi", "BJJ_NoGi", "JapaneseJJ"],
    "Wrestling": ["Freestyle", "GrecoRoman", "Folkstyle"],
    "Fighter": ["Brawler", "CounterStriker", "PressureFighter"],
    "Athlete": ["PowerAthlete", "SpeedAthlete", "EnduranceAthlete"],
    "Boxer": ["OutBoxer", "InFighter", "CounterPuncher"],
    "MartialArtist": ["TraditionalMaster", "ModernMixedArtist", "GrandMaster"]
}

# Ensure base directories exist
os.makedirs(styles_path, exist_ok=True)
os.makedirs(fighters_path, exist_ok=True)

for style, sub_styles in styles_map.items():
    style_dir = os.path.join(styles_path, style)
    os.makedirs(style_dir, exist_ok=True)
    
    for sub in sub_styles:
        sub_dir = os.path.join(style_dir, sub)
        os.makedirs(sub_dir, exist_ok=True)
        
        # Create profile.json, stats.json, abilities.json, readme.md
        for filename in ["profile.json", "stats.json", "abilities.json"]:
            with open(os.path.join(sub_dir, filename), 'w') as f:
                json.dump({}, f)
        
        with open(os.path.join(sub_dir, "readme.md"), 'w') as f:
            f.write(f"# {sub} ({style})\n\nDescription for {sub} style.")

        # Create empty fighter JSON in data/fighters/
        fighter_filename = f"{style}_{sub}_fighter.json"
        with open(os.path.join(fighters_path, fighter_filename), 'w') as f:
            json.dump({}, f)

print("Styles hierarchy and fighter data structure created successfully.")
