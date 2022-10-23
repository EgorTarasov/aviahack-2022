import React from 'react';
import Home from '../pages/Home/Home';

export interface IRoute {
    path: string;
    element: React.ComponentType;
}

export enum RouteNames {
    HOME = '/home',
    PENDING = '/pending',
}

export const routes: IRoute[] = [
    { path: RouteNames.HOME, element: Home },
    { path: RouteNames.PENDING, element: Home },
];
