import React from 'react';
import { Routes, Route, Navigate, BrowserRouter, Link } from 'react-router-dom';

import 'antd/dist/antd.css';
import './App.scss';
import Home from './pages/Home/Home';
import Bottom from './components/Bottom/Bottom';
import { RouteNames, routes } from './router';
import { useAuth } from './hooks/auth.hook';
import Auth from './pages/Auth/Auth';
import { observer } from 'mobx-react-lite';
import { useStores } from './hooks/useStores';

const App = observer(() => {
    const { driverStore } = useStores();

    const isAuthenticated = !!driverStore.driverId;

    return (
        <div className='app'>
            <BrowserRouter>
                {isAuthenticated && (
                    <>
                        <div className='body'>
                            <Routes>
                                {routes.map((route, index) => {
                                    if (route.path !== '/auth') {
                                        return (
                                            <Route
                                                key={index + route.path}
                                                path={route.path}
                                                element={<route.element />}
                                            />
                                        );
                                    }
                                })}
                                <Route
                                    path='*'
                                    element={<Navigate to={RouteNames.HOME} replace />}
                                />
                            </Routes>
                        </div>
                        <div className='bottom'>
                            <Bottom />
                        </div>
                    </>
                )}
                {!isAuthenticated && (
                    <Routes>
                        <Route path={'/auth'} element={<Auth />} />

                        <Route path='*' element={<Navigate to={RouteNames.AUTH} replace />} />
                    </Routes>
                )}
            </BrowserRouter>
            )
        </div>
    );
});

export default App;
