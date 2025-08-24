import React, { useState, useEffect, useCallback, useRef } from 'react';
import { Button, Dropdown, Divider } from 'antd';
import { EllipsisOutlined } from '@ant-design/icons';
import { useNavigate } from 'react-router-dom';
import { useGetProj } from './common/useGetProj';
import { useDeleteProj } from './common/useDeleteUser';
import "../../Theme/Css/ProjectList.css";

type ProjectValues = {
  id: number;
  name: string;
  description: string;
  start_date: Date;
  end_date: Date;
  owner_id: number;
};

export default function ProjectList() {
  const [proId, setProId] = useState<number | undefined>();
  const [proOwnerId, setProOwnerId] = useState<number | undefined>();
  const [expanded, setExpanded] = useState<{ [key: number]: boolean }>({});
  const [isOverflow, setIsOverflow] = useState<{ [key: number]: boolean }>({});
  const descriptionRefs = useRef<{ [key: number]: HTMLDivElement }>({});
  const navigate = useNavigate();

  const { data, error, isLoading, refetch: refetchUsers } = useGetProj();
  const { mutation: deleteMutation } = useDeleteProj(() => console.log("Successfully deleted"));

  const handleDelete = (id: number, owner_id: number) => {
    deleteMutation.mutate({ project_id: id, owner_id });
  };

  const handleClick = (e: React.MouseEvent<HTMLAnchorElement>, id: number, owner_id: number) => {
    e.preventDefault();
    setProId(id);
    setProOwnerId(owner_id);
  };

  const handleToggleExpand = (projectId: number) => {
    setExpanded((prev) => ({
      ...prev,
      [projectId]: !prev[projectId],
    }));
  };

  const checkOverflow = useCallback((projectId: number) => {
    const element = descriptionRefs.current[projectId];
    if (element) {
      setIsOverflow((prev) => ({
        ...prev,
        [projectId]: element.scrollHeight > 80, // 80px = 5rem
      }));
    }
  }, []);

  useEffect(() => {
    data?.Projects.forEach((project: ProjectValues) => checkOverflow(project.id));
  }, [data, checkOverflow]);

  useEffect(() => {
    if (deleteMutation.isSuccess) {
      console.log("Deleted successfully");
      refetchUsers();
    }
  }, [deleteMutation.isSuccess, refetchUsers]);

  const renderDescription = (description: string, projectId: number) => {
    const isExpanded = expanded[projectId];
    const showMore = isOverflow[projectId];
    
    // Truncate description
    const truncatedDescription = description.length > 165
      ? `${description.substring(0, 165)}    ....`
      : description;

    return (
      <>
        <div
          ref={(el) => (descriptionRefs.current[projectId] = el!)}
          className={`overflow-hidden ${isExpanded ? 'h-auto' : 'h-[5rem]'}`}
        >
          {isExpanded ? description : truncatedDescription}
        
        {showMore && (
          <button
            onClick={() => handleToggleExpand(projectId)}
            className="text-black inline ml-2 ms-[1px]"
          >
            {isExpanded ? 'see less' : 'see more'}
          </button>
        )}
        </div>
        </>
    );
  };

  const items = [
    {
      label: "Edit",
      key: '0',
    },
    {
      label: <div onClick={() => proId && proOwnerId && handleDelete(proId, proOwnerId)}>Delete</div>,
      key: '1',
    },
  ];

  const formatDate = (date: Date) => new Date(date).toLocaleDateString();

  const handleCreateProject = () => {
    navigate("/create_project");
  };

  const handleProjectClick = (id: number) => {
    navigate(`/taskForm?id=${encodeURIComponent(id)}`);
  };

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading projects</div>;

  return (
    <>
      <div className="titleBar flex justify-end">
        <Button type="primary" onClick={handleCreateProject} className="font-bold">
          Create Project
        </Button>
      </div>
      <div className="bg-white mt-6 pt-4 px-4">
        <div className="Head grid grid-cols-7 titleFont font-semibold mt-4 table">
          <div className="bg-gray-200 ps-10 p-3">ID</div>
          <div className="bg-gray-200 py-3 ps-10">Name</div>
          <div className="bg-gray-200 py-3 ps-10 col-span-2">Description</div>
          <div className="bg-gray-200 py-3 ps-[35px]">Start Date</div>
          <div className="bg-gray-200 py-3 ps-7 col-span-2">End Date</div>
        </div>
        <div className="HeroContent">
          {data?.Projects.map((project: ProjectValues) => (
            <React.Fragment key={project.id}>
              <div className="projectList grid grid-cols-7 ms-2 pt-[28px] pb-[28px]">
                <div className="ms-11" >
                  {project.id}
                </div>
                <div className="ms-7">{project.name}</div>
                <div className="ms-7 col-span-2 ms-[33px]">
                  {renderDescription(project.description, project.id)}
                </div>
                <div className="ms-[33px]">{formatDate(project.start_date)}</div>
                <div className="ms-[28px] ms-[33px]">{formatDate(project.end_date)}</div>
                <div>
            <button onClick={() => handleProjectClick(project.id)} id="bottone1">View Task</button>
            
          
                <div className="pe-[30px] flex justify-end">
                  <Dropdown menu={{ items }} trigger={['click']}>
                    <a onClick={(e) => handleClick(e, project.id, project.owner_id)} className="pe-15">
                      <EllipsisOutlined />
                    </a>
                  </Dropdown>
          </div>        
                </div>
              </div>
              <Divider className="m-0" />
            </React.Fragment>
          ))}

        </div>
      </div>
    </>
  );
}
