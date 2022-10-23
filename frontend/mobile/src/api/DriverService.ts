import axios, { AxiosResponse } from 'axios';
import { message } from 'antd';
import { API_URL } from '../config';

export interface IDriverService {}

class DriverService implements IDriverService {}

export const DriverServiceInstanse = new DriverService();
