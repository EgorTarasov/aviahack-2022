import { Badge, Col, Row, Typography, Button } from 'antd';
import React, { FC } from 'react';
import { useStores } from '../../hooks/useStores';
import { useNavigate } from 'react-router-dom';

import './Profile.scss';

const Profile: FC = () => {
    const { driverStore } = useStores();
    const navigate = useNavigate();

    return (
        <>
            <div>Profile</div>
            <Button
                onClick={() => {
                    driverStore.logout();
                    navigate('/auth');
                }}
            >
                Выйти
            </Button>
        </>
    );
};

export default Profile;
