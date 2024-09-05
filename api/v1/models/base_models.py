import sqlalchemy as sa
import sqlalchemy.orm as so
from uuid6 import uuid7
from datetime import datetime, timezone

class BaseModel():
    id: so.Mapped[str] = so.mapped_column(primary_key=True, 
                                          index=True, 
                                          default=lambda: str(uuid7())
                                          )
    created_at: so.Mapped[datetime] = so.mapped_column(index=True,
                                                       default=lambda: datetime.now(timezone.utc))
    updated_at: so.Mapped[datetime] = so.mapped_column(index=True,
                                                       default=lambda: datetime.now(timezone.utc))
