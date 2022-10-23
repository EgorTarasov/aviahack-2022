package scheduler

type Flight struct {
	ID              int    `json:"id" db:"id"`
	Number          int    `json:"number" db:"number"`
	Date            int    `json:"date" db:"date"`
	Type            string `json:"type" db:"type"`
	Terminal        string `json:"terminal" db:"terminal"`
	CompanyName     string `json:"companyName" db:"companyName"`
	ScheduledTime   int    `json:"scheduledTime" db:"scheduledTime"`
	AirportCode     string `json:"airportCode" db:"airportCode"`
	Airport         string `json:"airport" db:"airport"`
	PlaneType       string `json:"planeType" db:"planeType"`
	ParkingID       string `json:"parkingId" db:"parkingId"`
	GateID          string `json:"gateId" db:"gateId"`
	PassengersCount int    `json:"passengersCount" db:"passengersCount"`
}

type Point struct {
	PointID    int    `json:"pointId" db:"pointId"`
	LocationID string `json:"locationId" db:"locationId"`
}

type Journal struct {
	ID          int `json:"id" db:"id"`
	Flight      int    `json:"flight" db:"flight"`
	CurrentTask int    `json:"currentTask" db:"currentTask"`
	BusId       int    `json:"bus_id" db:"bus_id"`
}

type Bus struct {
	ID       int    `json:"id" db:"id"`
	Capacity int    `json:"flight" db:"flight"`
	Point    int    `json:"point" db:"point"`
	State    string `json:"state" db:"state"`
}

type Task struct {
	ID         int    `json:"id" db:"id"`
	Journal    int    `json:"journal" db:"journal"`
	TaskState  string `json:"taskState" db:"taskState"`
	BusState   string `json:"busState" db:"busState"`
	BusId      int    `json:"bus_id" db:"bus_id"`
	Distance   int    `json:"distance" db:"distance"`
	StartPoint int    `json:"startPoint" db:"startPoint"`
	EndPoint   int    `json:"endPoint" db:"endPoint"`
}
