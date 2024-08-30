from datetime import date
from typing import Optional
from config.database import session
from repository.repository import AbstractRepository
from models.projects import Project


class ProjectRepository(AbstractRepository):

    def get(self, owner_id) -> list[Project]:
        details = session.query(Project).filter(Project.owner_id == owner_id).all()
        if not details:
            return None
        try:
            return details
        except Exception as e:
            raise e

    def add(
        self,
        new_proj: str,
        project_description: str,
        owner_id: int,
        start_date: date,
        end_date: Optional[date] = None,
    ):
        new_project_obj = Project(
            name=new_proj,
            description=project_description,
            owner_id=owner_id,
            start_date=start_date,
            end_date=end_date,
        )
        session.add(new_project_obj)
        session.commit()
        return new_project_obj

    def remove(self, project_id: int):
        remove_project = session.query(Project).filter(Project.id == project_id).first()
        if not remove_project:
            return None  # Return None if the project does not exist
        try:
            session.delete(remove_project)
            session.commit()
        except Exception as e:
            session.rollback()
            # print(f"Error removing project {project_id}: {e}")  # Add logging for debugging
            return None
        return remove_project

    def update(
        self,
        project_id: int,
        new_project_name: str,
        new_project_description: str,
        start_date: date,
        end_date: date,
    ):
        update_project = session.query(Project).filter(Project.id == project_id).first()
        if update_project:
            if new_project_name is not None:
                update_project.name = new_project_name
            if new_project_description is not None:
                update_project.description = new_project_description
            if start_date is not None:
                update_project.start_date = start_date
            if end_date is not None:
                update_project.end_date = end_date
            session.commit()
        return update_project

    def get_project(self, project_id: int) -> list[Project]:
        details = session.query(Project).filter(Project.id == project_id).first()
        return details
