def create_piece(name, moved=False):
    """
    Factory function to create a chess piece dictionary.

    Args:
        name (str): The identifier of the piece (e.g., 'b', 'q', 'k', etc.).
        moved (bool): Indicates whether the piece has moved. Default is False.

    Returns:
        dict: A dictionary representing the chess piece.
    """
    figures = {
        "p": "Pawn",
        "r": "Rook",
        "n": "Knight",
        "b": "Bishop",
        "q": "Queen",
        "k": "King",
    }
    figure = figures.get(str(name).lower(), "Unknown")
    return {"name": name, "moved": moved, "figure": figure}
