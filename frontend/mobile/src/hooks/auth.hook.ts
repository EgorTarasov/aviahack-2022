import { useState, useCallback, useEffect } from 'react';

const storageName = 'userData';

export const useAuth = () => {
    const [token, setToken] = useState(null);
    const [ready, setReady] = useState(false);
    const [userId, setUserId] = useState(null);
    const [email, setEmail] = useState(null);

    const login = useCallback((jwtToken: any, email: any) => {
        setToken(jwtToken);
        setEmail(email);
        console.log(jwtToken);

        localStorage.setItem(storageName, JSON.stringify({ token: jwtToken }));
    }, []);

    const logout = useCallback(() => {
        setToken(null);
        setUserId(null);
        setEmail(null);
        localStorage.removeItem(storageName);
    }, []);

    useEffect(() => {
        //@ts-ignore
        const data = JSON.parse(localStorage.getItem(storageName));
        if (data && data.token) {
            login(data.token, data.userId);
        }
        setReady(true);
    }, [login]);

    return { login, logout, token, userId, ready, email };
};
