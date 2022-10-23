import React, { FC } from 'react';
import { observer } from 'mobx-react-lite';
import { useStores } from '../../hooks/useStores';
import { IFlight, IFlightRequest, ITask } from '../../models/TasksInterfaces';
import { Button, Col, Collapse, Progress, Row, Switch, Typography } from 'antd';

import './TasksList.scss';
import TaskDetail from '../TaskDetails/TaskDetail';
import { DownOutlined } from '@ant-design/icons';

const tasks: IFlightRequest[] = [
    {
        flight: {
            id: 1,
            number: 1144,
            date: 1666497255922,
            type: 'A',
            terminal: 'D',
            companyName: 'AF',
            scheduledTime: 1666497255922,
            airportCode: 'SVO',
            airport: 'Париж',
            planeType: '321',
            parkingId: '40',
            gateId: 'DGA_D',
            passengersCount: 122,
        },
        tasks: [
            {
                id: 458,
                bus_id: 1,
                bus_capacity: 100,
                distance: -776,
                duration: 10,
                startPoint: '935',
                endPoint: '159',
            },
        ],
    },
];

const TasksList: FC = observer(() => {
    const { operatorStore } = useStores();

    const renderCollapsePannels = (flights: IFlightRequest[]) => {
        // let prevDate = 0;
        return operatorStore.fetchedFlights.map((flight, index) => {
            // let splitTitle = task.flight.date;
            // if (split) {

            // }
            return (
                <React.Fragment key={flight.flight.id}>
                    {/* <Typography.Title className='tasks-list__split-title' level={4}>
                        17:00
                    </Typography.Title> */}
                    <Collapse.Panel
                        key={flight.flight.id}
                        header={renderCollapseHeader(flight, index)}
                    >
                        <TaskDetail task={flight} />
                    </Collapse.Panel>
                </React.Fragment>
            );
        });
    };

    //TO DO: разбивать по часам
    const renderCollapseHeader = (flight: IFlightRequest, index: number) => {
        const flightDate = new Date(flight.flight.scheduledTime * 1000);
        const durationInMs = flight.tasks[0]?.duration * 60000 || 0;
        const endDate = new Date(flight.flight.scheduledTime * 1000 + durationInMs);

        // console.log(Date.now());
        console.log(flight.flight.scheduledTime);
        //1666524071 - 1566634837
        // const progress = Math.round(
        //     (Math.abs(1566598837 - flight.flight.scheduledTime) /
        //         (flight.flight.scheduledTime +
        //             flight.tasks[0]?.duration -
        //             flight.flight.scheduledTime)) *
        //         100
        // );
        const progress = Math.round((50 / flight.tasks[0]?.duration) * 100);
        return (
            <Row className='tasks-list__row' align='middle' gutter={20}>
                <Col className='tasks-list__content tasks-list__content_time' span={3}>
                    {flightDate.getHours() +
                        ':' +
                        (flightDate.getMinutes() < 10 ? '0' : '') +
                        flightDate.getMinutes() +
                        ' - ' +
                        endDate.getHours() +
                        ':' +
                        (endDate.getMinutes() < 10 ? '0' : '') +
                        endDate.getMinutes()}
                </Col>
                <Col className='tasks-list__content tasks-list__content_bus-info' span={3}>
                    <Row>
                        <div className='tasks-list__bus-id'>{flight.flight.number}</div>
                    </Row>
                    <Row>
                        <div className='tasks-list__driver'>
                            {flight.tasks.map((task) => task.bus_id + ', ')}
                        </div>
                    </Row>
                </Col>
                <Col className='tasks-list__content tasks-list__flight' span={3}>
                    <Row className='tasks-list__flight_airport'>{flight.flight.airport}</Row>
                    <Row className='tasks-list__flight_type'>
                        {flight.flight.type === 'A' ? 'вылет' : 'прилет'}
                    </Row>
                </Col>
                <Col className='tasks-list__content' span={8}>
                    <Progress percent={progress} />
                </Col>
                <Col className='tasks-list__content tasks-list__status' span={6}>
                    <div className='tasks-list__status-box'>
                        {' '}
                        {progress > 100 ? 'Выполнен' : 'В пути'}
                    </div>
                </Col>
            </Row>
        );
    };
    return (
        <>
            <Collapse
                className='departments-table__content'
                defaultActiveKey={['1']}
                expandIconPosition={'end'}
                ghost={true}
            >
                {renderCollapsePannels(tasks)}
            </Collapse>
        </>
    );
});

export default TasksList;
