import json
import os
import random

def generate_fighter_stats(style, sub_style):
    # Base stats mapping for different archetypes
    archetypes = {
        "Wrestler": {"td_avg": 4.5, "td_acc": 55, "td_def": 85, "slpm": 2.5, "sapm": 2.1, "sub_avg": 0.8, "cardio": 88},
        "Striker": {"td_avg": 0.5, "td_acc": 25, "td_def": 75, "slpm": 5.2, "sapm": 3.5, "sub_avg": 0.1, "cardio": 82},
        "BJJ": {"td_avg": 1.8, "td_acc": 35, "td_def": 60, "slpm": 2.1, "sapm": 2.8, "sub_avg": 2.5, "cardio": 80},
        "Athlete": {"td_avg": 3.2, "td_acc": 45, "td_def": 80, "slpm": 3.1, "sapm": 2.4, "sub_avg": 0.3, "cardio": 95},
        "Brawler": {"td_avg": 1.2, "td_acc": 30, "td_def": 65, "slpm": 6.5, "sapm": 5.8, "sub_avg": 0.4, "cardio": 90},
    }

    # Assign archetype based on style
    if "Wrestling" in style or "Judo" in style: arch = "Wrestler"
    elif "Karate" in style or "MuayThai" in style or "Boxer" in style: arch = "Striker"
    elif "JiuJitsu" in style: arch = "BJJ"
    elif "Athlete" in style: arch = "Athlete"
    elif "Fighter" in style: arch = "Brawler"
    else: arch = "Striker"

    base = archetypes[arch]
    
    # Randomize slightly
    stats = {
        "height": random.randint(66, 76),
        "reach": random.randint(68, 80),
        "slpm": round(base["slpm"] + random.uniform(-0.5, 1.5), 2),
        "striking_accuracy": random.randint(40, 60),
        "sapm": round(base["sapm"] + random.uniform(-0.5, 1.0), 2),
        "striking_defense": random.randint(50, 70),
        "td_avg": round(base["td_avg"] + random.uniform(-0.5, 1.0), 2),
        "td_acc": random.randint(base["td_acc"]-10, base["td_acc"]+10),
        "td_def": random.randint(base["td_def"]-10, base["td_def"]+10),
        "sub_avg": round(base["sub_avg"] + random.uniform(-0.2, 0.5), 2),
        "cardio_index": base["cardio"] + random.randint(-5, 5),
        "damage_tolerance": random.randint(70, 95),
        "chaos_factor": round(random.uniform(0.1, 0.9), 2)
    }

    # Calculate OVR
    ovr = int((stats["slpm"]*10 + stats["striking_accuracy"] + stats["td_avg"]*15 + stats["td_acc"] + stats["cardio_index"]) / 5)
    stats["ovr"] = min(99, ovr)
    
    return stats

def generate_abilities(style, sub_style):
    abilities_pool = [
        "Iron Chin", "Heavy Hands", "Submission Wizard", "Cardio King", 
        "Cradle Master", "Counter Specialist", "Blitz Striker", "Cage Controller"
    ]
    return random.sample(abilities_pool, 3)

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

base_path = "/home/ubuntu/MMAMoneyMatrix"

for style, sub_styles in styles_map.items():
    for sub in sub_styles:
        sub_dir = os.path.join(base_path, "styles", style, sub)
        
        stats = generate_fighter_stats(style, sub)
        abilities = generate_abilities(style, sub)
        
        profile = {
            "name": f"Generic {sub} Fighter",
            "style": style,
            "sub_style": sub,
            "archetype": "Wrestler" if "Wrestling" in style else "Striker",
            "gender": random.choice(["Male", "Female"]),
            "ethnicity": random.choice(["White", "Black", "Asian", "Latino"]),
            "gi_style": "Street-Fighter style gi"
        }

        with open(os.path.join(sub_dir, "profile.json"), 'w') as f: json.dump(profile, f, indent=4)
        with open(os.path.join(sub_dir, "stats.json"), 'w') as f: json.dump(stats, f, indent=4)
        with open(os.path.join(sub_dir, "abilities.json"), 'w') as f: json.dump(abilities, f, indent=4)

        # Update fighter data
        fighter_file = os.path.join(base_path, "data", "fighters", f"{style}_{sub}_fighter.json")
        fighter_data = {**profile, **stats, "abilities": abilities}
        with open(fighter_file, 'w') as f: json.dump(fighter_data, f, indent=4)

print("All fighter stats and profiles generated.")
