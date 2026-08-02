from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker

# ---------------------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------------------

DATABASE_URL = "postgresql://YOUR_USER:YOUR_PASSWORD@YOUR_HOST:5432/YOUR_DB"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
metadata.reflect(bind=engine)

SessionLocal = sessionmaker(bind=engine)

fighters = metadata.tables.get("fighters")
abilities = metadata.tables.get("abilities")
stats = metadata.tables.get("stats")

# ---------------------------------------------------------
# MERGE FIGHTER DATA INTO ENGINE-FRIENDLY DICT
# ---------------------------------------------------------

def merge_fighter_data(f_row, a_row, s_row):
    return {
        "name": f_row["name"],
        "reach": f_row.get("reach_cm", 0),
        "height": f_row.get("height_cm", 0),

        # striking
        "striking_accuracy": s_row.get("sig_strikes_landed", 0),
        "slpm": s_row.get("sig_strikes_landed", 0),
        "sapm": s_row.get("sig_strikes_absorbed", 0),

        # grappling
        "td_avg": s_row.get("takedown_accuracy", 0),
        "td_acc": s_row.get("takedown_accuracy", 0),
        "sub_avg": a_row.get("grappling", 0),
        "td_def": s_row.get("takedown_defense", 0),

        # power / chaos
        "knockdown_avg": a_row.get("power", 0),

        # cardio
        "cardio_index": a_row.get("cardio", 50),

        # round dynamics
        "early_round_rating": a_row.get("aggression", 50),
        "late_round_rating": a_row.get("defense", 50),

        # finishing
        "finish_rate": a_row.get("power", 0) / 100,

        # durability
        "damage_tolerance": a_row.get("chin", 50),

        # gym
        "gym_tier": f_row.get("gym_tier", 1),
    }

# ---------------------------------------------------------
# PUBLIC API
# ---------------------------------------------------------

def get_fighter_by_name(name: str):
    session = SessionLocal()

    try:
        f_query = session.execute(select(fighters).where(fighters.c.name == name)).fetchone()
        if not f_query:
            return None

        a_query = session.execute(select(abilities).where(abilities.c.fighter_id == f_query["id"])).fetchone()
        s_query = session.execute(select(stats).where(stats.c.fighter_id == f_query["id"])).fetchone()

        return merge_fighter_data(f_query, a_query, s_query)

    finally:
        session.close()

