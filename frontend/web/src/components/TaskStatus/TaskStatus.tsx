import React, { FC } from 'react';
import { observer } from 'mobx-react-lite';
import { useStores } from '../../hooks/useStores';
import { ITask } from '../../models/TasksInterfaces';
import { Button, Col, Collapse, Progress, Row, Switch } from 'antd';

import './TasksList.scss';
import TaskDetail from '../TaskDetails/TaskDetail';

const TasksList: FC = observer(() => {
    return <>status</>;
});

export default TasksList;
