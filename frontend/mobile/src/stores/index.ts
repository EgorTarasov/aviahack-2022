import { createContext } from 'react';
import { DriverStore } from './DriverStore';

export const rootStoreContext = createContext({
    driverStore: new DriverStore(),
});
