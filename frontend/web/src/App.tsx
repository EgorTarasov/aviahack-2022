import React from 'react';
import { Layout, Menu } from 'antd';
import { Routes, Route, Navigate, BrowserRouter, Link } from 'react-router-dom';
import { RouteNames, routes } from './router';

import 'antd/dist/antd.css';
import './App.scss';

import {
    DashboardOutlined,
    MenuFoldOutlined,
    MenuUnfoldOutlined,
    QuestionCircleOutlined,
    UploadOutlined,
    VideoCameraOutlined,
} from '@ant-design/icons';
import { useStores } from './hooks/useStores';

const { Header, Sider, Content } = Layout;

const App: React.FC = () => {
    const [collapsed, setCollapsed] = React.useState(false);

    const { operatorStore } = useStores();

    React.useEffect(() => {
        operatorStore.fetchFlights();
    }, [operatorStore]);

    return (
        <Layout>
            <BrowserRouter>
                <Sider trigger={null} collapsible collapsed={collapsed}>
                    <div className='logo' />
                    <Menu
                        theme='dark'
                        mode='inline'
                        defaultSelectedKeys={['1']}
                        items={[
                            {
                                key: '1',
                                icon: <DashboardOutlined />,
                                label: <Link to={RouteNames.HOME}>Главная</Link>,
                            },
                            {
                                key: '2',
                                icon: <QuestionCircleOutlined />,
                                label: <Link to={RouteNames.PENDING}>Без исполнителя</Link>,
                            },
                        ]}
                    />
                </Sider>
                <Layout className='site-layout'>
                    <div className='menu-collapse-icon'>
                        {React.createElement(collapsed ? MenuUnfoldOutlined : MenuFoldOutlined, {
                            className: 'trigger',
                            onClick: () => setCollapsed(!collapsed),
                        })}
                    </div>
                    <Content
                        className='site-layout-background'
                        style={{
                            margin: '24px 16px',
                            padding: 0,
                            minHeight: '100vh',
                        }}
                    >
                        <Routes>
                            {routes.map((route, index) => (
                                <Route
                                    key={index + route.path}
                                    path={route.path}
                                    element={<route.element />}
                                />
                            ))}
                            <Route path='*' element={<Navigate to={RouteNames.HOME} replace />} />
                        </Routes>
                    </Content>
                </Layout>
            </BrowserRouter>
        </Layout>
    );
};

export default App;
