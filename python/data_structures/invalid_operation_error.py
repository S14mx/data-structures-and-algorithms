class InvalidOperationError(Exception):
    def __str__(self):
        return "Method not allowed on empty collection"
