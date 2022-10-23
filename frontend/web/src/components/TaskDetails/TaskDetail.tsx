import { ArrowRightOutlined, EditOutlined, PlusCircleOutlined } from '@ant-design/icons';
import { Col, Progress, Row, Statistic, Typography } from 'antd';
import React, { FC } from 'react';
import { IFlightRequest, ITask } from '../../models/TasksInterfaces';
import Journal from '../Journal/Journal';

type Props = {
    task: IFlightRequest;
};

const TaskDetail: FC<Props> = ({ task }) => {
    return (
        <Row gutter={16}>
            <div className='task-detail'>
                <Row align='middle' gutter={16}>
                    <Col span={8}>
                        <Row align='middle' gutter={20}>
                            <div className='tasks-list__status-box'>
                                {task.tasks[0]?.startPoint}
                            </div>
                            <ArrowRightOutlined className='task-detail__status-box-arrow-icon' />
                            <div className='tasks-list__status-box'>{task.tasks[0]?.endPoint}</div>
                        </Row>
                    </Col>
                    <Col span={16}>
                        <div className='task-detail__delay'>
                            <Row align='middle'>
                                <Typography.Title level={5}>Задержка</Typography.Title>
                                <div className='task-detail__delay-value'>0 минут</div>
                                <PlusCircleOutlined className='task-detail__change-delay-icon' />
                            </Row>
                        </div>
                    </Col>
                </Row>
                {task.tasks.map((task1, index) => (
                    <Journal key={index} task={task1} flight={task.flight} />
                ))}
            </div>
        </Row>
    );
};

export default TaskDetail;
