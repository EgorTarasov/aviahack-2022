import React from 'react';
import Auth from '../pages/Auth/Auth';
import Home from '../pages/Home/Home';
import List from '../pages/List/List';
import Profile from '../pages/Profile/Profile';

export interface IRoute {
    path: string;
    element: React.ComponentType;
}

export enum RouteNames {
    HOME = '/home',
    PROFILE = '/profile',
    LIST = '/list',
    AUTH = '/auth',
}

export const routes: IRoute[] = [
    { path: RouteNames.HOME, element: Home },
    { path: RouteNames.PROFILE, element: Profile },
    { path: RouteNames.LIST, element: List },
    { path: RouteNames.AUTH, element: Auth },
];
