class RangesRFI:
    """
    Classe que gerencia os ranges RFI por posição.
    """
    RANGES = {
        "UTG": {"AA", "KK", "QQ", "JJ", "AKs", "AQs", "AKo"},
        "MP 1": {"AA", "KK", "QQ", "JJ", "TT", "AKs", "AQs", "AJs", "KQs", "AKo"},
        "HJ": {"AA", "KK", "QQ", "JJ", "TT", "99", "AKs", "AQs", "AJs", "ATs", "KQs", "AKo"},
        "CO": {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "AKs", "AQs", "AJs", "ATs", "KQs", "KJs", "AKo", "AQo"},
        "BTN": {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "AKs", "AQs", "AJs", "ATs", "KQs", "KJs", "QJs", "AKo", "AQo", "AJo"},
        "SB": {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "AKs", "AQs", "AJs", "ATs", "KQs", "KJs", "QJs", "AKo", "AQo", "AJo", "ATo"},
        "BB": {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22", "AKs", "AQs", "AJs", "ATs", "KQs", "KJs", "QJs", "AKo", "AQo", "AJo", "ATo"}
    }

    @classmethod
    def is_in_range(cls, position, hand):
        return hand in cls.RANGES.get(position, set())
