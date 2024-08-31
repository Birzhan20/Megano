def directory_path(directory: str, user_id: int, order_id: int) -> str:
    """Функция генерации пути хранения заказа или продуктов в заказе."""

    return "media/{directory}/user{user_id}_order{order_id}.json".format(
        directory=directory,
        user_id=user_id,
        order_id=order_id,
    )
