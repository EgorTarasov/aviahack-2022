import { Badge, Col, Row, Typography, Form, Input, Button } from 'antd';
import React, { FC, useContext } from 'react';
import Request from '../../components/Request/Request';
import Task from '../../components/Task/Task';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import { useNavigate } from 'react-router-dom';

import './Auth.scss';
import { AuthContext } from '../../context/AuthContext';
import { useAuth } from '../../hooks/auth.hook';

const Auth: FC = () => {
    const { login, logout, token, userId, ready, email } = useAuth();
    const navigate = useNavigate();

    const onFinish = (values: any) => {
        const authToken = 'token';
        login(authToken, login);
        navigate('/list');
        window.location.reload();
    };

    return (
        <Row className='auth' align='middle'>
            <Col xs={{ span: 24, offset: 0 }} md={{ span: 6, offset: 9 }}>
                <Form
                    name='normal_login'
                    className='login-form'
                    initialValues={{
                        remember: true,
                    }}
                    onFinish={onFinish}
                >
                    <Form.Item
                        name='username'
                        rules={[
                            {
                                required: true,
                                message: 'Please input your Username!',
                            },
                        ]}
                    >
                        <Input
                            prefix={<UserOutlined className='site-form-item-icon' />}
                            placeholder='Номер автобуса'
                        />
                    </Form.Item>
                    <Form.Item
                        name='password'
                        rules={[
                            {
                                required: true,
                                message: 'Please input your Password!',
                            },
                        ]}
                    >
                        <Input
                            prefix={<LockOutlined className='site-form-item-icon' />}
                            type='password'
                            placeholder='Пароль'
                        />
                    </Form.Item>

                    <Form.Item>
                        <Button type='primary' htmlType='submit' className='login-form-button'>
                            Войти
                        </Button>
                    </Form.Item>
                </Form>
            </Col>
        </Row>
    );
};

export default Auth;
