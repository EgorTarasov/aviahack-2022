import { Badge, Col, Row, Typography } from 'antd';
import React, { FC } from 'react';
import TasksList from '../../components/TasksList/TasksList';

import './Home.scss';

const Home: FC = () => {
    const [curTime, setCurTime] = React.useState(new Date().toLocaleDateString());

    React.useEffect(() => {
        setInterval(() => setCurTime(new Date().toLocaleString()), 500);
    }, []);

    return (
        <>
            <Row style={{ marginTop: 50 }} justify='center'>
                <Col flex={'0 0 1200px'} xs={{ span: 20 }}>
                    <Row justify='space-between'>
                        <Col span={24}>
                            <Row align='middle'>
                                <Col span={12}>
                                    <div className='home-statistics'>
                                        <Typography.Title
                                            className='home-statistics__title'
                                            level={2}
                                        >
                                            {curTime}
                                        </Typography.Title>
                                    </div>
                                </Col>
                                <Col span={6}>
                                    <div className='home-statistics__buses'>
                                        <Typography.Title className='tasks-title' level={5}>
                                            На 100 мест
                                        </Typography.Title>

                                        <Col>
                                            <Row className='home-statistics__info'>
                                                <Badge
                                                    className='home-statistics__badge'
                                                    style={{ backgroundColor: '#52c41a' }}
                                                    count={14}
                                                />
                                                <span className='home-statistics__desc'>
                                                    Свободны
                                                </span>
                                            </Row>
                                            <Row className='home-statistics__info'>
                                                <Badge
                                                    className='home-statistics__badge'
                                                    style={{ backgroundColor: '#ffb813' }}
                                                    count={8}
                                                />
                                                <span className='home-statistics__desc'>
                                                    Заняты
                                                </span>
                                            </Row>
                                            <Row className='home-statistics__info'>
                                                <Badge
                                                    className='home-statistics__badge'
                                                    count={2}
                                                />
                                                <span className='home-statistics__desc'>
                                                    Сломаны
                                                </span>
                                            </Row>
                                        </Col>
                                    </div>
                                </Col>
                                <Col span={6}>
                                    <div className='home-statistics__buses'>
                                        <Typography.Title className='tasks-title' level={5}>
                                            На 50 мест
                                        </Typography.Title>
                                        <Col>
                                            <Row className='home-statistics__info'>
                                                <Badge
                                                    className='home-statistics__badge'
                                                    style={{ backgroundColor: '#52c41a' }}
                                                    count={16}
                                                />
                                                <span className='home-statistics__desc'>
                                                    Свободны
                                                </span>
                                            </Row>
                                            <Row className='home-statistics__info'>
                                                <Badge
                                                    className='home-statistics__badge'
                                                    style={{ backgroundColor: '#ffb813' }}
                                                    count={4}
                                                />
                                                <span className='home-statistics__desc'>
                                                    Заняты
                                                </span>
                                            </Row>
                                            <Row className='home-statistics__info'>
                                                <Badge
                                                    className='home-statistics__badge'
                                                    count={2}
                                                />
                                                <span className='home-statistics__desc'>
                                                    Сломаны
                                                </span>
                                            </Row>
                                        </Col>
                                    </div>
                                </Col>
                            </Row>
                            <Typography.Title className='tasks-title' level={2}>
                                Рейсы
                            </Typography.Title>
                            <TasksList />
                        </Col>
                    </Row>
                </Col>
            </Row>
        </>
    );
};

export default Home;
