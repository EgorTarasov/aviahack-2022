import internal from 'stream';

export interface ITask {
    id: number;
    // busState: IBusState;
    taskState: string;
    bus: IBus;
    driver: string;
    distance: number;
    flight: IFlight;
    startPoint: IPoint;
    endPoint: IPoint;
}

export interface IBusState {
    label: 'Посадка' | 'Высадка' | 'Ожидание' | 'В пути';
    duration: number;
    order: number;
}

export interface ITaskState {
    label: 'Ожидание' | 'Назначена' | 'Выполнение' | 'Failed' | 'Отменена' | 'Выполнена';
}

export interface IBus {
    id: number;
    state: IBusState;
}

export interface IPoint {
    pointId: number;
    locationId: number;
}

export interface IFlight {
    id: number;
    number: number;
    date: number;
    type: 'A' | 'B';
    terminal: string;
    companyName: string;
    scheduledTime: number;
    airportCode: string;
    airport: string;
    planeType: string;
    parkingId: string;
    gateId: string;
    passengersCount: number;
}

export interface ITask2 {
    id: number;
    bus_id: number;
    bus_capacity: number;
    distance: number;
    duration: number;
    startPoint: string;
    endPoint: string;
}

export interface IFlightRequest {
    flight: IFlight;
    tasks: ITask2[];
}
