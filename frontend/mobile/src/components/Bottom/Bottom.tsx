import React, { FC } from 'react';
import { TabBar } from 'antd-mobile';
// import { Route, Switch, useHistory, useLocation, MemoryRouter as Router } from 'react-router-dom';
import { AppOutline, UnorderedListOutline, UserOutline } from 'antd-mobile-icons';
import { useNavigate, useLocation } from 'react-router-dom';

const Bottom: FC = () => {
    let navigate = useNavigate();
    const location = useLocation();

    const setRouteActive = (value: string) => {
        navigate(value);
    };
    const tabs = [
        {
            key: '/home',
            title: 'Главная',
            icon: <AppOutline />,
        },
        {
            key: '/list',
            title: 'Задачи',
            icon: <UnorderedListOutline />,
        },
        {
            key: '/profile',
            title: 'Профиль',
            icon: <UserOutline />,
        },
    ];

    return (
        <TabBar activeKey={location.pathname} onChange={(value) => setRouteActive(value)}>
            {tabs.map((item) => (
                <TabBar.Item key={item.key} icon={item.icon} title={item.title} />
            ))}
        </TabBar>
    );
};

export default Bottom;
