from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True) #primary_key é quando o valor é gerado automaticamnete
    title: Mapped[str] = mapped_column(String,  
                                       index=True)
    description: Mapped[str] = mapped_column(String)
    priority: Mapped[str] = mapped_column(String)
    creation_date: Mapped[datetime] = mapped_column(DateTime,
                                                    default=datetime.utcnow)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    status: Mapped[str] = mapped_column(String)

    project = relationship("Project", back_populates="tasks")