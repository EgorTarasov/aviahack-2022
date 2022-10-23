package scheduler

import (
	"log"
	"mmm/pkg/utils"

	"github.com/jmoiron/sqlx"
)

type Scheduler struct {
	Env *utils.Env
}

func selectFlights() error {
	sch := Scheduler{
		Env: utils.GetEnv(),
	}
	db, err := sqlx.Connect("postgres", sch.Env.DatabaseUrl)
	if err != nil {
		log.Fatalln(err)
	}
	defer db.Close()

	flights := []Flight{}
	err = db.Select(&flights, "SELECT * FROM flight")

	return err
}

func generateJournal(flight Flight) *Journal {
	jrnl := Journal{
		ID:          flight.ID,
		Flight:      flight.ID,
		CurrentTask: 0,
	}
	lt := generateTasks(jrnl)
	jrnl.CurrentTask = lt
	return &jrnl
}

func findBus(point Point) int {
	return 1
}

func generateTasks(jrnl Journal) int {
	x := []int{}
	b := Bus{}
	x[0] = newTask("board", jrnl, b)
	x[1] = newTask("board", jrnl, b)
	return x[0]
}

func newTask(taskType string, jl Journal, b Bus) int {
	switch taskType {
	case "board":
		dist, endPoint := calculateDistance(b, 23)
		tsk := Task{
			ID:         jl.ID,
			Journal:    jl.ID,
			TaskState:  taskType,
			BusId:      b.ID,
			Distance:   dist,
			StartPoint: b.Point,
			EndPoint:   endPoint,
		}
		insertTask(tsk)
		return tsk.ID
	case "wait":

	case "drop":
	default:
		return 0
	}

}

func calculateDistance(bus Bus, dest int) (int, int) {
	return 100, 34
}

func insertTask(tsk Task) {
	sch := Scheduler{
		Env: utils.GetEnv(),
	}
	db, err := sqlx.Connect("postgres", sch.Env.DatabaseUrl)
	if err != nil {
		log.Fatalln(err)
	}
	defer db.Close()

	err = db.Insert

	return err
}
