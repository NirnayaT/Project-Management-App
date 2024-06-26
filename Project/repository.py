from Database.database import Project, session
from repository import AbstractRepository


class ProjectRepository(AbstractRepository):

    def get(self) -> list[Project]:
        details = session.query(Project).all()
        return details

    def add(self, new_proj: str, project_description: str, owner_id: int):
        new_project_obj = Project(
            name=new_proj, description=project_description, owner_id=owner_id
        )
        session.add(new_project_obj)
        session.commit()
        return new_project_obj

    def remove(self, project_id: int):
        remove_project = session.query(Project).filter(Project.id == project_id).first()
        session.delete(remove_project)
        session.commit()
        return remove_project

    def update(
        self, project_id: int, new_project_name: str, new_project_description: str
    ):
        update_project = session.query(Project).filter(Project.id == project_id).first()
        if update_project:
            update_project.name = new_project_name
            update_project.description = new_project_description
            session.commit()
        return update_project
