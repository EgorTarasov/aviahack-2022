import React, { createContext } from 'react';

function noop(a: any, b: any) {}

export const AuthContext = React.createContext({
    token: null,
    userId: null,
    email: null,
    login: noop,
    logout: noop,
    isAuthenticated: false,
});
