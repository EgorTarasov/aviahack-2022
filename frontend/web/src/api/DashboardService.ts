import axios, { AxiosResponse } from 'axios';
import { message } from 'antd';
import { API_URL } from '../config';
import { IFlightRequest } from '../models/TasksInterfaces';

export interface IDashboardService {
    fetchFlights(): Promise<Array<IFlightRequest>>;
    changeBus(task_id: number, bus_id: number): void;
}

class DashboardService implements IDashboardService {
    public async fetchFlights(): Promise<Array<IFlightRequest>> {
        try {
            const response = await axios.get(`${API_URL}/flight/all`);
            // const response = await axios.get(`./response_1666522055380.json`);
            // console.log(response);

            let data: Array<IFlightRequest> = response.data;

            return data;
        } catch (err) {
            message.error('Ошибка получения рейсов');
            console.log('Eroor: ', err);
            const error = new Error('Ошибка получения рейсов');
            throw error;
        }
    }

    public async changeBus(task_id: number, bus_id: number) {
        try {
            const response = await axios.put(`${API_URL}/task/update`, {
                task_id: task_id,
                bus_id: bus_id,
            });
        } catch (err) {
            message.error('Ошибка обновления рейсов');
            console.log('Eroor: ', err);
            const error = new Error('Ошибка обновления рейсов');
            throw error;
        }
    }
}

export const DashboardServiceInstanse = new DashboardService();
