import { observable, runInAction, makeAutoObservable } from 'mobx';
import { DashboardServiceInstanse } from '../api/DashboardService';
import { IFlightRequest } from '../models/TasksInterfaces';

export interface IOperatorStore {
    fetchedFlights: Array<IFlightRequest>;

    fetchFlights(): Promise<Array<IFlightRequest>>;
    updateBuses(task_id: number, bus_id: number): Promise<string>;
}

export class OperatorStore implements IOperatorStore {
    fetchedFlights: IFlightRequest[];

    constructor() {
        makeAutoObservable(this, {
            fetchedFlights: observable,
        });

        this.fetchedFlights = [];
    }

    public async fetchFlights(): Promise<IFlightRequest[]> {
        const flights = await DashboardServiceInstanse.fetchFlights();

        console.log(flights);
        runInAction(() => {
            this.fetchedFlights = flights;
        });

        return flights;
    }

    public async updateBuses(task_id: number, bus_id: number): Promise<string> {
        DashboardServiceInstanse.changeBus(task_id, bus_id);

        this.fetchFlights();

        //@ts-ignore
        return new Promise.resolve('ok');
    }
}
