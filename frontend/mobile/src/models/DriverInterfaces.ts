export interface IBus {
    bus: string;
}

export interface ITask {
    id: number;
    timeFrom: string;
    timeTo: string;
    locationFrom: string;
    locationTo: string;
    status: 'Подача' | 'Посадка' | 'Дорога' | 'Высадка';
    statusId: number;
}
