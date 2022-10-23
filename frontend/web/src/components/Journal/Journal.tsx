import { EditOutlined } from '@ant-design/icons';
import { Col, Modal, Progress, Row, Select, Typography } from 'antd';
import React, { FC, useState } from 'react';
import { useStores } from '../../hooks/useStores';
import { IFlight, IFlightRequest, ITask, ITask2 } from '../../models/TasksInterfaces';

type Props = {
    task: ITask2;
    flight: IFlight;
};

const buses: Array<number> = [];
for (let i = 1; i <= 50; i++) {
    buses[i] = i;
}

const { Option } = Select;

const onSearch = (value: string) => {
    console.log('search:', value);
};

const Journal: FC<Props> = ({ task, flight }) => {
    const [open, setOpen] = useState(false);
    const [confirmLoading, setConfirmLoading] = useState(false);
    const [selectedBus, setSelectedBus] = useState(0);
    const { operatorStore } = useStores();

    const onChange = (value: number) => {
        console.log(`selected ${value}`);
        setSelectedBus(value);
    };

    const flightDate = new Date(flight.scheduledTime);
    const endDate = new Date(flight.scheduledTime + task.duration);
    const durationInMs = task.duration * 60000;
    // const progress = Math.round(
    //     (Math.abs(Date.now() - flight.scheduledTime) /
    //         (flight.scheduledTime + durationInMs - flight.scheduledTime)) *
    //         100
    // );
    const progress = Math.round((50 / task.duration) * 100);

    const showModal = () => {
        setOpen(true);
    };

    const handleOk = () => {
        setConfirmLoading(true);

        if (selectedBus !== 0) {
            operatorStore.updateBuses(task.id, selectedBus);
        }

        setTimeout(() => {
            setOpen(false);
            setConfirmLoading(false);
        }, 2000);
    };

    const handleCancel = () => {
        console.log('Clicked cancel button');
        setOpen(false);
    };

    return (
        <>
            <Row align='middle' className='task-journal' gutter={16}>
                <Col span={3}>
                    <Row>
                        <Typography.Title level={5}>{task.bus_id}</Typography.Title>
                        <Typography.Paragraph>{task.bus_capacity} чел.</Typography.Paragraph>
                    </Row>
                </Col>
                <Col span={9}>
                    <div className='tasks-list__status-box'>
                        {progress > 100 ? 'Выполнен' : 'В пути'}
                    </div>
                </Col>
                <Col span={10}>
                    <Progress percent={progress} />
                </Col>
                <Col span={2}>
                    <EditOutlined onClick={showModal} className='icon' />
                </Col>
            </Row>
            <Modal
                title='Title'
                open={open}
                onOk={handleOk}
                confirmLoading={confirmLoading}
                onCancel={handleCancel}
            >
                <>
                    <Select
                        showSearch
                        placeholder='Выберите автобус'
                        optionFilterProp='children'
                        onChange={onChange}
                        onSearch={onSearch}
                        filterOption={(input, option) =>
                            (option!.children as unknown as string)
                                .toLowerCase()
                                .includes(input.toLowerCase())
                        }
                    >
                        {buses.map((bus) => (
                            <Option key={bus} value={bus}>
                                {' ' + bus}
                            </Option>
                        ))}
                    </Select>
                </>
            </Modal>
        </>
    );
};

export default Journal;
