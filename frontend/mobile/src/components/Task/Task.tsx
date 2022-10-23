import React, { FC } from 'react';
import { TabBar, Button, SwipeAction, Badge, Result } from 'antd-mobile';
import { Row, Col, Typography, Timeline } from 'antd';
import { DeliveredProcedureOutlined, ArrowRightOutlined } from '@ant-design/icons';
import { observer } from 'mobx-react-lite';

import './Task.scss';
import { useStores } from '../../hooks/useStores';

const states = ['Подача', 'Посадка', 'Дорога', 'Высадка'];

const Task: FC = observer(() => {
    // let [curState, setCurState] = React.useState(0);
    const { driverStore } = useStores();

    return (
        <>
            <div className='task'>
                <div className='task__body'>
                    {driverStore.tasks[driverStore.activeTask].statusId <= states.length && (
                        <Col>
                            <Row align='middle'>
                                <DeliveredProcedureOutlined className='task__icon' />
                                <Typography.Title className='task__title' level={5}>
                                    Текущая задача
                                </Typography.Title>
                            </Row>
                            <Row justify='center' className='task__time' align='middle'>
                                {driverStore.tasks[driverStore.activeTask].timeFrom} -{' '}
                                {driverStore.tasks[driverStore.activeTask].timeTo}
                            </Row>
                            <Row justify='center' align='middle' className='task__remaining-time'>
                                <Badge content='5 min' />
                            </Row>
                            <Row justify='center' align='middle' className='task__way'>
                                <div className='task__status-box'>
                                    {driverStore.tasks[driverStore.activeTask].locationFrom}
                                </div>
                                <ArrowRightOutlined className='task__status-box-arrow-icon' />
                                <div className='task__status-box'>
                                    {driverStore.tasks[driverStore.activeTask].locationTo}
                                </div>
                            </Row>
                            <Row align='middle' className='task__timeline'>
                                <Timeline pending={states[driverStore.activeTask]}>
                                    {states.map((state, index) => {
                                        if (
                                            index <
                                            driverStore.tasks[driverStore.activeTask].statusId
                                        ) {
                                            return (
                                                <Timeline.Item key={index} color='green'>
                                                    {state}
                                                </Timeline.Item>
                                            );
                                        }
                                    })}
                                </Timeline>
                            </Row>
                            <Row>
                                <Col>
                                    <Button
                                        onClick={() => {
                                            driverStore.completeSubTask(
                                                driverStore.tasks[driverStore.activeTask].id
                                            );
                                        }}
                                    >
                                        Закончить высадку
                                    </Button>
                                </Col>
                                <Col>
                                    <Button color='danger'>Отменить заявку</Button>
                                </Col>
                            </Row>
                        </Col>
                    )}
                    {driverStore.tasks[driverStore.activeTask].statusId > states.length && (
                        <Result
                            status='success'
                            title='Задача выполнена'
                            description='Все задачи выполнены'
                        />
                    )}
                </div>
            </div>
        </>
    );
});

export default Task;
