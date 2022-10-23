import { Badge, Col, Row, Typography } from 'antd';
import React, { FC } from 'react';
import Request from '../../components/Request/Request';
import { useStores } from '../../hooks/useStores';

import './List.scss';

const List: FC = () => {
    const { driverStore } = useStores();
    const tasks = driverStore.tasks;
    return (
        <>
            <div className='home'>
                {tasks.map((task, i) => {
                    return <Request task={task} />;
                })}
            </div>
        </>
    );
};

export default List;
