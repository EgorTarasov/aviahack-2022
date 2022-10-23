import { observable, runInAction, makeAutoObservable } from 'mobx';
import { ITask } from '../models/DriverInterfaces';

export interface IDriverStore {
    driverId: string;
    activeTask: number;
    tasks: ITask[];
    login(driverId: string): void;
    logout(): void;
    setActiveTask(id: number): void;
    completeSubTask(id: number): void;
}

const storageName = 'userData';

const states: ('Подача' | 'Посадка' | 'Дорога' | 'Высадка')[] = [
    'Подача',
    'Посадка',
    'Дорога',
    'Высадка',
];
const sampleTasks: ITask[] = [
    {
        id: 0,
        timeFrom: '15:00',
        timeTo: '15:15',
        locationFrom: 'DGA_D',
        locationTo: '34A',
        status: states[0],
        statusId: 0,
    },
    {
        id: 1,
        timeFrom: '16:00',
        timeTo: '16:15',
        locationFrom: '32A',
        locationTo: 'DGA_D',
        status: states[0],
        statusId: 0,
    },
    {
        id: 2,
        timeFrom: '16:30',
        timeTo: '17:00',
        locationFrom: '40B',
        locationTo: 'DGA_I',
        status: states[0],
        statusId: 0,
    },
];

export class DriverStore implements IDriverStore {
    driverId: string;
    activeTask: number;
    tasks: ITask[];

    constructor() {
        makeAutoObservable(this, {
            tasks: observable,
        });
        this.driverId = localStorage.getItem(storageName) || '';
        this.activeTask = 0;
        this.tasks = sampleTasks;
    }

    login(driverId: string): void {
        localStorage.setItem(storageName, driverId);
        this.driverId = driverId;
    }

    logout(): void {
        localStorage.removeItem(storageName);
        this.driverId = '';
    }

    setActiveTask(id: number): void {
        runInAction(() => {
            this.activeTask = id;
        });
    }

    completeSubTask(id: number): void {
        runInAction(() => {
            this.tasks[id].statusId = this.tasks[id].statusId + 1;
            this.tasks[id].status = states[this.tasks[id].statusId];
        });
        // if (this.tasks[this.activeTask].statusId > states.length) {
        //     this.tasks.splice(this.activeTask, 1);
        //     this.activeTask = 0;
        // }
    }
}
