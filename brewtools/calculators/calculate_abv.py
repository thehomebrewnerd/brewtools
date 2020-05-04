def calculate_abv(og, fg):
    """Calculate percent alcohol by volume based on starting and finishing
    gravity readings.

    Args:
        og (float): Measured initial specific gravity
        fg (float): Measured final specific gravity
    """

    return 131.25 * (og - fg)
