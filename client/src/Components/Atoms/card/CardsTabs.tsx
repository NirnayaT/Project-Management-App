import React, { useState } from 'react';
import { Card } from 'antd';
const tabListNoTitle = [
  {
    key: 'todo',
    label: 'To Do',
  },
  {
    key: 'ongoing',
    label: 'On Going',
  },
  {
    key: 'completed',
    label: 'Completed',
  },
];

const contentListNoTitle: Record<string, React.ReactNode> = {
  todo: <p>article content</p>,
  ongoing: <p>app content</p>,
  completed: <p>project content</p>,
};

const App: React.FC = () => {
  const [activeTabKey2, setActiveTabKey2] = useState<string>('article');

  const onTab2Change = (key: string) => {
    setActiveTabKey2(key);
  };

  return (
    <>
        <Card
        title="Tasks"
        style={{ width: '100%' }}
        tabList={tabListNoTitle}
        activeTabKey={activeTabKey2}
        onTabChange={onTab2Change}
        tabProps={{
          size: 'middle',
        }}
      >
        {contentListNoTitle[activeTabKey2]}
      </Card>
    </>
  );
};

export default App;