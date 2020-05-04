def calculate_abv(og, fg, method="simple"):
    """Calculate percent alcohol by volume based on starting and finishing
    gravity readings.

    Args:
        og (float): Measured initial specific gravity
        fg (float): Measured final specific gravity
    """
    if method == "advanced":
        return (76.08 * (og - fg) / (1.775 - og)) * (fg / 0.794)

    return 131.25 * (og - fg)
