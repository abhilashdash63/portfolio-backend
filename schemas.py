from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    title: str
    description: str
    github_url: str | None = None
    image_url: str | None = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int

    class Config:
        from_attributes = True



class ProfileBase(BaseModel):
    name: str
    title: str
    bio: str
    email: str
    location: str
    phone: str   # ← make sure this exists


class Profile(ProfileBase):
    id: int
    class Config:
        from_attributes = True
        phone: str



class ExperienceBase(BaseModel):
    company: str
    role: str
    duration: str
    description: str

class Experience(ExperienceBase):
    id: int
    class Config:
        from_attributes = True


class SkillBase(BaseModel):
    name: str
    level: str

class Skill(SkillBase):
    id: int
    class Config:
        from_attributes = True

