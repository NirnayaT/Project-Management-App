from datetime import date
from typing import Optional
from config.database import session
from repository.repository import AbstractRepository
from models.projects import Project


class ProjectRepository(AbstractRepository):
    """
    The `ProjectRepository` class is an implementation of the 
    `AbstractRepository` class that provides methods for managing 
    projects in the application.
    
    The `get` method retrieves a list of projects for a given owner ID. 
    If no projects are found, it returns `None`.
    
    The `add` method creates a new project with the provided details 
    and saves it to the database.
    
    The `remove` method deletes a project with the given ID from the 
    database. If the project does not exist, it returns `None`.
    
    The `update` method updates the details of an existing project with 
    the given ID. If the project does not exist, it returns `None`.
    
    The `get_project` method retrieves a single project with the given ID.
    """
        
    def get(self, owner_id) -> list[Project]:
        """
        Retrieves a list of projects for the given owner ID. If no projects 
        are found, returns `None`.
        
        Args:
            owner_id (int): The ID of the project owner.
        
        Returns:
            list[Project] or None: A list of `Project` objects, or `None` 
            if no projects are found.
        """
                
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
        """
        Adds a new project to the database with the provided details.
        
        Args:
            new_proj (str): The name of the new project.
            project_description (str): The description of the new project.
            owner_id (int): The ID of the project owner.
            start_date (date): The start date of the project.
            end_date (Optional[date]): The end date of the project, 
            if provided.
        
        Returns:
            Project: The newly created project object.
        """
                
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
        """
        Removes a project from the database by the given project ID.
        
        Args:
            project_id (int): The ID of the project to remove.
        
        Returns:
            Project or None: The removed project object, or None if 
            the project does not exist or an error occurred during removal.
        """
                
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
        """
        Updates an existing project in the database with the provided details.
        
        Args:
            project_id (int): The ID of the project to update.
            new_project_name (str): The new name for the project.
            new_project_description (str): The new description for the project.
            start_date (date): The new start date for the project.
            end_date (date): The new end date for the project.
        
        Returns:
            Project: The updated project object, or None if the project 
            does not exist or an error occurred during the update.
        """
                
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
        """
        Gets a single project from the database by its ID.
        
        Args:
            project_id (int): The ID of the project to retrieve.
        
        Returns:
            Project or None: The retrieved project object, or None if 
            the project does not exist.
        """
                
        details = session.query(Project).filter(Project.id == project_id).first()
        return details
