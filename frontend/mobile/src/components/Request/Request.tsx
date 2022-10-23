import React, { FC } from 'react';
import { TabBar, Button, SwipeAction } from 'antd-mobile';
import { Row, Col, Typography } from 'antd';
import { DeliveredProcedureOutlined, ArrowRightOutlined } from '@ant-design/icons';
import { useNavigate } from 'react-router-dom';

import './Request.scss';
import { ITask } from '../../models/DriverInterfaces';
import { useStores } from '../../hooks/useStores';

type Props = {
    task: ITask;
};

const Request: FC<Props> = ({ task }) => {
    const { driverStore } = useStores();
    const navigate = useNavigate();

    const onAccept = () => {
        driverStore.setActiveTask(task.id);
        navigate('/home');
    };

    return (
        <SwipeAction
            rightActions={[
                {
                    key: 'decline',
                    text: 'Отменить',
                    color: 'danger',
                },
            ]}
            leftActions={[
                {
                    key: 'accept',
                    text: 'Принять',
                    color: 'success',
                },
            ]}
            onAction={(action, e) => {
                switch (action.key) {
                    case 'accept':
                        onAccept();
                        break;

                    default:
                        break;
                }
            }}
        >
            <div className='request'>
                <div className='request__body'>
                    <Row align='middle'>
                        <DeliveredProcedureOutlined className='request__icon' />
                        <Typography.Title className='request__title' level={5}>
                            Новая задача
                        </Typography.Title>
                    </Row>
                    <Row className='request__time' align='middle'>
                        {task.timeFrom} - {task.timeTo}
                    </Row>
                    <Row align='middle' className='request__way'>
                        <div className='request__status-box'>{task.locationFrom}</div>
                        <ArrowRightOutlined className='request__status-box-arrow-icon' />
                        <div className='request__status-box'>{task.locationTo}</div>
                    </Row>
                    <Row>
                        <Col span={12}>
                            <Button
                                onClick={() => onAccept()}
                                className='request__btn'
                                color='success'
                            >
                                Принять
                            </Button>
                        </Col>
                        <Col span={12}>
                            <Button className='request__btn' color='danger'>
                                Отменить
                            </Button>
                        </Col>
                    </Row>
                </div>
            </div>
        </SwipeAction>
    );
};

export default Request;
