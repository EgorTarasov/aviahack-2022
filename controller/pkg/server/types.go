package server

type EnvRequest struct {
	Name string `json:"name"`
}

type EnvResponse struct {
	Baseline string `json:"baseline"`
	Result   string `json:"result"`
}

type Event struct {
	Id      string  `json:"id"`
	Image   string  `json:"image"`
	Raiting float64 `json:"rating"`
}
