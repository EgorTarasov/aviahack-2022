import { Badge, Col, Row, Typography } from 'antd';
import React, { FC } from 'react';
import Request from '../../components/Request/Request';
import Task from '../../components/Task/Task';
import { useStores } from '../../hooks/useStores';

import './Home.scss';

const Home: FC = () => {
    const { driverStore } = useStores();
    return (
        <>
            <div className='home'>
                {/* <Request task={} /> */}
                <Task />
            </div>
        </>
    );
};

export default Home;
