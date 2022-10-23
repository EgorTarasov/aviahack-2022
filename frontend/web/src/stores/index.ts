import { createContext } from 'react';
import { OperatorStore } from './OperatorStore';

export const rootStoreContext = createContext({
    operatorStore: new OperatorStore(),
});
