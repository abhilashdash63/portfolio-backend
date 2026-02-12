from sqlalchemy import Column, Integer, String, Text
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    github_url = Column(String(255), nullable=True)
    image_url = Column(String(500), nullable=True)



class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    title = Column(String(255))
    bio = Column(Text)
    email = Column(String(255))
    location = Column(String(255))
    phone = Column(String(20))



class Experience(Base):
    __tablename__ = "experience"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(255))
    role = Column(String(255))
    duration = Column(String(255))
    description = Column(Text)


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    level = Column(String(50))  # Beginner, Intermediate, Expert
