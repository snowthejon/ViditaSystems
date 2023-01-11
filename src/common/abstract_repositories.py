from abc import ABC


class __AbstractRepository(ABC):
	pass


class AbstractSQLRepository(__AbstractRepository):
	pass


class AbstractNOSQLRepository(__AbstractRepository):
	pass
