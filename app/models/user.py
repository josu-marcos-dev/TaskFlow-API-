from datetime import datetime
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True) #primery_key = é um identificador único
    email: Mapped[str] = mapped_column(String, 
                                       unique=True, 
                                       index=True)  #index se coloca sempre que o campo e muito solicitado e curto
    password: Mapped[str]
    username: Mapped[str] = mapped_column(String,
                                          unique=True,
                                          index=True)
    creation_date: Mapped[datetime] = mapped_column(DateTime,
                                                    default=datetime.utcnow)
    
    projects = relationship(
        "Project",
        back_populates="owner",
        cascade="all, delete-orphan"
    )#cria relação entre user e projects
