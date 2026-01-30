from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from datetime import datetime
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

owner = relationship("User", back_populates="projects")
tasks = relationship("Task", back_populates="project")
#relacionamento de campos user>project>task

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True) 
    title: Mapped[str] = mapped_column(String,  
                                       index=True)
    creation_date: Mapped[datetime] = mapped_column(DateTime,
                                                    default=datetime.utcnow)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    description: Mapped[str] = mapped_column(String)

    tasks = relationship(
        "Task",
        back_populates="project",
        cascade="all, delete-orphan"
    )